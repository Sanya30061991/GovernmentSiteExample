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
    ed_proj = models.IntegerField(name="ed_projects", default=0)
    health_proj = models.IntegerField(name="health_projects", default=0)
    military_proj = models.IntegerField(name="military_projects", default=0)
    social_proj = models.IntegerField(name="social_projects", default=0)
    cult_proj = models.IntegerField(name="cult_projects", default=0)
    is_staff = models.BooleanField(name="is_staff", default=False)

    class Meta:
        verbose_name = 'Citizen'
        verbose_name_plural = 'Citizens'

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " " + f"({self.department})" + f"[{self.rank}]"

# Create your models here.
class Project(models.Model):
    title = models.CharField(name="title", max_length=120)
    description = models.CharField(name="desc", max_length=1000)
    votes = models.IntegerField(default=0)
    sphere = models.CharField(name="sphere", max_length=15)
    date_of_creation = models.DateField(auto_now=True)
    creator = models.ForeignKey(Citizen, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title + f" {self.creator.user.first_name} {self.creator.user.last_name}"


class ProjectPhoto(models.Model):
    title = models.CharField(name="title", max_length=120)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    photo = models.ImageField(name="photo", upload_to='project_photos')

    class Meta:
        verbose_name = "Project photo"
        verbose_name_plural = "Project photos"
    
    def __str__(self):
        return self.title + f"({self.project.title})"