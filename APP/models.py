from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.TextField(max_length=50)
    reg_no=models.CharField(max_length=7)


