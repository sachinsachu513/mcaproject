from django.db import models

# Create your models here.
class samapletable(models.Model):
    name=models.CharField(max_length=15)
    age=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.name


class submitform(models.Model):
    first_name=models.CharField(max_length=15)
    age=models.IntegerField()
    emailid=models.EmailField()
    adress=models.CharField(max_length=300)

    def __str__(self):
        return self.first_name