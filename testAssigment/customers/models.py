from django.db import models
from django.utils import timezone

class Customer(models.Model):
    firstname = models.CharField(max_length=90, default='Unknown')
    lastname = models.CharField(max_length=90, default='Unknown')
    email = models.CharField(max_length=90, default='Not registered')
    rating = models.IntegerField(default='0')
    id = models.AutoField(primary_key = True, unique=True)
    rating_requested = models.BooleanField(default=False)

def __str__(self):
    return self.id
