from django.shortcuts import render
from django.views.generic import View
from emp.models import EmpMaster
from authapp.forms import SignupForm,LoginForm,ForgotForm
from django.http import HttpResponse
from authapp.models import UsersInfo
from django.core.mail import send_mail
# from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')
def showemp(request):
    if(request.session.has_key("password")):
        emprecs=EmpMaster.objects.all()
        return render(request,'showempdetails.html',{'emprecs':emprecs})
    else:
        request.session["path"]=request.path
        lgform=LoginForm(request.GET)
        return render(request,"login.html",{"from":LoginForm()})
def insertform(request):
    if (request.session.has_key("password")):
        return render(request, 'insert.html')
    else:
        request.session["path"] = request.path
        lgform = LoginForm(request.GET)
        return render(request, "login.html", {"form": lgform})
class CBVempinsert(View):
    def get(self,request):
        if (request.session.has_key("password")):
            return render(request,'insert.html')
        else:
            request.session["path"] = request.path
            lgform = LoginForm(request.GET)
            return render(request, "login.html", {"form": lgform})
    def post(self,request):
        eid= request.POST["id"]
        ename= request.POST["name"]
        salary= request.POST["sal"]
        gender = request.POST["gen"]
        deptno = request.POST["dptno"]
        rec = EmpMaster(eid=eid,ename=ename,salary=salary,gender=gender,deptno=deptno)
        rec.save()
        return HttpResponse("<h1>record is inserted</h1>")
class CBVSignUp(View):
    def get(self,request):
        form=SignupForm()
        return render(request,"signup.html",{"form":form})
    def post(self,request):
        form = SignupForm(request.POST)
        if (form.is_valid()):
            fname = form.cleaned_data['first_name']
            lname = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            pwd= form.cleaned_data['password']
            ph = form.cleaned_data['phone']
            data=UsersInfo(first_name=fname,last_name=lname,email=email,password=pwd,phone=ph)
            data.save()
            return HttpResponse("Sumitted Succ...")
        else:
            return render(request,'signup.html',{"form":form})
class ChkLogin(View):
    def get(self,request):
        return render(request,'login.html',{"form":LoginForm()})
    def post(self,request):
        lgform=LoginForm(request.POST)
        if lgform.is_valid():
            mail = lgform.cleaned_data['email']
            pwd = lgform.cleaned_data['password']
            rows = UsersInfo.objects.filter(email=mail,password=pwd)
            if(rows.count()):
                request.session["email"] = mail
                request.session["password"] = pwd
                request.session.set_expiry(60)
                if (request.session["path"] == "/showemp/"):
                    return render(request, "showempdetails.html", {"emp": EmpMaster.objects.all()})
                elif (request.session["path"] == "/insert/"):
                    return render(request, "insert.html")
                else:
                    return render(request, "welcome.html")
            else:
                msg="invalid login details"
                lgform=LoginForm(request.POST)
                return render(request,'login.html',{"form":lgform,"msg":msg})
        else:
            lgform=LoginForm(request.POST)
            return render(request,'login.html',{'form':lgform})
class Forgot(View):
    def get(self,request):
        return render(request,"forgot.html",{"form":ForgotForm})
    def post(self,request):
        form=ForgotForm(request.POST)
        if form.is_valid():
            mailnum=form.cleaned_data['mailnum']
            print(mailnum)
            if mailnum.isdigit():
                rec=UsersInfo.objects.filter(phone=mailnum)
                if(rec.count()):
                    email=rec[0].email
                    pwd=rec[0].password
                    res = send_mail("forgot password", pwd, "susmitarauta807@gmail.com", [email])
                    return render(request,"mailstatus.html")
                else:
                    return render(request, "forgot.html", {"msg": "invalid phone number", "form": ForgotForm(request.GET)})
            else:
                rec = UsersInfo.objects.filter(email=mailnum)
                if(rec.count()):
                    email=rec[0].email
                    pwd=rec[0].password
                    res = send_mail("forgot password", pwd, "susmitarauta807@gmail.com", [email])
                    return render(request, "mailstatus.html")
                else:
                    return render(request,"forgot.html",{"msg":"invalid mailid or phone number","form":ForgotForm(request.GET)})
def Logout(request):
    del request.session["password"]
    msg = "logged out succ...."
    return render(request, 'welcome.html')
