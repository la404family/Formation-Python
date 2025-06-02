import math

# présentation des fonctions du module math
variable_float = 3.14658468
variable_int = 427
# Afficher la valeur de pi
print(f"La valeur de pi est : {math.pi}")
# Afficher la valeur de e
print(f"La valeur de e est : {math.e}")
# Arrondir la valeur à l'entier supérieur
variable_arrondie_haut = math.ceil(variable_float)
print(
    f"La valeur arrondie à l'entier supérieur est : {variable_arrondie_haut}")
# Arrondir la valeur à l'entier inférieur
variable_arrondie_bas = math.floor(variable_float)
print(f"La valeur arrondie à l'entier inférieur est : {variable_arrondie_bas}")
# Calculer la racine carrée de la valeur
variable_racine_carre = math.sqrt(variable_float)
print(f"La racine carrée de la valeur est : {variable_racine_carre}")
# Calculer la puissance de la valeur
variable_puissance = math.pow(variable_float, 2)
print(f"La puissance de la valeur au carré est : {variable_puissance}")
# Calculer le logarithme naturel de la valeur
variable_logarithme = math.log(variable_float)
print(f"Le logarithme naturel de la valeur est : {variable_logarithme}")
# Calculer le logarithme en base 10 de la valeur
variable_logarithme_base_10 = math.log10(variable_float)
print(
    f"Le logarithme en base 10 de la valeur est : {variable_logarithme_base_10}")
# Calculer le sinus de la valeur
variable_sinus = math.sin(variable_float)
print(f"Le sinus de la valeur est : {variable_sinus}")
# Calculer le cosinus de la valeur
variable_cosinus = math.cos(variable_float)
print(f"Le cosinus de la valeur est : {variable_cosinus}")
# Calculer la tangente de la valeur
variable_tangente = math.tan(variable_float)
print(f"La tangente de la valeur est : {variable_tangente}")
