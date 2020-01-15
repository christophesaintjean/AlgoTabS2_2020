 lifrom supp_tp1 import levenshteinDistance as diss

# Les puissances de 2

L = [2**i for i in range(11)]

# Une liste de tuples

L = [(i, 2*i, -i) for i in range(5)]

# les mots du dico
dico = []
with open('dico.txt', 'r') as f:
    for ligne in f:
        dico.append(ligne.rstrip('\n'))


dico[:10]
## ['a', 'abaissa', 'abaissable', 'abaissables', 'abaissai', 'abaissaient', 'abaissais', 'abaissait', 'abaissames', 'abaissant']

filtre1 = [mot for mot in dico if len(mot) == 8]
filtre1[:10]
## ['abaissai', 'abaissas', 'abaissat', 'abaissee', 'abaisser', 'abaisses', 'abaissez', 'abajoues', 'abandons', 'abatages']

filtre2 = [mot for mot in filtre1 if mot[0] == "c" and mot[3] == "e"]
filtre2[:10]
## ['cabernet', 'cabestan', 'cadencai', 'cadencas', 'cadencat', 'cadencee', 'cadencer', 'cadences', 'cadencez', 'cadettes']

filtre3 = [mot for mot in filtre2 if "k" in mot]
filtre3[:10]
## ['cokefiai', 'cokefias', 'cokefiat', 'cokefiee', 'cokefier', 'cokefies', 'cokefiez', 'cokeries']

# Liste de listes : distance de levenshtein
dico2 = dico[:6]

D = [[diss(m1, m2)['distance'] for m2 in dico2] for m1 in dico2]
print(D)

