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