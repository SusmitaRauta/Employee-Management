"""EmployeeDetails URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from emp.views import welcome,showemp,insertform,CBVempinsert,CBVSignUp,ChkLogin,Forgot,Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",welcome,name='welcome'),
    path("showemp/", showemp, name='showemp'),
    path("insert/",insertform,name='insert'),
    path("CBVempinsert/",CBVempinsert.as_view(),name='empinsert'),
    path("signup/",CBVSignUp.as_view(),name='signup'),
    path("login/",ChkLogin.as_view(),name='login'),
    path("forgot/",Forgot.as_view(), name="forgot"),
    path("logout/",Logout,name="logout")
]

