from django.db import models
from django.utils import timezone

class Customer(models.Model):
    firstname = models.CharField(max_length=90, default='Unknown')
    lastname = models.CharField(max_length=90, default='Unknown')
    email = models.CharField(max_length=90, default='Not registered')
    check_requested = models.IntegerField(0, default='0')
    rating = models.IntegerField(default='-1')
    id = models.IntegerField(primary_key = True, default='0')

def __str__(self):
    return self.id
