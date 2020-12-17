from django.urls import path
from .views import main, start, reg, logon, log_ex, profile, project_make, finished_project


urlpatterns = [
    path('start', start, name="start"),
    path('main', main, name="main"),
    path('auth', reg),
    path('login', logon, name="login"),
    path('logout', log_ex),
    path('profile', profile),
    path('new_project', project_make),
    path('fin_project', finished_project)
]
