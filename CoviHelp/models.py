from django.db import models

# default User Model
from django.contrib.auth.models import User

# User Models for Information
class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)
    contact_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.user.username} - {self.contact_name}'


# Hospital Model
class Hospital(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.TextField(blank=True, default="")
    verified = models.BooleanField(default=False)
    verified_at = models.DateTimeField('verified', auto_now=True)


# Oxygen Supplier Model
class Oxygen(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.TextField(blank=True, default="")
    verified = models.BooleanField(default=False)
    verified_at = models.DateTimeField('verified', auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.state} - {self.city} - {self.contact} - {self.address} - {self.verified_at}'


# Medicine Supplier Model
class Pharma(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10, default="")
    state = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=50, default="")
    address = models.TextField(blank=True, default="")
    available_drugs = models.TextField(blank=True)
    verified = models.BooleanField(default=False)
    verified_at = models.DateTimeField('verified', auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.state} - {self.city} - {self.contact} - {self.address} -{self.available_drugs} - {self.verified_at}'
    ##available_drugs = models.ArrayField()

# Plasma Donor


class Plasma(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    donortype = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    verified = models.BooleanField(default=False)
    verified_at = models.DateTimeField('verified', auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.state} - {self.city} - {self.donortype} - {self.contact} - {self.verified_at}'

#Report
class Report(models.Model):
    item = models.CharField(max_length=200)
    comments = models.CharField(max_length=500)
    reported_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.item}'