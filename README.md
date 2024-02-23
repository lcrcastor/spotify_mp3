#Tools

Para descargar camciones o lista desde Spotify

descargar con pip spotdl

```python
pip install spotdl
spotdl --download-ffmpeg

```

Tener en cuenta de ingresar el path para correr la app 

En el archivo playlist.json es un ejemplo de como debe formarse la url de la lista o la cancion sale de spotify desde compartir -> copia enlace plylist 



```json
{
    "listas" : [
        ["ZAMBAS CARPERAS", "https://open.spotify.com/playlist/0abxyl8WW1QhPSkCqMaef2?si=f9c2de6c45454246"],
        ["This Is Jorge Rojas","https://open.spotify.com/playlist/37i9dQZF1DZ06evO2ohD8p?si=580681e4673647c4"]
    ]
}
```

---------

# Creando entornos virtuales

El script usado para crear y manejar entornos virtuales es pyvenv. pyvenv normalmente instalará la versión mas reciente de Python que tengas disponible; el script también es instalado con un número de versión, con lo que si tienes múltiples versiones de Python en tu sistema puedes seleccionar una versión de Python específica ejecutando python3 o la versión que desees.

Para crear un entorno virtual, decide en que carpeta quieres crearlo y ejecuta el módulo venv como script con la ruta a la carpeta:

```console
python3 -m venv tutorial-env
```
Esto creará el directorio tutorial-env si no existe, y también creará directorios dentro de él que contienen una copia del intérprete de Python y varios archivos de soporte.

Una ruta común para el directorio de un entorno virtual es .venv. Ese nombre mantiene el directorio típicamente escondido en la consola y fuera de vista mientras le da un nombre que explica cuál es el motivo de su existencia. También permite que no haya conflicto con los ficheros de definición de variables de entorno .env que algunas herramientas soportan.

Una vez creado el entorno virtual, podrás activarlo.

En Windows, ejecuta:

```console
tutorial-env\Scripts\activate
```

En Unix o MacOS, ejecuta:

```console
source tutorial-env/bin/activate
```
(Este script está escrito para la consola bash. Si usas las consolas csh or fish, hay scripts alternativos activate.csh y activate.fish que deberá usar en su lugar.)

Activar el entorno virtual cambiará el prompt de tu consola para mostrar que entorno virtual está usando, y modificará el entorno para que al ejecutar python sea con esa versión e instalación en particular. Por ejemplo:

```console
$ source ~/envs/tutorial-env/bin/activate
(tutorial-env) $ python
Python 3.5.1 (default, May  6 2016, 10:59:36)
  ...
>>> import sys
>>> sys.path
['', '/usr/local/lib/python35.zip', ...,
'~/envs/tutorial-env/lib/python3.5/site-packages']
>>>
```
Para desactivar el entorno virtual, digita:

deactivate
en el terminal.

