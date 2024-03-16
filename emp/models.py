from django.db import models


# Create your models here.
class EmpMaster(models.Model):
    eid = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=50)
    salary = models.FloatField()
    gender = models.CharField(max_length=1)
    deptno = models.IntegerField()
    def __str__(self):
        return "%s,%s,%s,%s,%s" % (str(self.eid), self.ename, str(self.salary), self.gender, self.deptno)
