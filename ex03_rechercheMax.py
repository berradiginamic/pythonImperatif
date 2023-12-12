liste =[1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4]
max_elet = liste[0]
for elet in liste:
    if elet>max_elet:
        max_elet = elet
print("le plus grand element de la liste est :", max_elet)
