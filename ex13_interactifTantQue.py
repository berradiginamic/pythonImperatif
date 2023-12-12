while True:
    nbr_utilisateur = int(input("Veuillez donner un nombre :"))
    if 1<=nbr_utilisateur<=10:
       print("la valeur est bonne ")
       break
    else:
       print("le nombre n'est pas entre 1 et 10, veuillez réessayer : ")
