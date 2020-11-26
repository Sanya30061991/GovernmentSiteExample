from django.urls import path
from .views import start, start_2, start_3


urlpatterns = [
    path('', start),
    path('start1', start_2),
    path('start2', start_3)
]
