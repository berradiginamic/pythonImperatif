liste1 =[1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4]
liste2 =[3, -8, 17, 5, -1, 4, 0, 6, 2, 11, -5, -4, 8]
set1 = set(liste1)
set2 = set(liste2)
elet_commun = set1 & set2
nbr_elet_commun = len(elet_commun)
print("nombre des valeurs communs de 2 listes est :", nbr_elet_commun)
