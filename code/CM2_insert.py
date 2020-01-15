from tqdm import tqdm_gui
import random
from time import time


for _ in tqdm_gui(range(10**8)):
    val = random.randint(0, 100)
    L.append(val)


for _ in tqdm_gui(range(10**6)):
    pos = random.randint(0, len(L))  ## insertion avant
    val = random.randint(0, 100)
    L.insert(pos, val)


## Astuce
L = []
debut = time()
for i in range(10**3):
    L.insert(0, i)
fin = time()
duree = fin - debut
print("Duree Insert: ", duree)
L = []
debut = time()
for i in range(10**3):
    L.append(i)
L.reverse()
fin = time()
duree = fin - debut
print("Duree Append+Reverse: ", duree)