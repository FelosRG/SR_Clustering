"""
Código de ejemplo que genera un grid sobre el territorio Mexicano
-------
Sample code that generates a grid over the mexican territory.
"""

import os
import sys
import numpy as np
import geopandas as geopd
import matplotlib.pyplot as plt

script_path = os.path.realpath(__file__)
script_dir  = "/".join(script_path.split("/")[:-1])

DIR_ROOT = "/".join(script_path.split("/")[:-2])
PATH_SHAPEFILE = f"{DIR_ROOT}/Recursos/Mexico/Shapefiles/shape_file.shp"

sys.path.append(DIR_ROOT)
import utils

geodf = geopd.read_file(PATH_SHAPEFILE)

# Generamos el grid
resolucion_str = input("\nIngrese una resolución (ejemplo: >> 30)\n>> ")
resolucion = int(resolucion_str)

print(f"Generando el grid con resolución {resolucion}...")
grid = utils.generar_grid(resolucion=resolucion)

X , Y = grid["grid"]
Z = np.random.normal(size=(resolucion,resolucion))
Z = Z*grid["mask"]
Z[Z == False] = np.nan 

num_puntos = np.sum(grid["mask"])

# Mostramos en pantalla
fig , ax = plt.subplots(1)

ax.set_title(f"Test grid",weight="bold")
ax.set_title(f"num puntos: {num_puntos}",loc="right")
geodf.plot(ax=ax,color='white', edgecolor='black',linewidth=4)
ax.pcolormesh(X,Y,Z,shading="nearest",alpha=0.7)

plt.show()

print("Ok")