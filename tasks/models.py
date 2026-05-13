from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
  user_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name="tasks")
  task=models.CharField(max_length=30)
  is_completed=models.BooleanField(default=False)
  
  def __str__(self):
    return f'{self.task}:{self.is_completed}'
  
admin.site.register(Task)
