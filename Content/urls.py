from django.urls import path
from .views import main, start, reg, logon, log_ex, profile


urlpatterns = [
    path('start', start, name="start"),
    path('main', main, name="main"),
    path('auth', reg),
    path('login', logon, name="login"),
    path('logout', log_ex),
    path('profile', profile)
]
