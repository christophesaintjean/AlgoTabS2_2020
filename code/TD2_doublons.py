from random import randint, seed

n = 10
T = [randint(1, n-1) for _ in range(2*n)]
T = [3, 4, 2, 1, 3, 2, 6, 3]

def doublons_naifs(T):
    cpt = 0
    for i, e in enumerate(T):
        for j in range(i+1, len(T)):
            if T[j] == e:
                #print("doublons:", i, ", ", j, " - > ", e)
                cpt += 1
                break
    print("Nombres de doublons: ", cpt)


def doublons_lineaire(T):
    cpt = 0
    for i in range(len(T)):
        print("i = ", i, T)
        if T[abs(T[i])] >= 0:
            T[abs(T[i])] = -T[abs(T[i])]
        else:
            print(abs(T[i]))
            cpt += 1
    print("Nombres de doublons: ", cpt)

print(T)
#doublons_naifs(T)
#doublons_lineaire(T)
#doublons_lineaire(sorted(T))
doublons_lineaire(T)
print(T)