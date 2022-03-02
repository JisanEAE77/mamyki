import imp
from typing import Dict, List, Any
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from password_validator import PasswordValidator
from mamyki.decorator import *
import re
from course.models import Request

# Create your views here.


def forget(request, *args, **kwargs):
    return render(request, "account/forgot-password.html")





# Create your views here.

# Registration Page

@guest_user
def userRegistration(request, *args, **kwargs):
    context = {
        "error": [],
    }

    # if request.user.is_authenticated:
    #     return redirect("/")
    if request.method == "POST":
        groups = ['Student', 'Instructor']
        usertype = request.POST.get('type')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('uname')
        username = username.lower()
        password = request.POST.get('pass')
        cpassword = request.POST.get('cpass')
        email = request.POST.get('email')
        email = email.lower()

        try:
            getUser = User.objects.get(username=username)
            uexists = False
        except:
            uexists = True

        try:
            getEmail = User.objects.get(email=email)
            mexists = False
        except:
            mexists = True

        if usertype in groups and uexists and mexists and checkEmail(email) and checkPassword(password) and (password == cpassword):
            print(username, email, password)
            user = User.objects.create_user(first_name=fname, last_name=lname, username=username, email=email, password=password)
            group = Group.objects.get(name=usertype)
            group.user_set.add(user)
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("/dashboard")
        else:
            if not uexists:
                context["error"].append("Username already exists, please choose another!")
            if not mexists and checkEmail(email):
                context["error"].append("This E-mail is already in use, please try again with another e-mail!")
            if not checkEmail(email):
                context["error"].append("Invalid E-mail format, enter a valid E-mail!")
            if not checkPassword(password):
                context["error"].append("Weak password! Your password should contain at least one lowercase letter, one uppercase letter, one numeric digit, one special character and must be at least 6 character long!")
            if not (password == cpassword):
                context["error"].append("Both password doesn't match. Try again with entering similar password for both password field!")

    return render(request, "account/register.html", context)


# Login Page

@guest_user
def userLogin(request, *args, **kwargs):
    users = User.objects.all()
    userlist = [user.username for user in users]
    context = {
        "error": [],
    }

    if request.method == "POST":
        username = request.POST.get('username')
        print(username)
        username = username.lower()
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/dashboard")
        if username not in userlist:
            context["error"].append("Username doesn't exist, please enter a valid username!")
        else:
            context["error"].append("Wrong password for this user, try again with correct username & password!")

    return render(request, "account/login.html", context)


# Username Validator


def validateusername(request, username):
    users = User.objects.all()
    userlist = [user.username for user in users]
    username = username.lower()

    if username in userlist:
        data = {
            "response": "VALID"
        }
        return JsonResponse(data)
    data = {
        "response": "INVALID"
    }
    return JsonResponse(data)


# Email Validator


def validateemail(request, email):
    users = User.objects.all()
    emaillist = [user.email for user in users]
    email = email.lower()

    if email in emaillist:
        data = {
            "response": "VALID"
        }
        return JsonResponse(data)
    data = {
        "response": "INVALID"
    }
    return JsonResponse(data)


# Login Validator


def validatelogin(request, username, password):
    username = username.lower()
    user = authenticate(username=username, password=password)

    if user is not None:
        data = {
            "response": "VALID"
        }
        return JsonResponse(data)

    data = {
        "response": "INVALID"
    }
    return JsonResponse(data)


# temporary dashboard


@logged_user
def dashboard(request, *args, **kwargs):
    group = request.user.groups.all()[0].name
    
    if group == "Student":
        req = Request.objects.filter(student=request.user).order_by('-reqTime')
        context = {
            "req": req
        }
        return render(request, "student/student-dashboard.html", context)
    elif group == "Instructor":
        req = Request.objects.filter(instructor=request.user).order_by('-reqTime')
        context = {
            "req": req
        }
        return render(request, "instructor/instructor-dashboard.html", context)
    else:
        return redirect("/apanel")

# Registration Page

# Email Format Validator


def checkEmail(email):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if re.search(regex, email):
        return True
    else:
        return False

# Password Strength Check


def checkPassword(password):
    schema = PasswordValidator()
    schema \
        .min(6) \
        .max(100000) \
        .has().uppercase() \
        .has().lowercase() \
        .has().digits() \
        .has().symbols() \
        .has().no().spaces() \

    if schema.validate(password):
        return True
    else:
        return False

@logged_user
def logOut(request):
    logout(request)
    return redirect('/')