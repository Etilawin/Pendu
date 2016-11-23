# -*- coding: utf-8 -*-

import os
import random
import string


def cls():
    """ Efface l'écran """
    # Petite ligne pour être cross-plateform
    os.system('cls' if os.name == 'nt' else 'clear')


def clear_word(ligne):
        """ supprime les charactères non compris dans string.ascii_letters"""
        ligne_propre = ""
        accents = {'a': ['à', 'ã', 'á', 'â'],
                    'e': ['é', 'è', 'ê', 'ë'],
                    'i': ['î', 'ï'],
                    'u': ['ù', 'ü', 'û'],
                    'o': ['ô', 'ö'],
                    'y': ['ÿ'],
                    'oe': ['œ'],
                    '': ['\n']}
        # On supprime d'abord les accents
        for (char, accented_chars) in accents.items():
            for accented_char in accented_chars:
                ligne = ligne.replace(accented_char, char)
        # Puis on supprime les charactères spéciaux
        for letter in ligne:
            if letter in string.ascii_letters:
                ligne_propre += letter
        return ligne_propre.lower()


def get_mot(liste):
    """ Récupère un mot au hasard dans une liste et le rend utilisable
        pour le pendu"""
    r = random.randint(0, len(liste))  # Nbr aléatoire
    try:
        mot = liste[r].decode("latin-1")  # On le décode correctement
    except:  # Pas besoin de le décoder
        mot = liste[r]
    return clear_word(mot).lower()  # On enlève les accents indésirables


def checked(mot, lettres_trouvees):
    """ Vérifie si toutes les lettres d'un mot sont trouvées """
    for l in mot:  # On parcourt le mot
        if l not in lettres_trouvees:  # Si une seule lettre n'est pas dans les
                                       # lettres trouvées on retourne FAUX
            return False
    return True