import pandas as pd
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "boardgames.settings")
django.setup()

from juegos.models import Juego, Tienda, Detalles

archivo_csv = 'juegos.csv'

data = pd.read_csv(archivo_csv)

for index, row in data.iterrows():
  tienda, created = Tienda.objects.get_or_create(nombre=row['tienda'])
  juego, created = Juego.objects.get_or_create(nombre=row['juego'])
  detalles, created = Detalles.objects.get_or_create(
    tienda = tienda,
    juego = juego,
    precio=row['precio'],
    url=row['url'],
    imagen_url=row['cover'])
  

