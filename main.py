# -*- coding: utf-8 -*-

from fonctions import cls, get_mot, checked, clear_word  # fonctions persos
from getpass import getpass  # Pour entrer un mot sans que l'utilisateur voit

welcome = """
  _____               _
 |  __ \             | |
 | |__) |__ _ __   __| |_   _
 |  ___/ _ \ '_ \ / _` | | | |
 | |  |  __/ | | | (_| | |_| |
 |_|   \___|_| |_|\__,_|\__,_|

                              """

perdu = """
  _
 | |
 | | ___   ___  ___  ___ _ __
 | |/ _ \ / _ \/ __|/ _ \ '__|
 | | (_) | (_) \__ \  __/ |
 |_|\___/ \___/|___/\___|_|

                              """

gagne = """
           _
          (_)
 __      ___ _ __  _ __   ___ _ __
 \ \ /\ / / | '_ \| '_ \ / _ \ '__|
  \ V  V /| | | | | | | |  __/ |
   \_/\_/ |_|_| |_|_| |_|\___|_|

                                   """

replay = True

while replay:  # On commence une nouvelle partie
    cls()
    print(welcome)
    nb_joueur = int(input('Veuillez entrer le nombre de joueurs [1/2] : '))
    if nb_joueur != 1 and nb_joueur != 2:  # On vérifie l'entrée
        continue
    difficulty = input('Veuillez entrer la difficulté'
                       ' [facile/moyen/difficile] : ')
    # Methode lower pour éviter les erreurs de majuscule
    difficulty = difficulty.lower()

    # On choisit la difficulté
    if difficulty == "difficile":
        nb_coup = 5
    elif difficulty == "moyen":
        nb_coup = 10
    elif difficulty == "facile":
        nb_coup = 15
    else:  # Par défaut
        print("Difficulté inconnue, mode facile automatique")
        nb_coup = 15

    # On vérifie le nombre de joueur
    if nb_joueur == 1:
        # Si c'est un joueur, on lui demande un fichier
        choix_mots = input("Veuillez entrer un nom de fichier contenant une "
                           "liste de mots (laisser vide pour avoir la liste "
                           "par défaut) : ")
        if choix_mots.lower() != "":
            with open(choix_mots, "r") as liste:
                mots = liste.readlines()

        # Si le choix est vide, on importe fichier par défaut
        else:
            fileName = "defaut.txt"
            with open(fileName, "rb") as myFile:
                mots = myFile.readlines()

        mot = get_mot(mots)  # On sélectionne un mot au hasard (voir fonctions)
    else:
        # Si c'est deux joueurs on lui demande d'entrer secrètment son mot
        # deux fois (pour éviter les erreurs)
        while True:
            print("Veuillez entrer deux fois le mot à trouver")
            # https://docs.python.org/2.7/library/getpass.html
            mot1 = getpass("Veuillez entrer le mot à faire deviner : ")
            mot2 = getpass("Veuillez entrer à nouveau le mot : ")
            # On vérifie si les deux entrées correspondent
            if mot1 == mot2:
                mot = clear_word(mot1)
                break

    # On initialise les variables
    lettres_trouvees = []
    lettres_entrees = []
    lettre = ""
    i = 0
    trouve = False
    # Tant qu'il lui reste des coups et qu'il n'a pas trouvé le mot
    while (nb_coup) and (not checked(mot, lettres_trouvees)):
        cls()  # Voir fonctions
        # Si la lettre entrée précédemment à déjà été entrée, on l'affiche
        if lettre in lettres_entrees:
            print("Vous avez déjà entré cette lettre {}".format(lettre))
        lettres_entrees.append(lettre)

        # On parcourt les lettres du mot à trouver
        for l in mot:
            if l in lettres_trouvees:  # Si lettre trouvée, on l'affiche
              print(l, end='')
            else:
                print(' _ ', end='')  # Sinon on affiche "_"
        print('\n')

        # On affiche le nombre de coups restants
        print("Il vous reste {} coup(s)".format(nb_coup))

        lettre = input("Veuillez entrer une lettre : ")  # On demande une lettre
        # On vérifie si la lettre est dans le mot...
        # Et on l'ajoute aux lettres trouvées si elle est dans le mot
        if (lettre in mot) and (lettre not in lettres_trouvees):
            lettres_trouvees.append(lettre)
        else:
            nb_coup -= 1  # Si la lettre n'est pas dans le mot on enlève un coup

    # Si le jeu est fini on lui demande si il veut rejouer
    if checked(mot, lettres_trouvees):
        print(gagne)
        rejouer = input("Bravo, le mot était bien {}"
                        ", voulez vous rejouer ? [oui/non] : ".format(mot))
    else:
        print(perdu)
        rejouer = input("Mince vous n'avez pas trouvé le mot {},"
                        " voulez vous rejouer ? [oui/non] : ".format(mot))
    # JE DOIS VRAIMENT EXPLIQUER CA? VRAIMENT?
    if rejouer.lower() != "oui":
        replay = False






