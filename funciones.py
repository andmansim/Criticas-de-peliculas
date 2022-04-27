import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


#media
def calculomedia(v_p, n_v):
    m = ((v_p * n_v).sum())/(n_v.sum())
    return m

#mediana
def calculo_mediana(df):
    ordenado = df.sort_values(by='Valoracion-pelicula')
    suma = ordenado['Numero-de-votos'].cumsum()
    q = df['Numero-de-votos'].sum() / 2
    e = 1
    for i in suma:
        if q < i:
            return ordenado.iloc[e - 1, 0]
        else:
            e = e + 1


#moda
def calculomoda(n_v):
    a = 1
    for i in n_v:
        if i == n_v.max():
            b = a
            return b
        else: 
            a = a + 1

#varianza
def varianza(v_p, n_v,m):
    v = ((n_v * ((v_p - m)**2)).sum()/(n_v.sum()))
    return v

#Cuartiles
def cuartiles(suma, df):
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

#Fórmula para la campana de Gauss
#x = np.arange(min, max, 0.01)
#f = 1/(desviacion_tipica * np.sqrt(2*np.pi)) * np.exp(-(x - media) ** 2/(2 * varianza))

#Pintamos gráfica

'''plt.style.use('seaborn')
plt.figure(figsize = (6,6))
plt.plot(x, f, color = 'black', linestyle = 'dashed')
plt.show()
'''
#Histograma
def representacion(df, desviacion_tipica, max, min, media, varianza):
    x = np.arange(min, max, 0.01)
    f = 1/(desviacion_tipica * np.sqrt(2*np.pi)) * np.exp(-(x - media) ** 2/(2 * varianza))
    
    fig, ax1 = plt.subplots()
    plt.subplot(1,1,1)
    ax1.hist(df['Valoracion-pelicula'])
    ax2 = ax1.twinx()
    ax2.plot(x, f, color = 'black', linestyle = 'dashed', linewidth=3)
    plt.axvline(media, color='red', linestyle='dashed', linewidth=1,label = str(media))
    plt.legend(loc='upper right')
    plt.show()

