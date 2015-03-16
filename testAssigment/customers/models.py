from django.db import models
from django.utils import timezone

class Customer(models.Model):
    firstname = models.CharField(max_length=90)
    lastname = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    check_requested = models.IntegerField()
    rating = models.IntegerField()
    id = models.IntegerField(primary_key = True)

def __str__(self):
    return self.id
