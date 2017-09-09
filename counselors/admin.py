from django.contrib import admin
from django.db import models

# Register your models here.
from .models import Counselor

admin.site.register(Counselor)
