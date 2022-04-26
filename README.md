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
