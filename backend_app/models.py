from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tasks(models.Model):
    category = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    priority = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    subtask = models.JSONField(blank=True, null=True)
    users = models.ManyToManyField(User, related_name='tasks')
    def __str__(self):
        return self.name
        
class Contacts(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    emblem = models.CharField(max_length=20)
    color = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    