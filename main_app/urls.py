from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addwidget/', views.add_widget,
         name='add_widget'),
     path('removewidget/<int:widget_id>/', views.remove_widget, name='remove_widget')
]