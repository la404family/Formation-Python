# Les variables servent à stocker des valeurs. 
# Les variables sont des noms qui sont utilisés pour faire référence à des valeurs stockées en mémoire.

# Les notations de variables
# Le camelCase
maVariable = 5
# Le snake_case
ma_variable = 5
# Le PascalCase
MaVariable = 5
# Le kebab-case /!\  non supporté par Python
    #  ma-variable = 5

# Le SCREAMING_SNAKE_CASE ou UPPER_CASE
MA_VARIABLE = 5
# Hungarian notation 
intMaVariable = 5
strMaVariable = "Bonjour"
boolMaVariable = True
floatMaVariable = 5.5
listMaVariable = [1, 2, 3]
tupleMaVariable = (1, 2, 3)
dictMaVariable = {"cle1": 1, "cle2": 2, "cle3": 3}

# Lorsqu'on assigne une valeur à une variable elle est stockée en mémoire
# Pour vérifier le code de stockage de sa variable on peut utiliser la fonction `id()`
# Entre 5 et 256 les variables ont la même adresse mémoire idem pour true et false
test_pour_id1 = 5
test_pour_id2 = test_pour_id1
print(id(test_pour_id1))
print(id(test_pour_id2)) # Les deux variables ont la même adresse mémoire

# On peut aussi utiliser la fonction `type()` pour vérifier le type de la variable
print(type(test_pour_id1))
print(type(test_pour_id2)) # Les deux variables ont le même type

#Il est possible de donner plusieurs valeurs à plusieurs variables en une seule ligne
a, b, c = 1, 2, 3
# Ont peut intervertir les valeurs de deux variables en une seule ligne
a, b = b, a
# On peut aussi donner la même valeur à plusieurs variables
a = b = c = 1
# Certains mots sont réservés par Python et ne peuvent pas être utilisés comme noms de variables
    # and, as, assert, break, class, continue, def, del, elif, else, except, exec, finally, for, from, global, if, import, in, is, lambda, not, or, pass, print, raise, return, try, while, with, yield
#une variable ne peut pas commencer par un chiffre.


'''
1. Kebab case
Description : Les mots sont séparés par des tirets (-). Utilisé principalement pour les noms de fichiers ou les URLs.
Exemple :
mon-fichier-de-test
lien-vers-ressource

2. Pascal case
Description : Chaque mot commence par une majuscule, y compris le premier. Utilisé souvent pour les noms de classes.
Exemple :
MonFichierDeTest
LienVersRessource

3. Snake case
Description : Les mots sont séparés par des underscores (_). Utilisé fréquemment en Python pour les variables ou les constantes.
Exemple :
mon_fichier_de_test
lien_vers_ressource

4. Camel case
Description : Chaque mot commence par une majuscule, sauf le premier. Utilisé fréquemment pour les noms de variables ou de fonctions.
Exemple :
monFichierDeTest
lienVersRessource

5. Train case
Description : Semblable au kebab case, mais chaque mot commence par une majuscule. Peu courant.
Exemple :
Mon-Fichier-De-Test
Lien-Vers-Ressource

6. Dot case
Description : Les mots sont séparés par des points (.). Utilisé parfois dans des fichiers de configuration.
Exemple :
mon.fichier.de.test
lien.vers.ressource

7. Screaming case ou Upper case
Description : Variante avec des majuscules. Rarement utilisé.
Exemple :
MON-FICHIER-DE-TEST
LIEN-VERS-RESSOURCE

8. Flat case
Description : Aucun séparateur, tout est écrit en minuscules. Peu lisible pour les longues chaînes.
Exemple :
monfichierdetest
lienversressource
'''