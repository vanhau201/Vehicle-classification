from django.db import models
from django.db.models.fields import CharField, DateTimeField, FloatField
from django.db.models.fields.files import ImageField

# Create your models here.

class Vehicle(models.Model):
    image = ImageField(upload_to='image/')
    result = CharField(max_length=20,null=False)
    confidence = FloatField(null=False)
    date_created = DateTimeField(null=False)

