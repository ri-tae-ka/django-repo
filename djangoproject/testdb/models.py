from django.db import models

class user(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
