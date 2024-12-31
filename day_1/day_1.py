#Importar las ubicaciones
import pandas as pd
#Parte Uno

# Crear el dataframe con los datos
datos = pd.read_csv("C:/Users/hpser/Downloads/proyectos/advent_of_code-2024/day_1/ubi.csv", header= None, delim_whitespace= True)
print(datos)
print(datos.head())  
print()
datos.columns = ['UbiID_1', 'UbiID_2']
print(datos)
#Ordenar los datos para poder calcular la distancia que existe entre ellos

print("\nDataFrame con las columnas ordenadas:")
datos['UbiID_1'] = datos['UbiID_1'].sort_values().reset_index(drop=True)
datos['UbiID_2'] = datos['UbiID_2'].sort_values().reset_index(drop=True)
print(datos)

#Calculo de las distancias
print()
datos['Distancia'] = abs(datos['UbiID_1']-datos['UbiID_2'])
print(datos)

#Calculo suma total de la distancia
total_distancia = sum(datos['Distancia'])
print(f"La distancia total entre las columnas 'UbiID_1', 'UbiID_2' será de {total_distancia} ")

#Parte Dos

# Calcular la frecuencia en la que cada número de la lista de la izquierda aparece en la lista de la derecha.
lista_izq = datos['UbiID_1']
lista_der = datos['UbiID_2']

frecuencia = lista_der.value_counts()
print(frecuencia)

similitud = (lista_izq.map(frecuencia).fillna(0) * lista_izq).sum()
print(f"La puntuación de similitud es: {similitud}")