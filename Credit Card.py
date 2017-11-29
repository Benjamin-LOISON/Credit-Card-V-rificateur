# coding: utf8

#-------------------------------------------------------------------------------
# Nom:          Vérificateur de Carte Bleue
# Description:  Vérifie les 16 numéros
#
# Auteur:       Benjamin Loison
#
# Crée le:      18/11/2017
# Copyright:    (c) Benjamin Loison 2017
# License:      Aucune license (citer l'auteur)
#-------------------------------------------------------------------------------

## 0123456789012345 (false) 7
## 4520337343105504 (false) 7
## 5135136065996745 (true)
## 4974991547039277 (false) 5
## 3573630054996611 (true)
## 4024007146302608 (true)
## CB personnelle (true)

numeros = input("Saisir les 16 numéros (sans espace)")

## Bloc try/catch pour prévenir un arrêt du programme (comment transformer un
## string en nombre ? ou diviser un nombre par 0 ?)
try:
    int(numeros)
except ValueError:
    exit("La saisie n'est pas un nombre (sans espace) !")

if len(numeros) != 16:
    exit("La saisie ne comporte pas 16 chiffres !")

## Formule de Luhn: doublement des chiffres de numéros impaires et si le
## résultat comporte deux chiffres alors on les additionne puis on somme tous
## les chiffres avec ceux modifiés par l'algo de Luhn. Si 10 divise la somme
## alors le code est "vérifié"
for k in range(0, 15, 2): ## 15 exclu
    ## Besoin de nombreux str et int pour compenser le typage dynamique
    numeroLuhn = str(int(numeros[k]) * 2)
    ## Somme des deux chiffres si c'est le cas
    if len(numeroLuhn) == 2:
        ## Avec une calculatrice (conversion de type impossible), l'instruction
        ## suivante peut-être réalisée avec:
        ## - le reste de la division euclidienne par 10 pour obtenir le chiffre
        ## des unités
        ## - le reste précédemment calculé soustrait au nombre et le résultat
        ## divisé par 10 correspond au chiffre des
        numeroLuhn = str(int(numeroLuhn[0]) + int(numeroLuhn[1]))
    ## Une technique de remplacement d'un caractère dans un string en Python
    numeros = numeros[:k] + numeroLuhn + numeros[k + 1:]

## Somme finale
somme = 0
for k in range(0, 16):
    somme += int(numeros[k])

reste = somme % 10
## Vérification avec la clé
if reste == 0:
    print("La Carte Bleue est \"vérifiée\" !")
else:
    cle = int(numeros[15])
    ## Détermination de la clé pour que la carte bleue soit "vérifiée"
    ## Avec une calculatrice pour obtenir un reste, utiliser la fonction:
    ## - Dividende (ici la variable somme) Rmdr quotient (ici 10) sur Casio
    ## - reste(dividente, quotient) ou en anglais remainder sur Texas et vérfier
    ## au paravant si dividende < 0, si oui ajouter + 10 (les Texas ne support
    ## pas les dividendes négatifs contrairement aux Casio)
    print("Pour que la Carte Bleue soit vérifiée, il faut que la clé soit: "
        + str((cle - reste) % 10))
