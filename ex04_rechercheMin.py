liste =[1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4]
min_elet = liste[0]
for elet in liste:
    if elet < min_elet:
        min_elet= elet
print("le plus petit element de la liste est :", min_elet)
