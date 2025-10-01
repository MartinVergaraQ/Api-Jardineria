from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Endpoint API REST para asignar jardinero a una solicitud
@api_view(['POST'])
def api_asignar_jardinero(request):
    if request.method == 'GET':
        return Response({
            'info': 'API para asignar jardinero a una solicitud.',
            'method': 'POST',
            'required_params': {
                'solicitud_id': 'int (ID de la solicitud)',
                'jardinero_id': 'int (ID del jardinero)'
            },
            'example': {
                'solicitud_id': 1,
                'jardinero_id': 2
            }
        }, status=status.HTTP_200_OK)

    solicitud_id = request.data.get('solicitud_id')
    jardinero_id = request.data.get('jardinero_id')
    # Validar parámetros
    if not solicitud_id or not jardinero_id:
        return Response({
            'success': False,
            'error': 'Debes enviar solicitud_id y jardinero_id.'
        }, status=status.HTTP_400_BAD_REQUEST)
    try:
        solicitud = Solicitud.objects.get(id=solicitud_id)
        jardinero = Jardinero.objects.get(id=jardinero_id)
    except Solicitud.DoesNotExist:
        return Response({
            'success': False,
            'error': 'Solicitud no encontrada.'
        }, status=status.HTTP_404_NOT_FOUND)
    except Jardinero.DoesNotExist:
        return Response({
            'success': False,
            'error': 'Jardinero no encontrado.'
        }, status=status.HTTP_404_NOT_FOUND)
    if solicitud.jardinero:
        return Response({
            'success': False,
            'error': f'La solicitud ya tiene un jardinero asignado: {solicitud.jardinero.nombre}.'
        }, status=status.HTTP_400_BAD_REQUEST)
    solicitud.jardinero = jardinero
    solicitud.save()
    return Response({
        'success': True,
        'message': 'Jardinero asignado correctamente.',
        'solicitud': {
            'id': solicitud.id,
            'cliente_nombre': solicitud.cliente_nombre,
            'jardinero': jardinero.nombre
        }
    }, status=status.HTTP_200_OK)
from django.shortcuts import render, redirect
from .models import Solicitud
from .forms import SolicitudForm
from .models import Jardinero

def bienvenida(request):
    return render(request, 'visitas/bienvenida.html')


def nueva_solicitud(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            solicitud = form.save()
            return redirect('confirmar_cita', solicitud_id=solicitud.id)
    else:
        form = SolicitudForm()
    return render(request, 'visitas/nueva.html', {'form': form})

from django.utils import timezone
def confirmar_cita(request, solicitud_id):
    solicitud = Solicitud.objects.get(id=solicitud_id)
    if request.method == 'POST':
        solicitud.confirmado = True
        solicitud.hora_confirmada = timezone.now()
        solicitud.save()
        return redirect('cita_confirmada', solicitud_id=solicitud.id)
    return render(request, 'visitas/confirmar_cita.html', {'solicitud': solicitud})

def cita_confirmada(request, solicitud_id):
    solicitud = Solicitud.objects.get(id=solicitud_id)
    return render(request, 'visitas/cita_confirmada.html', {'solicitud': solicitud})


def vista_empresa(request):
    solicitudes = Solicitud.objects.all()
    jardineros = Jardinero.objects.all()

    error = None
    if request.method == 'POST':
        solicitud_id = request.POST.get('solicitud_id')
        jardinero_id = request.POST.get('jardinero_id')
        if not solicitud_id or not jardinero_id:
            error = "Debes seleccionar una solicitud y un jardinero."
        else:
            solicitud = Solicitud.objects.get(id=solicitud_id)
            jardinero = Jardinero.objects.get(id=jardinero_id)
            if solicitud.jardinero:
                error = f"La solicitud ya tiene asignado a {solicitud.jardinero.nombre}."
            else:
                solicitud.jardinero = jardinero
                solicitud.save()
                return redirect('vista_empresa')

    return render(request, 'visitas/empresa.html', {
        'solicitudes': solicitudes,
        'jardineros': jardineros,
        'error': error,
    })