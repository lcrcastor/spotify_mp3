# -*- coding: utf-8 -*-
import subprocess
import json
import os


def playlist():
    #Abre el archivo en modo lectura
    with open("playlist.json") as datos:
        #Lee el contenido del archivo
        playlist = json.load(datos)

    lista= playlist['listas']
    print(lista)
    print(len(lista))
    return lista


def descargar_cancion(lista):
    #Comando para ejecutar spotdl con la URL de la canción
    # Obtener la ruta al directorio superior
    # ojo colocar la ruta de su equipo 
    
    ruta = "/Volumes/KINGSTON/proyectos/Spotify/Descargas"
    os.chdir(ruta)
    for  url in lista:
        print(url)
        ruta_lista=ruta + "/"+ url[0]
        os.makedirs(url[0])
        os.chdir(ruta_lista)
        comando = ["spotdl", url[1]]

        #Ejecutar el comando y capturar la salida
        try:
            resultado = subprocess.run(comando, capture_output=True, text=True, check=True)
            salida = resultado.stdout
            print(salida)
            os.chdir(ruta)
        except subprocess.CalledProcessError as e:
            print("Error al descargar la canción:", e)



#URL de la canción de Spotify
#url_cancion = "https://open.spotify.com/track/TU_URL_DE_CANCION_AQUI"

#Llamar a la función para descargar la canción
descargar_cancion(playlist())
#playlist()

