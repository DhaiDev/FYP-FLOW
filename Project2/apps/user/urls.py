from django.contrib import admin
from django.urls import path
from user.views import RegisterView

path('register/', RegisterView.as_view(), name='register'),
