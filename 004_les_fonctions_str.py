"""
======================================================================
LES FONCTIONS DE CHAÎNES DE CARACTÈRES - GUIDE COMPLET
======================================================================

📝 Les chaînes de caractères (strings) sont l'un des types les plus utilisés
en Python. Ce guide vous apprend toutes les techniques pour les manipuler
efficacement : nettoyer, transformer, rechercher, diviser, et bien plus !

"""

print("=" * 70)
print("LES FONCTIONS DE CHAÎNES DE CARACTÈRES - GUIDE COMPLET")
print("=" * 70)

print("\n" + "=" * 50)
print("1. CONCEPT DE BASE : QU'EST-CE QU'UNE CHAÎNE ?")
print("=" * 50)

# 📝 Les fonctions de manipulation de chaînes de caractères
chaines_de_caracteres = "Bonjour, je suis une chaîne de caractères."
print(f"📝 Chaîne d'exemple : '{chaines_de_caracteres}'")

print("\n💡 ANALOGIE - Une chaîne comme une ligne de texte :")
print("""
    B o n j o u r ,   j e   s u i s . . .
    0 1 2 3 4 5 6 7 8 9 ...
    
    Chaque caractère a une position (index) et peut être manipulé !
""")

print("\n🔍 INFORMATIONS DE BASE :")
# Afficher la longueur de la chaîne
longueur = len(chaines_de_caracteres)
print(f"   Longueur totale : {longueur} caractères")
print(f"   Type de donnée : {type(chaines_de_caracteres)}")
print(f"   Premier caractère : '{chaines_de_caracteres[0]}'")
print(f"   Dernier caractère : '{chaines_de_caracteres[-1]}'")

print("\n" + "=" * 50)
print("2. TRANSFORMATIONS DE CASSE (MAJUSCULES/MINUSCULES)")
print("=" * 50)

print("\n🔤 CHANGEMENT DE CASSE")
print("-" * 25)

# Convertir la chaîne en majuscules
chaine_majuscule = chaines_de_caracteres.upper()
print(f"✅ upper() - Tout en MAJUSCULES :")
print(f"   '{chaines_de_caracteres}' → '{chaine_majuscule}'")

# Convertir la chaîne en minuscules
chaine_minuscule = chaines_de_caracteres.lower()
print(f"✅ lower() - Tout en minuscules :")
print(f"   '{chaines_de_caracteres}' → '{chaine_minuscule}'")
# Autres transformations de casse
texte_exemple = "python EST un langage FORMIDABLE"
print(f"✅ capitalize() - Première lettre en majuscule :")
print(f"   '{texte_exemple}' → '{texte_exemple.capitalize()}'")

print(f"✅ title() - Première lettre de chaque mot :")
print(f"   '{texte_exemple}' → '{texte_exemple.title()}'")

print(f"✅ swapcase() - Inverse majuscules/minuscules :")
print(f"   '{texte_exemple}' → '{texte_exemple.swapcase()}'")

print("\n💡 USAGE PRATIQUE :")
nom_utilisateur = "JEAN dupont"
nom_formate = nom_utilisateur.title()
print(f"   Nom utilisateur formaté : '{nom_formate}'")

print("\n" + "=" * 50)
print("3. REMPLACEMENT ET SUBSTITUTION")
print("=" * 50)

print("\n🔄 REMPLACER DU TEXTE")
print("-" * 20)

# Remplacer une sous-chaîne par une autre
chaine_remplacee = chaines_de_caracteres.replace("chaîne", "ligne")
print(f"✅ replace() - Remplacement simple :")
print(f"   Original : '{chaines_de_caracteres}'")
print(f"   Résultat : '{chaine_remplacee}'")

# Remplacement avec limite
texte_multiple = "Python Python Python est formidable"
remplacement_limite = texte_multiple.replace("Python", "Java", 2)
print(f"✅ replace() avec limite (2 remplacements max) :")
print(f"   Original : '{texte_multiple}'")
print(f"   Résultat : '{remplacement_limite}'")

