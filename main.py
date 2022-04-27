import pandas as pd
from funciones import*
# abrimos DatasSet
df = pd.read_csv('pelicula.csv', delimiter = ';', encoding='UTF-8')
print(df)
df1 = df
#creamos un DataFrame
df = pd.DataFrame({'Valoracion-pelicula': df['Valoracion-pelicula'], 'Numero-de-votos': df['Numero-de-votos']})
print(df)
