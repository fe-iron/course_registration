from django.shortcuts import render, redirect
from .models import Message, Registration, User
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request, 'home-slider.html')


def about(request):
    return render(request, 'about.html')


def courses_list(request):
    return render(request, 'courses-list.html')


def teacher_list(request):
    return render(request, 'teacher-list.html')


def contact(request):
    return render(request, 'contact.html')


def message(request):
    # AJAX request
    csiname = request.GET.get('csiname')
    csiemail = request.GET.get('csiemail')
    csisubject = request.GET.get('csisubject')
    csimessage = request.GET.get('csimessage')

    msg = Message(name=csiname, email=csiemail, subject=csisubject, message=csimessage)
    msg.save()

    name = "Thank you for your message, your message has reached to us!"
    return JsonResponse({"message": name}, status=200)


def login(request):
    return render(request, 'login.html')


def signup(request):
    name = request.POST.get('name')
    fname = request.POST.get('fname')
    mname = request.POST.get('mname')
    email = request.POST.get('email')
    dob = request.POST.get('dob')
    password = request.POST.get('password')

    if User.objects.filter(username=email).exists():
        return render(request, "signup.html", {"msg": "Email already exists"})
    else:
        user = User.objects.create_user(username=email, email=email, password=password, first_name=name)
        user.save()

        reg = Registration(user=user, name=name, fname=fname, mname=mname, dob=dob, email=email)
        reg.save()

        return redirect("/")
