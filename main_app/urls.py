from django.urls import path

from main_app.models import Widget
from . import views

urlpatterns = [
    path('', views.home, name='home')
]