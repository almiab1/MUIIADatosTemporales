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
# #############################################################################

# Generate population
# #############################################################################
def gen_data(N):
    numeros = np.arange(1, N + 1, dtype=np.int64)  # Genera un arreglo de números del 1 al N
    # np.random.shuffle(numeros)  # Desordena el arreglo

    q3 = np.percentile(numeros, 75)  # tercer cuartil (75%)
    
    return numeros, q3

# #############################################################################
# Main
# #############################################################################
def main():
    random.seed(2023)
    
    N = 1000
    stream, cuartile = gen_data(N)
    
    n_intentos = 1000000
    n_subset = 1
    n_exec = 10
    
    tarjet_err = 0.1
    find_optimal = False
    
    while find_optimal != True:
        set_err = []
        
        for exec in range(1,n_exec+1):
            aciertos = 0
            for i in range(1,n_intentos+1):
                subset = np.random.choice(stream, n_subset)
                for item in subset:
                    if item >= cuartile:
                        aciertos += 1
                        break
            err = (n_intentos - aciertos) / n_intentos
            set_err.append(err)
            # print(f"Probabilidad de error del intento {exec} es {err}")
            
        final_err = sum(set_err) / n_exec
        print(f"El error final es {final_err} con k igual a {n_subset}")
        
        if(final_err < tarjet_err):
            find_optimal = True
        else:
            n_subset += 1
# #############################################################################
    
# #############################################################################
# Exec
# #############################################################################
if __name__ == "__main__":
    main()