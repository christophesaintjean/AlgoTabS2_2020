from time import time
from random import randint, seed
from utils import estTrie

from CM5_trirapide import trirapide, trirapide_bis

seed(13)
T = [randint(1, 100) for _ in range(10)]
print(T)
trirapide(T)
print(T)

seed(13)
T = [randint(1, 100) for _ in range(3000)]
trirapide(T)
print("Le tableau résultat est trié:", estTrie(T))

seed(13)
T = [randint(1, 100000) for _ in range(1000000)]
debut = time()
#trirapide(T)
fin = time()
print("Durée tri rapide: ", fin - debut)

seed(13)
T = [randint(1, 1000) for _ in range(1000000)]
debut = time()
trirapide_bis(T)
fin = time()
print("Durée tri rapide_bis: ", fin - debut)