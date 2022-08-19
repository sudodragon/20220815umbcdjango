from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=32)
    dog_name = models.CharField(max_length=32)

class Dog(models.Model):
    name = models.CharField(max_length=32)
    breed = models.CharField(max_length=32)

