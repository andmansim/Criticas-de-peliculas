# Criticas-de-peliculas

Mi dirección de GitHub para este repositorio es el siguiente: [GitHub](https://github.com/andmansim/Criticas-de-peliculas.git)
https://github.com/andmansim/Criticas-de-peliculas.git

He realizado una explicación de como realizar un análisis estadístico de los números de votos de las valoraciones de películas. La cual, es la siguiente:

# Explicar críticas de películas
En este ejercicio vamos a realizar algo similar al ejercicio de unas notas en clase, es decir, realizaremos un análisis estadístico usando las funciones que vienen en Python. El enunciado dice así: Tenemos unas películas que han sido clasificadas del 0 al 10 por 10000 personas. Calcularemos su análisis estadístico para saber más datos sobre este suceso.

# Inicio
Comenzaremos por importar las librerías que nos van a ser de gran utilidad, las cuales son:
- Pandas
-	NumPy
-	Matplotlib
Pandas es una librería de Python especializada en el manejo y análisis de estructuras de datos. Sus usos principales son: definir nuevas estructuras de datos basadas en arrays(listas) de la librería NumPy, (que hablaremos más adelante), permite leer y escribir ficheros en formato CSV, Excel y bases de datos SQL, permite acceder a datos mediante sus índices o nombres de filas y columnas. También podemos reordenar, dividir y combinar datos, trabajar con series temporales y, por último, realiza operaciones de manera eficiente. 
NumPy es una librería especializada en el cálculo numérico y en el análisis de datos, especialmente para un gran volumen de datos. Además, nos permite trabajar con arrays/listas, que sirve para representar datos de un mismo tipo en varias dimensiones, al igual que es muy fácil manipular dichos datos.
Matplotlib, es una librería especializada en la creación de gráficos en dos dimensiones y personalizarlos.

Tras esta explicación de las librerías, vamos a importarlas para poder utilizarlas.
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```
# Crear DataFrame
Tenemos un DataSet con el ID, título, descripción, idioma, número de votos y valoración de las películas, pero a nosotros solo nos importa la valoración y el número de votos. Entonces, primero leeremos el fichero csv, mediante pandas:
```
df = pd.read_csv('pelicula.csv', delimiter = ';', encoding='UTF-8')
```
Para leerlo usamos la función read_csv() y dentro indicamos el nombre del fichero CSV, su delimitador, es decir, su formato de separación y el formato para transformarlo a Python.
Si lo imprimimos obtenemos:
```
<<<
        Id                           title  ... Numero-de-votos Valoracion-pelicula
0        0                        Ad Astra  ...            2853                 5.9
1        1                       Bloodshot  ...            1349                 7.2
2        2               Bad Boys for Life  ...            2530                 7.1
3        3                         Ant-Man  ...           13611                 7.1
4        4  Percy Jackson: Sea of Monsters  ...            3542                 5.9
...    ...                             ...  ...             ...                 ...
9782  9995                           Cargo  ...             225                 5.9
9783  9996                  The Good Night  ...              67                 5.6
9784  9997              The World Is Yours  ...             234                 7.1
9785  9998             The Grand Seduction  ...             169                 6.7
9786  9999        Woochi: The Demon Slayer  ...              78                 6.7
>>>
```
Ahora vamos a crear un DataFrame con solo los datos que nos interesan, así que hacemos lo siguiente:
```
df_new = pd.DataFrame({'Valoracion-pelicula': df['Valoracion-pelicula'], 'Numero-de-votos': df['Numero-de-votos']})
```
Recogeremos en una nueva variable el DataFrame, donde le pasamos un diccionario con el nombre de las columnas que necesitamos y sus valores, que accedemos a ellos mediante df[‘nombre de la columna’].
Y obtenemos:
```
<<<
      Valoracion-pelicula  Numero-de-votos
0                     5.9             2853
1                     7.2             1349
2                     7.1             2530
3                     7.1            13611
4                     5.9             3542
...                   ...              ...
9782                  5.9              225
9783                  5.6               67
9784                  7.1              234
9785                  6.7              169
9786                  6.7               78
>>>
```
