#  Copyright (c) 2022.
#  iliouche

# Implémentation de la recherche récursive. Plus grande rapidité et efficacité dans la recherche de mots.

import re, os


#   CHARGE UNE LISTE DE MOTS PRÉDÉFINIS
def load_words():
    print("Loading word list_to_print from file...")
    wordlist = list()  # Création d'une liste de mots, vide pour l'instant
    with open(os.path.join(os.path.dirname(__file__), "ods6.txt"), 'r') as f:  # Ouvre le document en tant que "f"
        for Line in f:  # Pour chaque ligne du fichier
            # Ajout de la ligne sans "\n" à la liste de mots
            wordlist.append(Line.rstrip("\n"))
    # Impression du nombre de mots chargés dans la liste
    print(len(wordlist), "words loaded.")

    return wordlist


def set_length(wordlist, nbr_letter):
    wordlist_cn = list()
    for i in range(len(wordlist)):
        if len(wordlist[i]) == nbr_letter:
            wordlist_cn.append(wordlist[i])

    return wordlist_cn


def search_in_wordlist(matrice_result_ter, wordlist_cn, tried_words,
                       tried_words_res):  # matrice_try et matrice_result_ter sont des str
    list_filtered = list()
    filtered = wordlist_cn

    for j in range(len(tried_words)):

        matrice_try = tried_words[j]
        matrice_result_ter = tried_words_res[j]
        print(matrice_try, matrice_result_ter)

        for i in range(len(matrice_try)):

            # Si la lettre n'est pas dans la liste
            if matrice_result_ter[i] == '0':
                for word in filtered:  # Pour chaque mot
                    # Si la lettre sélectionnée n'est pas dans le mot
                    if matrice_try[i] not in word:
                        list_filtered.append(word)  # Ajout à la liste
                filtered = list_filtered  # MàJ de la liste des mots
                list_filtered = list()  # RàZ de la liste de présélection

            elif matrice_result_ter[i] == '2':  # Si la lettre est bonne
                for word in filtered:  # Pour chaque mot
                    # Liste des lettres contenues dans le mot
                    word_split = list(word)
                    # Si la lettre du mot candidat égale la lettre du mot tenté
                    if word_split[i] == matrice_try[i]:
                        list_filtered.append(word)  # Ajout à la liste
                filtered = list_filtered  # MàJ de la liste des mots
                list_filtered = list()  # RàZ de la liste de présélection

            # Si la lettre est comprise, mais mal placée
            elif matrice_result_ter[i] == '1':
                for word in filtered:  # Pour chaque mot
                    # Liste des lettres contenues dans le mot
                    word_split = list(word)
                    if (matrice_try[i] in word) and (word_split[i] != matrice_try[
                            i]):  # Si la lettre est dans le mot tenté ET si la lettre du mot candidat est différent de la lettre du mot tenté pour une même position.
                        list_filtered.append(word)  # Ajout à la liste
                filtered = list_filtered  # MàJ de la liste des mots
                list_filtered = list()  # RàZ de la liste de présélection

    return filtered


def is_in_dic(wordlist_cn, word_try):
    if word_try in wordlist_cn:
        return 1
    else:
        return 0


def print_list(list_to_print, name_list):
    print(name_list + " ")
    for i in range(len(list_to_print)):
        print(list_to_print[i])
    print(len(list_to_print), " mots trouvés !")


def ask_try(nbr_letter):
    matrice_try = str('')
    matrice_try = matrice_try.rjust(nbr_letter, '_')

    res = input("Saisir le mot tenté : ")
    while (len(res) != nbr_letter) or (re.search('[0-9]', res)) or (is_in_dic(Wordlist_CN, res)):
        res = input("Saisir le mot tenté : ")

    res_split = list(res)
    matrice_try_split = list(matrice_try)

    for i in range(len(matrice_try)):
        matrice_try_split[i] = res_split[i]
    matrice_try = ''.join(list(matrice_try_split))

    return matrice_try


# Fonction de remplissage de la matrice de Résultat : composée d'entiers
def ask_result(nbr_letter):
    matrice_result_ter = nbr_letter * [8]

    res = input("Saisir le résultat (R=2, J=1, N=0) : ")
    while (len(res) != nbr_letter) or (re.search('[a-zA-Z]', res)):
        res = input("Saisir le résultat (R=2, J=1, N=0) : ")

    # Transforme la matrice de Résultat (1 nombre entier) en liste des chiffres du nombre
    res_split = list(res)
    matrice_result_ter_split = list(matrice_result_ter)

    for i in range(len(matrice_result_ter)):
        matrice_result_ter_split[i] = res_split[i]
    matrice_result_ter = ''.join(list(matrice_result_ter_split))

    return matrice_result_ter


##
#   DEBUT DU CODE
##
Wordlist = load_words()
global Wordlist_CN
Wordlist_CN = Wordlist
Wordlist_Restrict = list()
Tried_Words = list()
Tried_Words_Res = list()

Is_Found = False
Is_Leaving = False

while not Is_Leaving:
    #   Initialisation de la matrice d'essais
    Nbr_Letter = int(input("Combien de lettre y a-t'il ? : "))
    while Nbr_Letter < 6 or Nbr_Letter > 9:
        Nbr_Letter = int(input("Combien de lettre y a-t'il ? : "))

    #   AJOUTE TOUS LES MOTS D'UNE CERTAINE LONGUEUR A LA LISTE DE MOTS RETENUS
    Wordlist_CN = set_length(Wordlist, Nbr_Letter)
    print(len(Wordlist_CN), " mots correspondants au nombre de lettres requis !")

    while not Is_Found:
        Matrice_Try = ask_try(Nbr_Letter)
        Tried_Words.append(Matrice_Try.upper())

        Matrice_Result_Ter = ask_result(Nbr_Letter)
        Tried_Words_Res.append(Matrice_Result_Ter)

        Wordlist_R = search_in_wordlist(
            Matrice_Result_Ter, Wordlist_CN, Tried_Words, Tried_Words_Res)
        print_list(Wordlist_R, "Restricted wordlist")
        if (int(input("Solved ? (0,1) : "))) == 1:
            Is_Found = True

    Wordlist_CN = Wordlist
    Wordlist_Restrict = list()
    Tried_Words = list()
    Tried_Words_Res = list()
    Is_Found = False
    if (int(input("Rejouer ? (0,1) : "))) == 0:
        Is_Leaving = True
