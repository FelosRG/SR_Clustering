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

from pathlib import Path

script_path = Path(os.path.realpath(__file__))
script_dir  = script_path.parent.absolute()
DIR_ROOT = script_dir.parent.absolute()

sys.path.append(str(DIR_ROOT))
import utils

geodf = geopd.read_file(utils.PATH_SHAPEFILE_MEXICO)

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
ax.set_title(f"resolución: {resolucion}",loc="left")
geodf.plot(ax=ax,color='white', edgecolor='black',linewidth=2.5)
ax.pcolormesh(X,Y,Z,shading="nearest",alpha=0.7)
plt.show()

print("Ok")