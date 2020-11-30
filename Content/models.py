from django.db import models
from django.contrib.auth.models import User

class Citizen(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    avatar = models.ImageField(name="avatar", upload_to='avatars')
    amount_of_accepted_projects = models.IntegerField(default=0)
    last_name = models.CharField(name="surname", max_length=100, default="")

    class Meta:
        verbose_name = 'Citizen'
        verbose_name_plural = 'Citizens'

# Create your models here.