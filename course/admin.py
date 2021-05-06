from django.contrib import admin
from .models import Message, Registration


# Register your models here.
admin.site.register(Message)

admin.site.register(Registration)