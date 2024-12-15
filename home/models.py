from django.db import models


class Test(models.Model):
    firstname = models.CharField(max_length=200, blank=True)
    lastname = models.CharField(max_length=200, blank=True)
    number = models.BigIntegerField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.CharField(max_length=200, blank=True)
    password = models.CharField(max_length=128, blank=True)
    paddress = models.CharField(max_length=200, blank=True)
    taddress = models.CharField(max_length=200, blank=True)
    selectpradesh = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=200, blank=True)
    message = models.TextField(blank=True)
    stream = models.CharField(max_length=200, blank=True)
    file = models.FileField(null=True, upload_to='')
    checkbox = models.CharField(max_length=200, blank=True)

