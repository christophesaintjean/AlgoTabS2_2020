import matplotlib.pyplot as plt
from time import time
from random import randint, seed

from CM3_triinsert import triinsert
from CM3_triselect import triselect

seed(13)

rep = 10
pmax = 16
N = [2**p for p in range(pmax)]

TopsTS_m, TopsTS_M = [], []
TopsTI_m, TopsTI_M = [], []


for n in N:
    temp = []
    for _ in range(rep):
        T = [randint(1, 100) for _ in range(n)]
        debut = time()
        triselect(T)
        fin = time()
        temp.append(fin - debut)
    TopsTS_m.append(min(temp))
    TopsTS_M.append(max(temp))

    temp = []
    for _ in range(rep):
        T = [randint(1, 100) for _ in range(n)]
        debut = time()
        triinsert(T)
        fin = time()
        temp.append(fin - debut)
    TopsTI_m.append(min(temp))
    TopsTI_M.append(max(temp))


plt.fill_between(N, TopsTS_m, TopsTS_M, label='Selection', alpha=0.5)
plt.fill_between(N, TopsTI_m, TopsTI_M, label='Insertion', alpha=0.5)
plt.legend()
plt.xscale("log")
plt.show()