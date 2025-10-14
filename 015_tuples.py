#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
======================================================================
LES TUPLES EN PYTHON - GUIDE COMPLET
======================================================================

🎯 Ce fichier couvre les tuples en détail :
   • Création et caractéristiques
   • Immutabilité et avantages
   • Accès et manipulation
   • Tuples nommés (namedtuple)
   • Unpacking et packing
   • Comparaisons avec les listes

📚 Concepts abordés :
   • tuple() et ()
   • Immutabilité vs mutabilité
   • Déballage multiple
   • collections.namedtuple
   • Hachage et dictionnaires
   • Optimisations mémoire

💡 Objectif : Maîtriser les structures de données immutables
"""

import time
import sys
from collections import namedtuple

print("=" * 70)
print("LES TUPLES EN PYTHON - GUIDE COMPLET")
print("=" * 70)

print("\n" + "=" * 50)
print("1. CRÉATION ET CARACTÉRISTIQUES")
print("=" * 50)

print("\n📝 DIFFÉRENTES FAÇONS DE CRÉER UN TUPLE")
print("-" * 38)

# Création d'un tuple vide
tuple_vide1 = ()
tuple_vide2 = tuple()

print(f"📋 Tuple vide avec () : {tuple_vide1}")
print(f"📋 Tuple vide avec tuple() : {tuple_vide2}")
print(f"📋 Type : {type(tuple_vide1)}")

# Création avec des éléments
couleurs = ("rouge", "vert", "bleu")
nombres = (1, 2, 3, 4, 5)
mixte = ("texte", 42, 3.14, True)

print(f"🎨 Tuple de couleurs : {couleurs}")
print(f"🔢 Tuple de nombres : {nombres}")
print(f"🎭 Tuple mixte : {mixte}")

print("\n⚠️ ATTENTION AU TUPLE À UN ÉLÉMENT")
print("-" * 35)

# Piège classique : parenthèses ≠ tuple
pas_un_tuple = ("seul")
vrai_tuple = ("seul",)  # Virgule obligatoire !
aussi_tuple = "seul",   # Parenthèses optionnelles

print(f"❌ Pas un tuple : {pas_un_tuple} (type: {type(pas_un_tuple)})")
print(f"✅ Vrai tuple : {vrai_tuple} (type: {type(vrai_tuple)})")
print(f"✅ Aussi un tuple : {aussi_tuple} (type: {type(aussi_tuple)})")

print("\n🏗️ CRÉATION À PARTIR D'AUTRES STRUCTURES")
print("-" * 40)

# Conversion liste → tuple
ma_liste = [1, 2, 3, 4, 5]
tuple_depuis_liste = tuple(ma_liste)
print(f"📋 Liste : {ma_liste}")
print(f"📋 Tuple depuis liste : {tuple_depuis_liste}")

# Conversion string → tuple
phrase = "Python"
tuple_lettres = tuple(phrase)
print(f"🔤 String : '{phrase}'")
print(f"🔤 Tuple de lettres : {tuple_lettres}")

# Conversion range → tuple
tuple_range = tuple(range(5, 10))
print(f"📊 Tuple depuis range(5,10) : {tuple_range}")

print("\n" + "=" * 50)
print("2. IMMUTABILITÉ ET CONSÉQUENCES")
print("=" * 50)

print("\n🔒 CARACTÈRE IMMUTABLE")
print("-" * 23)

coordonnees = (10, 20)
print(f"📍 Coordonnées initiales : {coordonnees}")

# Tentative de modification (ERROR)
print("❌ Tentative de modification :")
print("   coordonnees[0] = 15  # → TypeError!")

try:
    coordonnees[0] = 15
except TypeError as e:
    print(f"   Erreur : {e}")

print("\n✅ MODIFICATION PAR REMPLACEMENT")
print("-" * 33)

# On peut créer un nouveau tuple
nouvelles_coordonnees = (15, coordonnees[1])
print(f"📍 Nouvelles coordonnées : {nouvelles_coordonnees}")

# Ou utiliser l'opérateur +
coordonnees_decalees = (coordonnees[0] + 5, coordonnees[1] + 5)
print(f"📍 Coordonnées décalées : {coordonnees_decalees}")

print("\n⚠️ IMMUTABILITÉ VS CONTENU MUTABLE")
print("-" * 35)

# Tuple contenant des objets mutables
tuple_avec_liste = ([1, 2, 3], "texte", 42)
print(f"📋 Tuple avec liste : {tuple_avec_liste}")

# Le tuple est immutable, mais pas son contenu !
tuple_avec_liste[0].append(4)  # Modifie la liste à l'intérieur
print(f"📋 Après modification de la liste : {tuple_avec_liste}")

# L'ID du tuple reste le même
print(f"🆔 ID du tuple : {id(tuple_avec_liste)}")

print("\n🔑 CONSÉQUENCE : HACHAGE")
print("-" * 25)

# Les tuples peuvent être clés de dictionnaire
dictionnaire_coords = {
    (0, 0): "origine",
    (1, 0): "axe_x",
    (0, 1): "axe_y",
    (1, 1): "diagonal"
}

print("🗂️ Dictionnaire avec tuples comme clés :")
for coord, description in dictionnaire_coords.items():
    print(f"   {coord} → {description}")

# Les listes ne peuvent pas être clés
print("\n❌ Les listes ne peuvent pas être clés :")
try:
    dict_impossible = {[1, 2]: "valeur"}  # TypeError
except TypeError as e:
    print(f"   Erreur : {e}")

print("\n" + "=" * 50)
print("3. ACCÈS ET MANIPULATION")
print("=" * 50)

print("\n🎯 ACCÈS AUX ÉLÉMENTS")
print("-" * 21)

jours_semaine = ("lundi", "mardi", "mercredi", "jeudi",
                 "vendredi", "samedi", "dimanche")
print(f"📅 Jours de la semaine : {jours_semaine}")

print("📍 Accès par index :")
print(f"   Premier jour : {jours_semaine[0]}")
print(f"   Dernier jour : {jours_semaine[-1]}")
print(f"   Milieu de semaine : {jours_semaine[3]}")

print("\n🔪 SLICING SUR TUPLES")
print("-" * 20)

print("✂️ Exemples de slicing :")
print(f"   Jours ouvrés : {jours_semaine[:5]}")
print(f"   Weekend : {jours_semaine[5:]}")
print(f"   Un jour sur deux : {jours_semaine[::2]}")
print(f"   Semaine inversée : {jours_semaine[::-1]}")

print("\n🔍 RECHERCHE ET COMPTAGE")
print("-" * 26)

notes_musique = ("do", "ré", "mi", "fa", "sol", "la", "si", "do")
print(f"🎵 Notes : {notes_musique}")

# Recherche d'index
index_mi = notes_musique.index("mi")
print(f"🎯 Index de 'mi' : {index_mi}")

# Recherche avec début et fin
index_do_2 = notes_musique.index("do", 1)  # Chercher après le premier
print(f"🎯 Index du second 'do' : {index_do_2}")

# Comptage d'occurrences
count_do = notes_musique.count("do")
print(f"🔢 Nombre de 'do' : {count_do}")

# Vérification de présence
print(f"❓ 'fa#' dans les notes ? {'fa#' in notes_musique}")
print(f"❓ 'sol' dans les notes ? {'sol' in notes_musique}")

print("\n" + "=" * 50)
print("4. UNPACKING ET PACKING")
print("=" * 50)

print("\n📦 PACKING (CRÉATION DE TUPLES)")
print("-" * 31)

# Packing implicite
a, b, c = 1, 2, 3  # Crée un tuple implicitement
point = 10, 20, 30  # Parenthèses optionnelles
print(f"📦 Variables empaquetées : a={a}, b={b}, c={c}")
print(f"📦 Point : {point}")

print("\n📂 UNPACKING (DÉBALLAGE)")
print("-" * 26)

# Déballage simple
coordonnees_3d = (100, 200, 300)
x, y, z = coordonnees_3d
print(f"📍 Coordonnées 3D : {coordonnees_3d}")
print(f"📍 Déballées : x={x}, y={y}, z={z}")

# Déballage avec étoile (Python 3+)
nombres_varies = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
premier, second, *milieu, avant_dernier, dernier = nombres_varies

print(f"🔢 Nombres : {nombres_varies}")
print(f"🔢 Premier : {premier}")
print(f"🔢 Second : {second}")
print(f"🔢 Milieu : {milieu}")
print(f"🔢 Avant-dernier : {avant_dernier}")
print(f"🔢 Dernier : {dernier}")

print("\n🔄 ÉCHANGE DE VARIABLES")
print("-" * 26)

# Échange pythonique (sans variable temporaire)
var1, var2 = "Alice", "Bob"
print(f"🔄 Avant échange : var1={var1}, var2={var2}")

var1, var2 = var2, var1  # Magie des tuples !
print(f"🔄 Après échange : var1={var1}, var2={var2}")

print("\n🎯 RETOUR MULTIPLES DE FONCTIONS")
print("-" * 33)


def analyser_nombre(n):
    """Retourne plusieurs informations sur un nombre"""
    return n, n**2, n**3, n % 2 == 0


# Utilisation
nombre = 5
valeur, carre, cube, est_pair = analyser_nombre(nombre)
print(f"🔢 Analyse de {nombre} :")
print(f"   Carré : {carre}")
print(f"   Cube : {cube}")
print(f"   Est pair : {est_pair}")

# On peut aussi garder le tuple
resultat_complet = analyser_nombre(7)
print(f"🔢 Résultat complet pour 7 : {resultat_complet}")

print("\n" + "=" * 50)
print("5. TUPLES NOMMÉS (namedtuple)")
print("=" * 50)

print("\n🏷️ CRÉATION DE NAMEDTUPLE")
print("-" * 26)


# Définir un type de tuple nommé
Point = namedtuple('Point', ['x', 'y'])
Personne = namedtuple('Personne', ['nom', 'age', 'ville'])

# Création d'instances
point1 = Point(10, 20)
point2 = Point(x=30, y=40)  # Avec noms des paramètres

print(f"📍 Point 1 : {point1}")
print(f"📍 Point 2 : {point2}")

# Création de personnes
alice = Personne("Alice", 25, "Paris")
bob = Personne(nom="Bob", age=30, ville="Lyon")

print(f"👤 Alice : {alice}")
print(f"👤 Bob : {bob}")

print("\n✨ AVANTAGES DES NAMEDTUPLES")
print("-" * 30)

# Accès par nom (plus lisible)
print(f"📍 Coordonnée X du point1 : {point1.x}")
print(f"📍 Coordonnée Y du point1 : {point1.y}")

print(f"👤 Nom d'Alice : {alice.nom}")
print(f"👤 Âge d'Alice : {alice.age}")

# Toujours accessible par index (compatibilité tuple)
print(f"📍 Point1[0] : {point1[0]}")
print(f"👤 Alice[1] : {alice[1]}")

# Déballage fonctionne toujours
nom, age, ville = alice
print(f"👤 Déballage Alice : {nom}, {age} ans, {ville}")

print("\n🔧 MÉTHODES UTILES DES NAMEDTUPLES")
print("-" * 34)

# _asdict() : conversion en dictionnaire
alice_dict = alice._asdict()
print(f"📚 Alice comme dict : {alice_dict}")

# _replace() : création d'une nouvelle instance modifiée
alice_plus_agee = alice._replace(age=26)
print(f"👤 Alice originale : {alice}")
print(f"👤 Alice plus âgée : {alice_plus_agee}")

# _fields : liste des champs
print(f"🏷️ Champs de Point : {Point._fields}")
print(f"🏷️ Champs de Personne : {Personne._fields}")

# _make() : création depuis un itérable
coordonnees_liste = [50, 60]
point3 = Point._make(coordonnees_liste)
print(f"📍 Point depuis liste : {point3}")

print("\n🎯 EXEMPLE PRATIQUE : BASE DE DONNÉES")
print("-" * 37)

# Modèle de données pour une bibliothèque
Livre = namedtuple('Livre', ['titre', 'auteur', 'annee', 'isbn', 'pages'])

# Base de données de livres
bibliotheque = [
    Livre("1984", "George Orwell", 1949, "978-0-452-28423-4", 328),
    Livre("Le Petit Prince", "Antoine de Saint-Exupéry",
          1943, "978-2-07-040857-4", 96),
    Livre("Python Tricks", "Dan Bader", 2017, "978-1-77539-608-9", 301),
    Livre("Clean Code", "Robert Martin", 2008, "978-0-13-235088-4", 464)
]

print("📚 Bibliothèque :")
for livre in bibliotheque:
    print(f"   📖 {livre.titre:<20} | {livre.auteur:<25} | {livre.annee}")

# Recherche par critère
livres_recents = [livre for livre in bibliotheque if livre.annee > 2000]
print(f"\n📚 Livres récents (> 2000) : {len(livres_recents)}")
for livre in livres_recents:
    print(f"   📖 {livre.titre} ({livre.annee})")

# Tri par nombre de pages
par_pages = sorted(bibliotheque, key=lambda livre: livre.pages)
print(f"\n📚 Du plus court au plus long :")
for livre in par_pages:
    print(f"   📖 {livre.titre:<20} : {livre.pages:>3} pages")

print("\n" + "=" * 50)
print("6. COMPARAISONS ET OPÉRATIONS")
print("=" * 50)

print("\n⚖️ COMPARAISON DE TUPLES")
print("-" * 24)

# Comparaison lexicographique
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)
tuple3 = (1, 3, 2)
tuple4 = (1, 2)

print(f"📊 Tuples à comparer :")
print(f"   tuple1 : {tuple1}")
print(f"   tuple2 : {tuple2}")
print(f"   tuple3 : {tuple3}")
print(f"   tuple4 : {tuple4}")

print(f"\n🔍 Comparaisons :")
print(f"   tuple1 < tuple2 : {tuple1 < tuple2}")  # True (3 < 4)
print(f"   tuple1 < tuple3 : {tuple1 < tuple3}")  # True (2 < 3 au 2e élément)
print(f"   tuple1 > tuple4 : {tuple1 > tuple4}")  # True (plus long à égalité)

# Tri de tuples
liste_tuples = [(3, 1), (1, 2), (2, 1), (1, 1)]
liste_triee = sorted(liste_tuples)
print(f"\n📊 Liste de tuples : {liste_tuples}")
print(f"📊 Liste triée : {liste_triee}")

print("\n➕ OPÉRATIONS SUR TUPLES")
print("-" * 24)

# Concaténation
tuple_a = (1, 2, 3)
tuple_b = (4, 5, 6)
tuple_concat = tuple_a + tuple_b
print(f"➕ {tuple_a} + {tuple_b} = {tuple_concat}")

# Répétition
tuple_repete = (0, 1) * 3
print(f"🔁 (0, 1) * 3 = {tuple_repete}")

# Longueur
print(f"📏 Longueur de {tuple_concat} : {len(tuple_concat)}")

# Min, max, sum (si applicable)
nombres_tuple = (10, 5, 8, 12, 3, 15)
print(f"🔢 Tuple de nombres : {nombres_tuple}")
print(f"📊 Min : {min(nombres_tuple)}")
print(f"📊 Max : {max(nombres_tuple)}")
print(f"📊 Somme : {sum(nombres_tuple)}")

print("\n" + "=" * 50)
print("7. TUPLES VS LISTES : COMPARAISON")
print("=" * 50)

print("\n📊 PERFORMANCES : MÉMOIRE ET VITESSE")
print("-" * 35)


# Comparaison mémoire
liste_1000 = list(range(1000))
tuple_1000 = tuple(range(1000))

taille_liste = sys.getsizeof(liste_1000)
taille_tuple = sys.getsizeof(tuple_1000)

print(f"💾 Mémoire pour 1000 éléments :")
print(f"   Liste : {taille_liste} bytes")
print(f"   Tuple : {taille_tuple} bytes")
print(
    f"   Économie : {(taille_liste - taille_tuple)} bytes ({(taille_liste - taille_tuple)/taille_liste*100:.1f}%)")

# Comparaison vitesse de création


def mesurer_creation(type_structure, taille=10000):
    """Mesure le temps de création"""
    start = time.time()
    if type_structure == 'liste':
        data = [i for i in range(taille)]
    else:  # tuple
        data = tuple(i for i in range(taille))
    return time.time() - start


temps_liste = mesurer_creation('liste')
temps_tuple = mesurer_creation('tuple')

print(f"\n⏱️ Temps de création (10000 éléments) :")
print(f"   Liste : {temps_liste*1000:.3f}ms")
print(f"   Tuple : {temps_tuple*1000:.3f}ms")
print(f"   Différence : {abs(temps_tuple - temps_liste)*1000:.3f}ms")

print("\n🎯 QUAND UTILISER QUOI ?")
print("-" * 25)

scenarios = [
    ("📍 Coordonnées géographiques", "Tuple", "Données immutables, clé de dict"),
    ("📚 Collection de livres", "Liste", "Ajout/suppression fréquents"),
    ("🎨 Palette de couleurs fixes", "Tuple", "Configuration constante"),
    ("📝 Notes d'un étudiant", "Liste", "Modifications possibles"),
    ("🏷️ Métadonnées de fichier", "NamedTuple", "Structure + noms de champs"),
    ("🛒 Panier d'achat", "Liste", "Contenu variable"),
    ("📊 Point 3D en géométrie", "Tuple", "Structure mathématique fixe"),
    ("🎵 Playlist musicale", "Liste", "Ordre modifiable")
]

print("🤔 Guide de choix :")
for scenario, recommandation, raison in scenarios:
    print(f"   {scenario:<25} → {recommandation:<10} ({raison})")

print("\n" + "=" * 50)
print("8. APPLICATIONS PRATIQUES")
print("=" * 50)

print("\n📊 SYSTÈME DE COORDONNÉES")
print("-" * 27)


class GestionnaireCoordonnees:
    def __init__(self):
        self.points = {}  # Dictionnaire avec tuples comme clés

    def ajouter_point(self, nom, x, y, z=0):
        """Ajoute un point nommé"""
        coordonnees = (x, y, z) if z != 0 else (x, y)
        self.points[coordonnees] = nom
        return coordonnees

    def distance_origine(self, coordonnees):
        """Calcule la distance à l'origine"""
        if len(coordonnees) == 2:
            x, y = coordonnees
            return (x**2 + y**2)**0.5
        else:
            x, y, z = coordonnees
            return (x**2 + y**2 + z**2)**0.5

    def points_dans_rayon(self, rayon):
        """Trouve les points dans un rayon donné"""
        resultats = []
        for coord, nom in self.points.items():
            if self.distance_origine(coord) <= rayon:
                distance = self.distance_origine(coord)
                resultats.append((nom, coord, distance))

        return sorted(resultats, key=lambda x: x[2])  # Tri par distance


