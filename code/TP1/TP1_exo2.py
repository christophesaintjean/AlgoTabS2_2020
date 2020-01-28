import random
from time import time
import matplotlib.pyplot as plt # a installer

def plusproche(T, x, diss):
    imin, dmin = 0, diss(T[0], x)
    for i, ti in enumerate(T):
        di = diss(ti, x)
        if  di <= dmin:
            imin, dmin = i, di
    return imin

def distance(a,b):
    return abs(a -b)

## Liste de taille n
def rand_liste(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1, 100))
    return L

## Liste de taille n
def rand_liste_comp(n):
    return [random.randint(1, 100) for _ in range(n)]

random.seed(13)
L = rand_liste(10)
print(L)
print(plusproche(L, 89, distance))


for n in [10, 1000, 1000000]:
    L = rand_liste(n)
    debut = time()
    plusproche(L, 3, distance)
    fin = time()
    duree = fin - debut
    print("Duree: ", duree, " pour ", n)
        

N = [1, 10**1, 10**2, 10**3, 10**4, 10**5,
     10**6, 2*10**6, 3*10**6, 4*10**6,
     5*10**6, 6*10**6, 7*10**6, 8*10**6,]  

tps = []
for n in N:
    L = rand_liste(n)
    debut = time()
    plusproche(L, 3, distance)
    fin = time()
    duree = fin - debut
    tps.append(duree)
    
plt.plot(N, tps)
plt.show()