import matplotlib.pyplot as plt
from time import time
from random import randint, seed

from CM3_triinsert import triinsert
from CM3_triselect import triselect

seed(13)

rep = 30
n = 20000

TopsTS, TopsTI = [], []
for _ in range(rep):
    T = [randint(1, 100) for _ in range(n)]
    debut = time()
    triselect(T)
    fin = time()
    TopsTS.append(fin - debut)

    T = [randint(1, 100) for _ in range(n)]
    debut = time()
    triinsert(T)
    fin = time()
    TopsTI.append(fin - debut)

plt.hist([TopsTS, TopsTI],
         label=['Selection', 'Insertion'],
         histtype='step', stacked=True, fill=False)
plt.legend()
plt.show()