#  Copyright (c) 2022.
#  iliouche

# Création d'un solveur de Motus
# Algorithme peu efficace, lent, et peu sélectif

import fnmatch, os


#   CHARGE UNE LISTE DE MOTS PRÉDÉFINIS
def load_words():
    print("Loading word list_to_print from file...")
    Wordlist = list()
    with open(os.path.join(os.path.dirname(__file__), "ods6.txt"), 'r') as f:
        for Line in f:
            Wordlist.append(Line.rstrip("\n"))
    print(" ", len(Wordlist), "words loaded.")
    print("\n".join(Wordlist))
    return Wordlist


def set_letter(Matrice_Res, Nbr_Letter):
    Finished = False

    while not Finished:
        Pos_Letter = int(input("Saisir la position de la lettre à modifier : "))
        while (Pos_Letter > Nbr_Letter) or (Pos_Letter < 1):
            Pos_Letter = int(input("Saisir la position de la lettre à modifier : "))
        Letter_2_Change = input("Saisir la lettre a affecter : ")
        Modifying = list(Matrice_Res)
        Modifying[Pos_Letter - 1] = Letter_2_Change
        Matrice_Res = "".join(Modifying)
        if int(input("Finit ? 0/1 : ")) == 1: Finished = True
    return Matrice_Res


def search_in_wordlist(Matrice_Res, Wordlist_Correct_Nbr, Not_In, In):
    List = list()
    filtered = fnmatch.filter(Wordlist_Correct_Nbr, Matrice_Res)
    print(Not_In)
    print(In)
    if len(In) > 0:
        for j in range(len(In)):
            for word in filtered:
                if In[j] in word:
                    List.append(word)
            filtered = List
            List = list()

    if len(Not_In) > 0:
        for i in range(len(Not_In)):
            for word in filtered:
                if Not_In[i] not in word:
                    List.append(word)
            filtered = List
            List = list()
    return filtered


def print_list(List):
    for i in range(len(List)):
        print(List[i])


def set_not_in(Not_In):
    Finished = False
    while not Finished:
        letter_2_set = input("Saisir les lettres interdites : ")
        if letter_2_set != '':
            Not_In.append(letter_2_set)
        if int(input("Saisie lettres interdites finie ? : ")): Finished = True
    return Not_In


def set_in(In):
    Finished = False
    while not Finished:
        letter_2_set = input("Saisir la lettre comprise dans le mot : ")
        if letter_2_set != '':
            In.append(letter_2_set)
        if int(input("Saisie lettre comprise terminée ? : ")): Finished = True
    return In


def ask_result(Matrice_Result_Bin):
    print("")


##
#   DEBUT DU CODE
##
Wordlist = load_words()
Wordlist_Correct_Nbr = Wordlist
Wordlist_Restrict = list()
Is_Found = False
Not_In = list()
In = list()

#   Initialisation de la matrice d'essais
Matrice_Res = ''
Matrice_Try = ''
Nbr_Letter = int(input("Combien de lettre y a-t'il ? : "))
Matrice_Res = Matrice_Res.rjust(Nbr_Letter, '?')
Matrice_Try = Matrice_Try.rjust(Nbr_Letter, '_')
Matrice_Result_Bin = Nbr_Letter * [0]

#   AJOUTE TOUS LES MOTS D'UNE CERTAINE LONGUEUR A LA LISTE DE MOTS SÉLECTIONNÉE
for i in range(len(Wordlist)):
    if len(Wordlist[i]) == Nbr_Letter:
        Wordlist_Correct_Nbr.append(Wordlist[i])
        print(Wordlist[i])

while (Is_Found != True):
    print(Matrice_Result_Bin)
    if int(input("Modifier matrice ? : ")) == 1:
        Matrice_Res = set_letter(Matrice_Res, Nbr_Letter)
    print_list(Wordlist_Restrict)
    print(Matrice_Res)

    print("Not_In : ", Not_In)
    if int(input("Set_Not_In ? : ")) == 1:
        Not_In = set_not_in(Not_In)

    if int(input("Set_In ? : ")) == 1:
        In = set_in(In)
    print("In : ", In)

    Wordlist_Restrict = search_in_wordlist(Matrice_Res, Wordlist_Correct_Nbr, Not_In, In)
    print_list(Wordlist_Restrict)
    print("Not_In : ", Not_In)
    print("In : ", In)
    print(Matrice_Res)
    if (int(input("Solved ? (0,1) : "))) == 1: Is_Found = True
