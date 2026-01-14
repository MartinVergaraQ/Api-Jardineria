# Jardinería App (Django)

Aplicación demo en Django para gestión de solicitudes de jardinería, con dos vistas principales (Cliente / Empresa) y visualización de ubicaciones en mapa (Leaflet).

## Tecnologías
- Python 3.11+
- Django 4.2+
- Bootstrap + FontAwesome (CDN)
- Leaflet (mapa)

## Instalación (local)

1) Clonar el repositorio:
bash
git clone https://github.com/MartinVergaraQ/Api-Jardineria.git
cd Api-Jardineria

python -m venv .venv
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

Instalar dependencias:
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Uso

/cliente/: crear una solicitud de visita.

/empresa/: visualizar solicitudes y asignar jardineros, incluyendo mapa.

/admin/: administración de datos.


