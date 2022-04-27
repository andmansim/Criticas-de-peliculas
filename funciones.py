import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# abrimos DatasSet
df = pd.read_csv('pelicula.csv', delimiter = ';', encoding='UTF-8')
print(df)
df1 = df
#creamos un DataFrame
df = pd.DataFrame({'Valoracion-pelicula': df['Valoracion-pelicula'], 'Numero-de-votos': df['Numero-de-votos']})
print(df)

#media
def calculomedia(v_p, n_v):
    m = ((v_p * n_v).sum())/(n_v.sum())
    return m
media = calculomedia(df['Valoracion-pelicula'], df['Numero-de-votos'])
#media = ((df['Valoracion-pelicula'] * df['Numero-de-votos']).sum())/(df['Numero-de-votos'].sum())
media = round(media, 2)
print('La media es: ' + str(media))

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

#moda
def calculomoda(n_v):
    a = 1
    for i in n_v:
        if i == n_v.max():
            b = a
            return b
        else: 
            a = a + 1
b = calculomoda(df['Numero-de-votos'])
moda = df.iloc[b-1,0]
print('La moda es: ' + str(moda))

#varianza
def varianza(v_p, n_v,m):
    v = ((n_v * ((v_p - media)**2)).sum()/(n_v.sum()))
    return v
varianza = varianza(df['Valoracion-pelicula'], df['Numero-de-votos'], media)
#varianza = ((df['Numero-de-votos'] * ((df['Valoracion-pelicula'] - media)**2)).sum()/(df['Numero-de-votos'].sum()))
varianza = round(varianza, 2)
print('La varianza es: ' + str(varianza))

#desviación típica
desviacion_tipica = varianza ** (1/2)
desviacion_tipica = round(desviacion_tipica, 2)
print('La desviación típica es: ' + str(desviacion_tipica))

#máximo y mínimo
max = df['Valoracion-pelicula'].max()
print('El valor máximo es: ' + str(max))
min = df['Valoracion-pelicula'].min()
print('El valor mínimo es: ' + str(min))

#Cuartiles
def cuartiles(suma):
    e1 = 1
    e3 = 1
    q1 = (df['Numero-de-votos'].sum() * 1)/4
    q3 = (df['Numero-de-votos'].sum() * 3)/4
    
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


ordenado = df.sort_values(by='Valoracion-pelicula')
suma = ordenado['Numero-de-votos'].cumsum()
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
axis = df.plot.bar(x='Valoracion-pelicula', rot = 0)
plt.show()