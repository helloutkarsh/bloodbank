from django.db import models
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.constraints import UniqueConstraint
from django.db.models.enums import Choices
# Create your models here
bloodGroupChoices=(
    ('A+','A+'),
    ('B+','B+'),
    ('A-','A-'),
    ('B-','B-'),
    ('AB+','AB+'),
    ('AB-','AB-'),
    ('O+','O+'),
    ('O-','O-')
)

class Donors(models.Model):
    id = models.UUIDField(default = uuid.uuid1, editable = False)
    Full_Name = models.CharField(max_length=75)
    Mobile_Number = models.CharField(primary_key=True,max_length=10 )
    City=models.CharField(max_length=75)
    Pincode=models.CharField(max_length=6)
    Gender=models.TextChoices('Male','Female')
    Document_ID=models.CharField(unique=True,max_length=12)
    date=models.DateTimeField(auto_now_add=True,editable=False)
    BLOOD_GROUP = models.CharField(max_length=9,choices=bloodGroupChoices, default='A+')
    
   