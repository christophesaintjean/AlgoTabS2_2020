from time import time
from random import randint, seed
from utils import estTrie

from CM3_triinsert import triinsert

seed(13)
T = [randint(1, 100) for _ in range(10)]
print(T)
triinsert(T)
print(T)

seed(13)
T = [randint(1, 100) for _ in range(3000)]
print("Le tableau résultat est trié:", estTrie(triinsert(T)))


seed(13)
T = [randint(1, 100) for _ in range(30000)]
debut = time()
triinsert(T)
fin = time()
print("Durée (tri par insertion): ", fin - debut)

debut = time()
triinsert(T)
fin = time()
print("Cas favorable (tri par insertion): ", fin - debut)

debut = time()
triinsert(T[::-1])
fin = time()
print("Cas défavorable (tri par insertion): ", fin - debut)
