# Solar Radiation Clustering


## Instalación Requerimientos Mac Os / Windows

1. Instalar  Anaconda o miniconda <br>

2. Descargar este repositorio y descoprimimos el .zip

3. Instalamos las librerías requeridas

    Nos vamos a la carpeta donde se descomprimió el repositorio y ejecutamos en una cosola o el powershell (Windows):

    ```
    conda create --name SRC --file requirements.txt

    ```


## Tests

### Generar un grid
Genera un mapa donde se divide al territorio mexicano en un grid de una resolución dada por el usuario.

[Solo Windows] <br>
Abrimos en un powersheel de anaconda o miniconda

[Windows/Mac/Linux] <br> 
Abrimos el enviroment donde tenemos instaladas las librerías:

```
conda activate SRC

```
Y ejecutamos el código

```
python Test/grid.py

```
