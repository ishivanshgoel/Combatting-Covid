from django.db import models

# default User Model
from django.contrib.auth.models import User

# User Models for Information
class UserInfo(models.Model):
    TYPE = (
        ('H', 'Hospital'),
        ('O', 'Oxygen'),
        ('P', 'Pharma'),
        ('B', 'Plasma Donor'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)
    user_type = models.CharField(max_length=1, choices=TYPE)
    contact_name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.CharField(max_length=6)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username} - {self.user_type} - {self.city}'


## Hospital Model
class Hospital(models.Model):
    hospital_id = models.ForeignKey(User, on_delete=models.CASCADE)

## Oxygen Supplier Model
class Oxygen(models.Model):
    oxygen_id = models.ForeignKey(User, on_delete=models.CASCADE)
    available = models.CharField(max_length=5)

## Medicine Supplier Model
class Pharma(models.Model):
    pharma_id = models.ForeignKey(User, on_delete=models.CASCADE)
    ##available_drugs = models.ArrayField()
