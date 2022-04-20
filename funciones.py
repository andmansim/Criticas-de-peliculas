import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#creamos un DataFrame
df = pd.DataFrame({'Valoración película': np.array([5, 4, 3, 2, 1, 0]), 'Número de votos': np.array([40, 99, 145, 133, 96, 40])})
print(df)
#media
media = ((df['Valoración película'] * df['Número de votos']).sum())/(df['Número de votos'].sum())
print(round(media, 2))

