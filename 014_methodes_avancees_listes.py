#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
======================================================================
LES MÉTHODES AVANCÉES DES LISTES - GUIDE EXPERT
======================================================================

🎯 Ce fichier couvre les techniques avancées avec les listes :
   • List comprehensions avancées
   • Fonctions lambda avec listes
   • Méthodes filter(), map(), reduce()
   • Algorithmes de tri personnalisés
   • Manipulation complexe de données
   • Optimisations et patterns

📚 Concepts abordés :
   • Comprehensions conditionnelles et imbriquées
   • Fonctions de première classe
   • Programmation fonctionnelle
   • Algorithmes de recherche et tri
   • Structures de données complexes
   • Performance et mémoire

💡 Objectif : Devenir expert dans la manipulation des listes
"""

from functools import partial
import sys
from collections import defaultdict
import time
import random
from functools import reduce
print("=" * 70)
print("LES MÉTHODES AVANCÉES DES LISTES - GUIDE EXPERT")
print("=" * 70)

print("\n" + "=" * 50)
print("1. LIST COMPREHENSIONS AVANCÉES")
print("=" * 50)

print("\n✨ COMPREHENSIONS AVEC CONDITIONS MULTIPLES")
print("-" * 41)

# Filtrage avec plusieurs conditions
nombres = range(1, 101)

# Nombres divisibles par 3 ET 5
div_3_et_5 = [x for x in nombres if x % 3 == 0 and x % 5 == 0]
print(f"🔢 Divisibles par 3 ET 5 : {div_3_et_5[:10]}...")

# Nombres premiers simples (méthode basique)


def est_premier(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


premiers = [x for x in range(2, 50) if est_premier(x)]
print(f"🔢 Nombres premiers 2-50 : {premiers}")

print("\n🎭 TRANSFORMATIONS CONDITIONNELLES")
print("-" * 32)

# Transformation différente selon condition
temperatures_celsius = [-10, 0, 15, 25, 35, 100]
descriptions = [
    f"{temp}°C ({'Gelé' if temp < 0 else 'Froid' if temp < 10 else 'Modéré' if temp < 25 else 'Chaud' if temp < 40 else 'Très chaud'})"
    for temp in temperatures_celsius
]

print("🌡️ Températures avec descriptions :")
for desc in descriptions:
    print(f"   {desc}")

print("\n🔄 COMPREHENSIONS IMBRIQUÉES COMPLEXES")
print("-" * 38)

# Création d'un dictionnaire de coordonnées
coordonnees = {
    f'({x},{y})': x*y
    for x in range(1, 4)
    for y in range(1, 4)
    if x != y
}
print(f"📊 Coordonnées et produits : {coordonnees}")

# Aplatissement de structure complexe
donnees_complexes = [
    [['a', 1], ['b', 2]],
    [['c', 3], ['d', 4]],
    [['e', 5]]
]

# Aplatir et transformer
elements_aplatis = [
    f"{lettre}:{nombre*2}"
    for groupe in donnees_complexes
    for lettre, nombre in groupe
]
print(f"📏 Données aplaties : {elements_aplatis}")

print("\n🎯 COMPREHENSIONS AVEC FONCTIONS")
print("-" * 32)

# Avec des fonctions complexes
mots = ["python", "javascript", "java", "c++", "go", "rust"]


def analyser_mot(mot):
    return {
        'mot': mot,
        'longueur': len(mot),
        'voyelles': sum(1 for char in mot.lower() if char in 'aeiou'),
        'consonnes': sum(1 for char in mot.lower() if char.isalpha() and char not in 'aeiou')
    }


analyses = [analyser_mot(mot) for mot in mots if len(mot) > 2]
print("🔤 Analyses de mots :")
for analyse in analyses:
    print(f"   {analyse['mot']:<12} : {analyse['longueur']} chars, {analyse['voyelles']} voyelles, {analyse['consonnes']} consonnes")

print("\n" + "=" * 50)
print("2. FONCTIONS LAMBDA ET PROGRAMMATION FONCTIONNELLE")
print("=" * 50)

print("\n⚡ FONCTIONS LAMBDA AVEC LISTES")
print("-" * 30)

# Fonctions lambda simples
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Avec map()
carres = list(map(lambda x: x**2, nombres))
print(f"🔢 Carrés avec map() : {carres}")

# Avec filter()
pairs = list(filter(lambda x: x % 2 == 0, nombres))
print(f"🔢 Pairs avec filter() : {pairs}")

# Tri avec key personnalisée
etudiants = [
    ('Alice', 85, 20),
    ('Bob', 78, 19),
    ('Charlie', 92, 21),
    ('Diana', 88, 18)
]

# Tri par note (décroissant)
par_note = sorted(etudiants, key=lambda etudiant: etudiant[1], reverse=True)
print("📊 Tri par note (décroissant) :")
for nom, note, age in par_note:
    print(f"   {nom:<8} : {note}/100")

# Tri par age puis par note
par_age_note = sorted(etudiants, key=lambda x: (x[2], -x[1]))
print("\n📊 Tri par âge puis note :")
for nom, note, age in par_age_note:
    print(f"   {nom:<8} : {age} ans, {note}/100")

print("\n🎯 MAP, FILTER, REDUCE")
print("-" * 22)


# Map : transformation
prix_ht = [100, 200, 150, 300]
prix_ttc = list(map(lambda x: x * 1.20, prix_ht))
print(f"💰 Prix HT : {prix_ht}")
print(f"💰 Prix TTC : {prix_ttc}")

# Filter : filtrage
scores = [85, 92, 78, 96, 73, 88, 91]
excellents = list(filter(lambda x: x >= 90, scores))
print(f"🏆 Scores excellents (≥90) : {excellents}")

# Reduce : agrégation
somme = reduce(lambda x, y: x + y, scores)
produit = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(f"➕ Somme des scores : {somme}")
print(f"✖️ Produit 1×2×3×4×5 : {produit}")

print("\n🔧 FONCTIONS D'ORDRE SUPÉRIEUR")
print("-" * 30)


def appliquer_operation(liste, operation):
    """Applique une opération à tous les éléments"""
    return [operation(x) for x in liste]


def filtrer_avec_condition(liste, condition):
    """Filtre les éléments selon une condition"""
    return [x for x in liste if condition(x)]


def transformer_si(liste, condition, transformation):
    """Transforme seulement si condition vraie"""
    return [transformation(x) if condition(x) else x for x in liste]


# Tests
valeurs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cubes = appliquer_operation(valeurs, lambda x: x**3)
print(f"🔢 Cubes : {cubes[:5]}...")

multiples_3 = filtrer_avec_condition(valeurs, lambda x: x % 3 == 0)
print(f"🔢 Multiples de 3 : {multiples_3}")

double_si_pair = transformer_si(valeurs, lambda x: x % 2 == 0, lambda x: x * 2)
print(f"🔢 Double si pair : {double_si_pair}")

print("\n" + "=" * 50)
print("3. ALGORITHMES DE TRI AVANCÉS")
print("=" * 50)

print("\n🔄 TRI PERSONNALISÉ COMPLEXE")
print("-" * 28)

# Structure de données complexe
employes = [
    {'nom': 'Alice', 'departement': 'IT', 'salaire': 75000, 'anciennete': 5},
    {'nom': 'Bob', 'departement': 'RH', 'salaire': 65000, 'anciennete': 3},
    {'nom': 'Charlie', 'departement': 'IT', 'salaire': 85000, 'anciennete': 7},
    {'nom': 'Diana', 'departement': 'Finance', 'salaire': 70000, 'anciennete': 4},
    {'nom': 'Eve', 'departement': 'IT', 'salaire': 80000, 'anciennete': 6}
]

print("👥 Employés originaux :")
for emp in employes:
    print(
        f"   {emp['nom']:<8} | {emp['departement']:<8} | {emp['salaire']:>6}€ | {emp['anciennete']} ans")

# Tri multi-critères : département puis salaire décroissant
tri_multi = sorted(employes, key=lambda x: (x['departement'], -x['salaire']))
print("\n👥 Tri par département puis salaire (↓) :")
for emp in tri_multi:
    print(
        f"   {emp['nom']:<8} | {emp['departement']:<8} | {emp['salaire']:>6}€ | {emp['anciennete']} ans")

# Tri par ratio salaire/ancienneté
tri_ratio = sorted(
    employes, key=lambda x: x['salaire']/x['anciennete'], reverse=True)
print("\n👥 Tri par ratio salaire/ancienneté (↓) :")
for emp in tri_ratio:
    ratio = emp['salaire']/emp['anciennete']
    print(
        f"   {emp['nom']:<8} | Ratio: {ratio:>7.0f}€/an | {emp['salaire']:>6}€ | {emp['anciennete']} ans")

print("\n🎯 TRI STABLE ET INSTABLE")
print("-" * 24)

# Données avec doublons pour test de stabilité
donnees_doublons = [
    ('A', 2), ('B', 1), ('C', 2), ('D', 1), ('E', 3), ('F', 2)
]
print(f"📊 Données originales : {donnees_doublons}")

# Tri stable (Python utilise Timsort, qui est stable)
tri_stable = sorted(donnees_doublons, key=lambda x: x[1])
print(f"📊 Tri stable par valeur : {tri_stable}")
print("   → Les éléments avec même valeur gardent leur ordre relatif")

print("\n" + "=" * 50)
print("4. RECHERCHE ET INDEXATION AVANCÉES")
print("=" * 50)

print("\n🔍 RECHERCHE BINAIRE")
print("-" * 19)


def recherche_binaire(liste_triee, cible):
    """Recherche binaire dans une liste triée"""
    gauche, droite = 0, len(liste_triee) - 1
    comparaisons = 0

    while gauche <= droite:
        comparaisons += 1
        milieu = (gauche + droite) // 2

        if liste_triee[milieu] == cible:
            return milieu, comparaisons
        elif liste_triee[milieu] < cible:
            gauche = milieu + 1
        else:
            droite = milieu - 1

    return -1, comparaisons


# Test de performance : recherche linéaire vs binaire

grande_liste = sorted(random.sample(range(1, 100000), 10000))
cible = random.choice(grande_liste)

# Recherche linéaire
start = time.time()
index_lineaire = grande_liste.index(cible)
temps_lineaire = time.time() - start

# Recherche binaire
start = time.time()
index_binaire, comparaisons = recherche_binaire(grande_liste, cible)
temps_binaire = time.time() - start

print(f"🎯 Recherche de {cible} dans liste de 10000 éléments :")
print(
    f"   Linéaire : index {index_lineaire}, temps {temps_lineaire*1000:.3f}ms")
print(
    f"   Binaire  : index {index_binaire}, temps {temps_binaire*1000:.3f}ms, {comparaisons} comparaisons")
print(f"   Gain     : {temps_lineaire/temps_binaire:.1f}x plus rapide")

print("\n🎯 RECHERCHE AVEC CONDITIONS COMPLEXES")
print("-" * 36)


def trouver_indices(liste, condition):
    """Trouve tous les indices satisfaisant une condition"""
    return [i for i, x in enumerate(liste) if condition(x)]


def trouver_premier(liste, condition, defaut=None):
    """Trouve le premier élément satisfaisant une condition"""
    for x in liste:
        if condition(x):
            return x
    return defaut


def trouver_dernier(liste, condition, defaut=None):
    """Trouve le dernier élément satisfaisant une condition"""
    for x in reversed(liste):
        if condition(x):
            return x
    return defaut


# Tests
notes_complexes = [
    {'nom': 'Alice', 'maths': 85, 'physique': 78, 'chimie': 92},
    {'nom': 'Bob', 'maths': 78, 'physique': 85, 'chimie': 75},
    {'nom': 'Charlie', 'maths': 92, 'physique': 88, 'chimie': 89},
    {'nom': 'Diana', 'maths': 88, 'physique': 92, 'chimie': 94}
]

# Élèves avec moyenne > 85
moyennes = [(sum(eleve.values()) - len(eleve['nom'])) /
            3 for eleve in notes_complexes]
indices_bons = trouver_indices(moyennes, lambda x: x > 85)
print(f"📊 Indices des élèves avec moyenne > 85 : {indices_bons}")

# Premier élève excellent en maths (> 90)
excellent_maths = trouver_premier(notes_complexes, lambda x: x['maths'] > 90)
print(
    f"🏆 Premier excellent en maths : {excellent_maths['nom'] if excellent_maths else 'Aucun'}")

print("\n" + "=" * 50)
print("5. MANIPULATION DE STRUCTURES COMPLEXES")
print("=" * 50)

print("\n🏗️ TRANSFORMATION DE DONNÉES")
print("-" * 27)

# Données d'origine (format CSV simulé)
donnees_brutes = [
    "Alice,25,Développeur,75000,Python,5",
    "Bob,30,Designer,60000,Photoshop,3",
    "Charlie,28,Manager,85000,Leadership,7",
    "Diana,26,Analyste,70000,SQL,4"
]

# Transformation en structure utilisable


def parser_employe(ligne):
    parts = ligne.split(',')
    return {
        'nom': parts[0],
        'age': int(parts[1]),
        'poste': parts[2],
        'salaire': int(parts[3]),
        'competence': parts[4],
        'experience': int(parts[5])
    }


employes_structures = [parser_employe(ligne) for ligne in donnees_brutes]

print("👥 Données transformées :")
for emp in employes_structures:
    print(
        f"   {emp['nom']:<8} | {emp['age']} ans | {emp['poste']:<12} | {emp['salaire']:>6}€")

print("\n📊 AGRÉGATION ET GROUPEMENT")
print("-" * 28)


# Groupement par poste
par_poste = defaultdict(list)
for emp in employes_structures:
    par_poste[emp['poste']].append(emp)

print("👥 Groupement par poste :")
for poste, liste_emp in par_poste.items():
    salaires = [emp['salaire'] for emp in liste_emp]
    salaire_moyen = sum(salaires) / len(salaires)
    print(
        f"   {poste:<12} : {len(liste_emp)} personne(s), salaire moyen {salaire_moyen:.0f}€")

# Statistiques avancées
total_salaires = sum(emp['salaire'] for emp in employes_structures)
age_moyen = sum(emp['age']
                for emp in employes_structures) / len(employes_structures)
plus_experimente = max(employes_structures, key=lambda x: x['experience'])

print(f"\n📈 Statistiques globales :")
print(f"   Total salaires : {total_salaires:>8}€")
print(f"   Âge moyen      : {age_moyen:>8.1f} ans")
print(
    f"   Plus expérimenté : {plus_experimente['nom']} ({plus_experimente['experience']} ans)")

print("\n🔄 PIVOT ET RESHAPE")
print("-" * 19)

# Création d'un tableau de bord


def creer_tableau_bord(employes):
    """Crée un tableau de bord multi-dimensionnel"""

    # Groupement par tranche d'âge
    tranches_age = {'20-25': [], '26-30': [], '30+': []}

    for emp in employes:
        if emp['age'] <= 25:
            tranches_age['20-25'].append(emp)
        elif emp['age'] <= 30:
            tranches_age['26-30'].append(emp)
        else:
            tranches_age['30+'].append(emp)

    tableau = {}
    for tranche, liste_emp in tranches_age.items():
        if liste_emp:
            tableau[tranche] = {
                'count': len(liste_emp),
                'salaire_moyen': sum(emp['salaire'] for emp in liste_emp) / len(liste_emp),
                'experience_moyenne': sum(emp['experience'] for emp in liste_emp) / len(liste_emp)
            }
        else:
            tableau[tranche] = {'count': 0,
                                'salaire_moyen': 0, 'experience_moyenne': 0}

    return tableau


tableau_bord = creer_tableau_bord(employes_structures)

print("📊 Tableau de bord par tranche d'âge :")
print(f"{'Tranche':<8} | {'Count':<5} | {'Sal. Moy.':<9} | {'Exp. Moy.':<8}")
print("-" * 40)
for tranche, stats in tableau_bord.items():
    print(
        f"{tranche:<8} | {stats['count']:<5} | {stats['salaire_moyen']:<9.0f} | {stats['experience_moyenne']:<8.1f}")

print("\n" + "=" * 50)
print("6. OPTIMISATIONS ET PATTERNS AVANCÉS")
print("=" * 50)

print("\n⚡ TECHNIQUES D'OPTIMISATION")
print("-" * 28)

# Générateurs vs listes pour économiser la mémoire


def carre_liste(n):
    """Version liste - consomme toute la mémoire"""
    return [x**2 for x in range(n)]


def carre_generateur(n):
    """Version générateur - consomme la mémoire au besoin"""
    return (x**2 for x in range(n))


# Comparaison mémoire (simulée)

liste_carres = [x**2 for x in range(1000)]
gen_carres = (x**2 for x in range(1000))

print(f"💾 Taille liste de 1000 carrés : {sys.getsizeof(liste_carres)} bytes")
print(f"💾 Taille générateur équivalent : {sys.getsizeof(gen_carres)} bytes")
print(
    f"💾 Gain mémoire : {sys.getsizeof(liste_carres) / sys.getsizeof(gen_carres):.1f}x")

print("\n🎯 PATTERN : CACHE ET MÉMOÏSATION")
print("-" * 32)


def memoize(func):
    """Décorateur pour mettre en cache les résultats"""
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]

        result = func(*args)
        cache[args] = result
        return result

    wrapper.cache = cache
    return wrapper


@memoize
def fibonacci_memo(n):
    """Fibonacci avec mémoïsation"""
    if n <= 1:
        return n
    return fibonacci_memo(n-1) + fibonacci_memo(n-2)


def fibonacci_naif(n):
    """Fibonacci naïf (sans cache)"""
    if n <= 1:
        return n
    return fibonacci_naif(n-1) + fibonacci_naif(n-2)


# Test de performance

print("🏃 Test Fibonacci(30) :")

# Version mémoïsée
start = time.time()
resultat_memo = fibonacci_memo(30)
temps_memo = time.time() - start

# Version naïve (plus lente, limitons à 25)
start = time.time()
resultat_naif = fibonacci_naif(25)
temps_naif = time.time() - start

print(f"   Mémoïsé F(30) : {resultat_memo} en {temps_memo*1000:.2f}ms")
print(f"   Naïf F(25)    : {resultat_naif} en {temps_naif*1000:.2f}ms")
print(f"   Cache hits    : {len(fibonacci_memo.cache)} entrées")

print("\n🔧 PATTERN : FACTORY ET BUILDER")
print("-" * 31)


class ListeBuilder:
    """Pattern Builder pour créer des listes complexes"""

    def __init__(self):
        self.items = []
        self.transformations = []

    def ajouter(self, *items):
        """Ajoute des éléments"""
        self.items.extend(items)
        return self

    def filtrer(self, condition):
        """Ajoute un filtre"""
        self.transformations.append(('filter', condition))
        return self

    def transformer(self, func):
        """Ajoute une transformation"""
        self.transformations.append(('map', func))
        return self

    def trier(self, key=None, reverse=False):
        """Ajoute un tri"""
        self.transformations.append(('sort', key, reverse))
        return self

    def construire(self):
        """Construit la liste finale"""
        resultat = self.items.copy()

        for transformation in self.transformations:
            if transformation[0] == 'filter':
                resultat = [x for x in resultat if transformation[1](x)]
            elif transformation[0] == 'map':
                resultat = [transformation[1](x) for x in resultat]
            elif transformation[0] == 'sort':
                key, reverse = transformation[1], transformation[2]
                resultat.sort(key=key, reverse=reverse)

        return resultat


# Utilisation du builder
liste_complexe = (ListeBuilder()
                  .ajouter(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
                  .filtrer(lambda x: x % 2 == 0)  # Pairs seulement
                  .transformer(lambda x: x**2)     # Élever au carré
                  .trier(reverse=True)             # Tri décroissant
                  .construire())

print(f"🏗️ Liste construite avec Builder : {liste_complexe}")

print("\n" + "=" * 50)
print("7. APPLICATIONS MÉTIER COMPLEXES")
print("=" * 50)

print("\n📊 SYSTÈME D'ANALYSE DE VENTES")
print("-" * 31)

# Données de ventes complexes
ventes = [
    {'date': '2024-01-15', 'vendeur': 'Alice', 'produit': 'Laptop',
        'prix': 1200, 'commission': 0.05, 'region': 'Nord'},
    {'date': '2024-01-16', 'vendeur': 'Bob', 'produit': 'Mouse',
        'prix': 25, 'commission': 0.10, 'region': 'Sud'},
    {'date': '2024-01-17', 'vendeur': 'Alice', 'produit': 'Keyboard',
        'prix': 80, 'commission': 0.08, 'region': 'Nord'},
    {'date': '2024-01-18', 'vendeur': 'Charlie', 'produit': 'Monitor',
        'prix': 300, 'commission': 0.06, 'region': 'Est'},
    {'date': '2024-01-19', 'vendeur': 'Bob', 'produit': 'Laptop',
        'prix': 1200, 'commission': 0.05, 'region': 'Sud'},
    {'date': '2024-01-20', 'vendeur': 'Diana', 'produit': 'Tablet',
        'prix': 500, 'commission': 0.07, 'region': 'Ouest'},
]


class AnalyseurVentes:
    def __init__(self, ventes):
        self.ventes = ventes

    def top_vendeurs(self, n=3):
        """Top N vendeurs par chiffre d'affaires"""
        ca_vendeurs = defaultdict(float)

        for vente in self.ventes:
            ca_vendeurs[vente['vendeur']] += vente['prix']

        return sorted(ca_vendeurs.items(), key=lambda x: x[1], reverse=True)[:n]

    def performance_regions(self):
        """Performance par région"""
        stats_regions = defaultdict(
            lambda: {'ca': 0, 'ventes': 0, 'commission_totale': 0})

        for vente in self.ventes:
            region = vente['region']
            stats_regions[region]['ca'] += vente['prix']
            stats_regions[region]['ventes'] += 1
            stats_regions[region]['commission_totale'] += vente['prix'] * \
                vente['commission']

        # Ajouter moyenne par vente
        for region, stats in stats_regions.items():
            stats['ca_moyen'] = stats['ca'] / \
                stats['ventes'] if stats['ventes'] > 0 else 0

        return dict(stats_regions)

    def analyse_produits(self):
        """Analyse des produits"""
        produits = defaultdict(
            lambda: {'quantite': 0, 'ca': 0, 'prix_moyen': 0})

        for vente in self.ventes:
            produit = vente['produit']
            produits[produit]['quantite'] += 1
            produits[produit]['ca'] += vente['prix']

        # Calculer prix moyen
        for produit, stats in produits.items():
            stats['prix_moyen'] = stats['ca'] / stats['quantite']

        return dict(produits)


