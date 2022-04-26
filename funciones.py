import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# abrimos DatasSet
df = pd.read_csv('peliculas.CSV', delimiter= ',', encoding = 'UTF-8')
print(df)

#creamos un DataFrame
df_new = pd.DataFrame({'Valoración película': df['vote_count'], 'Número de votos': df['vote_average']})
print(df_new)

#media
media = ((df['Valoración película'] * df['Número de votos']).sum())/(df['Número de votos'].sum())
media = round(media, 2)
print('La media es: ' + str(media))

#mediana
def calculo_mediana():
    ordenado = df.sort_values(by='Valoración película')
    suma = ordenado['Número de votos'].cumsum()
    q = df['Número de votos'].sum() / 2
    e = 1
    for i in suma:
        if q < i:
            return ordenado.iloc[e - 1, 0]
        else:
            e = e + 1

mediana = calculo_mediana()    
print('La mediana es:' + str(mediana))

#moda
a = 1
for i in df['Número de votos']:
    if i == df['Número de votos'].max():
        b = a
    else: 
        a = a + 1
moda = df.iloc[b-1,0]
print('La moda es: ' + str(moda))

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

#Cuartiles
def cuartiles(suma):
    e1 = 1
    e3 = 1
    q1 = (df['Número de votos'].sum() * 1)/4
    q3 = (df['Número de votos'].sum() * 3)/4
    
    for i in suma:
        if q1 < i:
            pass
        else:
            e1 = e1 + 1
        
        if q3 < i:
            pass
        else:
            e3 = e3 + 1 
    return [e1, e3]


ordenado = df.sort_values(by='Valoración película')
suma = ordenado['Número de votos'].cumsum()
Q = cuartiles(suma)

#Q1
Q1 = ordenado.iloc[Q[0] - 1, 0]
print('El 25% de los votos tiene un valor inferior a ' + str(Q1))

#Q2
Q2 = mediana
print('El 50% de los votos tiene un valor inferior a ' + str(Q2))

#Q3
Q3 = ordenado.iloc[Q[1] - 1, 0]
print('El 75% de los votos tiene un valor inferior a ' + str(Q3))


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