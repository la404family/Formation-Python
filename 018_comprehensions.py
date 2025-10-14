#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
======================================================================
LES COMPRÉHENSIONS EN PYTHON - GUIDE COMPLET
======================================================================

🎯 Ce fichier couvre toutes les compréhensions en détail :
   • List comprehensions
   • Dict comprehensions
   • Set comprehensions
   • Generator expressions
   • Compréhensions imbriquées
   • Optimisations et bonnes pratiques

📚 Concepts abordés :
   • Syntaxe [expr for item in iterable if condition]
   • Filtrage et transformation
   • Compréhensions conditionnelles
   • Imbrications multiples
   • Performances vs boucles classiques
   • Lisibilité et maintenabilité

💡 Objectif : Maîtriser l'art des compréhensions pythoniques
"""

import random
from collections import Counter
import re
import time
import sys

print("=" * 70)
print("LES COMPRÉHENSIONS EN PYTHON - GUIDE COMPLET")
print("=" * 70)

print("\n" + "=" * 50)
print("1. LIST COMPREHENSIONS - BASES")
print("=" * 50)

print("\n📝 SYNTAXE FONDAMENTALE")
print("-" * 22)

# Syntaxe de base : [expr for item in iterable]
nombres = [1, 2, 3, 4, 5]

# Méthode traditionnelle
carres_traditionnel = []
for x in nombres:
    carres_traditionnel.append(x**2)

# List comprehension
carres_comprehension = [x**2 for x in nombres]

print(f"🔢 Nombres : {nombres}")
print(f"🔢 Carrés (traditionnel) : {carres_traditionnel}")
print(f"✨ Carrés (comprehension) : {carres_comprehension}")

print("\n🔍 AVEC CONDITIONS")
print("-" * 17)

# Syntaxe avec condition : [expr for item in iterable if condition]
nombres_etendus = range(1, 11)

# Carrés des nombres pairs seulement
carres_pairs = [x**2 for x in nombres_etendus if x % 2 == 0]
print(f"🔢 Carrés des pairs (1-10) : {carres_pairs}")

# Transformation conditionnelle dans l'expression
absolus = [x if x >= 0 else -x for x in [-3, -1, 0, 2, 5]]
print(f"🔢 Valeurs absolues : {absolus}")

# Condition ternaire complexe
descriptions = [
    f"{x} est {'pair' if x % 2 == 0 else 'impair'}"
    for x in range(1, 6)
]
print(f"📝 Descriptions :")
for desc in descriptions:
    print(f"   {desc}")

print("\n🔄 TRANSFORMATIONS DIVERSES")
print("-" * 26)

# Transformation de strings
mots = ["python", "java", "javascript", "go", "rust"]

# Majuscules
mots_majuscules = [mot.upper() for mot in mots]
print(f"🔤 Majuscules : {mots_majuscules}")

# Longueurs
longueurs = [len(mot) for mot in mots]
print(f"📏 Longueurs : {longueurs}")

# Première lettre
premieres_lettres = [mot[0] for mot in mots if mot]
print(f"🔤 Premières lettres : {premieres_lettres}")

# Mots longs seulement
mots_longs = [mot for mot in mots if len(mot) > 4]
print(f"📚 Mots longs (>4) : {mots_longs}")

print("\n" + "=" * 50)
print("2. DICT COMPREHENSIONS")
print("=" * 50)

print("\n📚 CRÉATION DE DICTIONNAIRES")
print("-" * 27)

# Syntaxe : {key_expr: value_expr for item in iterable}
nombres = range(1, 6)

# Dictionnaire nombre → carré
carres_dict = {x: x**2 for x in nombres}
print(f"📊 Carrés dict : {carres_dict}")

# Dictionnaire nombre → description
descriptions_dict = {
    x: f"Le carré de {x} est {x**2}"
    for x in nombres
}
print(f"📊 Descriptions dict :")
for num, desc in descriptions_dict.items():
    print(f"   {num}: {desc}")

print("\n🔄 TRANSFORMATION DE DONNÉES")
print("-" * 28)

# Inversion clé-valeur
original = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
inverse = {valeur: cle for cle, valeur in original.items()}
print(f"📚 Original : {original}")
print(f"📚 Inversé : {inverse}")

# Filtrage avec condition
pairs_seulement = {cle: valeur for cle,
                   valeur in original.items() if valeur % 2 == 0}
print(f"📚 Pairs seulement : {pairs_seulement}")

# Transformation des valeurs
double_valeurs = {cle: valeur * 2 for cle, valeur in original.items()}
print(f"📚 Valeurs doublées : {double_valeurs}")

print("\n🎯 APPLICATIONS PRATIQUES")
print("-" * 25)

# Comptage de caractères dans un texte
texte = "python est fantastique"
compteur_chars = {char: texte.count(char)
                  for char in set(texte) if char != ' '}
print(f"📝 Texte : '{texte}'")
print(f"📊 Compteur caractères : {dict(sorted(compteur_chars.items()))}")

# Informations sur une liste de mots
mots_info = {
    mot: {
        'longueur': len(mot),
        'voyelles': sum(1 for char in mot.lower() if char in 'aeiou'),
        'consonnes': sum(1 for char in mot.lower() if char.isalpha() and char not in 'aeiou')
    }
    for mot in ['python', 'java', 'go', 'rust']
}

print(f"📊 Infos sur les mots :")
for mot, info in mots_info.items():
    print(f"   {mot:<8} : {info}")

print("\n" + "=" * 50)
print("3. SET COMPREHENSIONS")
print("=" * 50)

print("\n📦 CRÉATION D'ENSEMBLES")
print("-" * 23)

# Syntaxe : {expr for item in iterable}
phrase = "les ensembles sont très utiles"

# Ensemble des caractères uniques (sans espaces)
chars_uniques = {char for char in phrase if char != ' '}
print(f"📝 Phrase : '{phrase}'")
print(f"📦 Caractères uniques : {sorted(chars_uniques)}")

# Ensemble des longueurs de mots
mots_phrase = phrase.split()
longueurs_uniques = {len(mot) for mot in mots_phrase}
print(f"📏 Longueurs uniques : {sorted(longueurs_uniques)}")

print("\n🔍 DÉDUPLICATION AVANCÉE")
print("-" * 26)

# Données avec doublons
etudiants = [
    ("Alice", "Informatique", 20),
    ("Bob", "Mathématiques", 19),
    ("Charlie", "Informatique", 21),
    ("Diana", "Physique", 20),
    ("Eve", "Mathématiques", 19)
]

# Ensemble des filières uniques
filieres = {etudiant[1] for etudiant in etudiants}
print(f"🎓 Filières : {sorted(filieres)}")

# Ensemble des âges uniques
ages = {etudiant[2] for etudiant in etudiants}
print(f"🎂 Âges : {sorted(ages)}")

# Ensemble des étudiants en informatique
etudiants_info = {etudiant[0]
                  for etudiant in etudiants if etudiant[1] == "Informatique"}
print(f"💻 Étudiants en informatique : {etudiants_info}")

print("\n🎯 OPÉRATIONS MATHÉMATIQUES")
print("-" * 27)

# Ensembles de nombres avec conditions
multiples_3 = {x for x in range(1, 31) if x % 3 == 0}
multiples_5 = {x for x in range(1, 31) if x % 5 == 0}

print(f"🔢 Multiples de 3 (1-30) : {multiples_3}")
print(f"🔢 Multiples de 5 (1-30) : {multiples_5}")
print(f"🔢 Multiples de 3 ET 5 : {multiples_3 & multiples_5}")
print(f"🔢 Multiples de 3 OU 5 : {sorted(multiples_3 | multiples_5)}")

print("\n" + "=" * 50)
print("4. GENERATOR EXPRESSIONS")
print("=" * 50)

print("\n⚡ GÉNÉRATEURS VS LISTES")
print("-" * 24)


# List comprehension (charge tout en mémoire)
carres_liste = [x**2 for x in range(1000)]

# Generator expression (calcul à la demande)
carres_generateur = (x**2 for x in range(1000))

print(f"💾 Mémoire liste : {sys.getsizeof(carres_liste)} bytes")
print(f"💾 Mémoire générateur : {sys.getsizeof(carres_generateur)} bytes")
print(
    f"💾 Gain : {sys.getsizeof(carres_liste) / sys.getsizeof(carres_generateur):.1f}x")

# Utilisation du générateur
print(f"🔢 Premiers carrés (générateur) : {list(carres_generateur)[:10]}...")

print("\n🔄 CONSOMMATION LAZY")
print("-" * 19)


def nombre_avec_log(n):
    """Fonction qui affiche quand elle est appelée"""
    print(f"   Calcul pour {n}")
    return n**2


# Générateur - calcul à la demande
gen_lazy = (nombre_avec_log(x) for x in range(1, 6))
print("🔧 Générateur créé (aucun calcul encore)")

print("🔧 Consommation du générateur :")
for i, valeur in enumerate(gen_lazy):
    print(f"   Résultat {i+1}: {valeur}")
    if i == 2:  # S'arrêter après 3 éléments
        break

print("\n🎯 APPLICATIONS PRATIQUES")
print("-" * 25)

# Traitement de gros fichiers (simulé)


def lignes_fichier_simule():
    """Simule la lecture d'un gros fichier"""
    for i in range(1, 11):
        yield f"Ligne {i}: données importantes"


