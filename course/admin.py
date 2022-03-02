from ast import Subscript
import imp
from django.contrib import admin
from .models import *

admin.site.register(State)
admin.site.register(City)
admin.site.register(Language)
admin.site.register(Time)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Status)
admin.site.register(Request)
admin.site.register(Days)
admin.site.register(Class)