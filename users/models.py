from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):
	name = models.CharField(max_length=50, blank=False)
	email = models.CharField(max_length=50, blank=False, unique=True)
	hashed_password = models.CharField(max_length=200)