# Generator expression pour filtrer
lignes_importantes = (
    ligne.upper()
    for ligne in lignes_fichier_simule()
    if "importantes" in ligne
)

print("📄 Lignes filtrées :")
for ligne in lignes_importantes:
    print(f"   {ligne}")

# Pipeline de transformations
nombres_bruts = range(1, 21)
pipeline = (
    str(x**2)[::-1]  # Carré puis inversion de string
    for x in nombres_bruts
    if x % 2 == 0  # Pairs seulement
)

print(f"🔧 Pipeline (carrés pairs inversés) : {list(pipeline)}")

print("\n" + "=" * 50)
print("5. COMPRÉHENSIONS IMBRIQUÉES")
print("=" * 50)

print("\n🎯 BOUCLES MULTIPLES")
print("-" * 19)

# Syntaxe : [expr for x in iter1 for y in iter2]
# Équivalent à : for x in iter1: for y in iter2: append(expr)

# Coordonnées 2D
coordonnees = [(x, y) for x in range(3) for y in range(3)]
print(f"📊 Coordonnées 3x3 : {coordonnees}")

# Avec condition
coordonnees_diagonale = [(x, y) for x in range(3) for y in range(3) if x == y]
print(f"📊 Diagonale : {coordonnees_diagonale}")

# Table de multiplication
table_mult = [
    f"{x}×{y}={x*y}"
    for x in range(1, 4)
    for y in range(1, 4)
]
print(f"🔢 Table multiplication :")
for i, operation in enumerate(table_mult):
    print(f"   {operation}", end="  ")
    if (i + 1) % 3 == 0:  # Nouvelle ligne tous les 3
        print()

