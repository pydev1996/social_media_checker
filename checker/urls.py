from django.urls import path
from .views import add_socialmediaurl

app_name = 'checker'

urlpatterns = [
    path('', add_socialmediaurl, name='add_socialmediaurl'),
]
