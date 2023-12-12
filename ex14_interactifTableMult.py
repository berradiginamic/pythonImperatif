while True:
    nbr_utilisateur = int(input("Veuillez donner un nombre entre 1 et 10 :"))
    if 1<=nbr_utilisateur<=10:
       print(f"table de multiplication de {nbr_utilisateur} est :")
       for i in range(1, 11):
           result = nbr_utilisateur*i
           print(f"{nbr_utilisateur} * {i} = {result}")
       break
    else:
       print("le nombre n'est pas entre 1 et 10, veuillez réessayer : ")
