#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
======================================================================
BOUCLE FOR EN PYTHON - GUIDE COMPLET
======================================================================

🎯 Ce fichier couvre la boucle for en détail :
   • Syntaxe et itération sur séquences
   • range() et ses variations
   • For avec else
   • Itération sur différents types
   • Boucles imbriquées
   • Enumerate et zip

📚 Concepts abordés :
   • for element in sequence:
   • range(start, stop, step)
   • Listes, chaînes, tuples, dictionnaires
   • Compréhensions de listes (introduction)
   • Patterns d'itération

💡 Objectif : Maîtriser les itérations sur séquences
"""

print("=" * 70)
print("BOUCLE FOR EN PYTHON - GUIDE COMPLET")
print("=" * 70)

print("\n" + "=" * 50)
print("1. SYNTAXE ET PRINCIPES DE BASE")
print("=" * 50)

print("\n🔄 ITÉRATION SUR UNE LISTE")
print("-" * 24)

fruits = ["pomme", "banane", "orange", "kiwi", "mangue"]
print(f"🍎 Liste de fruits : {fruits}")

print("🔄 Parcours simple :")
for fruit in fruits:
    print(f"   - {fruit}")

print("\n🔢 ITÉRATION SUR UNE CHAÎNE")
print("-" * 26)

mot = "Python"
print(f"📝 Mot : '{mot}'")

print("🔠 Parcours des caractères :")
for lettre in mot:
    print(f"   '{lettre}'", end=" ")
print()  # Saut de ligne

print("\n📊 ITÉRATION SUR UN TUPLE")
print("-" * 24)

coordonnees = (10, 20, 30)
print(f"📍 Coordonnées : {coordonnees}")

print("🎯 Parcours du tuple :")
for valeur in coordonnees:
    print(f"   Valeur : {valeur}")

print("\n" + "=" * 50)
print("2. LA FONCTION RANGE()")
print("=" * 50)

print("\n🎯 RANGE SIMPLE")
print("-" * 14)

print("🔢 range(5) - nombres de 0 à 4 :")
for i in range(5):
    print(f"   {i}", end=" ")
print()

print("\n📈 RANGE AVEC DÉBUT ET FIN")
print("-" * 25)

print("🔢 range(2, 8) - nombres de 2 à 7 :")
for i in range(2, 8):
    print(f"   {i}", end=" ")
print()

print("\n⚡ RANGE AVEC PAS")
print("-" * 17)

print("🔢 range(0, 20, 3) - de 0 à 20 par pas de 3 :")
for i in range(0, 20, 3):
    print(f"   {i}", end=" ")
print()

print("\n📉 RANGE DÉCROISSANT")
print("-" * 19)

print("🔢 range(10, 0, -2) - de 10 à 1 par pas de -2 :")
for i in range(10, 0, -2):
    print(f"   {i}", end=" ")
print()

print("\n💡 APPLICATIONS PRATIQUES DE RANGE")
print("-" * 33)

# Table de multiplication
nombre = 7
print(f"📊 Table de multiplication de {nombre} :")
for i in range(1, 11):
    resultat = nombre * i
    print(f"   {nombre} × {i:2d} = {resultat:2d}")

print("\n" + "=" * 50)
print("3. ITÉRATION AVEC INDEX")
print("=" * 50)

print("\n🔍 ACCÈS AUX INDEX AVEC RANGE ET LEN")
print("-" * 35)

animaux = ["chat", "chien", "oiseau", "poisson"]
print(f"🐾 Animaux : {animaux}")

print("📍 Parcours avec index :")
for i in range(len(animaux)):
    print(f"   Index {i} : {animaux[i]}")

print("\n⭐ FONCTION ENUMERATE (RECOMMANDÉE)")
print("-" * 36)

print("📍 Parcours avec enumerate :")
for index, animal in enumerate(animaux):
    print(f"   Index {index} : {animal}")

print("\n🎯 ENUMERATE AVEC DÉBUT PERSONNALISÉ")
print("-" * 34)

print("📍 Parcours avec enumerate(start=1) :")
for numero, animal in enumerate(animaux, start=1):
    print(f"   Animal #{numero} : {animal}")

print("\n" + "=" * 50)
print("4. ITÉRATION SUR DICTIONNAIRES")
print("=" * 50)

print("\n📖 PARCOURS DES CLÉS")
print("-" * 19)

personne = {
    "nom": "Alice",
    "age": 30,
    "ville": "Paris",
    "profession": "Développeuse"
}

print(f"👤 Dictionnaire personne : {personne}")

print("🔑 Parcours des clés :")
for cle in personne:
    print(f"   Clé : {cle}")

print("\n📄 PARCOURS DES VALEURS")
print("-" * 22)

print("💎 Parcours des valeurs :")
for valeur in personne.values():
    print(f"   Valeur : {valeur}")

print("\n🔗 PARCOURS DES PAIRES CLÉ-VALEUR")
print("-" * 31)

print("📋 Parcours avec items() :")
for cle, valeur in personne.items():
    print(f"   {cle} : {valeur}")

print("\n" + "=" * 50)
print("5. FONCTION ZIP ET ITÉRATIONS PARALLÈLES")
print("=" * 50)

print("\n🤝 COMBINER PLUSIEURS LISTES")
print("-" * 27)

noms = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
villes = ["Paris", "Lyon", "Marseille"]

print(f"👥 Noms : {noms}")
print(f"🎂 Âges : {ages}")
print(f"🏙️ Villes : {villes}")

print("\n🔗 Itération parallèle avec zip :")
for nom, age, ville in zip(noms, ages, villes):
    print(f"   {nom}, {age} ans, habite à {ville}")

print("\n⚠️ ZIP AVEC LISTES DE TAILLES DIFFÉRENTES")
print("-" * 38)

couleurs = ["rouge", "vert", "bleu", "jaune", "violet"]
objets = ["pomme", "herbe", "ciel"]

print(f"🎨 Couleurs : {couleurs}")
print(f"🏺 Objets : {objets}")

print("🔗 Zip s'arrête à la liste la plus courte :")
for couleur, objet in zip(couleurs, objets):
    print(f"   {objet} {couleur}")

print("\n" + "=" * 50)
print("6. FOR AVEC ELSE")
print("=" * 50)

print("\n🔍 RECHERCHE AVEC FOR...ELSE")
print("-" * 27)

nombres = [2, 4, 6, 8, 10]
nombre_cherche = 7

print(f"🔢 Liste : {nombres}")
print(f"🎯 Recherche de : {nombre_cherche}")

for nombre in nombres:
    if nombre == nombre_cherche:
        print(f"✅ {nombre_cherche} trouvé !")
        break
else:
    # Cette clause s'exécute si aucun break n'a eu lieu
    print(f"❌ {nombre_cherche} non trouvé dans la liste")

print("\n💡 VALIDATION DE DONNÉES")
print("-" * 23)

mots_de_passe = ["123456", "password", "motdepasse123", "Secure2024!"]

for mdp in mots_de_passe:
    print(f"🔐 Test de '{mdp}' :")

    # Vérifications
    for char in mdp:
        if char.isupper():
            print("   ✅ Contient une majuscule")
            break
    else:
        print("   ❌ Aucune majuscule")

    for char in mdp:
        if char.isdigit():
            print("   ✅ Contient un chiffre")
            break
    else:
        print("   ❌ Aucun chiffre")

    if len(mdp) >= 8:
        print("   ✅ Longueur suffisante")
    else:
        print("   ❌ Trop court")
    print()

print("\n" + "=" * 50)
print("7. BOUCLES IMBRIQUÉES")
print("=" * 50)

print("\n🎯 MATRICE ET TABLEAUX 2D")
print("-" * 24)

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("🔢 Matrice 3x3 :")
print("   ", end="")
for j in range(len(matrice[0])):
    print(f"Col{j}", end="  ")
print()

for i, ligne in enumerate(matrice):
    print(f"L{i} ", end="")
    for element in ligne:
        print(f"{element:4d}", end="  ")
    print()

print("\n🎨 MOTIFS ET PATTERNS")
print("-" * 20)

print("⭐ Triangle d'étoiles :")
for ligne in range(1, 6):
    for etoile in range(ligne):
        print("*", end="")
    print()

print("\n🔢 Table de Pythagore (5x5) :")
print("    ", end="")
for j in range(1, 6):
    print(f"{j:3d}", end="")
print()

for i in range(1, 6):
    print(f"{i:2d} |", end="")
    for j in range(1, 6):
        produit = i * j
        print(f"{produit:3d}", end="")
    print()

print("\n" + "=" * 50)
print("8. PATTERNS D'ITÉRATION AVANCÉS")
print("=" * 50)

print("\n🎯 FILTRAGE PENDANT L'ITÉRATION")
print("-" * 30)

nombres = list(range(1, 21))  # 1 à 20
print(f"🔢 Nombres : {nombres}")

print("🔍 Nombres pairs :")
for nombre in nombres:
    if nombre % 2 == 0:
        print(f"   {nombre}", end=" ")
print()

print("\n📊 GROUPEMENT DE DONNÉES")
print("-" * 22)

etudiants = [
    {"nom": "Alice", "note": 85, "mention": ""},
    {"nom": "Bob", "note": 72, "mention": ""},
    {"nom": "Charlie", "note": 91, "mention": ""},
    {"nom": "Diana", "note": 68, "mention": ""}
]

print("🎓 Attribution des mentions :")
for etudiant in etudiants:
    if etudiant["note"] >= 90:
        etudiant["mention"] = "Excellent"
    elif etudiant["note"] >= 80:
        etudiant["mention"] = "Très Bien"
    elif etudiant["note"] >= 70:
        etudiant["mention"] = "Bien"
    else:
        etudiant["mention"] = "Assez Bien"

    print(
        f"   {etudiant['nom']:8} : {etudiant['note']:2d}/100 - {etudiant['mention']}")

print("\n🔄 TRANSFORMATION DE DONNÉES")
print("-" * 26)

temperatures_celsius = [0, 10, 20, 30, 40]
print(f"🌡️ Températures Celsius : {temperatures_celsius}")

print("🌡️ Conversion en Fahrenheit :")
temperatures_fahrenheit = []
for celsius in temperatures_celsius:
    fahrenheit = (celsius * 9/5) + 32
    temperatures_fahrenheit.append(fahrenheit)
    print(f"   {celsius}°C = {fahrenheit}°F")

print(f"📊 Résultat : {temperatures_fahrenheit}")

print("\n" + "=" * 50)
print("9. INTRODUCTION AUX COMPRÉHENSIONS")
print("=" * 50)

print("\n✨ LIST COMPREHENSIONS")
print("-" * 21)

# Méthode traditionnelle avec for
carres_traditionnel = []
for x in range(1, 6):
    carres_traditionnel.append(x**2)

print(f"🔢 Carrés (méthode traditionnelle) : {carres_traditionnel}")

# Compréhension de liste (plus concise)
carres_comprehension = [x**2 for x in range(1, 6)]
print(f"✨ Carrés (compréhension) : {carres_comprehension}")

print("\n🎯 COMPRÉHENSIONS AVEC CONDITIONS")
print("-" * 32)

# Nombres pairs avec for traditionnel
pairs_traditionnel = []
for x in range(1, 11):
    if x % 2 == 0:
        pairs_traditionnel.append(x)

print(f"🔢 Pairs traditionnels : {pairs_traditionnel}")

# Avec compréhension
pairs_comprehension = [x for x in range(1, 11) if x % 2 == 0]
print(f"✨ Pairs compréhension : {pairs_comprehension}")

print("\n" + "=" * 50)
print("10. APPLICATIONS PRATIQUES")
print("=" * 50)

print("\n📊 ANALYSE DE DONNÉES")
print("-" * 19)

ventes = [
    {"produit": "Ordinateur", "prix": 800, "quantite": 2},
    {"produit": "Souris", "prix": 25, "quantite": 10},
    {"produit": "Clavier", "prix": 60, "quantite": 5},
    {"produit": "Écran", "prix": 300, "quantite": 3}
]

print("💰 Calcul du chiffre d'affaires :")
total_ca = 0

for vente in ventes:
    ca_produit = vente["prix"] * vente["quantite"]
    total_ca += ca_produit
    print(
        f"   {vente['produit']:12} : {vente['quantite']} × {vente['prix']}€ = {ca_produit}€")

print(f"📈 Total CA : {total_ca}€")

print("\n🎮 GÉNÉRATION DE GRILLE DE JEU")
print("-" * 29)


def generer_grille_morpion():
    """Génère une grille de morpion vide"""
    grille = []
    for ligne in range(3):
        rangee = []
        for colonne in range(3):
            rangee.append(" ")
        grille.append(rangee)
    return grille


def afficher_grille(grille):
    """Affiche la grille de morpion"""
    print("  0   1   2")
    for i, ligne in enumerate(grille):
        print(f"{i} ", end="")
        for j, case in enumerate(ligne):
            print(f"{case}", end="")
            if j < 2:
                print(" | ", end="")
        print()
        if i < 2:
            print("  ---------")


# Test de la grille
grille = generer_grille_morpion()
grille[1][1] = "X"  # Placer un X au centre
grille[0][0] = "O"  # Placer un O en haut à gauche

print("🎮 Grille de Morpion :")
afficher_grille(grille)

print("\n📝 STATISTIQUES DE TEXTE")
print("-" * 23)

texte = "Python est un langage de programmation puissant et facile à apprendre"
print(f"📄 Texte : '{texte}'")

# Comptage des caractères
compteurs = {}
for caractere in texte.lower():
    if caractere.isalpha():  # Seulement les lettres
        if caractere in compteurs:
            compteurs[caractere] += 1
        else:
            compteurs[caractere] = 1

print("📊 Fréquence des lettres :")
for lettre in sorted(compteurs.keys()):
    print(f"   '{lettre}' : {compteurs[lettre]} fois")

# Trouver la lettre la plus fréquente
lettre_max = ""
freq_max = 0
for lettre, freq in compteurs.items():
    if freq > freq_max:
        freq_max = freq
        lettre_max = lettre

print(f"🏆 Lettre la plus fréquente : '{lettre_max}' ({freq_max} fois)")

print("\n" + "=" * 50)
print("11. EXERCICES PRATIQUES")
print("=" * 50)

print("""
💪 EXERCICES À FAIRE (décommentez pour tester) :

