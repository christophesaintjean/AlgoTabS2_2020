import matplotlib.pyplot as plt
from time import time
from random import randint, seed
from tqdm import tqdm

from CM3_triinsert import triinsert
from CM3_triselect import triselect
from CM4_trifusion import trifusion

seed(13)

rep = 10
pmax = 14
N = [2**p for p in range(pmax)]

TopsTS_m, TopsTS_mean, TopsTS_M = [], [], []
TopsTI_m, TopsTI_mean, TopsTI_M = [], [], []
TopsTF_m, TopsTF_mean, TopsTF_M = [], [], []


for n in tqdm(N):
    temp = []
    for _ in range(rep):
        T = [randint(1, 100) for _ in range(n)]
        debut = time()
        triselect(T)
        fin = time()
        temp.append(fin - debut)
    TopsTS_m.append(min(temp))
    TopsTS_mean.append(sum(temp)/len(temp))
    TopsTS_M.append(max(temp))

    temp = []
    for _ in range(rep):
        T = [randint(1, 100) for _ in range(n)]
        debut = time()
        triinsert(T)
        fin = time()
        temp.append(fin - debut)
    TopsTI_m.append(min(temp))
    TopsTI_mean.append(sum(temp) / len(temp))
    TopsTI_M.append(max(temp))

    temp = []
    for _ in range(rep):
        T = [randint(1, 100) for _ in range(n)]
        debut = time()
        trifusion(T)
        fin = time()
        temp.append(fin - debut)
    TopsTF_m.append(min(temp))
    TopsTF_mean.append(sum(temp) / len(temp))
    TopsTF_M.append(max(temp))


plt.fill_between(N, TopsTS_m, TopsTS_M, label='Selection', alpha=0.5)
plt.fill_between(N, TopsTI_m, TopsTI_M, label='Insertion', alpha=0.5)
plt.fill_between(N, TopsTF_m, TopsTF_M, label='Fusion', alpha=0.5)
plt.plot(N, TopsTS_m, N, TopsTI_m, N, TopsTF_m)
plt.legend()
plt.xscale("log")
plt.show()