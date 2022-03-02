"""mamyki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
from instructor.views import *
from student.views import *
from account.views import *
from course.views import *

urlpatterns = [
    path('apanel/', admin.site.urls),
    path('', index, name='home'),
    path('dashboard', dashboard, name='dashboard'),
    path('manage-class', manageClass, name='manage-class'),
    path('manage/<int:id>', attendance, name="manage"),
    path('my-students', myStudents, name='my-students'),
    path('invoicesi', invoicesi, name="instructor-invoices"),
    path('instructor-settings', settingsi, name='instructor-settings'),
    path('changepasswordi', changepassi, name='changepasswordi'),
    path('favourites', favourite, name="favourites"),
    path('settings', settingsp, name="settings"),
    path('changepassword', changepassword, name="change-password"),
    path('login', userLogin, name='login'),
    path('register', userRegistration, name='register'),
    path('forgot', forget, name="forgot"),
    path('courses', search, name="search"),
    path('booking/<int:id>', booking, name="booking"),
    path('booking-success', bookings, name='booking-success'),
    path('calendar', calendar, name='calendar'),
    path('add-course', addCourse, name="add-course"),
    path('course-details/<int:id>', courseDetails, name="course-details"),
    path('book/<int:id>', book, name="book"),
    path('accept/<int:id>', accept, name="accept"),
    path('cancel/<int:id>', cancel, name="cancel"),
    path('present/<int:id>', present, name="present"),
    path('absent/<int:id>', absent, name="absent"),
    path('logOut', logOut, name="logOut"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)