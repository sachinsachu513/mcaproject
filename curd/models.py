from django.db import models

# Create your models here.
class employees(models.Model):
    empno=models.IntegerField()
    empname=models.CharField(max_length=15)
    age=models.IntegerField()
    salary=models.IntegerField()
    adresss=models.CharField(max_length=50)
    email=models.EmailField()


    def __str__(self):
       return self.empname


