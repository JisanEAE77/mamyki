from django.shortcuts import render, redirect
from course.models import *
from mamyki.decorator import logged_user, allowed_user
# Create your views here.
def courseDetails(request, id):
    course = Course.objects.get(id=id)
    context = {
        'course': course,
    }
    return render(request, "course-details.html", context)

@logged_user
@allowed_user(["Student"])
def book(request, id):
    course = Course.objects.get(id=id)
    user = request.user
    author = course.author
    date = course.date
    status = Status.objects.get(name="Pending")

    req = Request(course=course, student=user, instructor=author, date=date, attendance="", status=status)
    req.save()

    return redirect("/dashboards")

@logged_user
@allowed_user(["Instructor"])
def cancel(request, id):
    req = Request.objects.get(id=id)

    if req.course.author.username == request.user.username:
        status = Status.objects.get(name="Rejected")
        req.status = status
        req.save()
    
    return redirect("/dashboard")

@logged_user
@allowed_user(["Instructor"])
def accept(request, id):
    req = Request.objects.get(id=id)
    if req.course.author.username == request.user.username:
        status = Status.objects.get(name="Accepted")
        req.status = status
        req.save()
    
    return redirect("/manage-class")


@logged_user
@allowed_user(["Instructor"])
def absent(request, id):
    req = Class.objects.get(id=id)
    if req.request.course.author.username == request.user.username and req.request.status.name == "Accepted":
        req.attendance = "Absent"
        req.save()
    
    return redirect("/manage/" + str(req.request.id))

@logged_user
@allowed_user(["Instructor"])
def present(request, id):
    req = Class.objects.get(id=id)
    if req.request.course.author.username == request.user.username and req.request.status.name == "Accepted":
        req.attendance = "Present"
        req.save()
    
    return redirect("/manage/" + str(req.request.id))