# Exercice 1 : Somme et moyenne
# def calculer_statistiques():
#     nombres = [10, 15, 20, 25, 30, 35, 40]
#     
#     somme = 0
#     for nombre in nombres:
#         somme += nombre
#     
#     moyenne = somme / len(nombres)
#     print(f"Somme : {somme}")
#     print(f"Moyenne : {moyenne:.2f}")

# Exercice 2 : Recherche du maximum
# def trouver_maximum():
#     valeurs = [45, 23, 67, 89, 12, 56, 78]
#     
#     maximum = valeurs[0]
#     position = 0
#     
#     for i, valeur in enumerate(valeurs):
#         if valeur > maximum:
#             maximum = valeur
#             position = i
#     
#     print(f"Maximum : {maximum} à la position {position}")

# Exercice 3 : Palindrome
# def verifier_palindrome():
#     mot = input("Entrez un mot : ").lower()
#     
#     est_palindrome = True
#     longueur = len(mot)
#     
#     for i in range(longueur // 2):
#         if mot[i] != mot[longueur - 1 - i]:
#             est_palindrome = False
#             break
#     
#     if est_palindrome:
#         print(f"'{mot}' est un palindrome !")
#     else:
#         print(f"'{mot}' n'est pas un palindrome")

# Exercice 4 : Génération de mots de passe
# def generer_motdepasse():
#     import random
#     
#     minuscules = "abcdefghijklmnopqrstuvwxyz"
#     majuscules = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     chiffres = "0123456789"
#     speciaux = "!@#$%^&*"
#     
#     tous_caracteres = minuscules + majuscules + chiffres + speciaux
#     
#     longueur = 12
#     motdepasse = ""
#     
#     for i in range(longueur):
#         motdepasse += random.choice(tous_caracteres)
#     
#     print(f"Mot de passe généré : {motdepasse}")

