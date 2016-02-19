from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


#This is the task model.
class Task(models.Model):
    owner = models.ForeignKey(User, related_name="owned_tasks") #owner is an User object.
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=5000)
    collaborators = models.ManyToManyField(User, related_name="tasks") #collaborators can be multiple User objects
    isComplete = models.BooleanField() #Boolean attribute to inform if the task is complete.

