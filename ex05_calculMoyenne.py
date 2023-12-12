liste =[1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4]
moy = sum(liste)/len(liste)
print("la moyenne des valeurs de la liste: ", moy)
elet_positif = [elet for elet in liste if elet>0]
moy_positif = sum(elet_positif)/len(elet_positif) if elet_positif else 0
print("la moyenne des valeurs positives de la liste est :", moy_positif)
