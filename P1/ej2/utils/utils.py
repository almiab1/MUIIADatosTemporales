# #############################################################################
# IMPORTS
# #############################################################################
import numpy as np
from memory_profiler import memory_usage
import time
# #############################################################################

# Generator
# #############################################################################
def gen_data(N):
    numeros = np.arange(1, N + 1, dtype=np.int64)  # Genera un arreglo de números del 1 al N
    # np.random.shuffle(numeros)  # Desordena el arreglo

    q3 = np.percentile(numeros, 75)  # tercer cuartil (75%)
    
    return numeros, q3
# #############################################################################