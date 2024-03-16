from django.db import models

# Create your models here.
class UsersInfo(models.Model):
    first_name=models.TextField(max_length=20)
    last_name=models.TextField(max_length=20)
    email=models.EmailField()
    password=models.TextField(max_length=20)
    phone=models.IntegerField()
    def __str__(self):
        return "fname:%s,lname:%s,mailid:%s,phone:%d"%(self.first_name,self.last_name,self.email,self.phone)
