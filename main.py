"""
Fichier main.py
"""
#### Imports et définition des variables globales

# import random
FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename, mode='r', encoding='utf8') as f:
        for line in f:
            l.append(list(map(int, line.strip().split(';'))))
    return l

def get_list_k(data, k):
    """
    Retourne la k-ieme ligne de la liste
    """
    return data[k]

def get_first(l):
    """
    Retourne le premier element de la liste
    """
    return l[0]

def get_last(l):
    """
    Retourne le dernier element de la liste
    """
    return l[-1]

def get_max(l):
    """
    Retourne le max element de la liste
    """
    return max(l)

def get_min(l):
    """
    Retourne le min element de la liste
    """
    return min(l)

def get_sum(l):
    """
    Retourne la somme de la liste
    """
    somme = 0
    for i in l:
        somme = somme + i
    return somme


#### Fonction principale


def main():
    """
    Définition du main
    """
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    # k = 37
    # print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
