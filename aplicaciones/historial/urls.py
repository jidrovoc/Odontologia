from django.urls import path
from . import views

urlpatterns=[
    path('', views.inicio, name='inicio'),
    path('Historial',views.historial,name='historial'),
    path('Historial/nuevo', views.nuevaHistoria, name='nuevaHistoria')

]