# Test du gestionnaire
gestionnaire = GestionnaireCoordonnees()

# Ajout de points
gestionnaire.ajouter_point("Origine", 0, 0)
gestionnaire.ajouter_point("Nord", 0, 10)
gestionnaire.ajouter_point("Est", 10, 0)
gestionnaire.ajouter_point("Centre", 5, 5)
gestionnaire.ajouter_point("Loin", 20, 20)

print("📍 Points enregistrés :")
for coord, nom in gestionnaire.points.items():
    distance = gestionnaire.distance_origine(coord)
    print(f"   {nom:<8} : {coord} (distance: {distance:.2f})")

# Recherche dans un rayon
points_proches = gestionnaire.points_dans_rayon(12)
print(f"\n📍 Points dans un rayon de 12 :")
for nom, coord, distance in points_proches:
    print(f"   {nom:<8} : {coord} (distance: {distance:.2f})")

print("\n🎯 BASE DE DONNÉES AVEC NAMEDTUPLES")
print("-" * 35)

# Modèle pour un système de gestion d'employés
Employe = namedtuple(
    'Employe', ['id', 'nom', 'poste', 'departement', 'salaire', 'date_embauche'])

# Base de données
employes = [
    Employe(1, "Alice Martin", "Développeur", "IT", 65000, (2020, 3, 15)),
    Employe(2, "Bob Durand", "Designer", "Marketing", 55000, (2019, 7, 22)),
    Employe(3, "Charlie Dubois", "Manager", "IT", 75000, (2018, 1, 8)),
    Employe(4, "Diana Leroy", "Analyste", "Finance", 60000, (2021, 5, 3)),
    Employe(5, "Eve Bernard", "Développeur", "IT", 68000, (2020, 11, 12))
]

