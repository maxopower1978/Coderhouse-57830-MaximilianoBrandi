# Coderhouse-57830-MaximilianoBrandi
Coderhouse - Proyecto Final Python

## Autor

Maximiliano Brandi: [Linkedin](linkedin.com/in/maximiliano-brandi-02725b61)

## Creación del repositorio y del proyecto Django

Este proyecto (webjuridica) se creó pensandolo para un estudio jurídico donde trabaja una amiga abogada.
En principio le servirá, ya que solo ella y yo tenemos acceso, a gestionar la parte de consultas y clientes.
A futuro la idea es mejora el principio DRY ya que no tengo conocimeintos en HTML, además que un usuario pueda loguearse, pero que este restringido solo a ver sus datos y a cargar documentos que necesite la abogada.
También podrá ver el styatus de sus procesos de asesoramiento

### Para clonar este proyecto

Abrir la Terminal o Powershell en un lugar donde sea accesible, cuyo directorio superior no tenga inicializado otro repositorio Git. Luego clonar el repositorio. Escribir `git clone` y luego presionar `ctrl + may + v` para pegar la URL copiada desde GitHub:

    git clone https://github.com/maxopower1978/Coderhouse-57830-MaximilianoBrandi.git

Acceder al repositorio:

    cd Coderhouse-57830-MaximilianoBrandi.git

Abrir  Visual Studio Code (VSCode) en la carpeta esta carpeta:

    code .

Nota: si no llegara a abrirse VSCode, abrirlo de la forma habitual, y luego en el menú elegir 'Archivo' y 'Abrir Carpeta', y buscar la carpeta creada por git clone.

### Dar permisos a Windows para luego activar el entorno virtual

Si usas Windows aparece, por única vez, abrir `Microsoft PowerShell` en modo **administrador**, y ejecutar el comando:

    Set-ExecutionPolicy Unrestricted

Luego cerrar todas las terminales abiertas para que los cambios tengan efecto.

### Activación del entorno virtual

Usuarios de Windows:
    python -m venv .venv
    .venv\Scripts\activate

### Instalación de dependencias

Ahora agregaremos los paquetes que usaremos en el proyecto:

    pip install django
    pip install pillow

## Crear rama `dev` en Git

Crear una rama `dev` y acceder a ella:

    git checkout -b dev

## Acceder al proyecto

Accedemos a la carpeta llamada `proyecto`:

    cd proyecto

Probamos que el servidor de Django funcione y abra el proyecto:

    python manage.py runserver

## Actualizar cambios de la nube a nuestro dispositivo

Si se llagaran a hacer cambios sobre rama main del repositorio remoto de GitHub, y esos cambios no fueron hechos en nuestro repositorio local, necesitamos actualizar nuestro repositorio local trayendo todos los commits desde GitHub.

Para ello usaramos pull. Verificamos que no tengamos ninguna modificación en nuestros archivos, o los descartamos, para no tener conflictos que resolver. Luego ejecutar:

    git pull

### Descripción del proyecto:

Como se menciono al principio, se trata de una web para un estudio jurídico, este fue realizado armando su estructura en:
1- Carpeta del proyecto - configuraciones (Config): 
Allí se parametrizaron el archivo settings.py y urls.py

2- Carpeta del proyecto - manejo de inicio y aspecto de página (App Home): 
Contiene los archivos 'static': las imágenes que carga la página. También los estilos CSS y las migraciones de esta app
Gestiona el incio, restringe consultas y clientes si no estás logueado, permite además cambios en los datos del perfil 

3- Carpeta del proyecto - App nosotros:
Es para mostrar un about_me de la profesional y de la persona que creo este proyecto.
También sirve para mostar los datos de contacto donde existe un formulario para enviar una consulta y un mapa de la localización del estudio. En el video la consulta es enviada pero al terminar el video se quitaron los datos del mail.

4- Carpeta del proyecto - App Derechos:
Aquí se crearon los difentes tipos de derechos que asesora la profesional, muestra solo un listado de los mismos
Se puede acceder desde el Inicio haciendo click en las fotos.
A futuro se linkeará la foto con el derecho que representa.

5- Carpeta del proyecto - App consultas:
Para acceder a esta app hay que tener usuario y contraseña de user (como comente al principio, solo la tenemos la abogada y yo(admin), no permitiendo el acceso de clientes hasta no hacer las modificaciones).
En esta app se realizo un CRUD. Se encarga de llevar el registro de todas las consultas que le van realizando.
Al modificar puede incluir la fecha de respuesta ya que la de consulta es la de hoy.
Para borrar pide confirmación.

6- Carpeta del proyecto - App clientes:
Para acceder a esta app hay que tener usuario y contraseña de user (como comente al principio, solo la tenemos la abogada y yo(admin), no permitiendo el acceso de clientes hasta no hacer las modificaciones).
En esta app se realizo un CRUD. Se encarga de llevar el registro de todos los clientes que van consultando.
Puede modificar todos los datos de los campos y además utiliza los avatares. Los avatares se encuentran en la carpeta media/avatares.
Para borrar pide confirmación.

#### Modificar la base datos:
Para modificar la base de datos ir al siguiente enlace:

http://127.0.0.1:8000/admin/login/?next=/admin/

y entrar con    Usuario: admin 
                Contraseña: 123

##### Sugerencias
Cualquier sugerencia puede ser enviada a maxi.brandi.2011@gmail.com

Gracias por leer este README.md