# Exercice 5 : FizzBuzz
# def fizzbuzz():
#     for i in range(1, 101):
#         if i % 15 == 0:  # Divisible par 3 ET 5
#             print("FizzBuzz", end=" ")
#         elif i % 3 == 0:
#             print("Fizz", end=" ")
#         elif i % 5 == 0:
#             print("Buzz", end=" ")
#         else:
#             print(i, end=" ")
#         
#         if i % 10 == 0:  # Nouvelle ligne tous les 10 nombres
#             print()
""")

print("\n" + "=" * 50)
print("12. RÉSUMÉ FINAL")
print("=" * 50)

print("""
🎯 POINTS CLÉS À RETENIR :

1. 🔄 SYNTAXE FOR :
   • for element in sequence:
   • Plus lisible que while pour les séquences
   • Itération directe sur les éléments

2. 🔢 FONCTION RANGE :
   • range(stop) : de 0 à stop-1
   • range(start, stop) : de start à stop-1
   • range(start, stop, step) : avec pas personnalisé

3. 📍 ACCÈS AUX INDEX :
   • enumerate() plutôt que range(len())
   • zip() pour itérations parallèles
   • items() pour les dictionnaires

4. 🔍 FOR...ELSE :
   • else s'exécute si pas de break
   • Utile pour les recherches et validations

5. 🎯 BOUCLES IMBRIQUÉES :
   • Attention à la complexité
   • Utiles pour matrices et grilles
   • Bien indenter pour la lisibilité

6. ✨ COMPRÉHENSIONS :
   • Plus concises que les boucles classiques
   • [expression for item in sequence if condition]

💡 FORMULE MAGIQUE for :
   Séquence → Itération → Traitement → Résultat

🎉 Félicitations ! Vous maîtrisez la boucle for !
💡 Prochaine étape : Contrôle de flux (break, continue) !
📚 For maîtrisé, passez au contrôle de flux !
""")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE - BOUCLE FOR MAÎTRISÉE !")
print("=" * 70)
