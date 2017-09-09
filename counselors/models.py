from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CounselorManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Insira um email válido.')

        if not kwargs.get('username'):
            raise ValueError('Insira um nome de usuário válido')

        if not kwargs.get('first_name'):
            raise ValueError('Insira um nome válido')

        if not kwargs.get('last_name'):
            raise ValueError('Insira um sobrenome válido')

        if not kwargs.get('phone'):
            raise ValueError('Insira um número de telefone válido')

        if not kwargs.get('county'):
            raise ValueError('Insira um município válido')

        if not kwargs.get('cpf'):
            raise ValueError('Insira um CPF válido')

        counselor = self.model(
            email = self.normalize_email(email),
            username = kwargs.get('username'),
            first_name = kwargs.get('first_name'),
            last_name = kwargs.get('last_name'),
            phone = kwargs.get('phone'),
            county = kwargs.get('county'),
            cpf = kwargs.get('county')
        )

        counselor.set_password(password)
        counselor.save()

        return counselor

    def create_superuser(self, email, password, **kwargs):
        counselor = self.create_user(email, password, **kwargs)

        counselor.is_admin = True
        counselor.save()

        return counselor

class Counselor(AbstractBaseUser):
    first_name = models.CharField(max_length=40, default='NOME')
    last_name = models.CharField(max_length=40, default='SOBRENOME')

    email = models.EmailField(max_length=200, unique = True)
    username = models.CharField(max_length=25, unique = True, default = 'username')
    phone = models.CharField(max_length=14)
    county = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11)

    tagline = str(first_name) + str(last_name)
    full_name = str(first_name) + " " + str(last_name)

    # criar classe CounselorManager
    # objects = CounselorManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name',
                       'last_name',
                       'email',
                       'phone',
                       'county',
                       'cpf']

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.username

    def make_appointment(self):
        pass