print("\n🏗️ STRUCTURES COMPLEXES")
print("-" * 24)

# Matrice aplatie depuis matrice 2D
matrice_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrice_aplatie = [element for ligne in matrice_2d for element in ligne]
print(f"📊 Matrice 2D : {matrice_2d}")
print(f"📏 Aplatie : {matrice_aplatie}")

# Mots depuis phrases
phrases = ["Python est génial", "Java est verbeux", "Go est rapide"]
tous_mots = [mot for phrase in phrases for mot in phrase.split()]
print(f"📝 Phrases : {phrases}")
print(f"🔤 Tous les mots : {tous_mots}")

# Mots longs seulement
mots_longs = [
    mot for phrase in phrases
    for mot in phrase.split()
    if len(mot) > 3
]
print(f"📚 Mots longs : {mots_longs}")

print("\n🎭 COMPRÉHENSIONS CONDITIONNELLES COMPLEXES")
print("-" * 43)

# Données d'étudiants
etudiants_notes = [
    {"nom": "Alice", "notes": [15, 17, 16], "filiere": "Info"},
    {"nom": "Bob", "notes": [12, 14, 13], "filiere": "Math"},
    {"nom": "Charlie", "notes": [18, 19, 17], "filiere": "Info"},
    {"nom": "Diana", "notes": [16, 15, 18], "filiere": "Physique"}
]

# Toutes les notes des étudiants en informatique
notes_info = [
    note
    for etudiant in etudiants_notes
    if etudiant["filiere"] == "Info"
    for note in etudiant["notes"]
]
print(f"📊 Notes Info : {notes_info}")

# Moyennes avec mention
moyennes_mentions = [
    {
        "nom": etudiant["nom"],
        "moyenne": sum(etudiant["notes"]) / len(etudiant["notes"]),
        "mention": "TB" if sum(etudiant["notes"]) / len(etudiant["notes"]) >= 16
                   else "B" if sum(etudiant["notes"]) / len(etudiant["notes"]) >= 14
                   else "AB" if sum(etudiant["notes"]) / len(etudiant["notes"]) >= 12
                   else "P"
    }
    for etudiant in etudiants_notes
]