print("👥 Base de données employés :")
for emp in employes:
    annee_embauche = emp.date_embauche[0]
    anciennete = 2024 - annee_embauche
    print(f"   {emp.id}. {emp.nom:<15} | {emp.poste:<12} | {emp.departement:<10} | {emp.salaire:>6}€ | {anciennete} ans")

# Analyses avec les tuples


def analyser_employes(employes):
    """Analyse la base de données d'employés"""

    # Groupement par département
    par_dept = {}
    for emp in employes:
        if emp.departement not in par_dept:
            par_dept[emp.departement] = []
        par_dept[emp.departement].append(emp)

    print("\n📊 Analyse par département :")
    for dept, liste_emp in par_dept.items():
        nombre = len(liste_emp)
        salaire_moyen = sum(e.salaire for e in liste_emp) / nombre
        salaire_total = sum(e.salaire for e in liste_emp)

        print(
            f"   {dept:<10} : {nombre} employés, {salaire_moyen:>7.0f}€ moy., {salaire_total:>8}€ total")

    # Top 3 salaires
    top_salaires = sorted(employes, key=lambda e: e.salaire, reverse=True)[:3]
    print(f"\n🏆 Top 3 salaires :")
    for i, emp in enumerate(top_salaires, 1):
        print(f"   {i}. {emp.nom:<15} : {emp.salaire}€ ({emp.poste})")

    # Ancienneté moyenne
    anciennetes = [2024 - emp.date_embauche[0] for emp in employes]
    anciennete_moyenne = sum(anciennetes) / len(anciennetes)
    print(f"\n📅 Ancienneté moyenne : {anciennete_moyenne:.1f} ans")


