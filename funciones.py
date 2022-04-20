
from typing import Counter
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

#máximo y mínimo
max = df['Valoración película'].max()
print('El valor máximo es: ' + str(max))
min = df['Valoración película'].min()
print('El valor mínimo es: ' + str(min))

#mediana
mediana = df['Valoración película'].median()
mediana = df['Número de votos'].sum() / 2
print(mediana)

#moda
moda = df['Número de votos'].max()
#fnfnfnf
print('La moda es : ' + str(moda))

#Q2
Q2 = mediana
print('El 50% de los votos tiene un valor inferior a ' + str(Q2))
#Q1


#Fórmula para la campana de Gauss
x = np.arange(min, max, 0.01)
f = 1/(desviacion_tipica * np.sqrt(2*np.pi)) * np.exp(-(x - media) ** 2/(2 * varianza))

#Pintamos gráfica

'''plt.style.use('seaborn')
plt.figure(figsize = (6,6))
plt.plot(x, f, color = 'black', linestyle = 'dashed')
plt.show()
'''
#Histograma
axis = df.plot.bar(x='Valoración película', rot = 0)
plt.show()