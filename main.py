import pandas as pd
from funciones import*

if __name__ == '__main__':
    # abrimos DatasSet
    df = pd.read_csv('pelicula.csv', delimiter = ';', encoding='UTF-8')
    print(df)
    df1 = df
    #creamos un DataFrame
    df = pd.DataFrame({'Valoracion-pelicula': df['Valoracion-pelicula'], 'Numero-de-votos': df['Numero-de-votos']})
    print(df)

    #media
    media = calculomedia(df['Valoracion-pelicula'], df['Numero-de-votos'])
    media = round(media, 2)
    print('La media es: ' + str(media))

    #mediana
    mediana = calculo_mediana(df)    
    print('La mediana es:' + str(mediana))

    #moda
    b = calculomoda(df['Numero-de-votos'])
    moda = df.iloc[b-1,0]
    print('La moda es: ' + str(moda))

    #varianza
    varianza = varianza(df['Valoracion-pelicula'], df['Numero-de-votos'], media)
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

    #cuartiles
    ordenado = df.sort_values(by='Valoracion-pelicula')
    suma = ordenado['Numero-de-votos'].cumsum()
    Q = cuartiles(suma, df)

    #Q1
    Q1 = ordenado.iloc[Q[0] - 1, 0]
    print('El 25% de los votos tiene un valor inferior a ' + str(Q1))

    #Q2
    Q2 = mediana
    print('El 50% de los votos tiene un valor inferior a ' + str(Q2))

    #Q3
    Q3 = ordenado.iloc[Q[1] - 1, 0]
    print('El 75% de los votos tiene un valor inferior a ' + str(Q3))

    #Representación 
    representacion(df)