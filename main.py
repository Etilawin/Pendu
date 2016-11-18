# -*- coding: utf-8 -*-

import random
import os


def cls():
    """ Efface l'écran """
    os.system('cls' if os.name=='nt' else 'clear')


def supprime_accent(ligne):
        """ supprime les accents du texte source """
        accents = {'a': ['à', 'ã', 'á', 'â'],
                    'e': ['é', 'è', 'ê', 'ë'],
                    'i': ['î', 'ï'],
                    'u': ['ù', 'ü', 'û'],
                    'o': ['ô', 'ö'],
                    'y': ['ÿ'],
                    'oe': ['œ'],
                    '': ['\n']}
        for (char, accented_chars) in accents.items():
            for accented_char in accented_chars:
                ligne = ligne.replace(accented_char, char)
        return ligne


def get_mot(liste):
    """ Récupère un mot au hasard dans une liste et le rend utilisable
        pour le pendu"""
    r = random.randint(0, len(liste))
    mot = liste[r].decode("latin-1")  # On le décode correctement
    return supprime_accent(mot)  # On enlève les accents indésirables


def checked(mot, lettres_trouvees):
    """ Vérifie si toutes les lettres d'un mot sont trouvées """
    for l in mot:
        if l not in lettres_trouvees:
            return False
    return True

fileName = "liste.de.mots.francais.frgut.txt"

with open(fileName, "rb") as myFile:
    a = myFile.readlines()

replay = True

while replay:  # On entre dans la console du jeu
    nb_joueur = int(input('Veuillez entrer le nombre de joueurs [1/2] : '))
    if nb_joueur != 1 and nb_joueur != 2:  # On vérifie l'entrée
        break
    difficulty = input('Veuillez entrer la difficulté'
                       ' [facile/moyen/difficile] : ')
    # Methode lower pour éviter les erreurs de majuscule
    # (Diffcile au lieu de difficile)
    if difficulty.lower() == "difficile":
        nb_coup = 5
    elif difficulty.lower() == "moyen":
        nb_coup = 10
    elif difficulty.lower() == "facile":
        nb_coup = 15
    else:  # Par défaut
        print("Difficulté inconnue, mode facile automatique")
        nb_coup = 15

    if nb_joueur == 1:
        choix_mots = input("Veuillez entrer un nom de fichier contenant une "
                           "liste de mots (laisser vide pour avoir la liste "
                           "par défaut) : ")
    if choix_mots.lower() != "":
        with open(choix_mots, "r") as liste:
            mots = liste.readlines()

    mot = get_mot(a)  # On sélectionne un mot au hasard grâce au module random

    lettres_trouvees = []
    i = 0
    trouve = False
    while (nb_coup) and (not checked(mot, lettres_trouvees)):
        cls()
        for l in mot:
            if l in lettres_trouvees:
              print(l, end='')
            else:
                print(' _ ', end='')
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

    if checked(mot, lettres_trouvees):
        rejouer = input("Bravo")




