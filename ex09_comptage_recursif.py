def nbr_entier(liste, min_elet, max_elet):
    total = 0
    for elet in liste:
        if isinstance(elet, int):
            if min_elet <= elet <= max_elet:
                total += 1
        elif isinstance(elet, list):
            total += nbr_entier(elet, min_elet, max_elet)
    return total

liste1 = [28, [12, [13, 1], -2, [[4, 5], -5]]]
min_elet = 10
max_elet = 15
result = nbr_entier(liste1, min_elet, max_elet)
print("le nombre des entiers dans la liste  entre 10 et 15 est :", result)
