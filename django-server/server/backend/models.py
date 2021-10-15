from django.db import models
from uuid import uuid4

def gen_uuid():
    return uuid4().hex

# Create your models here.

class User(models.Model):
    _id = models.UUIDField(primary_key=True, default=gen_uuid, editable=False)
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=30, unique=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, unique=True, editable=True)
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=True)