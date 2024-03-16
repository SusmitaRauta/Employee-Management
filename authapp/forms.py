import re
from django import forms
from django.core.exceptions import ValidationError
from authapp.models import UsersInfo

class ForgotForm(forms.Form):
    mailnum= forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Mailid or phone number'}
    ))
class LoginForm(forms.Form):
    email=forms.CharField(max_length=50,widget=forms.EmailInput(attrs={'class':"form-control",'placeholder':'Enter mailid'}))
    pwd=forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':'Enter password'}))
class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'Enter first name'}))
    last_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'Enter last name'}))
    email = forms.CharField(max_length=30,widget=forms.EmailInput(attrs={'class':"form-control",'placeholder':'Enter email'}))
    password= forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':'Enter password'}))
    confirmpwd =forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':'Enter confirm password'}))
    phone=forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'Enter mob no'}))
    def clean_first_name(self):
        fname=self.cleaned_data.get('first_name')
        if not fname.isalpha():
            raise ValidationError("please enter only alphabet")
        return fname
    def clean_last_name(self):
        fname=self.cleaned_data.get('first_name')
        lname=self.cleaned_data.get('last_name')
        rows=UsersInfo.objects.filter(first_name=fname,last_name=lname)
        if not lname.isalpha():
            raise ValidationError("please enter only alphabet")
        elif(rows.count()):
            raise ValidationError("user name already exists")
        return lname
    def clean_email(self):
        mail=self.cleaned_data.get('email')
        rows=UsersInfo.objects.filter(email=mail)
        if rows.count():
            raise ValidationError("mailid already exist")
        return mail
    def clean_password(self):
        pwd=self.cleaned_data.get('password')
        print(pwd)
        pattern='[A-Z]+[a-z]+[@#$&][0-9]+'
        if not re.search(pattern,pwd):
            raise ValidationError("please enter at least one uppercase,lowercase,symbol and digit")
        return(pwd)
    def clean_confirmpwd(self):
        password1=self.cleaned_data.get('password')
        password2=self.cleaned_data.get('confirmpwd')
        print(password1)
        print(password2)
        if (password1 != password2):
            raise ValidationError("confirm password not match with password")
        return password2
    def clean_phone(self):
        ph=self.cleaned_data.get('phone')
        if (ph.isdigit()):
            if(len(ph)==8):
                return ph
            else:
                raise ValidationError("Enter 8 digit number only")
        else:
            raise ValidationError("Enter Only Digits")