analyser_employes(employes)

print("\n" + "=" * 50)
print("9. PATTERNS AVANCÉS AVEC TUPLES")
print("=" * 50)

print("\n🎯 PATTERN : CONFIGURATION IMMUTABLE")
print("-" * 34)

# Configuration d'application avec namedtuple
Config = namedtuple('Config', [
    'db_host', 'db_port', 'db_name',
    'cache_ttl', 'max_connections',
    'debug_mode', 'log_level'
])

# Configuration par défaut
config_default = Config(
    db_host='localhost',
    db_port=5432,
    db_name='myapp',
    cache_ttl=3600,
    max_connections=100,
    debug_mode=False,
    log_level='INFO'
)

# Configuration de développement (avec override)
config_dev = config_default._replace(
    debug_mode=True,
    log_level='DEBUG',
    cache_ttl=60
)

# Configuration de production
config_prod = config_default._replace(
    db_host='prod-server.com',
    max_connections=500,
    log_level='WARNING'
)

print("⚙️ Configurations :")
print(
    f"   Défaut : debug={config_default.debug_mode}, log={config_default.log_level}")
print(f"   Dev    : debug={config_dev.debug_mode}, log={config_dev.log_level}")
print(
    f"   Prod   : debug={config_prod.debug_mode}, log={config_prod.log_level}")

