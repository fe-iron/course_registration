from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('courses-list', views.courses_list, name='courses-list'),
    path('teacher-list', views.teacher_list, name='teacher-list'),
    path('contact', views.contact, name='contact'),
    path('message', views.message, name='message'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]
