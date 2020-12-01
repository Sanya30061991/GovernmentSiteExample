from django.urls import path
from .views import main, start_2, start_3, reg, logon, log_ex


urlpatterns = [
    path('start1', start_2, name="start"),
    path('main', main, name="main"),
    path('auth', reg),
    path('login', logon, name="login"),
    path('logout', log_ex)
]
