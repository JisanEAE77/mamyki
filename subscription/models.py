import imp
from lib2to3.pgen2 import token
from logging import NullHandler
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name

class Plan(models.Model):
    name = models.CharField(max_length=1000, blank=False, null=False)
    price = models.BigIntegerField(default=0, blank=False, null=False)
    allowClass = models.ManyToManyField(Type, blank=False, null=False)
    credit = models.BigIntegerField(default=0, blank=False, null=False)
    classAmount = models.BigIntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return self.name

class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True, blank=True)
    credit = models.BigIntegerField(default=0, blank=False, null=False)
    classAmount = models.BigIntegerField(default=0, blank=False, null=False)
    sdate = models.DateTimeField(blank=True, null=True)
    edate = models.DateTimeField(blank=True, null=True)
    subscribed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return user