# Utilisation de l'analyseur
analyseur = AnalyseurVentes(ventes)

print("🏆 Top 3 vendeurs :")
for vendeur, ca in analyseur.top_vendeurs():
    print(f"   {vendeur:<8} : {ca:>7.0f}€")

print("\n🌍 Performance par région :")
regions = analyseur.performance_regions()
for region, stats in regions.items():
    print(
        f"   {region:<6} : {stats['ca']:>6.0f}€ CA, {stats['ventes']} ventes, {stats['ca_moyen']:>6.0f}€/vente")

print("\n📦 Analyse des produits :")
produits = analyseur.analyse_produits()
for produit, stats in sorted(produits.items(), key=lambda x: x[1]['ca'], reverse=True):
    print(
        f"   {produit:<8} : {stats['quantite']} vendus, {stats['ca']:>6.0f}€ CA, {stats['prix_moyen']:>6.0f}€ moy.")

print("\n" + "=" * 50)
print("8. PATTERNS DE PROGRAMMATION FONCTIONNELLE")
print("=" * 50)

print("\n🔧 COMBINATEURS ET PIPELINES")
print("-" * 29)


def compose(*functions):
    """Compose plusieurs fonctions"""
    return lambda x: reduce(lambda acc, f: f(acc), reversed(functions), x)