print("\n🔄 PATTERN : IMMUTABLE BUILDER")
print("-" * 30)


class TupleBuilder:
    """Builder pour créer des tuples de manière fluide"""

    def __init__(self, tuple_class):
        self.tuple_class = tuple_class
        self.data = {}

    def set(self, field, value):
        """Définit un champ"""
        new_builder = TupleBuilder(self.tuple_class)
        new_builder.data = self.data.copy()
        new_builder.data[field] = value
        return new_builder

    def build(self):
        """Construit le tuple final"""
        # Récupérer les champs dans l'ordre
        fields = self.tuple_class._fields
        values = [self.data.get(field) for field in fields]
        return self.tuple_class(*values)


# Test du builder
Produit = namedtuple('Produit', ['nom', 'prix', 'categorie', 'stock'])

produit = (TupleBuilder(Produit)
           .set('nom', 'MacBook Pro')
           .set('prix', 2499)
           .set('categorie', 'Informatique')
           .set('stock', 5)
           .build())

print(f"🛍️ Produit créé : {produit}")

print("\n🎭 PATTERN : UNION TYPES AVEC TUPLES")
print("-" * 36)

# Simulation d'union types pour retours de fonctions


def diviser_securise(a, b):
    """Retourne soit le résultat, soit une erreur"""
    if b == 0:
        return ('erreur', 'Division par zéro')
    else:
        return ('succès', a / b)


