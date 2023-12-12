def nbr_entier(liste):
    total = 0
    for elet in liste:
        if isinstance(elet, int):
            total += 1
        elif isinstance(elet, list):
            total += nbr_entier(elet)
    return total

liste1 = [28, [12, [13, 1], -2, [[4, 5], -5]]]
result = nbr_entier(liste1)
print("le nombre des entiers dans la liste est :", result)
