from django.urls import path
from .views import start, start_2, start_3, reg, logon


urlpatterns = [
    path('start1', start_2),
    path('main', main, name="main"),
    path('auth', reg),
    path('login', logon, name="login")
]