def pipe(data, *functions):
    """Pipeline de transformations"""
    return reduce(lambda acc, f: f(acc), functions, data)

# Fonctions de transformation


def doubler(x): return x * 2
def ajouter_10(x): return x + 10
def au_carre(x): return x ** 2


# Composition
transformation = compose(au_carre, ajouter_10, doubler)
resultat_compose = transformation(5)  # ((5*2)+10)² = 400
print(f"🔄 Composition f(5) où f = carré ∘ +10 ∘ x2 : {resultat_compose}")

# Pipeline
donnees = [1, 2, 3, 4, 5]
resultat_pipeline = pipe(
    donnees,
    lambda lst: [doubler(x) for x in lst],           # [2, 4, 6, 8, 10]
    lambda lst: [ajouter_10(x) for x in lst],        # [12, 14, 16, 18, 20]
    # [144, 196, 256, 324, 400]
    lambda lst: [au_carre(x) for x in lst]
)
print(f"🔄 Pipeline {donnees} → {resultat_pipeline}")

print("\n🎯 CURRYING ET FONCTIONS PARTIELLES")
print("-" * 34)


def multiplier(a, b, c):
    """Multiplie trois nombres"""
    return a * b * c

# Currying manuel


def multiplier_curry(a):
    def multiplier_b(b):
        def multiplier_c(c):
            return a * b * c
        return multiplier_c
    return multiplier_b