print("\n💡 USAGE PRATIQUE - Nettoyage de données :")
texte_sale = "Email@@domain..com"
texte_propre = texte_sale.replace("@@", "@").replace("..", ".")
print(f"   Nettoyage email : '{texte_sale}' → '{texte_propre}'")

print("\n" + "=" * 50)
print("4. NETTOYAGE DES ESPACES ET CARACTÈRES")
print("=" * 50)

print("\n🧹 SUPPRIMER LES ESPACES")
print("-" * 25)

# Exemple avec des espaces
texte_avec_espaces = "   Python est génial   "
print(f"Texte avec espaces : '{texte_avec_espaces}'")

# Supprimer les espaces au début et à la fin de la chaîne
chaine_espaces_supprimes = texte_avec_espaces.strip()
print(f"✅ strip() - Supprime espaces début ET fin :")
print(f"   Résultat : '{chaine_espaces_supprimes}'")

# Supprimer les espaces au début de la chaîne
chaine_espaces_debut = texte_avec_espaces.lstrip()
print(f"✅ lstrip() - Supprime espaces à GAUCHE :")
print(f"   Résultat : '{chaine_espaces_debut}'")

# Supprimer les espaces à la fin de la chaîne
chaine_espaces_fin = texte_avec_espaces.rstrip()
print(f"✅ rstrip() - Supprime espaces à DROITE :")
print(f"   Résultat : '{chaine_espaces_fin}'")

print("\n🎯 SUPPRIMER CARACTÈRES SPÉCIFIQUES")
print("-" * 35)

# Supprimer des caractères spécifiques au début et à la fin de la chaîne
texte_ponctuation = "...!!!Python est top!!!..."
chaine_caracteres_specifiques = texte_ponctuation.strip(".!")
print(f"✅ strip() avec caractères spécifiques :")
print(f"   Original : '{texte_ponctuation}'")
print(f"   Résultat : '{chaine_caracteres_specifiques}'")

print("\n💡 USAGE PRATIQUE - Nettoyage input utilisateur :")
saisie_utilisateur = "  Jean Dupont  "
saisie_propre = saisie_utilisateur.strip().title()
print(f"   Saisie brute : '{saisie_utilisateur}'")
print(f"   Saisie nettoyée : '{saisie_propre}'")
print("\n" + "=" * 50)
print("5. DIVISER ET JOINDRE DES CHAÎNES")
print("=" * 50)

print("\n✂️ DIVISER UNE CHAÎNE - split()")
print("-" * 30)

# Diviser la chaîne en une liste de mots
phrase = "Python est un langage formidable"
liste_de_mots = phrase.split()
print(f"✅ split() - Division par espaces (défaut) :")
print(f"   Phrase : '{phrase}'")
print(f"   Mots : {liste_de_mots}")

# Division avec séparateur personnalisé
email = "jean.dupont@email.com"
parties_email = email.split("@")
print(f"✅ split('@') - Division par @ :")
print(f"   Email : '{email}'")
print(f"   Parties : {parties_email}")

# Division avec limite
texte_csv = "nom,prenom,age,ville,pays"
colonnes = texte_csv.split(",", 2)  # Maximum 2 divisions
print(f"✅ split(',', 2) - Division limitée :")
print(f"   CSV : '{texte_csv}'")
print(f"   Résultat : {colonnes}")

print("\n🔗 JOINDRE UNE LISTE - join()")
print("-" * 25)

# Joindre une liste de mots en une chaîne
liste_de_mots = ["Bonjour", "je", "suis", "une", "chaîne", "de", "caractères"]
chaine_jointe = " ".join(liste_de_mots)
print(f"✅ ' '.join() - Joindre avec espaces :")
print(f"   Liste : {liste_de_mots}")
print(f"   Chaîne : '{chaine_jointe}'")

# Joindre avec différents séparateurs
mots = ["Python", "Java", "JavaScript", "C++"]
langages_virgule = ", ".join(mots)
langages_tiret = " - ".join(mots)
print(f"✅ Joindre avec différents séparateurs :")
print(f"   Avec virgules : '{langages_virgule}'")
print(f"   Avec tirets : '{langages_tiret}'")

