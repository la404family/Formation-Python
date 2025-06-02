# Les fonctions de manipulation de nombres à virgule flottante
variable_float = 3.14156456489
# Afficher la valeur de la variable
print(f"La valeur de la variable float est : {variable_float}")
# Arrondir la valeur à 2 décimales
variable_arrondie = round(variable_float, 2)
# Afficher la valeur arrondie
print(f"La valeur arrondie à 2 décimales est : {variable_arrondie}")
# Convertir la valeur en chaîne de caractères
variable_float_str = str(variable_float)
# Afficher la valeur convertie en chaîne de caractères
print(
    f"La valeur convertie en chaîne de caractères est : {variable_float_str}")
# Convertir la chaîne de caractères en nombre à virgule flottante
variable_float_from_str = float(variable_float_str)
# Vérifier si la valeur est un nombre à virgule flottante
est_float = isinstance(variable_float, float)
print(f"La variable est un nombre à virgule flottante : {est_float}")
# Vérifier si la valeur est un entier
est_entier = isinstance(variable_float, int)
print(f"La variable est un entier : {est_entier}")
# Vérifier si la valeur est un nombre
est_nombre = isinstance(variable_float, (int, float))
print(f"La variable est un nombre : {est_nombre}")
# Vérifier si la valeur est un nombre entier
est_entier = variable_float.is_integer()
print(f"La variable est un nombre entier : {est_entier}")
# Vérifier si la valeur est un nombre positif
est_positif = variable_float > 0
print(f"La variable est un nombre positif : {est_positif}")
# Vérifier si la valeur est un nombre négatif
est_negatif = variable_float < 0
print(f"La variable est un nombre négatif : {est_negatif}")
# Vérifier si la valeur est zéro
est_zero = variable_float == 0
print(f"La variable est zéro : {est_zero}")
# Vérifier si la valeur est inférieure à un seuil
seuil = 5.0
est_inferieur_seuil = variable_float < seuil
print(f"La variable est inférieure à {seuil} : {est_inferieur_seuil}")
# Vérifier si la valeur est supérieure à un seuil
est_superieur_seuil = variable_float > seuil
print(f"La variable est supérieure à {seuil} : {est_superieur_seuil}")
