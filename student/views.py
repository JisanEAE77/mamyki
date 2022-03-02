from urllib.request import Request
from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from course.models import Request, Course, Time, Class, Status
from student.forms import DateForm
from mamyki.decorator import logged_user, allowed_user
# Create your views here.


def favourite(request, *args, **kwargs):
    return render(request, "student/favourites.html")

def settingsp(request, *args, **kwargs):
    return render(request, "student/profile-settings.html")

def changepassword(request, *args, **kwargs):
    return render(request, "student/change-password.html")

def search(request, *args, **kwargs):
    course = Course.objects.all()
    context = {
        'course': course,
    }
    return render(request, "student/search.html", context)

@logged_user
@allowed_user(["Instructor"])
def booking(request, id):
    
    if request.method == "POST":
        time = request.POST.get('time')
        dates = request.POST.get('dates')

        dates = dates.split(",")
        course = Course.objects.get(id=id)
        user = request.user
        author = course.author
        status = Status.objects.get(name="Pending")

        req = Request(course=course, student=user, instructor=author, status=status)
        req.save()

        for date in dates:
            classes = Class(request=req, date=date, time=time, attendance="")
            classes.save()

        return redirect("/dashboard")

    course = Course.objects.get(id=id)
    times = Time.objects.all()
    context = {
        'course': course,
        'times': times
    }
    return render(request, "student/booking.html", context)

def bookings(request, *args, **kwargs):
    return render(request, "student/booking-success.html")