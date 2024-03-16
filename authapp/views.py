from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render
from authapp.forms import SignupForm,LoginForm,ForgotForm
from authapp.models import UsersInfo
from django.http import HttpResponse

# Create your views here.
