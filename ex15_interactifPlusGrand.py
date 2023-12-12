liste = []
for i in range(1, 11):
    nbre = float(input(f"veuillez donner un nombre {i} :"))
    liste.append(nbre)
max_nbre = max(liste)
print(f"le plus grand nombre des nombres donnés est : {max_nbre}")
