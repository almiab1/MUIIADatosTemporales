# #############################################################################
# IMPORTS
# #############################################################################
import numpy as np
from memory_profiler import memory_usage
import time
# #############################################################################

# Generator
# #############################################################################
def gen_data(x, N, nombre_fichero):
    numeros = np.arange(1, N + 1, dtype=np.int64)  # Genera un arreglo de números del 1 al N

    numeros = np.delete(numeros, np.where(numeros == x))  # Elimina el número x del arreglo

    np.random.shuffle(numeros)  # Desordena el arreglo

    with open(nombre_fichero, 'w') as fichero:
        for numero in numeros:
            fichero.write(str(numero) + '\n')  # Escribe cada número en una línea del fichero
# #############################################################################

# Performance
# #############################################################################
def get_performance(func, *args):
    start_time = time.time()
    start_mem = memory_usage()[0]
    result = func(*args)
    end_time = time.time()
    mem_used = memory_usage()[0]
     
    time_elapsed = end_time - start_time
    # mem_used = end_mem - start_mem

    return result, time_elapsed, mem_used

