import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#creamos un DataFrame
df = pd.DataFrame({'Valoración película': np.array([5, 4, 3, 2, 1, 0]), 'Número de votos': np.array([40, 99, 145, 133, 96, 40])})
print(df)

#media
media = ((df['Valoración película'] * df['Número de votos']).sum())/(df['Número de votos'].sum())
media = round(media, 2)
print('La media es: ' + str(media))

#varianza
varianza = ((df['Número de votos'] * ((df['Valoración película'] - media)**2)).sum()/(df['Número de votos'].sum()))
varianza = round(varianza, 2)
print('La varianza es: ' + str(varianza))

#desviación típica
desviacion_tipica = varianza ** (1/2)
desviacion_tipica = round(desviacion_tipica, 2)
print('La desviación típica es: ' + str(desviacion_tipica))