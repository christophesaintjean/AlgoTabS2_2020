from tqdm import tqdm, tqdm_gui  # a installer
from time import sleep
from random import randint

"""
for i in tqdm_gui(range(7)):
    duree_sommeil = randint(1, 4)
    #print("Iteration: ", i, "Duree : ", duree_sommeil)
    sleep(duree_sommeil)   
"""

for i in tqdm(range(3)):
    for j in tqdm(range(4)):
        duree_sommeil = randint(1, 4)
        sleep(duree_sommeil)