print(f"🏆 Moyennes et mentions :")
for info in moyennes_mentions:
    print(f"   {info['nom']:<8} : {info['moyenne']:.1f} ({info['mention']})")

print("\n" + "=" * 50)
print("6. PERFORMANCES ET OPTIMISATIONS")
print("=" * 50)

print("\n⚡ COMPARAISON DE PERFORMANCES")
print("-" * 32)


def mesurer_temps(operation, description, iterations=1000):
    """Mesure le temps d'exécution"""
    start = time.time()
    for _ in range(iterations):
        operation()
    duree = (time.time() - start) * 1000 / iterations
    print(f"   {description:<35} : {duree:.3f}ms")

# Comparaison : boucle vs comprehension


def boucle_traditionnelle():
    result = []
    for x in range(100):
        if x % 2 == 0:
            result.append(x**2)
    return result


def comprehension():
    return [x**2 for x in range(100) if x % 2 == 0]


def generateur():
    return list(x**2 for x in range(100) if x % 2 == 0)


print("🏃 Test de performance (carrés pairs 0-99) :")
mesurer_temps(boucle_traditionnelle, "Boucle traditionnelle")
mesurer_temps(comprehension, "List comprehension")
mesurer_temps(generateur, "Generator expression")

print("\n💾 OPTIMISATION MÉMOIRE")
print("-" * 23)


def analyser_memoire():
    """Analyse l'utilisation mémoire"""
    import tracemalloc

    tracemalloc.start()

    # List comprehension
    snapshot1 = tracemalloc.take_snapshot()
    grandes_donnees_liste = [x**2 for x in range(10000)]
    snapshot2 = tracemalloc.take_snapshot()

    # Generator expression
    snapshot3 = tracemalloc.take_snapshot()
    grandes_donnees_gen = (x**2 for x in range(10000))
    snapshot4 = tracemalloc.take_snapshot()

    # Calcul des différences
    diff_liste = snapshot2.compare_to(snapshot1, 'lineno')[0]
    diff_gen = snapshot4.compare_to(snapshot3, 'lineno')[
        0] if snapshot4.compare_to(snapshot3, 'lineno') else None

    print(f"💾 Mémoire liste : {diff_liste.size / 1024:.1f} KB")
    if diff_gen:
        print(f"💾 Mémoire générateur : {diff_gen.size / 1024:.1f} KB")

    tracemalloc.stop()

# Décommentez pour tester l'analyse mémoire
# analyser_memoire()


print("\n🎯 BONNES PRATIQUES")
print("-" * 19)

print("""
💡 Guide d'optimisation des compréhensions :

✅ QUAND UTILISER :
• Transformations simples
• Filtrage de données
• Création de structures
• Code plus lisible qu'une boucle

❌ QUAND ÉVITER :
• Logique trop complexe
• Effets de bord nécessaires
• Compréhensions > 2-3 lignes
• Imbrications > 2 niveaux

🚀 OPTIMISATIONS :
• Generator expressions pour gros datasets
• Éviter les calculs répétés
• Utiliser des fonctions externes si complexe
• Préférer filter/map pour certains cas

📏 LISIBILITÉ :
• Maximum 80 caractères par ligne
• Découper les compréhensions complexes
• Noms de variables explicites
• Commenter si logique non évidente
""")

print("\n" + "=" * 50)
print("7. APPLICATIONS PRATIQUES AVANCÉES")
print("=" * 50)

print("\n📊 TRAITEMENT DE DONNÉES CSV")
print("-" * 28)

# Simulation de données CSV
donnees_csv = [
    "nom,age,salaire,departement",
    "Alice,25,65000,IT",
    "Bob,30,55000,RH",
    "Charlie,28,70000,IT",
    "Diana,26,60000,Finance",
    "Eve,24,52000,RH"
]

# Parsing avec compréhensions


def parser_csv(lignes):
    headers = lignes[0].split(',')
    return [
        {headers[i]: (int(val) if val.isdigit() else val)
         for i, val in enumerate(ligne.split(','))}
        for ligne in lignes[1:]
    ]


employes = parser_csv(donnees_csv)
print("👥 Employés parsés :")
for emp in employes:
    print(f"   {emp}")

# Analyses avec compréhensions
salaire_moyen_it = sum(emp['salaire'] for emp in employes if emp['departement'] == 'IT') / \
    len([emp for emp in employes if emp['departement'] == 'IT'])

employes_jeunes = [emp['nom'] for emp in employes if emp['age'] < 27]

