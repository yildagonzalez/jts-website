from django.urls import path
from . import views


urlpatterns = [
    path('', views.jts_contact, name='contact')
]