print("\n💡 USAGE PRATIQUE - Traitement de fichiers CSV :")
ligne_csv = "Jean,Dupont,30,Paris"
donnees = ligne_csv.split(",")
print(f"   Ligne CSV : '{ligne_csv}'")
print(f"   Données extraites : {donnees}")
nouvelle_ligne = ";".join(donnees)
print(f"   Nouveau format : '{nouvelle_ligne}'")

print("\n" + "=" * 50)
print("6. RECHERCHE ET VÉRIFICATION")
print("=" * 50)

print("\n🔍 VÉRIFIER LA PRÉSENCE D'UN TEXTE")
print("-" * 35)

texte_recherche = "Python est un excellent langage de programmation"

# Vérifier si une sous-chaîne est présente dans la chaîne
sous_chaine = "Python"
est_present = sous_chaine in texte_recherche
print(f"✅ Opérateur 'in' - Présence d'un mot :")
print(f"   '{sous_chaine}' dans '{texte_recherche}' : {est_present}")

sous_chaine_absente = "Java"
est_absent = sous_chaine_absente not in texte_recherche
print(f"✅ Opérateur 'not in' - Absence d'un mot :")
print(f"   '{sous_chaine_absente}' PAS dans le texte : {est_absent}")

print("\n📍 TROUVER LA POSITION - find() et index()")
print("-" * 40)

# Trouver la position d'une sous-chaîne dans la chaîne
position = texte_recherche.find("excellent")
print(f"✅ find() - Position de 'excellent' : {position}")

position_inexistant = texte_recherche.find("Java")
print(f"✅ find() - Mot inexistant : {position_inexistant} (retourne -1)")

# Recherche depuis la fin
position_fin = texte_recherche.rfind("e")
print(f"✅ rfind() - Dernier 'e' à la position : {position_fin}")

print("\n🎯 VÉRIFIER DÉBUT ET FIN - startswith() / endswith()")
print("-" * 50)

# Vérifier si la chaîne commence par une sous-chaîne
commence_par = texte_recherche.startswith("Python")
print(f"✅ startswith('Python') : {commence_par}")

# Vérifier si la chaîne se termine par une sous-chaîne
se_termine_par = texte_recherche.endswith("programmation")
print(f"✅ endswith('programmation') : {se_termine_par}")

# Vérification multiple
extensions_valides = (".py", ".pyw", ".pyc")
fichier = "mon_script.py"
est_python = fichier.endswith(extensions_valides)
print(f"✅ Vérification multiple - '{fichier}' est Python : {est_python}")

print("\n📊 COMPTER LES OCCURRENCES - count()")
print("-" * 35)

texte_count = "Python Python Python est partout en Python"
# Compter le nombre d'occurrences d'une sous-chaîne
nombre_python = texte_count.count("Python")
print(f"✅ count('Python') dans '{texte_count}' : {nombre_python} fois")

nombre_voyelles = texte_count.lower().count("a") + texte_count.lower().count("e") + \
    texte_count.lower().count("i") + texte_count.lower().count("o") + \
    texte_count.lower().count("u")
print(f"✅ Nombre total de voyelles : {nombre_voyelles}")
print("\n" + "=" * 50)
print("7. VÉRIFICATIONS DE TYPE ET CONTENU")
print("=" * 50)

print("\n🔢 VÉRIFICATIONS NUMÉRIQUES")
print("-" * 28)

# Tests avec différents types de chaînes
exemples_numeriques = ["123", "12.5", "abc", "123abc", "  ", ""]

for exemple in exemples_numeriques:
    if exemple:  # Si la chaîne n'est pas vide
        print(f"\n📝 Analyse de : '{exemple}'")
        # Vérifier si la chaîne est numérique
        est_numerique = exemple.isnumeric()
        print(f"   ✅ isnumeric() : {est_numerique}")

        # Vérifier si la chaîne ne contient que des chiffres
        est_digit = exemple.isdigit()
        print(f"   ✅ isdigit() : {est_digit}")

        # Vérifier si la chaîne peut être convertie en nombre
        try:
            float(exemple)
            peut_etre_nombre = True
        except:
            peut_etre_nombre = False
        print(f"   ✅ Peut être converti en nombre : {peut_etre_nombre}")

