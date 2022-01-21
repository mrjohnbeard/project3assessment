from django.shortcuts import render
from .models import Widget

# Create your views here.

def home(request):
  widgets = Widget.objects.all()
  return render (request, 'home.html', {' widgets': widgets})