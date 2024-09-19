# Coderhouse-57830-MaximilianoBrandi
Coderhouse - Proyecto Final Python


## Autor

Maximiliano Brandi: [Linkedin](linkedin.com/in/maximiliano-brandi-02725b61)

## Creación del repositorio y del proyecto Django

Este proyecto (webjuridica) se creó pensandolo para un estudio jurídico. una amiga abogadacreado servirá para dos cosas. Primero: seguir la clase con lo mismo que estoy haciendo, con sus respectivos ejercicios. Y segundo, para que puedan crear ramas, y hacer pruebas. Para eso, dejen la rama principal (main) solamente para la clase, y para las pruebas, utilicen otra rama, como puede ser alguna  llamada "prueba".

### Crear un repositorio en GitHub y clonarlo

Abrir GitHub e iniciar sesión. Crear un nuevo repositorio y darle un nombre (usar la plantilla Python para `.gitignore` y activar casilla `README.md`). Hacer clic en el botón 'Code' y copiar el enlace que comienza con `https`.

Abrir la Terminal o Powershell en un lugar donde sea accesible, cuyo directorio superior no tenga inicializado otro repositorio Git. Luego clonar el repositorio. Escribir `git clone` y luego presionar `ctrl + may + v` para pegar la URL copiada desde GitHub:

    git clone NombreRepositorio

Acceder al repositorio:

    cd NombreRepositorio

Abrir  Visual Studio Code (VSCode) en la carpeta esta carpeta:

    code .

Nota: si no llegara a abrirse VSCode, abrirlo de la forma habitual, y luego en el menú elegir 'Archivo' y 'Abrir Carpeta', y buscar la carpeta creada por git clone.

### Dar permisos a Windows para luego activar el entorno virtual

Si usas Windows aparece, por única vez, abrir `Microsoft PowerShell` en modo **administrador**, y ejecutar el comando:

    Set-ExecutionPolicy Unrestricted

Luego cerrar todas las terminales abiertas para que los cambios tengan efecto.

### Instalación de `uv`

Usaremos `uv`, que es un moderno rápido administrador de proyectos para Python, escrito en Rust. Ver la [página oficial](https://docs.astral.sh/uv/).

Instalación para Windows:

    powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

Instalación para macOs y Linux:

    curl -LsSf https://astral.sh/uv/install.sh | sh

Luego de la instalación, reiniciar la terminal.

Para actualizar `uv` (cuando ya lo hayamos instalado) ejecutar en la terminal:

    uv self update

### Sincronización de un proyecto Python

Si tenemos en algún proyecto el archivo `pyproject.toml` que tiene las dependencias que necesitamos para el desarrollo, por ejemplo: `django` y `pillow`, y otras  herramientas para el desarrollo, que no son propias del proyecto, como por ejemplo: `ruff`, `djlint` y `ipython`, entonces, sólo necesitamos sincronizar el proyecto con el siguiente comando:

    uv sync

Automáticamente se creará el entorno virtual y agregará las dependencias ya predefinidas. Restará activar el entorno para poder ejecutar los scripts, como por ejemplo `django-admin`

### Creación de un proyecto desde 0 con `uv`

Una vez `uv` instalado y actualizado, crear una carpeta con el nombre del proyecto, vacía, acceder a ella, y ejecutar:

    uv init

Esto creará algunos archivos. Nunca deberemos eliminar `pyproject.toml` y `uv.lock`. Podemos probar ejecutando:

    python hello.py

Ya podemos borrar `hello.py`

Luego creamos el entorno virtual:

    uv venv

### Activación del entorno virtual

Una vez que se haya creado la carpeta `.venv` gracias al comando `uv venv` (si el proyecto no tiene el archivo pyproject.toml) o `uv sync` (si el proyecto sí tiene el archivo pyproject.toml), entonces, debemos activarlo, para luego agregar las dependencias que usaremos en el proyecto:

Usuarios de Windows:

    .venv\Scripts\activate

Uuarios de Linux o Mac:

    source .venv/bin/activate

### Instalación de dependencias

Ahora agregaremos los paquetes que usaremos en el proyecto:

    uv add django
    uv add pillow

Y los paquetes que servirán de herramienta para el desarrollo:

    uv add ruff --dev
    uv add djlint --dev
    uv add ipython --dev

Finalmente podemos ver la estructura de los paquetes:

    uv tree

Si queremos borrar un paquete, podemos usar:

    uv remove djlint --dev

o

    uv remove pillow

Hemos visto una herramiento superior a `pip` y otros administradores, por su velocidad y simplicidad. Además, no hace falta que tengamos Python instalado en el sistema. Ver la documentación oficial para más información.

## Crear rama `dev` en Git

Crear una rama o branch llamada `dev`, que es una abreviatura de development, es decir, desarrollo:

    git branch dev

Cambiar a esa rama:

    git switch dev

Listar las ramas para ver que se esté bien parado.

    git branch

## Creación del proyecto Django

Creamos una carpeta llamada `project`:

    mkdir project

Accedemos a ella:

    cd project

Instalamos la configuración de Django ahí

    django-admin startproject config .

Observemos el espacio y el punto del comando anterior. son importantes.

Probamos que el servidor de Django funcione:

    python manage.py runserver

Abrir en el navegador la ruta y el puerto que nos da Django:

    127.0.0.1:8000

En el navegador, veremos la bienvenida de Django.

## Fusión de cambios a la rama principal y actualiza del repositorio GitHub

Como nuestro proyecto fue creado y el servidor se ejecuta normalmente, uniremos lo nuevo de la rama `dev` a la rama principal.

Agregamos todos los nuevos archivos al área de preparación (staging area):

    git add .

Observar el espacio y el punto del comando anterior.

Hacemos el commit y pasamos todo lo del área de preparación al área de repositorio:

    git commit -m "Agregado proyecto django"

Nos cambiamos a la rama main:

    git switch main

Traemos los commits de dev a main. Podemos hacerlo de dos formas:

    git merge dev

También podemos usar `git rebase dev` según nuestras preferencias.

Llevaremos nuestro repositorio local de la rama main, al repositorio remoto GitHub (Git llama al repositorio remoto:  origin)

    git push

Verificar los cambios en Github, presionando F5 para recargar la página

## Actualizar cambios de la nube a nuestro dispositivo

Si se llagaran a hacer cambios sobre rama main del repositorio remoto de GitHub, y esos cambios no fueron hechos en nuestro repositorio local, necesitamos actualizar nuestro repositorio local trayendo todos los commits desde GitHub.

Para ello usaramos pull. Verificamos que no tengamos ninguna modificación en nuestros archivos, o los descartamos, para no tener conflictos que resolver. Luego ejecutar:

    git pull