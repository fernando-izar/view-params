from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=255)
