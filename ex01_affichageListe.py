liste = [1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4]
print("Affichage des elements de la liste:")
for elt in liste:
    print(elt)

print("Affichage des elements de la liste dans l'ordre inverse:")
for i in range(len(liste) -1, -1, -1):
    print(liste[i])

