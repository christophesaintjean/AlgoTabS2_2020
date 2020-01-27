from time import time
from random import randint, seed
from utils import estTrie

from CM3_triselect import triselect, triselect2

## Verification
seed(13)
T = [randint(1, 100) for _ in range(10)]
print(T)
triselect(T)
print("version 1 :", T)

seed(13)
T = [randint(1, 100) for _ in range(10)]
T2 = triselect2(T)
print("version 2 :", T2)

seed(13)
T = [randint(1, 100) for _ in range(3000)]
print("Le tableau résultat est trié:", estTrie(triselect(T)))



seed(13)
T = [randint(1, 100) for _ in range(30000)]
debut = time()
triselect(T)
fin = time()
print("Durée (tri par selection en place): ", fin - debut)

seed(13)
T = [randint(1, 100) for _ in range(30000)]
debut = time()
T2 = triselect2(T)
fin = time()
print("Durée (tri par selection version 2): ", fin - debut)