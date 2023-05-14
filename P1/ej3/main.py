# #############################################################################
# File: main.py
# Description: 
# Author: Mira Abad, Alejandro
# #############################################################################

# #############################################################################
# IMPORTS
# #############################################################################
import random
import numpy as np
import pandas as pd
# #############################################################################

# Generate population
# #############################################################################
def gen_data(dict):
    # Crear la lista basada en el diccionario
    lista = [valor for valor, frecuencia in dict.items() for _ in range(frecuencia)]
    return lista


# #############################################################################
# Main
# #############################################################################
def main():
    random.seed(2023)
    # Definir los valores y las frecuencias
    valores = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    frecuencias = np.array([7, 3, 4, 5, 9, 10, 8, 1, 9, 4])

    # Calcular la frecuencia total
    frecuencia_total = sum(frecuencias)

    # Definir el número de intervalos
    num_intervalos = 6

    # Calcular la frecuencia objetivo para cada intervalo
    frecuencia_objetivo = frecuencia_total / num_intervalos

    # Crear los intervalos
    intervalos = []
    frecuenciasFin = []
    intervalo_actual = []
    frecuencia_actual = 0

    for valor, frecuencia in zip(valores, frecuencias):
        frecuenciasFin.append(0)
        
        if frecuencia_actual + frecuencia <= frecuencia_objetivo:
            # Si agregar el valor actual no excede la frecuencia objetivo, agregarlo al intervalo actual
            intervalo_actual.append(valor)
            frecuencia_actual += frecuencia
            
            index = intervalos.index(intervalos[-1]) if len(intervalos) > 0 else 0
            frecuenciasFin[index] = frecuencia_actual
        else:
            # Si agregar el valor actual excede la frecuencia objetivo, iniciar un nuevo intervalo
            intervalos.append(intervalo_actual)
            intervalo_actual = [valor]
            frecuencia_actual = frecuencia
            
            index = intervalos.index(intervalos[-1]) if len(intervalos) > 0 else 0
            frecuenciasFin[index] = frecuencia_actual
        
        
    # Asegurarse de agregar el último intervalo
    if intervalo_actual:
        intervalos.append(intervalo_actual)
        # frecuenciasFin.append(frecuencia_actual)

    # Imprimir los intervalos
    for i, intervalo in enumerate(intervalos):
        print(f'Intervalo {i+1}: {intervalo}')
    for i, freq in enumerate(frecuenciasFin):
        print(f'Freq {i+1}: {freq}')
# #############################################################################
    
# #############################################################################
# Exec
# #############################################################################
if __name__ == "__main__":
    main()