stats_departements = {
    dept: {
        'count': len([e for e in employes if e['departement'] == dept]),
        'salaire_moyen': sum(e['salaire'] for e in employes if e['departement'] == dept) /
        len([e for e in employes if e['departement'] == dept])
    }
    for dept in {emp['departement'] for emp in employes}
}

print(f"\n📊 Analyses :")
print(f"   Salaire moyen IT : {salaire_moyen_it:.0f}€")
print(f"   Employés jeunes (<27) : {employes_jeunes}")
print(f"   Stats par département : {stats_departements}")

print("\n🎯 ANALYSE DE LOGS")
print("-" * 17)

# Simulation de logs
logs = [
    "2024-01-15 10:30:15 INFO User alice logged in",
    "2024-01-15 10:31:20 ERROR Database connection failed",
    "2024-01-15 10:32:10 INFO User bob logged in",
    "2024-01-15 10:33:45 WARNING High memory usage detected",
    "2024-01-15 10:34:12 ERROR Authentication failed for user charlie",
    "2024-01-15 10:35:30 INFO File uploaded by user alice",
    "2024-01-15 10:36:45 ERROR Disk space low",
    "2024-01-15 10:37:20 INFO User diana logged in"
]

# Parsing et analyse des logs


def parser_log(ligne):
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.*)'
    match = re.match(pattern, ligne)
    if match:
        return {
            'timestamp': match.group(1),
            'level': match.group(2),
            'message': match.group(3)
        }
    return None


logs_structures = [parser_log(log) for log in logs if parser_log(log)]

# Analyses avec compréhensions
erreurs = [log for log in logs_structures if log['level'] == 'ERROR']
utilisateurs_connectes = {
    re.search(r'user (\w+)', log['message']).group(1)
    for log in logs_structures
    if 'logged in' in log['message'] and re.search(r'user (\w+)', log['message'])
}

# Comptage par niveau
compteur_niveaux = Counter(log['level'] for log in logs_structures)

print(f"📄 Analyse des logs :")
print(f"   Erreurs : {len(erreurs)}")
print(f"   Utilisateurs connectés : {sorted(utilisateurs_connectes)}")
print(f"   Par niveau : {dict(compteur_niveaux)}")

print("\n🌐 GÉNÉRATION DE DONNÉES DE TEST")
print("-" * 33)


# Générateur de données de test avec compréhensions

def generer_utilisateurs(nb_users=10):
    prenoms = ['Alice', 'Bob', 'Charlie',
               'Diana', 'Eve', 'Frank', 'Grace', 'Henry']
    domaines = ['gmail.com', 'yahoo.fr', 'hotmail.com', 'company.com']
    departements = ['IT', 'RH', 'Finance', 'Marketing', 'Ventes']

    return [
        {
            'id': i + 1,
            'nom': random.choice(prenoms),
            'email': f"{random.choice(prenoms).lower()}{random.randint(1, 999)}@{random.choice(domaines)}",
            'age': random.randint(22, 60),
            'departement': random.choice(departements),
            'salaire': random.randint(35000, 100000),
            'competences': random.sample(['Python', 'Java', 'SQL', 'React', 'Docker', 'AWS'],
                                         random.randint(2, 4))
        }
        for i in range(nb_users)
    ]


utilisateurs_test = generer_utilisateurs(5)
print("👥 Utilisateurs de test générés :")
for user in utilisateurs_test:
    print(
        f"   {user['nom']} : {user['departement']}, {user['age']} ans, {len(user['competences'])} compétences")

# Analyses rapides
competences_populaires = Counter(
    comp
    for user in utilisateurs_test
    for comp in user['competences']
)

print(
    f"🏆 Compétences populaires : {dict(competences_populaires.most_common(3))}")

print("\n" + "=" * 50)
print("8. PATTERNS AVANCÉS ET ASTUCES")
print("=" * 50)

print("\n🎭 COMPRÉHENSIONS CONDITIONNELLES COMPLEXES")
print("-" * 43)

# Pattern : transformation différente selon condition


def classifier_nombres(nombres):
    return [
        f"{n} est {'petit' if n < 10 else 'moyen' if n < 100 else 'grand'}"
        for n in nombres
    ]


test_nombres = [5, 15, 150, 3, 99, 1000]
classifications = classifier_nombres(test_nombres)
print("🔢 Classifications :")
for classif in classifications:
    print(f"   {classif}")

