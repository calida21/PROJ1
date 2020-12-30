from django.db import models

class patient(models.Model):
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    number=models.CharField(max_length=10)
    emergency_number=models.CharField(max_length=10)
    age=models.IntegerField()
    health_condition=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    alternate_email=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    psw=models.CharField(max_length=100)

class doctor(models.Model):
    full_name=models.CharField(max_length=100)
    hospital_name=models.CharField(max_length=100)
    number_doc=models.CharField(max_length=10)
    email_doc=models.CharField(max_length=100)
    username_doc=models.CharField(max_length=100)
    psw_doc=models.CharField(max_length=100)