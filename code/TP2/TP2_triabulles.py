from random import randint, seed

def estTrie(L, deb=0, fin=None):
    if fin is None:
        fin = len(L)
    for i in range(fin-1):
        if L[i] > L[i+1]:
            return False
    return True


def tribulles(T):
    for fin in range(len(T)-2, -1, -1):
        print(f"fin: {fin} ", T)
        for j in range(0, fin+1, 1):
            if T[j+1] < T[j]:
                print(j, f": Echange de {T[j]} et {T[j+1]}" )
                T[j+1], T[j] = T[j], T[j+1]
    return T


def tribulles2(T):
    for fin in range(len(T)-2, -1, -1):
        echange = False
        for j in range(0, fin+1, 1):
            if T[j+1] < T[j]:
                echange = True
                T[j+1], T[j] = T[j], T[j+1]
        if not echange:
            return T
    return T

seed(13)
T = [randint(1, 100) for _ in range(20)]
print(T)
tribulles2(T)
print(T)

"""
seed(13)
T = [randint(1, 100) for _ in range(30000)]
print("Le tableau résultat est trié:", estTrie(tribulles(T)))
"""