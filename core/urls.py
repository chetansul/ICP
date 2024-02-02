from django.contrib import admin
from django.urls import path
from core import views


urlpatterns = [
    path('', views.index, name="home"),
    path('appointment/', views.booking, name="booked"),
    path('home/', views.home, name="home"),
    path('aboutus/',views.about,name="about"),
    path('sendmail/', views.send_mail_to_all, name="sendmail")
]
