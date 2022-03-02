import imp
from django.shortcuts import render
from course.models import Course
# Create your views here.

def index(request, *args, **kwargs):
    course = Course.objects.all()[:10]
    context = {
        "course": course
    }
    return render(request, 'index.html', context)

def calendar(request, *args, **kwargs):
    return render(request, "calendar.html")