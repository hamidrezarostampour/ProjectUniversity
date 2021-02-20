from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='ایمیل', default='test@tes.te')
    address = models.TextField(verbose_name='آدرس', default='lahijan')
    fullname = models.CharField(max_length=200, verbose_name='نام و نام خانوادگی', default='taghi taghizade')