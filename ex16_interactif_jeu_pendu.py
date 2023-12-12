import random

# Lecture du fichier et création d'une liste de mots
file = open("mots.txt")
mots = [ligne.strip() for ligne in file.readlines()]
file.close()

# Choix d'un mot aléatoire
mot=mots[random.randint(0, len(mots))]

# Masque du mot
masque="_"*len(mot)

# Nom d'erreur du joueur
nb_error=0

# Nombre d'erreur max.
nb_max=random.randint(5, 10)

# Nombre de lettres restantes à trouver
nb_lettres=len(mot)

# Lettres déjà proposées
lettres_proposes=[]

# Affichage des infos sur le mot à découvrir
# et le nombre d'erreurs max autorisés
print("Le mot à découvrir contient :"+str(len(mot))+" lettres")
print("Pour gagner vous devez faire moins de "+str(nb_max)+" fautes.")
# démarrage du jeu
game=True

# Tant que game vaut true le jeu continu
while game:

    # Affichage du masque
    print(masque)

    choix_lettre= ""
    while len(choix_lettre)!=1:
        print("Veuillez saisir une lettre:")
        choix_lettre = input().upper()

    # On regarde si le choix de lettre n'a pas déjà été proposé
    if choix_lettre not in lettres_proposes:
        lettres_proposes.append(choix_lettre)

        # On regarde ensuite si le choix est dans le mot
        if choix_lettre in mot:
            print("La lettre est présente dans le mot")

            # Si la lettre est présente, il faut récupérer tous ses index
            indexes = [index for index, c in enumerate(mot) if c == choix_lettre]

            # _____ et j'ai trouvé la lettre E à l'index 2
            for index in indexes:
                masque = masque[0:index] + choix_lettre + masque[index + 1:len(masque)]
                nb_lettres-=1
        else:
            nb_error+=1
            print(f"La lettre n'est présente dans le mot. Vous avez {nb_error} erreur(s)")
    else:
        print("Vous avez déjà proposé cette lettre")

    if nb_error>=nb_max:
        print(f"Le mot à trouver était {mot}. Vous avez perdu :-(")
        game=False
    if nb_lettres==0:
        print(f"Le mot à trouver était {mot}. Vous avez gagné avec {nb_error} erreur(s) :)")
        game=False
