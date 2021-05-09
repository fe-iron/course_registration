from django.contrib import admin
from .models import Message, Registration, Courses


# Register your models here.
admin.site.register(Message)

admin.site.register(Registration)

admin.site.register(Courses)

