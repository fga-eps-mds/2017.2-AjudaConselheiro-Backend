from django.db import models


class Counselor(models.Model):
    full_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=200, unique=True)
    phone_number = models.CharField(max_length=14)
    county = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11)
