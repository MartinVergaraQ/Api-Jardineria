# Jardinería App

## Instalación

1. Clona el repositorio:
   ```
   git clone <URL-del-repositorio>
   cd jardineria
   ```
2. Instala dependencias:
   ```
   pip install -r requirements.txt
   ```
3. Realiza migraciones:
   ```
   python manage.py migrate
   ```
4. Ejecuta el servidor:
   ```
   python manage.py runserver
   ```

## Uso
- Accede a `/cliente/` para crear una solicitud de visita.
- Accede a `/empresa/` para ver y asignar jardineros.
- Accede al admin en `/admin/` para gestionar datos.

## Eliminar solicitud por consola
Usa shell_plus:
```
python manage.py shell_plus
Solicitud.objects.filter(id=<ID>).delete()
```

## Mapa
La vista empresa muestra las ubicaciones usando Leaflet.

## Base de datos
Puedes usar SQLite (por defecto) o cambiar a Postgres editando `settings.py`.

## Requisitos
- Python 3.11+
- Django 4.2+
- Bootstrap, Leaflet, FontAwesome (CDN)


