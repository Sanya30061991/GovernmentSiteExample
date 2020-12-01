from django.db import models
from django.contrib.auth.models import User

class Citizen(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # first_name = models.CharField(name="first_name", max_length=100)
    # email = models.CharField(name="email", max_length=100)
    # password = models.CharField(name="password", max_length=100)
    # last_name = models.CharField(name="last_name", max_length=100, default="")
    department = models.CharField(max_length=100)
    avatar = models.ImageField(name="avatar", upload_to='avatars')
    amount_of_accepted_projects = models.IntegerField(default=0)
    bday = models.DateField(name="birth_day", auto_now=False)
    gender = models.CharField(name="gender", default="Other", max_length=15, choices=[('Male','Male'), ('Female','Female'), ('Other','Other')])
    age = models.IntegerField(name="age", default=0)
    rank = models.CharField(name="rank", default="", max_length=100)

    class Meta:
        verbose_name = 'Citizen'
        verbose_name_plural = 'Citizens'

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + f"({self.department})" + f"[{self.rank}]"



# Create your models here.