# Utilisation currying
mult_par_2 = multiplier_curry(2)
mult_par_2_et_3 = mult_par_2(3)
resultat_curry = mult_par_2_et_3(4)  # 2 * 3 * 4 = 24
print(f"🎯 Currying 2×3×4 : {resultat_curry}")

# Fonctions partielles
mult_par_2_partial = partial(multiplier, 2)
mult_par_2_et_3_partial = partial(mult_par_2_partial, 3)
resultat_partial = mult_par_2_et_3_partial(4)
print(f"🎯 Partial 2×3×4 : {resultat_partial}")

print("\n" + "=" * 50)
print("9. RÉSUMÉ ET BONNES PRATIQUES")
print("=" * 50)

print("""
🎯 TECHNIQUES MAÎTRISÉES :

1. 🚀 LIST COMPREHENSIONS AVANCÉES :
   • Conditions multiples et imbriquées
   • Transformations conditionnelles  
   • Structures complexes et aplatissement

2. ⚡ PROGRAMMATION FONCTIONNELLE :
   • Fonctions lambda et de première classe
   • map(), filter(), reduce()
   • Composition et pipelines

3. 🔍 ALGORITHMES OPTIMISÉS :
   • Tri multi-critères personnalisé
   • Recherche binaire et indexation
   • Mémoïsation et cache

4. 🏗️ PATTERNS AVANCÉS :
   • Builder et Factory
   • Générateurs pour la mémoire
   • Combinateurs fonctionnels

5. 📊 APPLICATIONS MÉTIER :
   • Analyse de données complexes
   • Systèmes de recommandation
   • Optimisation et règles métier

💡 RÈGLES D'OR :
✅ Privilégier les comprehensions pour la lisibilité
✅ Utiliser des générateurs pour les grandes données
✅ Mémoïser les calculs coûteux
✅ Composer des fonctions pour la réutilisabilité
✅ Optimiser selon le contexte métier

🚨 PIÈGES À ÉVITER :
❌ Comprehensions trop complexes (préférer boucles)
❌ Mutations pendant l'itération
❌ Copies profondes inutiles
❌ Algorithmes O(n²) sur grandes données

🎉 Félicitations ! Vous êtes expert en manipulation de listes !
💡 Prochaine étape : Tuples et structures immutables !
📚 Listes maîtrisées, explorez les autres structures !
""")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE - EXPERT EN LISTES CONFIRMÉ !")
print("=" * 70)