print("\n🔤 VÉRIFICATIONS ALPHABÉTIQUES")
print("-" * 30)

exemples_alpha = ["Python", "Python3", "HELLO", "hello", "Hello World", "123"]

for exemple in exemples_alpha:
    print(f"\n📝 Analyse de : '{exemple}'")
    # Vérifier si la chaîne est alphabétique
    est_alphabetique = exemple.isalpha()
    print(f"   ✅ isalpha() (que des lettres) : {est_alphabetique}")

    # Vérifier si la chaîne est alphanumérique
    est_alphanumerique = exemple.isalnum()
    print(f"   ✅ isalnum() (lettres + chiffres) : {est_alphanumerique}")

    # Vérifier si la chaîne est en majuscules
    est_en_majuscules = exemple.isupper()
    print(f"   ✅ isupper() (tout en majuscules) : {est_en_majuscules}")

    # Vérifier si la chaîne est en minuscules
    est_en_minuscules = exemple.islower()
    print(f"   ✅ islower() (tout en minuscules) : {est_en_minuscules}")

print("\n🎯 VÉRIFICATIONS SPÉCIALES")
print("-" * 25)

exemples_speciaux = ["   ", "", "mon_variable",
                     "class", "2variable", "_private"]

for exemple in exemples_speciaux:
    print(f"\n📝 Analyse de : '{exemple}' (longueur: {len(exemple)})")

    # Vérifier si la chaîne est un espace
    est_espace = exemple.isspace()
    print(f"   ✅ isspace() (que des espaces) : {est_espace}")

    # Vérifier si la chaîne est vide
    est_vide = not exemple
    print(f"   ✅ Chaîne vide : {est_vide}")

    if exemple.strip():  # Si pas vide après nettoyage
        # Vérifier si la chaîne est un identifiant Python valide
        est_identifiant = exemple.isidentifier()
        print(f"   ✅ isidentifier() (nom variable valide) : {est_identifiant}")

print("\n" + "=" * 50)
print("8. FORMATAGE ET ALIGNEMENT")
print("=" * 50)

print("\n📐 FORMATAGE DE LARGEUR")
print("-" * 25)

mot = "Python"
largeur = 20

print(f"✅ center() - Centrer sur {largeur} caractères :")
resultat_center = mot.center(largeur, "-")
print(f"   '{resultat_center}'")

print(f"✅ ljust() - Aligner à gauche :")
resultat_ljust = mot.ljust(largeur, ".")
print(f"   '{resultat_ljust}'")

print(f"✅ rjust() - Aligner à droite :")
resultat_rjust = mot.rjust(largeur, "*")
print(f"   '{resultat_rjust}'")

print(f"✅ zfill() - Remplir avec des zéros :")
nombre = "42"
resultat_zfill = nombre.zfill(8)
print(f"   '{nombre}' → '{resultat_zfill}'")

print("\n💡 USAGE PRATIQUE - Tableau formaté :")
noms = ["Alice", "Bob", "Charlotte"]
ages = [25, 30, 28]
print(f"{'Nom':<12} {'Age':>5}")
print("-" * 17)
for nom, age in zip(noms, ages):
    print(f"{nom:<12} {age:>5}")

print("\n" + "=" * 50)
print("9. TECHNIQUES AVANCÉES")
print("=" * 50)

print("\n🎨 ENCODAGE ET CARACTÈRES SPÉCIAUX")
print("-" * 35)

# Gestion des caractères spéciaux
texte_accents = "Café, naïveté, coïncidence"
print(f"✅ Texte avec accents : '{texte_accents}'")
print(f"   Longueur : {len(texte_accents)} caractères")
print(f"   encode('utf-8') : {texte_accents.encode('utf-8')}")

# Normalisation des caractères
texte_avec_espaces = "Python    est    génial"
texte_normalise = " ".join(texte_avec_espaces.split())
print(f"✅ Normalisation des espaces multiples :")
print(f"   Avant : '{texte_avec_espaces}'")
print(f"   Après : '{texte_normalise}'")

print("\n🔄 MÉTHODES CHAÎNÉES")
print("-" * 20)

