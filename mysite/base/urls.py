from django.urls import path
from .views import ListaPendientes
from .views import DetalleTarea

urlpatterns = [path('',ListaPendientes.as_view(),name='pendientes'),
               path('tarea/<int:pk>',DetalleTarea.as_view(),name='tarea')]
