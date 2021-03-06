
from operator import mod, truediv
from os import name
from pyexpat import model
from statistics import mode
from wsgiref.handlers import format_date_time
from django.contrib.auth.models import User
from django.db import models
from subscription.models import Type

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Time(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name

class Days(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Course(models.Model):
    id = models.AutoField(blank=False, null=False, primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    title = models.CharField(max_length=250, blank=False, null=False)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=False)
    desc = models.TextField(max_length=3000, blank=False, null=False)
    cover = models.ImageField(blank=False, null=False, upload_to="covers/")
    sage = models.IntegerField(blank=False, null=False)
    eage = models.IntegerField(blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    stime = models.CharField(blank=False, null=False, max_length=50)
    etime = models.CharField(blank=False, null=False, max_length=50)
    lang = models.ForeignKey(Language, on_delete=models.CASCADE, blank=False, null=False)
    loc = models.ForeignKey(City, on_delete=models.CASCADE, blank=False, null=False)
    typo = models.ForeignKey(Type, on_delete=models.CASCADE, blank=False, null=False)
    days = models.ManyToManyField(Days)
    # date = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.title + " - " + self.author.username

class Status(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name



class Request(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="student")
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="instructor")
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    reqTime = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class Class(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.CharField(max_length=50)
    attendance = models.CharField(max_length=100, blank=True, null=True)