print("\n🔧 COMPRÉHENSIONS AVEC FONCTIONS")
print("-" * 31)

# Pattern : utiliser des fonctions dans les compréhensions


def est_premier(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))


def factorielle(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Nombres premiers et leurs factorielles
premiers_factorielles = {
    n: factorielle(n)
    for n in range(2, 10)
    if est_premier(n)
}
print(f"🔢 Premiers et factorielles : {premiers_factorielles}")

print("\n🎯 PATTERN : VALIDATION ET NETTOYAGE")
print("-" * 35)

# Données sales à nettoyer
donnees_sales = [
    "  alice@email.com  ",
    "BOB@TEST.COM",
    "invalid-email",
    "  charlie@demo.com",
    "",
    "diana@site.com  ",
    "eve@",
    "frank@mail.co.uk"
]


def est_email_valide(email):
    return '@' in email and '.' in email.split('@')[-1]


# Nettoyage et validation en une compréhension
emails_propres = [
    email.strip().lower()
    for email in donnees_sales
    if email.strip() and est_email_valide(email.strip())
]

print(f"📧 Emails sales : {donnees_sales}")
print(f"📧 Emails propres : {emails_propres}")

print("\n🔄 PATTERN : TRANSFORMATION PIPELINE")
print("-" * 35)

# Pipeline de transformations avec compréhensions


def pipeline_transformation(donnees):
    # Étape 1 : Nettoyer
    etape1 = [d.strip().lower() for d in donnees if d.strip()]

    # Étape 2 : Filtrer
    etape2 = [d for d in etape1 if len(d) > 3]

    # Étape 3 : Transformer
    etape3 = [d.title() for d in etape2]

    # Étape 4 : Enrichir
    etape4 = [{'nom': d, 'longueur': len(d)} for d in etape3]

    return etape4


donnees_test = ["  alice  ", "bo", "CHARLIE", "", "diana", "   eve   "]
resultat_pipeline = pipeline_transformation(donnees_test)

print(f"🔧 Données originales : {donnees_test}")
print(f"🔧 Après pipeline :")
for item in resultat_pipeline:
    print(f"   {item}")

print("\n" + "=" * 50)
print("1-1. RÉSUMÉ FINAL")
print("=" * 50)

print("""
🎯 POINTS CLÉS À RETENIR :

1. 📋 LIST COMPREHENSIONS :
   • [expr for item in iterable if condition]
   • Plus rapide et lisible qu'une boucle
   • Créent une liste complète en mémoire

2. 📚 DICT COMPREHENSIONS :
   • {key: value for item in iterable if condition}
   • Idéal pour transformations et mapping
   • Alternative élégante aux boucles de dict

3. 📦 SET COMPREHENSIONS :
   • {expr for item in iterable if condition}
   • Déduplication automatique
   • Parfait pour unicité et opérations ensemblistes

4. ⚡ GENERATOR EXPRESSIONS :
   • (expr for item in iterable if condition)
   • Évaluation paresseuse (lazy)
   • Économise la mémoire pour gros datasets

5. 🎭 COMPRÉHENSIONS IMBRIQUÉES :
   • [expr for x in iter1 for y in iter2 if condition]
   • Équivalent à des boucles imbriquées
   • Attention à la lisibilité

💡 BONNES PRATIQUES :
✅ Utiliser pour transformations simples
✅ Préférer la lisibilité à la concision
✅ Éviter les compréhensions > 2-3 lignes
✅ Generator expressions pour gros volumes
✅ Noms de variables explicites
✅ Découper les logiques complexes

🚨 PIÈGES À ÉVITER :
❌ Compréhensions trop complexes
❌ Effets de bord dans les expressions
❌ Imbrications trop profondes
❌ Calculs coûteux répétés
❌ Variables de boucle qui fuient

⚡ PERFORMANCES :
• Comprehensions généralement plus rapides
• Generator expressions économisent la mémoire
• Éviter les calculs répétés dans l'expression
• Utiliser des fonctions externes si logique complexe

🎯 APPLICATIONS :
• Transformation de données
• Filtrage et nettoyage
• Analyses rapides
• Génération de structures
• Parsing de fichiers
• Pipelines de traitement

🎉 Félicitations ! Vous maîtrisez les compréhensions !
💡 Prochaine étape : Fonctions et paramètres !
📚 Compréhensions maîtrisées, passez aux fonctions !
""")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE - COMPRÉHENSIONS MAÎTRISÉES !")
print("=" * 70)
