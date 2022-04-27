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
# Media aritmética
La media aritmética es el valor promedio de un conjunto de datos numéricos, en nuestro caso el número de votos, y se calcula sumando todos los conjuntos de valores y dividiéndolo entre el número total de valores.  
Pasos: 

1º Multiplicamos cada valoración de las películas por el número de votos que ha tenido cada una de ellas. Sumamos todos los resultados y los dividimos entre la suma total de los datos, en este caso los 10000.

2º Redondeamos al segundo decimal, mediante la función round(), dentro le indicamos el valor a redondear y los decimales.
```
media = ((df['Valoracion-pelicula'] * df['Numero-de-votos']).sum())/(df['Numero-de-votos'].sum())
media = round(media, 2)
print('La media es: ' + str(media))
```
# Mediana
La mediana es el valor que ocupa el lugar central de todos los datos cuando estos están ordenados de menor a mayor.

1º Hacemos una función que se va a encargar de ordenar las valoraciones de las películas, mediante la función .sort_values(by=columna), también nos mueve todas las columnas relacionadas con sus valores.

2º Tras ordenarla sumamos cada fila, es decir, sumaremos el primero con el anterior, al no haber sería sumarle cero, el segundo con el primero y ese valor se quedaría en la fila dos. Tras hacerlo con todos quien estaría en la última fila sería el número total de datos, es decir, los 10000. A todo esto, se le llama suma acumulativa, donde vamos sumando valores y al final obtenemos el conjunto entero. En vez de calcularlo a mano, usaremos .cumsum(), que nos creará una columna con dichos valores acumulados.

3º Como hemos explicado anteriormente, la mediana es el valor que ocupa la posición central, así que dividiremos el número total de datos entre 2. 

4º Haremos un bucle for donde irá mirando si el valor del medio es menor que alguno de los acumulados, si es así, el primer número mayor que el corresponde a la mediana. Pero claro, nosotros sabemos el valor acumulado que corresponde a la mediana y la fila que se encuentra, pero no la valoración que le corresponde. Para eso está la variable e, que se encarga de contar cuántos datos son menores que nuestro centro.

5º Esta función nos devolverá la valoración correspondiente en dicha fila. Accederemos a las filas mediante la función .iloc[número de fila, columna]

```
#mediana
def calculo_mediana():
    ordenado = df.sort_values(by='Valoracion-pelicula')
    suma = ordenado['Numero-de-votos'].cumsum()
    q = df['Numero-de-votos'].sum() / 2
    e = 1
    for i in suma:
        if q < i:
            return ordenado.iloc[e - 1, 0]
        else:
            e = e + 1

mediana = calculo_mediana()    
print('La mediana es:' + str(mediana))
```
# Moda
La moda, es el valor que más se repite de todos nuestros datos. Para calcularlo vamos a ver el máximo de número de votos y hallarnos su valoración correspondiente, seguiremos el mismo procedimiento que la del cálculo de la mediana.
```
#moda
a = 1
for i in df['Numero-de-votos']:
    if i == df['Numero-de-votos'].max():
        b = a
    else: 
        a = a + 1
moda = df.iloc[b-1,0]
print('La moda es: ' + str(moda))
```
# Varianza y desviación típica
La varianza es una medida de dispersión que representa cuanto varían los datos respecto a la media. Se calcula de la siguiente manera: 〖∑▒〖(valores(valoración películas)-〗 media)〗^2/n A cada valor de la valoración se le resta la media y se le eleva al cuadrado. Después se suman todos ellos y los dividimos entre el número total de valores.
La desviación típica es lo mismo que la varianza, pero en vez de ser en valores tan globales, es respecto a algunos en concreto. Para calcularla solo hay que hacer la raíz de la varianza. 
Pasos: 

1º Es aplicar la fórmula y le debemos multiplicar a cada valoración el número de votos que tiene.

2º Redondeamos al segundo decimal
```
# varianza
varianza = ((df['Numero-de-votos'] * ((df['Valoracion-pelicula'] - media)**2)).sum()/(df['Numero-de-votos'].sum()))
varianza = round(varianza, 2)
print('La varianza es: ' + str(varianza))
```
Con la desviación típica tan solo hacemos la raíz cuadrada de la varianza y lo redondeamos al segundo decimal.
```
#desviación típica
desviacion_tipica = varianza ** (1/2)
desviacion_tipica = round(desviacion_tipica, 2)
print('La desviación típica es: ' + str(desviacion_tipica))
```

