with open("liste_mots.txt", mode='r') as fichier:
    liste_mots = fichier.read().split("\n")

bornes = {}
i = 0
for c in range(65,91):
    char = chr(c)
    borne_debut = i
    while liste_mots[i][0] == char and i < len(liste_mots)-1:
        i += 1
    bornes[char] = (borne_debut, i)

# print(*bornes.items(), sep='\n')

def mot_existe(mot):
    deb, fin = bornes[mot[0]]
    for i, m in enumerate(liste_mots[deb:fin+1]):
        if mot == m:
            # print(f"Le mot existe !\nC'est: {liste_mots[i+deb]} ({i+deb})")
            return True
    return False

# for i in bornes.items():
#     print(i[0], liste_mots[i[1][0]], liste_mots[i[1][1]-1])
