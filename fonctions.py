# -*- coding: utf-8 -*-

import os
import random


def cls():
    """ Efface l'écran """
    os.system('cls' if os.name == 'nt' else 'clear')


def sup_accent(ligne):
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
    try:
        mot = liste[r].decode("latin-1")  # On le décode correctement
    except:  # Pas besoin de le décoder
        mot = liste[r]
    return sup_accent(mot).lower()  # On enlève les accents indésirables


def checked(mot, lettres_trouvees):
    """ Vérifie si toutes les lettres d'un mot sont trouvées """
    for l in mot:
        if l not in lettres_trouvees:
            return False
    return True