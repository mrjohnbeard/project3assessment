from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm
# Create your views here.

def home(request):
  widgets = Widget.objects.all()
  form = WidgetForm()
  return render (request, 'home.html', {'widgets': widgets, 'form': form })

def add_widget(request):
    widget = WidgetForm(request.POST)
    if widget.is_valid():
        widget.save()
        return redirect('home')
    return redirect('home') 
  
def remove_widget(request, widget_id):
    widget = Widget.objects.get(id=widget_id)
    widget.delete()
    return redirect('home')