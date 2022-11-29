#  Copyright (c) 2022.
#  iliouche

# Ajout de plusieurs langage pour l'utilisateur
# Anglais et Français sont désormais disponibles
# Implémentation de la fonction check_doublon qui permet de vérifier si une lettre est présente plusieurs fois dans le mot tenté
# et corriger les erreurs de saisie de l'utilisateur
#
# Relecture du code et variables renommées pour une meilleure compréhension

import re
import os


#   Charge une liste de mots prédéfinis
def loadWords(language):
    print(f"Loading word list_to_print from file...")
    # Création d'une liste de mots, vide pour l'instant
    wordList = list()

    # ods6 -> Français / ods5-7 -> Anglais
    if language == 'FR':
        path = os.path.join(os.path.dirname(__file__), "ods{}.txt".format(6))

    elif language == 'EN':
        path = os.path.join(os.path.dirname(__file__), "ods{}.txt".format(5))

    else:
        path = os.path.join(os.path.dirname(__file__), "ods{}.txt".format(6))

    with open(path, 'r') as f:  # Ouvre le document en tant que "f"
        for line in f:  # Pour chaque ligne du fichier
            # Ajout de la ligne sans "\n" à la liste de mots
            wordList.append(line.rstrip("\n"))
    # Impression du nombre de mots chargés dans la liste
    print(f"{len(wordList)} words loaded.")

    return wordList


def setLength(wordList, nbLetter):
    wordListCorrectLength = list()
    for i in range(len(wordList)):
        if len(wordList[i]) == nbLetter:
            wordListCorrectLength.append(wordList[i])

    return wordListCorrectLength


# Fonction qui recherche toutes les possibilités dans une liste
def searchInWordlist(wordListCorrectLength, historyWordsTried,
                     historyWordsTriedResult):  # matrice_try et matrice_result_ter sont des str
    tempFilteredWordList = list()
    filteredWordList = wordListCorrectLength

    for j in range(len(historyWordsTried)):

        wordTried = historyWordsTried[j]
        wordTriedResult = historyWordsTriedResult[j]
        wordTriedResult = checkDoublon(wordTried, wordTriedResult)

        print(f"{wordTried} {wordTriedResult}")

        for i in range(len(wordTried)):

            # Si la lettre n'est pas dans la liste
            if wordTriedResult[i] == '0':
                for word in filteredWordList:  # Pour chaque mot
                    # Si la lettre sélectionnée n'est pas dans le mot
                    if wordTried[i] not in word:
                        tempFilteredWordList.append(word)  # Ajout à la liste
                filteredWordList = tempFilteredWordList  # MàJ de la liste des mots
                tempFilteredWordList = list()  # RàZ de la liste de présélection

            elif wordTriedResult[i] == '2':  # Si la lettre est bonne
                for word in filteredWordList:  # Pour chaque mot
                    # Liste des lettres contenues dans le mot
                    wordSplit = list(word)
                    # Si la lettre du mot candidat égale la lettre du mot tenté
                    if wordSplit[i] == wordTried[i]:
                        tempFilteredWordList.append(word)  # Ajout à la liste
                filteredWordList = tempFilteredWordList  # MàJ de la liste des mots
                tempFilteredWordList = list()  # RàZ de la liste de présélection

            # Si la lettre est comprise, mais mal placée
            elif wordTriedResult[i] == '1':
                for word in filteredWordList:  # Pour chaque mot
                    # Liste des lettres contenues dans le mot
                    wordSplit = list(word)
                    if (wordTried[i] in word) and (wordSplit[i] != wordTried[
                            i]):  # Si la lettre est dans le mot tenté ET si la lettre du mot candidat est différent de la lettre du mot tenté pour une même position.
                        tempFilteredWordList.append(word)  # Ajout à la liste
                filteredWordList = tempFilteredWordList  # MàJ de la liste des mots
                tempFilteredWordList = list()  # RàZ de la liste de présélection

    return filteredWordList