def traiter_resultat(resultat):
    """Traite le résultat d'une opération"""
    statut, valeur = resultat

    if statut == 'succès':
        print(f"✅ Résultat : {valeur}")
        return valeur
    else:
        print(f"❌ Erreur : {valeur}")
        return None


# Tests
print("🧮 Tests de division sécurisée :")
test1 = diviser_securise(10, 2)
traiter_resultat(test1)

test2 = diviser_securise(10, 0)
traiter_resultat(test2)

print("\n" + "=" * 50)
print("10. RÉSUMÉ FINAL")
print("=" * 50)

print("""
🎯 POINTS CLÉS À RETENIR :

1. 📦 CARACTÉRISTIQUES DES TUPLES :
   • Immutables une fois créés
   • Ordonnés et indexables
   • Hashables (clés de dict)
   • Plus économes en mémoire

2. 🏗️ CRÉATION :
   • () ou tuple() pour vides
   • (a,) pour un élément (virgule!)
   • (a, b, c) pour plusieurs
   • tuple(iterable) pour conversion

3. 🎯 UNPACKING/PACKING :
   • a, b = (1, 2) déballage
   • a, *rest, b = tuple déballage étendu
   • return a, b, c retour multiple

4. 🏷️ NAMEDTUPLES :
   • Structure + noms de champs
   • Accès par nom ET index
   • Méthodes _replace(), _asdict()
   • Parfait pour modèles de données

5. ⚖️ COMPARAISONS :
   • Lexicographique par défaut
   • Utilisables dans sorted()
   • Clés de dictionnaire idéales

💡 USAGES RECOMMANDÉS :
✅ Coordonnées et points
✅ Configurations immutables  
✅ Retours multiples de fonctions
✅ Clés de dictionnaire complexes
✅ Modèles de données simples

🚨 ATTENTION :
❌ Contenu mutable dans tuple
❌ Oublier la virgule pour un élément
❌ Confondre immutabilité du tuple et de son contenu

🎉 Félicitations ! Vous maîtrisez les tuples !
💡 Prochaine étape : Dictionnaires et mappings !
📚 Tuples maîtrisés, explorez les structures associatives !
""")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE - TUPLES MAÎTRISÉS !")
print("=" * 70)
