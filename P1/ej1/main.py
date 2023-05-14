# #############################################################################
# File: main.py
# Description: 
# Author: Mira Abad, Alejandro
# #############################################################################

# #############################################################################
# IMPORTS
# #############################################################################
import numpy as np
import pandas as pd
import random as rand

from memory_profiler import profile
from utils.utils import *
# #############################################################################

@profile
def encontrar_numero_faltante(stream_file, N):
    total_sum = N * (N + 1) // 2  # Calcula la suma total esperada de la secuencia de 1 a N
    sum_actual = 0

    with open(stream_file, 'r') as fichero:
        for linea in fichero:
            numero = int(linea.strip())  # Lee un número del fichero y lo convierte a entero
            sum_actual += numero  # Actualiza la suma actual

    numero_faltante = total_sum - sum_actual  # Calcula el número faltante

    return numero_faltante

# #############################################################################
# Main
# #############################################################################
def main():
    # Ejemplo de uso
    x = 455
    stream_file = './src/datos_desordenados.txt'
    
    problem_size= [100,500,1000,5000,10000,50000,100000,500000,1000000]
    resultados = []
    
    # N = 100000
    # gen_data(x, N, stream_file)
    # numero_faltante = encontrar_numero_faltante(stream_file, N)
    # print("El número faltante es:", numero_faltante)
    
    for N in problem_size:  # Prueba valores de N desde 100 hasta 100000 en pasos de 11100
        # Ejecutar experimeinto
        gen_data(x, N, stream_file)
        numero_faltante, tiempo, memoria = get_performance(encontrar_numero_faltante, stream_file, N)
        resultados.append({"N": N, "Tiempo (s)": tiempo, "Memoria (MB)": memoria})
        print(f"Para N={N}, el número faltante es: {numero_faltante}, tiempo: {tiempo} segundos, memoria: {memoria} MB")

    df = pd.DataFrame(resultados)
    print(df)
    df.to_csv("./src/results.csv")
# #############################################################################
    
# #############################################################################
# Exec
# #############################################################################
if __name__ == "__main__":
    main()