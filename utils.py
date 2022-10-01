import os
import numpy as np
import geopandas as geopd

from pathlib import Path
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


# Método multiplataforma para manejar los directorios y paths.
script_path = Path(os.path.realpath(__file__))
script_dir  = script_path.parent.absolute()
PATH_SHAPEFILE_MEXICO = str(script_dir / "Recursos" / "Mexico" / "Shapefiles" / "shape_file.shp")

# Límites de las coordenadas que contienen el territorio mexicano.
LIM_SUP_LATITUD_MEX = 33
LIM_INF_LATITUD_MEX = 14.5
LIM_SUP_LONGITUD_MEX = -86.5
LIM_INF_LONGITUD_MEX = -117

def punto_valido(geopd,coord):
    """
    Un punto válido es aquel que está en algunos
    de los polígonos de la geometría.
    """
    p = Point(*coord)
    resultado = False
    for poligono in geopd["geometry"]:
        if resultado == True:
            break
        else:
            resultado = poligono.contains(p)
    return resultado

def generar_grid(resolucion):
    """
    Dados los límites establecidos y la resolución, genera 
    un grid de tamaño (resolucion,resolucion).

    Además genera un mask donde se indica que puntos pertenecen
    al territorio continental.
    """
    mexico_shapefile = geopd.read_file(PATH_SHAPEFILE_MEXICO)
    x = np.linspace(LIM_INF_LONGITUD_MEX,LIM_SUP_LONGITUD_MEX,resolucion)
    y = np.linspace(LIM_INF_LATITUD_MEX ,LIM_SUP_LATITUD_MEX,resolucion )
    X , Y = np.meshgrid(x,y) # El meshgrid es que nos proporciona las coordendas del grid.
    mask  = np.zeros(X.shape)
    # Revisamos que puntos son válidos.
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            mask_value = punto_valido(mexico_shapefile,(X[i,j],Y[i,j]))
            mask[i,j]  = mask_value

    output = {
        "points":(x,y),
        "grid"  :(X,Y),
        "mask"  :mask,
    }

    return output
