# Les fonctions de manipulation de chaînes de caractères

chaines_de_caracteres = "Bonjour, je suis une chaîne de caractères."
# Afficher la longueur de la chaîne
longueur = len(chaines_de_caracteres)
print(f"La longueur de la chaîne est : {longueur}")
# Convertir la chaîne en majuscules
chaine_majuscule = chaines_de_caracteres.upper()
print(f"Chaîne en majuscules : {chaine_majuscule}")
# Convertir la chaîne en minuscules
chaine_minuscule = chaines_de_caracteres.lower()
print(f"Chaîne en minuscules : {chaine_minuscule}")
# Remplacer une sous-chaîne par une autre
chaine_remplacee = chaines_de_caracteres.replace("chaîne", "ligne")
print(f"Chaîne après remplacement : {chaine_remplacee}")
# Supprimer les espaces au début et à la fin de la chaîne
chaine_espaces_supprimes = chaines_de_caracteres.strip()
print(f"Chaîne sans espaces : {chaine_espaces_supprimes}")
# Supprimer des caractères spécifiques au début et à la fin de la chaîne
chaine_caracteres_specifiques = chaines_de_caracteres.strip("Bonjour, .")
print(
    f"Chaîne sans les caractères 'Bonjour, .' : {chaine_caracteres_specifiques}")
# Supprimer les espaces au début de la chaîne
chaine_espaces_debut = chaines_de_caracteres.lstrip()
print(f"Chaîne sans espaces au début : {chaine_espaces_debut}")
# Supprimer les espaces à la fin de la chaîne
chaine_espaces_fin = chaines_de_caracteres.rstrip()
print(f"Chaîne sans espaces à la fin : {chaine_espaces_fin}")
# Diviser la chaîne en une liste de mots
liste_de_mots = chaines_de_caracteres.split()
print(f"Liste de mots : {liste_de_mots}")
# Joindre une liste de mots en une chaîne
liste_de_mots = ["Bonjour", "je", "suis", "une", "chaîne", "de", "caractères."]
chaine_jointe = " ".join(liste_de_mots)
print(f"Chaîne jointe : {chaine_jointe}")
# Vérifier si une sous-chaîne est présente dans la chaîne
sous_chaine = "Bonjour"
est_present = sous_chaine in chaines_de_caracteres
print(f"La sous-chaîne '{sous_chaine}' est présente : {est_present}")
# Trouver la position d'une sous-chaîne dans la chaîne
position = chaines_de_caracteres.find("chaîne")
print(f"La position de la sous-chaîne 'chaîne' est : {position}")
# Vérifier si la chaîne commence par une sous-chaîne
commence_par = chaines_de_caracteres.startswith("Bonjour")
print(f"La chaîne commence par 'Bonjour' : {commence_par}")
# Vérifier si la chaîne se termine par une sous-chaîne
se_termine_par = chaines_de_caracteres.endswith("caractères.")
print(f"La chaîne se termine par 'caractères.' : {se_termine_par}")
# Vérifier si la chaîne est numérique
est_numerique = chaines_de_caracteres.isnumeric()
print(f"La chaîne est numérique : {est_numerique}")
# Vérifier si la chaîne est alphabétique
est_alphabetique = chaines_de_caracteres.isalpha()
print(f"La chaîne est alphabétique : {est_alphabetique}")
# Vérifier si la chaîne est alphanumérique
est_alphanumerique = chaines_de_caracteres.isalnum()
print(f"La chaîne est alphanumérique : {est_alphanumerique}")
# Vérifier si la chaîne est en majuscules
est_en_majuscules = chaines_de_caracteres.isupper()
print(f"La chaîne est en majuscules : {est_en_majuscules}")
# Vérifier si la chaîne est en minuscules
est_en_minuscules = chaines_de_caracteres.islower()
print(f"La chaîne est en minuscules : {est_en_minuscules}")
# Vérifier si la chaîne est un espace
est_espace = chaines_de_caracteres.isspace()
print(f"La chaîne est un espace : {est_espace}")
# Vérifier si la chaîne est vide
est_vide = not chaines_de_caracteres
print(f"La chaîne est vide : {est_vide}")
# counter le nombre d'occurrences d'une sous-chaîne
sous_chaine = "chaîne"
nombre_occurrences = chaines_de_caracteres.count(sous_chaine)
print(f"Le nombre d'occurrences de '{sous_chaine}' est : {nombre_occurrences}")
# Vérifier si la chaîne est un identifiant Python valide
est_identifiant = chaines_de_caracteres.isidentifier()
print(f"La chaîne est un identifiant Python valide : {est_identifiant}")
