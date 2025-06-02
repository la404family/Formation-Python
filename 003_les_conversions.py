# convertir une chaîne en caractères en nombre entier
# int('123') # 123
ma_variable_entiere = "123"
print(ma_variable_entiere)
# afficher le type de la variable
print(type(ma_variable_entiere))

# convertir la chaine de caractères en nombre entier
ma_variable_entiere = int(ma_variable_entiere)
print(ma_variable_entiere)

# afficher le type de la variable
print(type(ma_variable_entiere))
# la fonction type() renvoie la classe de l’objet, c’est-à-dire son type en tant qu’objet Python.

# Les autres conversions
# convertir une chaîne en nombre flottant
ma_variable_flottante = "123.456"
ma_variable_flottante = float(ma_variable_flottante)
print(ma_variable_flottante)
# convertir un nombre entier en chaîne de caractères
ma_variable_entiere = 123
ma_variable_entiere = str(ma_variable_entiere)
print(ma_variable_entiere)
# convertir un nombre flottant en chaîne de caractères
ma_variable_flottante = 123.456
ma_variable_flottante = str(ma_variable_flottante)
print(ma_variable_flottante)
# convertir un booléen en chaîne de caractères
ma_variable_booleenne = True
ma_variable_booleenne = str(ma_variable_booleenne)
print(ma_variable_booleenne)
# convertir une chaîne de caractères en booléen
ma_variable_chaine = "True"
ma_variable_booleenne = bool(ma_variable_chaine)
print(ma_variable_booleenne)  # True, car la chaîne n'est pas vide
# convertir une chaîne vide en booléen
ma_variable_chaine_vide = ""
ma_variable_booleenne_vide = bool(ma_variable_chaine_vide)
print(ma_variable_booleenne_vide)  # False, car la chaîne est vide
# convertir un nombre entier en booléen
ma_variable_entiere = 0
ma_variable_booleenne = bool(ma_variable_entiere)
print(ma_variable_booleenne)  # False, car 0 est considéré comme faux
# convertir un nombre entier non nul en booléen
ma_variable_entiere_non_nul = 42
ma_variable_booleenne_non_nul = bool(ma_variable_entiere_non_nul)
# True, car tout nombre entier non nul est considéré comme vrai
print(ma_variable_booleenne_non_nul)
# convertir un nombre flottant en booléen
ma_variable_flottante = 0.0
ma_variable_booleenne_flottante = bool(ma_variable_flottante)
# False, car 0.0 est considéré comme faux
print(ma_variable_booleenne_flottante)
# convertir un nombre flottant non nul en booléen
ma_variable_flottante_non_nul = 3.14
ma_variable_booleenne_flottante_non_nul = bool(ma_variable_flottante_non_nul)
# True, car tout nombre flottant non nul est considéré comme vrai
print(ma_variable_booleenne_flottante_non_nul)
# convertir une liste en chaîne de caractères
ma_liste = [1, 2, 3]
ma_liste_chaine = str(ma_liste)
print(ma_liste_chaine)  # "[1, 2, 3]"
