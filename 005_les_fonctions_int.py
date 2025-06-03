# Les fonctions relatives aux entiers
int_d_exemple = 42
# Afficher la valeur absolue d'un entier
valeur_absolue = abs(int_d_exemple)
print(f"La valeur absolue de {int_d_exemple} est : {valeur_absolue}")
# Convertir un entier en binaire
binaire = bin(int_d_exemple)
print(f"La représentation binaire de {int_d_exemple} est : {binaire}")
# Convertir un entier en octal
octal = oct(int_d_exemple)
print(f"La représentation octale de {int_d_exemple} est : {octal}")
# Convertir un entier en hexadécimal
hexadecimal = hex(int_d_exemple)
print(f"La représentation hexadécimale de {int_d_exemple} est : {hexadecimal}")
# Comparer deux entiers
int_a = 10
int_b = 20
est_egal = int_a == int_b
print(f"{int_a} est égal à {int_b} : {est_egal}")
# Comparer deux entiers (plus grand que)
est_plus_grand = int_a > int_b
print(f"{int_a} est plus grand que {int_b} : {est_plus_grand}")
# Comparer deux entiers (plus petit que)
est_plus_petit = int_a < int_b
print(f"{int_a} est plus petit que {int_b} : {est_plus_petit}")
# Comparer deux entiers (plus grand ou égal)
est_plus_grand_ou_egal = int_a >= int_b
print(f"{int_a} est plus grand ou égal à {int_b} : {est_plus_grand_ou_egal}")
# Comparer deux entiers (plus petit ou égal)
est_plus_petit_ou_egal = int_a <= int_b
print(f"{int_a} est plus petit ou égal à {int_b} : {est_plus_petit_ou_egal}")
# Compléter un entier avec des zéros à gauche
int_a = 5
int_b = 42
int_a_zfill = str(int_a).zfill(3)
int_b_zfill = str(int_b).zfill(3)
print(f"{int_a} avec zfill : {int_a_zfill}")
print(f"{int_b} avec zfill : {int_b_zfill}")
