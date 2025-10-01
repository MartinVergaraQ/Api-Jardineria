from django.urls import path
from . import views

urlpatterns = [
    path('', views.bienvenida, name='bienvenida'),
    path('cliente/', views.nueva_solicitud, name='nueva_solicitud'),
    path('empresa/', views.vista_empresa, name='vista_empresa'),
    path('confirmar-cita/<int:solicitud_id>/', views.confirmar_cita, name='confirmar_cita'),
    path('cita-confirmada/<int:solicitud_id>/', views.cita_confirmada, name='cita_confirmada'),
    path('api/asignar-jardinero/', views.api_asignar_jardinero, name='api_asignar_jardinero'),
]
