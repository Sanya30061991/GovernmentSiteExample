from django.contrib import admin
from .models import Citizen, Project, ProjectPhoto

admin.site.register(Citizen)
admin.site.register(Project)
admin.site.register(ProjectPhoto)