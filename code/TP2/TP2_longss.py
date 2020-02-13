def longss1(T, x):
    longueur_courante = 0
    position_max, longueur_max = None, 0

    for i in range(len(T)):
        if T[i] == x:
            longueur_courante += 1
            if longueur_courante > longueur_max:
                longueur_max = longueur_courante
                position_max = i - longueur_courante + 1
        else:
            longueur_courante = 0
    if longueur_max > 0:
        return position_max, longueur_max
    return None, 0






def longss2(chaine):
    caractere_courant, longueur_courante = chaine[0], 0
    caractere_max, position_max, longueur_max = chaine[0], 0, 0

    for i in range(len(chaine)):
        if chaine[i] == caractere_courant:
            longueur_courante += 1
            if longueur_courante > longueur_max:
                longueur_max = longueur_courante
                position_max = i - longueur_courante + 1
                caractere_max = caractere_courant
        else:
            caractere_courant = chaine[i]
            longueur_courante = 1

    return caractere_max, position_max, longueur_max


def longss2_bis(chaine):
    longueur_courante = 1
    caractere_max, position_max, longueur_max = chaine[0], 0, 1

    for i in range(1, len(chaine)):
        if chaine[i] == chaine[i - 1]:
            longueur_courante += 1
            if longueur_courante > longueur_max:
                longueur_max = longueur_courante
                position_max = i - longueur_courante + 1
                caractere_max = chaine[i]
        else:
            longueur_courante = 1
    return caractere_max, position_max, longueur_max


def longss3(chaine):
    dico = {}
    caractere_courant, longueur_courante = chaine[0], 0
    for i in range(len(chaine)):
        if chaine[i] == caractere_courant:
            longueur_courante += 1
            if chaine[i] not in dico.keys() or longueur_courante > dico[chaine[i]][1]:
                dico[chaine[i]] = (i - longueur_courante + 1, longueur_courante)
        else:
            longueur_courante = 1
            caractere_courant = chaine[i]
    return dico


if __name__ == "__main__":
    str = "aabbbccccaaaca"
    #str = ["a", "a", "b", "b", "b", "c", "c", "c", "c", "a", "a", "a", "c", "a"]
    print(str)

    print(longss1(str, "a"))
    print(longss1(str, "b"))
    print(longss1(str, "c"))
    print(longss1(str, "d"))

    T = [1, 2, 3, 3, 3, 2, 4, 4, 4, 4, 3]
    print(T)

    print(longss1(T, 4))

    print(longss2(str))
    print(longss2_bis(str))
    print(longss3(str))