# Fonction qui vérifie si un mot est dans une liste de mots
def isInDic(wordListCorrectLength, wordTried):
    1 if wordTried in wordListCorrectLength else 0


# Fonction qui affiche une liste de mots
def printList(list2Print, listName):
    print(f"{listName} : ")
    for i in range(len(list2Print)):
        print(f"{list2Print[i]}")
    print(f"{len(list2Print)} mots trouvés !")


def askWordTried(nbLetter):
    wordTried = str('')
    wordTried = wordTried.rjust(nbLetter, '_')

    wordResult = input("Saisir le mot tenté : ")
    while (len(wordResult) != nbLetter) or (re.search('[0-9]', wordResult)) or (isInDic(wordList, wordResult)):
        wordResult = input("Saisir le mot tenté : ")

    wordResultSplit = list(wordResult)
    wordTriedSplit = list(wordTried)

    for i in range(len(wordTried)):
        wordTriedSplit[i] = wordResultSplit[i]
    wordTried = ''.join(wordTriedSplit)

    return wordTried


# Fonction de remplissage de la matrice de Résultat : composée d'entiers
def askWordTriedResult(nbLetter):
    wordTriedResultGrid = nbLetter * [8]

    wordTriedResultB4Cast = input("Saisir le résultat (R=2, J=1, N=0) : ")
    while (len(wordTriedResultB4Cast) != nbLetter) or (re.search('[a-zA-Z]', wordTriedResultB4Cast)):
        wordTriedResultB4Cast = input("Saisir le résultat (R=2, J=1, N=0) : ")

    # Transforme la matrice de Résultat (1 nombre entier) en liste des chiffres
    wordTriedResultSplit = list(wordTriedResultB4Cast)

    wordTriedResultGrid = ''.join(wordTriedResultSplit)

    return wordTriedResultGrid


# Fonction qui vérifie les doublons dans la matrice du résultat, évite les doublons dans la liste des mots filtrés
def checkDoublon(wordTried, wordTriedResult):
    wordTriedSplit = list(wordTried)
    wordTriedResultSplit = list(wordTriedResult)

    for i in range(len(wordTriedResultSplit)):
        if wordTriedResultSplit[i] == '2' or wordTriedResultSplit[i] == '1':
            for j in range(len(wordTriedResultSplit)):
                if wordTriedSplit[i] == wordTriedSplit[j] and wordTriedResultSplit[j] == '0':
                    wordTriedResultSplit[j] = '1'

    word2Send = ''.join(wordTriedResultSplit)
    return word2Send


##
#   DEBUT DU CODE
##
language = input("Choose language (FR/EN) : ")
while (language != 'FR') and (language != 'EN'):
    language = input("Choose language (FR/EN) : ")

global wordList
wordList = loadWords(language)
wordListRestricted = wordList
historyWordsTried = list()
historyWordsTriedResult = list()

isFound = False
isLeaving = False

while not isLeaving:
    #   Initialisation de la matrice d'essais
    nbLetter = int(input("Combien de lettre y a-t'il ? : "))
    while nbLetter < 5 or nbLetter > 10:
        nbLetter = int(input("Combien de lettre y a-t'il ? : "))

    #   Ajoute tous les mots d'une certaine longueur a la liste de mots retenus
    wordListRestricted = setLength(wordList, nbLetter)
    print(f"{len(wordListRestricted)} mots correspondants au nombre de lettres requis !")

    while not isFound:
        matriceTrySet = askWordTried(nbLetter)
        historyWordsTried.append(matriceTrySet.upper())
        historyWordsTriedResult.append(askWordTriedResult(nbLetter))

        filteredWordList = searchInWordlist(
            wordListRestricted, historyWordsTried, historyWordsTriedResult)
        printList(filteredWordList, "Filtered wordlist")
        isFound = True if (int(input("Solved ? (0,1) : "))) == 1 else False

    wordListRestricted.clear()
    historyWordsTried.clear()
    historyWordsTriedResult.clear()
    isFound = False
    isLeaving = True if (int(input("Rejouer ? (0,1) : "))) == 0 else False
