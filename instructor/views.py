import imp
import re
from django.shortcuts import render, redirect
from course.models import *
from subscription.models import*
from mamyki.decorator import allowed_user, logged_user
from course.models import Request, Status, Class

# Create your views here.
@logged_user
def manageClass(request, *args, **kwargs):
    group = request.user.groups.all()[0].name
    
    if group == "Student":
        status = Status.objects.get(name="Accepted")
        req = Request.objects.filter(student=request.user, status=status).order_by('-reqTime')
        context = {
            'req': req,
        }
        return render(request, "student/student-classes.html", context)
    
    if group == "Instructor":
        status = Status.objects.get(name="Accepted")
        req = Request.objects.filter(instructor=request.user, status=status).order_by('-reqTime')
        context = {
            'req': req,
        }
        return render(request, "instructor/instructor-classes.html", context)

@logged_user
def attendance(request, id):
    group = request.user.groups.all()[0].name
    
    if group == "Student":
        req = Request.objects.get(id=id)
        classReq = Class.objects.filter(request=req)
        if req.student.username != request.user.username:
            return redirect('/dashboard')
        context = {
            'req': req,
            'class': classReq,
        }
        return render(request, "student/student-attendance.html", context)
    if group == "Instructor":
        req = Request.objects.get(id=id)
        classReq = Class.objects.filter(request=req)
        if req.course.author.username != request.user.username:
            return redirect('/dashboard')
        context = {
            'req': req,
            'class': classReq,
        }
        return render(request, "instructor/instructor-attendance.html", context)

@logged_user
@allowed_user(["Instructor"])
def myStudents(request, *args, **kwargs):
    courses = Course.objects.filter(author=request.user)

    context = {
        'courses': courses
    }
    return render(request, "instructor/my-students.html", context)

def invoicesi(request, *args, **kwargs):
    return render(request, "instructor/invoices.html")

def settingsi(request, *args, **kwargs):
    return render(request, "instructor/instructor-profile-setting.html")

def changepassi(request, *args, **kwargs):
    return render(request, "instructor/instructor-change-password.html")

def addCourse(request, *args, **kwargs):
    if request.method == "POST":
        days = request.POST.getlist('days')
        print(days)
        category = request.POST['category']
        print(category)
        category = Category.objects.get(name=category)
        typo = request.POST['type']
        typo = Type.objects.get(name=typo)
        city = request.POST['city']
        city = City.objects.get(name=city)
        lang = request.POST['lang']
        lang = Language.objects.get(name=lang)
        price = request.POST['price']
        title = request.POST['title']
        stime = request.POST['stime']
        etime = request.POST['etime']
        sage = request.POST['sage']
        eage = request.POST['eage']
        desc = request.POST['description']
        thumbnail = request.FILES['thumbnail']
        user = request.user
        print(lang)
        print(request.user)
        course = Course(author=user, title=title, cat=category, desc=desc, cover=thumbnail, sage=sage, eage=eage, stime=stime, etime=etime, price=price, lang=lang, loc=city, typo=typo)

        course.save()

        for i in days:
            day = Days.objects.get(name=i)
            course.days.add(day)

        


    category = Category.objects.all()
    typo = Type.objects.all()
    city = City.objects.all()
    lang = Language.objects.all()
    time = Time.objects.all()
    days = Days.objects.all()

    context = {
        "category": category,
        "typo": typo,
        "city": city,
        "lang": lang,
        "time": time,
        "days": days,
    }
    
    return render(request, "instructor/add-course.html", context)