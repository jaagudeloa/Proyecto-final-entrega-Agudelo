# Tercera-pre-entrega-Agudelo

# Web para registro y seguimiento de condiciones Climatologicas

Este proyecto es una app web desarrollada con **Django** que permite gestionar algunas variables climatológicas como Temperatura[°C], Velocidad del Viento [m/s], horas solar pico (psh) [kWh/m2/d]. A meadiano plazo, se buscaria generar un modulo de análisis de datos que permita a través de dichas variables climatologicas identificar los mejores lugares geógraficos para desarrollar proyectos de energías renovables de tipo solar/fotovoltaica ó de energía eólica.

Fue creado respetando el  diseño **MVT (Model-View-Template)**

La aplicación incluye funcionalidades para agregar nuevos registros a la base de datos y buscar.

# Pasos para ejecutar:
1. Clonar el repositorio en la terminal de tu maquina local: 
git clone https://github.com/jaagudeloa/Proyecto-final-entrega-Agudelo

2. Crear entorno virtual: python -m venv env

3. Activar el entorno virtual: 
   env/Scripts/activate

4. Instalar las dependencias del proyecto en el entorno virtual: 
   pip install –r requirements.txt 

5. Iniciar el servidor:
   python manage.py runserver

6. Acceder desde el navegador al inicio del proyecto:
   http://127.0.0.1:8000

# Funcionalidades:

1. Pagina de inicio :
- URL : http://127.0.0.1:8000
- Descripcion: Es la pagina principal del proyecto donde se visualiza una barra de navegación para acceder a las diferentes secciones [Nosotros, Temperatura, Velocidad Viento, Radiación Solar, User]. La mayoria de menu son desplegables

2. CRUD de Temperatura:
- URL (http://127.0.0.1:8000/temperatura/) ó haciendo click en "Temperatura" en la barra de navegacion
- Descripcion: En este menú desplegable se puede realizar el registro de Temperatura para una ubicación determinada. Además se pueden hacer las operaciones CRUD. Se debe completar todos los campos.

3. CRUD de Velocidad Viento:
- URL (http://127.0.0.1:8000/wind/) ó haciendo click en "Velocidad Viento" en la barra de navegacion
- Descripcion: En este menú desplegable se puede realizar el registro de Velocidad de Viento para una ubicación determinada. Además se pueden hacer las operaciones CRUD. Se debe completar todos los campos.

4. CRUD de Radiación Solar:
- URL (http://127.0.0.1:8000/solar/) ó haciendo click en "Radiación sOLAR" en la barra de navegacion
- Descripcion:  En este menú desplegable se puede realizar el registro de Radiación Global para una ubicación determinada. Además se pueden hacer las operaciones CRUD. Se debe completar todos los campos.

5. User:
- URL (http://127.0.0.1:8000/cuentas/) ó haciendo click en "User" en la barra de navegacion
- Descripcion: En este menú desplegable se puede realizar el registro, el acceso y el logout de los usuarios

# Acceso al panel de administracion:
Inicia sesion con tu usuario para acceder al panel de administracion de Django y ver la base de datos:
Accede desde el navegador al login de administracion: http://127.0.0.1:8000/admin/ 

- Nombre de usuario: admin
- Contraseña: 1234