
from django.db import models

# Create your models here.
class student(models.Model):
    name = models.TextField(max_length=20)
    id = models.TextField(primary_key=True,max_length=10)
    doa = models.DateField(auto_now_add=True)

class classroom(models.Model):
   c_no = models.IntegerField(primary_key=True)
   c_teacher = models.TextField(max_length=20)

class marks(models.Model):
    physics = models.IntegerField()
    chemistry = models.IntegerField()
    maths = models.IntegerField(primary_key=True)

class teachers(models.Model):
    t_name = models.TextField(max_length=30)
    t_id = models.IntegerField(primary_key=True,max_length=10)    

     
        