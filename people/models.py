from django.db import models

# Create your models here.
class Person(models.Model):
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    nickname = models.CharField(max_length = 50, null = True, blank = True)
    email = models.EmailField()