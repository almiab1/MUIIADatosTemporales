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
import matplotlib.pyplot as plt
# #############################################################################

# Generate histogram
# #############################################################################


def gen_hist(data, k, freq):
    # Generar el histograma
    hist, bins = np.histogram(
        data, bins=k, weights=freq)

    return hist, bins


def sq_error(a, b):
    s1 = p[b] - p[a]
    s2 = pp[b] - pp[a]
    print(f"S1 - {s1}, S2 - {s2}")
    return (s2 - (s1*s1)) / (b-a+1)

# #############################################################################
# Main
# #############################################################################


# random.seed(2023)<
# Definir los valores y las frecuencias
# data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# f = np.array([7, 3, 4, 5, 9, 10, 8, 1, 9, 4])
f = [4, 2, 3, 6, 5, 6, 12, 16]
n = len(f)
k = 3

# p = list(np.zeros(n+1))
# pp = list(np.zeros(n+1))

p = [0]
pp = [0]
for i in range(1, n+1):
    p.append(p[i-1] + f[i-1])
    pp.append(pp[i-1] + (f[i-1] ** 2))

best_err = []

for i in range(0, k):
    best_err.append([0])

#for i in range(0, n+1):
#    print(i, n)
#    best_err[0].append(sq_error(0, i))

index = []
index.append(0)

for bucket in range(1, k+1):
    # Find optimal histograms for [1..k]
    for item in range(1, n+1):
        if bucket == 1:
            best_err[item][bucket] = sq_error(1, item)
        else:
            # Multiple buckets
            best_err[item][bucket] = 999999999999
            # Try every possible last bucket
            for j in range(1, item-1):
                best_err[item][bucket] = best_err[j][bucket-1] + \
                    sq_error(j+1, item)


# ---------------------------------------------------------
#  Now we compute the V-opt. histogram with B buckets

#  Output:

#     BestError[k][i] = best error of histogram
#                       using k buckets
# 		  on data points (1..i)
#  ---------------------------------------------------------
# The dynamic algorithm uses these variables:

#  k = # buckets
#  i = current item - items processed are: (1..i)
#  BestError[k][i] = min. error in histogram of k buckets for f1..fi
for bucket in range(1, k+1):
    for item in range(1, n+1):
        best_err[bucket].append(999999999)
        for j in range(0, item):
            err = sq_error(j, item) + best_err[bucket-1][j]
            if err < best_err[bucket][item]:
                best_err[bucket][item] = err
                index.append(j)
