from visitas.models import Solicitud

# Cambia el ID por el que deseas eliminar
def eliminar_solicitud(id):
    Solicitud.objects.filter(id=id).delete()
    print(f"Solicitud {id} eliminada.")

# Ejemplo de uso:
# eliminar_solicitud(1)
