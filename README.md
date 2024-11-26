# Tercera-pre-entrega-Agudelo

# Web para registro y seguimiento de condiciones Climatologicas

Este proyecto es una app web desarrollada con **Django** que permite gestionar algunas variables climatologicas como Temperatura[°C], Velocidad del Viento [m/s], horas solar pico (psh) [kWh/m2/d]. A meadiano plazo, se buscaria generar un modulo de análisis de datos que permita a través de dichas variables climatologicas identificar los mejores lugares geógraficos para desarrollar proyectos de energías renovables de tipo solar/fotovoltaica ó de energía eólica.

Fue creado respetando el  diseño **MVT (Model-View-Template)**

La aplicación incluye funcionalidades para agregar nuevos registros a la base de datos y buscar.

# Pasos para ejecutar:
1. Clona el repositorio en la terminal de tu maquina local: 
git clone https://github.com/jaagudeloa/Tercera-pre-entrega-Agudelo.git

2. Crear entorno virtual: python -m venv env

3. Activar el entorno virtual: 
   env/Scripts/activate

4. Instalar las dependencias del proyecto en el entorno virtual: 
   pip install –r requirements.txt 

5. Iniciar el servidor:
   python manage.py runserver

6. Acceder desde el navegador al inicio del proyecto:
   http://127.0.0.1:8000/home/

# Funcionalidades:

1. Pagina de inicio :
- URL : http://127.0.0.1:8000/home/
- Descripcion: Es la pagina principal del proyecto donde se visualiza una barra de navegación para acceder a las secciones de registro 

2. Registro de articulos:
- URL /art/ O haciendo click en "Articulos" en la barra de navegacion
- Descripcion: En esta pagina se puede realizar el registro de articulos, ingresando un codigo en formato texto, una descripcion en formato texto y un precio en formato decimal. Es obligatorio completar todos los campos y presionar el boton "Enviar" para realizar el registro del articulo. Podes realizar el registro de un articulo y luego buscarlo en la pagina de inicio, para comprobar que se creo exitosamente.

3. Registro de rubros:
- URL /rub/ O haciendo click en "Rubros" en la barra de navegacion
- Descripcion: En esta pagina se puede realizar el registro de rubros, ingresando un codigo en formato texto y una descripcion en el mismo formato. Es obligatorio completar todos los campos y presionar el boton "Enviar" para realizar el registro del rubro.

4. Registro de clientes:
- URL /cli/ O haciendo click en "Clientes" en la barra de navegacion
- Descripcion: En esta pagina se puede realizar el registro de clientes, ingresando un nombre en formato texto, un email en formato Email, un telefono y una direccion en formato texto. Es obligatorio completar todos los campos y presionar el boton "Enviar" para realizar el registro del cleinte.

5. Registro de proveedores:
- URL /prov/ O haciendo click en "Proveedores" en la barra de navegacion
- Descripcion: En esta pagina se puede realizar el registro de proveedores, ingresando un nombre en formato texto, un email en formato Email, un telefono y una direccion en formato texto. Es obligatorio completar todos los campos y presionar el boton "Enviar" para realizar el registro del proveedor.

# Acceso al panel de administracion:
Inicia sesion con tu usuario para acceder al panel de administracion de Django y ver la base de datos:
Accede desde el navegador al login de administracion: http://127.0.0.1:8000/admin/ 

- Nombre de usuario: admin
- Contraseña: 1234


## Funcionalidades

1. **Listar registros:**
   - Libros: Visualiza todos los libros disponibles con su titulo, autor y genero
   - Autores: Muestra una lista de autores registrados
   - Generos: Visualiza los generos literarios disponibles.

2. **Buscar libros:**
   - Encuentra libros ingresando su título o parte del mismo en el formulario de busqueda.

3. **Agregar registros:**
   - Agrega nuevos libros, autores o géneros por medio de formularios

4. **Navegacion de la aplicacion:**
http://127.0.0.1:8000

Funcionalidad
Pagina principal        http://127.0.0.1:8000
Lista de libros         http://127.0.0.1:8000/libros/
Lista de autores	    http://127.0.0.1:8000/autores/
Lista de generos	    http://127.0.0.1:8000/generos/
Buscar libros	        http://127.0.0.1:8000/buscar/
Agregar nuevo libro	    http://127.0.0.1:8000/agregar_libro/
Agregar nuevo autor	    http://127.0.0.1:8000/agregar_autor/
Agregar nuevo genero	http://127.0.0.1:8000/agregar_genero/



- **Lista de libros:** Muestra todos los libros disponibles.
- **Lista de autores:** Muestra todos los autores registrados.
- **Lista de generos:** Muestra los generos literarios disponibles.
- **Formulario de busqueda:** Busca libros por su título.
- **Agregar registros:** Formularios para agregar libros, autores y generos.
