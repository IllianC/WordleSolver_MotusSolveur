#  Copyright (c) 2022.
#  iliouche

# Tout nouveau système d'entrée de données, plus intuitif.

import re, os


#   CHARGE UNE LISTE DE MOTS PRÉDÉFINIS
def load_words():
    print("Loading word list_to_print from file...")
    Wordlist = list()  # Création d'une liste de mots, vide pour l'instant
    # Ouvre le document en tant que "f"
    with open(os.path.join(os.path.dirname(__file__), "ods6.txt"), 'r') as f:
        for Line in f:  # Pour chaque lignes du fichier
            # Ajout de la ligne sans "\n" à la liste de mots
            Wordlist.append(Line.rstrip("\n"))
    # Impression du nombre de mots chargés dans la liste
    print(len(Wordlist), "words loaded.")

    return Wordlist


def set_length(Wordlist, nbr_letter):
    Wordlist_CN = list()
    for i in range(len(Wordlist)):
        if len(Wordlist[i]) == nbr_letter:
            Wordlist_CN.append(Wordlist[i])

    return Wordlist_CN


# Matrice_Try et matrice_result_ter sont des str
def search_in_wordlist(Matrice_Try, Matrice_Result_Ter, Wordlist_CN):
    List = list()
    filtered = Wordlist_CN

    for i in range(len(Matrice_Try)):

        print(Matrice_Try[i], Matrice_Result_Ter[i])

        if Matrice_Result_Ter[i] == '0':  # Si la lettre n'est pas dans la liste
            for word in filtered:  # Pour chaque mots
                # Si la lettre sélectionnée n'est pas dans le mot
                if Matrice_Try[i] not in word:
                    List.append(word)  # Ajout à la liste
            filtered = List  # MàJ de la liste des mots
            List = list()  # RàZ de la liste de présélection

        if Matrice_Result_Ter[i] == '2':  # Si le lettre est bonne
            for word in filtered:  # Pour chaque mot
                # Liste des lettres contenues dans le mot
                word_split = list(word)
                # Si la lettre du mot candidat égale la lettre du mot tenté
                if word_split[i] == Matrice_Try[i]:
                    List.append(word)  # Ajout à la liste
            filtered = List  # MàJ de la liste des mots
            List = list()  # RàZ de la liste de présélection

        # Si la lettre est à comprise mais mal placée
        if Matrice_Result_Ter[i] == '1':
            for word in filtered:  # Pour chaque mots
                # Liste des lettres contenues dans le mot
                word_split = list(word)
                if (Matrice_Try[i] in word) and (word_split[i] != Matrice_Try[
                        i]):  # Si la lettre est dans le mot tenté ET si la lettre du mot candidat est différent de la lettre du mot tenté pour une même position
                    List.append(word)  # Ajout à la liste
            filtered = List  # MàJ de la liste des mots
            List = list()  # RàZ de la liste de présélection

    return filtered


def print_list(List, Name_List):
    print(Name_List + " ")
    for i in range(len(List)):
        print(List[i])


def ask_try(Nbr_Letter):
    Matrice_Try = str('')
    Matrice_Try = Matrice_Try.rjust(Nbr_Letter, '_')

    Res = input("Saisir le mot tenté : ")
    while (len(Res) != Nbr_Letter):
        Res = input("Saisir le mot tenté : ")

    Res_split = list(Res)
    Matrice_Try_split = list(Matrice_Try)

    for i in range(len(Matrice_Try)):
        Matrice_Try_split[i] = Res_split[i]
    Matrice_Try = ''.join(list(Matrice_Try_split))

    return Matrice_Try


# Fonction de remplissage de la matrice de Résultat : composée d'entiers
def ask_result(Nbr_Letter):
    Matrice_Result_Ter = Nbr_Letter * [8]

    Res = input("Saisir le résultat (R=2, J=1, N=0) : ")
    while (len(Res) != Nbr_Letter) or (re.search('[a-zA-Z]', Res)):
        Res = input("Saisir le résultat (R=2, J=1, N=0) : ")

    # Transforme la matrice de Résultat (1 nombre entier) en liste des chiffres du nombre
    Res_split = list(Res)
    Matrice_Result_Ter_split = list(Matrice_Result_Ter)

    for i in range(len(Matrice_Result_Ter)):
        Matrice_Result_Ter_split[i] = Res_split[i]
    Matrice_Result_Ter = ''.join(list(Matrice_Result_Ter_split))

    return Matrice_Result_Ter


##
#   DEBUT DU CODE
##
Wordlist = load_words()
Wordlist_Correct_Nbr = Wordlist
Wordlist_Restrict = list()
Is_Found = False

#   Initialisation de la matrice d'essais
Nbr_Letter = int(input("Combien de lettre y a-t'il ? : "))

#   AJOUTE TOUS LES MOTS D'UNE CERTAINE LONGUEUR A LA LISTE DE MOTS SÉLECTIONNÉS
Wordlist_CN = set_length(Wordlist, Nbr_Letter)

while (Is_Found != True):
    Matrice_Try = ask_try(Nbr_Letter)
    Matrice_Result_Ter = ask_result(Nbr_Letter)

    Wordlist_R = search_in_wordlist(
        Matrice_Try, Matrice_Result_Ter, Wordlist_CN)
    print_list(Wordlist_R, "Wordlist_R")
    if (int(input("Solved ? (0,1) : "))) == 1:
        Is_Found = True
