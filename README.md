# Registro de Entidades (Proyecto Django)

Este proyecto es una aplicación web desarrollada con Django para la gestión y registro de diferentes tipos de entidades de servicio (públicas y privadas), como hospitales, talleres, clínicas, comisarías, etc. Permite la creación, edición y visualización de estas entidades, incluyendo su nombre, un icono representativo y su estado (activo/inactivo).

## Características Principales

* **Gestión de Tipos de Entidad:** CRUD (Crear, Leer, Actualizar, Desactivar/Activar) para los tipos de entidades.
* **Iconos de Material Design:** Integración de iconos de Google Material Design para una representación visual clara de cada tipo de entidad.
* **Interfaz de Usuario Amigable:** Basado en un tema de Material Dashboard para una experiencia de usuario moderna y responsiva.
* **Notificaciones de Usuario:** Mensajes de éxito para confirmar operaciones realizadas.

## Tecnologías Utilizadas

* **Backend:** Python 3.x, Django
* **Bases de Datos:** PostgreSQL (desarrollo), compatible con PostgreSQL (producción)
* **Entornos Virtuales:** Pipenv (con compatibilidad para Pip)
* **Frontend:** HTML, CSS (Bootstrap, Material Dashboard), JavaScript
* **Iconos:** Google Material Design Icons
* **Herramientas de Desarrollo:** django-widget-tweaks

## Instalación y Configuración (Para Desarrolladores)

Sigue estos pasos para poner el proyecto en marcha en tu máquina local.

### Prerrequisitos

* Python 3.x instalado.
* Git instalado.
* Pipenv instalado (`pip install pipenv`).

### Pasos de Instalación

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/tu-usuario/nombre-del-repositorio.git](https://github.com/tu-usuario/nombre-del-repositorio.git)
    cd nombre-del-repositorio
    ```

2.  **Configura el entorno virtual con Pipenv:**
    Instala las dependencias y crea el entorno virtual:
    ```bash
    pipenv install
    ```
    Si ya tienes un `Pipfile.lock`, puedes usar:
    ```bash
    pipenv sync
    ```

3.  **Configura las variables de entorno:**
    Crea un archivo `.env` en la raíz del proyecto basándote en el archivo `.env.example`.
    ```bash
    cp .env.example .env
    ```
    Edita el archivo `.env` y rellena los valores. **¡Asegúrate de generar una `SECRET_KEY` segura para entornos de producción!**

4.  **Ejecuta las migraciones de la base de datos:**
    Activa el entorno virtual y ejecuta las migraciones:
    ```bash
    pipenv shell
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Crea un superusuario (opcional, para acceder al admin de Django):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Inicia el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```

    Ahora puedes acceder a la aplicación en tu navegador en `http://127.0.0.1:8000/`.

## Despliegue (Recomendaciones)

Para el despliegue en producción, se recomienda usar un servidor web como Gunicorn (para servir la aplicación Django) y Nginx (como proxy inverso y para servir archivos estáticos). La base de datos debe ser PostgreSQL.

### Generación de `requirements.txt` (Para compatibilidad con Pip)

Si necesitas desplegar tu aplicación o compartir las dependencias con un entorno que no use Pipenv (sino Pip directamente, como Heroku o algunos servicios de hosting), puedes generar un archivo `requirements.txt` a partir de tu `Pipfile.lock`.

Para generar `requirements.txt`:

1.  Asegúrate de que tu entorno virtual de Pipenv esté activo (`pipenv shell`).
2.  Ejecuta el siguiente comando:
    ```bash
    pipenv lock -r > requirements.txt
    ```
    Este comando lee el `Pipfile.lock` (que es el archivo exacto de tus dependencias fijas) y las exporta al formato `requirements.txt`.

Luego, en un entorno que use Pip, la instalación se haría con:
```bash
pip install -r requirements.txt