texte_brut = "  PYTHON est UN langage FORMIDABLE  "
resultat_chaine = texte_brut.strip().lower().title().replace("Un", "un excellent")
print(f"✅ Chaînage de méthodes :")
print(f"   Original : '{texte_brut}'")
print(f"   Résultat : '{resultat_chaine}'")

print("\n🎯 VALIDATION DE DONNÉES")
print("-" * 25)


def valider_email(email):
    """Validation simple d'email"""
    email = email.strip().lower()
    return "@" in email and "." in email and not email.startswith("@") and not email.endswith("@")


def valider_telephone(tel):
    """Validation simple de téléphone"""
    tel_propre = tel.replace(" ", "").replace("-", "").replace(".", "")
    return tel_propre.isdigit() and 10 <= len(tel_propre) <= 15


# Tests de validation
emails_test = ["jean@email.com", "invalid-email", "@test.com", "test@"]
telephones_test = ["06.12.34.56.78", "0123456789", "abc123", "123"]

print("Tests d'emails :")
for email in emails_test:
    valide = valider_email(email)
    print(f"   '{email}' : {'✅ Valide' if valide else '❌ Invalide'}")

print("Tests de téléphones :")
for tel in telephones_test:
    valide = valider_telephone(tel)
    print(f"   '{tel}' : {'✅ Valide' if valide else '❌ Invalide'}")

print("\n" + "=" * 50)
print("11. TABLEAU RÉCAPITULATIF DES MÉTHODES")
print("=" * 50)

print("""
📊 GUIDE DE RÉFÉRENCE RAPIDE

🔤 TRANSFORMATION :
   • upper() / lower() / title() / capitalize()
   • swapcase() - Inverse maj/min
   • strip() / lstrip() / rstrip() - Supprime espaces
   • replace(ancien, nouveau) - Remplace texte

✂️ DIVISION/JOINTURE :
   • split(séparateur) - Divise en liste
   • join(liste) - Joint liste en chaîne
   • partition() / rpartition() - Divise en 3 parties

🔍 RECHERCHE :
   • find() / rfind() - Position (retourne -1 si absent)
   • index() / rindex() - Position (erreur si absent)
   • count() - Nombre d'occurrences
   • in / not in - Présence/absence

✅ VÉRIFICATIONS :
   • startswith() / endswith() - Début/fin
   • isalpha() / isdigit() / isalnum() - Type de caractères
   • isupper() / islower() - Casse
   • isspace() / isidentifier() - Caractères spéciaux

📐 FORMATAGE :
   • center() / ljust() / rjust() - Alignement
   • zfill() - Remplissage avec zéros
   • format() / f-string - Formatage moderne
""")

print("\n" + "=" * 50)
print("12. RÉSUMÉ FINAL")
print("=" * 50)

print("""
🎯 POINTS CLÉS À RETENIR :

1. 📝 CHAÎNES = SÉQUENCES IMMUTABLES :
   • Chaque méthode retourne une NOUVELLE chaîne
   • L'original n'est jamais modifié
   • Pensez à stocker le résultat : texte = texte.upper()

2. 🔍 RECHERCHE ET VÉRIFICATION :
   • 'in' pour vérifier la présence
   • find() vs index() (erreur ou -1)
   • startswith() / endswith() pour début/fin

3. 🧹 NETTOYAGE ESSENTIEL :
   • strip() pour nettoyer les saisies utilisateur
   • replace() pour corriger les données
   • split() / join() pour restructurer

4. ✅ VALIDATION DE DONNÉES :
   • isdigit() / isnumeric() pour les nombres
   • isalpha() / isalnum() pour le contenu
   • isidentifier() pour les noms de variables

5. 🎨 FORMATAGE PROFESSIONNEL :
   • F-strings pour l'affichage moderne
   • center() / ljust() / rjust() pour l'alignement
   • Méthodes chaînées pour plus d'efficacité

💡 FORMULE MAGIQUE pour traiter les chaînes :
   Nettoyer → Transformer → Valider → Formater

🎉 Félicitations ! Vous maîtrisez les chaînes Python !
💡 Prochaine étape : Les nombres et calculs !
📚 Continuez avec 005_les_fonctions_int.py
""")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE")
print("=" * 70)
