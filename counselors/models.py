from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Counselor(AbstractBaseUser):
    first_name = models.CharField(max_length=100, default='NOME')
    last_name = models.CharField(max_length=100, default='SOBRENOME')
    
    email = models.EmailField(max_length=200, unique=True)
    phone = models.CharField(max_length=14)
    county = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11)

    tagline = str(first_name) + str(last_name)
    full_name = str(first_name) + " " + str(last_name)

    # criar classe CounselorManager 
    # objects = CounselorManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def make_appointment(self):
        pass
