def somme_nombres_pairs(liste):
    somme = 0
    for element in liste:
        if element % 2 == 0:
            somme += element
    return somme
liste = [1, -5, 9, 41, -16, 52, 11]
resultat = somme_nombres_pairs(liste)
print("resultat est", resultat)



print("-----------------------")

def est_palindrome(chaine):
    revert_chaine = chaine[::-1]
    return revert_chaine == chaine
chaine = "rattar"
print(est_palindrome(chaine))

print("------------------------")

def extraction(liste1, minimum, maximum):
    resultat1 =[]
    for element1 in liste1:
        if minimum<=element1<=maximum:
            resultat1.append(element1)
    return resultat1

liste1 = [1, 5, -10, 8, 9, -4, 0]
resultat1 = extraction(liste1, 1, 8)
print(resultat1)


print("--------------------")

def moyenne(liste):
    return sum(liste)/len(liste)

liste2 = [10, 15, 20, 25, -9]
result = moyenne(liste2)
print("la moyenne est :", result)
