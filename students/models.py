from django.db import models

# Create your models here.
class students(models.Model):
    sroll_no=models.IntegerField()
    sname=models.CharField(max_length=30)
    slastname=models.CharField(max_length=30)

def __str__(self):
    return 'Student object with sroll_no: +str(self.no)'