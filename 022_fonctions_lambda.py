#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
======================================================================
FONCTIONS LAMBDA EN PYTHON - GUIDE COMPLET
======================================================================

🎯 Ce fichier couvre les fonctions lambda en détail :
   • Syntaxe et utilisation des lambda
   • Comparaison avec def
   • Lambda avec map, filter, reduce
   • Lambda dans les structures de données
   • Fonctions d'ordre supérieur
   • Bonnes pratiques et limitations

📚 Concepts abordés :
   • Expressions lambda simples et complexes
   • Fonctions anonymes
   • Programming fonctionnel
   • Closures avec lambda
   • Tri personnalisé
   • Event handlers

💡 Objectif : Maîtriser les fonctions lambda et leur usage approprié
"""

import time
from operator import itemgetter, attrgetter
from functools import reduce

print("=" * 70)
print("FONCTIONS LAMBDA EN PYTHON - GUIDE COMPLET")
print("=" * 70)

print("\n" + "=" * 50)
print("1. SYNTAXE FONDAMENTALE")
print("=" * 50)

print("\n🎯 LAMBDA VS DEF")
print("-" * 14)

# Fonction classique avec def


def carre_def(x):
    return x ** 2


# Fonction lambda équivalente
def carre_lambda(x): return x ** 2


print("🔧 Comparaison def vs lambda :")
nombre_test = 5
print(f"   def carre : {carre_def(nombre_test)}")
print(f"   lambda carre : {carre_lambda(nombre_test)}")

# Les deux sont des objets fonction
print(f"   Type def : {type(carre_def)}")
print(f"   Type lambda : {type(carre_lambda)}")
print(f"   Nom def : {carre_def.__name__}")
print(f"   Nom lambda : {carre_lambda.__name__}")

print("\n📝 SYNTAXE LAMBDA")
print("-" * 16)

print("""
🎯 STRUCTURE D'UNE LAMBDA :

lambda paramètres: expression

• lambda : mot-clé
• paramètres : comme une fonction normale
• : séparateur
• expression : une seule expression (pas de statements)

Exemples :
• lambda x: x * 2
• lambda x, y: x + y
• lambda name: f"Bonjour {name}"
• lambda: "Pas de paramètres"
""")

# Exemples de syntaxes lambda
exemples_lambda = {
    "sans_param": lambda: "Hello World!",
    "un_param": lambda x: x * 3,
    "deux_params": lambda x, y: x + y,
    "avec_defaut": lambda x, y=10: x + y,
    "conditionnel": lambda x: "positif" if x > 0 else "négatif ou nul",
    "complexe": lambda x: x**2 + 2*x + 1
}

print("🔧 Tests de syntaxes lambda :")
for nom, func in exemples_lambda.items():
    if nom == "sans_param":
        print(f"   {nom} : {func()}")
    elif nom == "un_param":
        print(f"   {nom} : {func(4)}")
    elif nom in ["deux_params", "avec_defaut"]:
        print(f"   {nom} : {func(5, 3)}")
    elif nom == "conditionnel":
        print(f"   {nom} : {func(-2)} | {func(7)}")
    elif nom == "complexe":
        print(f"   {nom} : {func(3)}")

print("\n⚠️ LIMITATIONS DES LAMBDA")
print("-" * 25)

print("""
❌ CE QU'ON NE PEUT PAS FAIRE AVEC LAMBDA :

• Statements (if, for, while, try, etc.)
• Assignations (x = 5)
• Fonctions multiples lignes
• Annotations de type détaillées
• Docstrings
• Instructions print (sauf dans expressions)

✅ CE QU'ON PEUT FAIRE :

• Expressions conditionnelles (x if condition else y)
• Appels de fonctions
• Opérations arithmétiques
• Compréhensions (dans certains cas)
• Accès aux attributs et méthodes
""")

# Exemples de ce qui ne marche PAS (commenté)
print("❌ Exemples de code invalide avec lambda :")
print("   # lambda x: x = 5  # Assignation interdite")
print("   # lambda x: print(x)  # Statement interdit")
print("   # lambda x: if x > 0: return x  # Statement if interdit")

# Exemples de ce qui marche
print("\n✅ Alternatives valides :")
print("   lambda x: x if x > 0 else 0  # Expression conditionnelle OK")
def assignation_lambda(x): return x if x > 0 else 0


print(f"   Test : {assignation_lambda(-3)} | {assignation_lambda(5)}")

print("\n" + "=" * 50)
print("2. LAMBDA AVEC LES FONCTIONS BUILT-IN")
print("=" * 50)

print("\n🗺️ MAP() AVEC LAMBDA")
print("-" * 18)

# map() applique une fonction à chaque élément
nombres = [1, 2, 3, 4, 5]

# Avec def (verbeux)


def au_cube(x):
    return x ** 3


cubes_def = list(map(au_cube, nombres))

# Avec lambda (concis)
cubes_lambda = list(map(lambda x: x ** 3, nombres))

print("🗺️ map() transforme chaque élément :")
print(f"   Nombres originaux : {nombres}")
print(f"   Cubes (def) : {cubes_def}")
print(f"   Cubes (lambda) : {cubes_lambda}")

# Exemples plus complexes
noms = ["alice", "bob", "charlie"]
noms_formates = list(map(lambda nom: nom.capitalize(), noms))
print(f"   Noms formatés : {noms_formates}")

# Map avec plusieurs listes
liste1 = [1, 2, 3, 4]
liste2 = [10, 20, 30, 40]
additions = list(map(lambda x, y: x + y, liste1, liste2))
print(f"   Additions {liste1} + {liste2} = {additions}")

print("\n🔍 FILTER() AVEC LAMBDA")
print("-" * 21)

# filter() garde les éléments qui respectent une condition
nombres_test = list(range(-5, 6))  # -5 à 5

# Filtrer les nombres positifs
positifs = list(filter(lambda x: x > 0, nombres_test))
print(f"🔍 Filtrage des nombres positifs :")
print(f"   Nombres : {nombres_test}")
print(f"   Positifs : {positifs}")

# Filtrer les nombres pairs
pairs = list(filter(lambda x: x % 2 == 0, nombres_test))
print(f"   Pairs : {pairs}")

# Filtrer les chaînes longues
mots = ["a", "hello", "python", "hi", "programming", "code"]
mots_longs = list(filter(lambda mot: len(mot) > 4, mots))
print(f"   Mots > 4 lettres : {mots_longs}")

# Filtrer avec condition complexe
ages = [12, 25, 17, 30, 45, 16, 60]
adultes_actifs = list(filter(lambda age: 18 <= age < 65, ages))
print(f"   Adultes actifs (18-64) : {adultes_actifs}")

print("\n🔄 REDUCE() AVEC LAMBDA")
print("-" * 21)


# reduce() applique une fonction de façon cumulative
nombres_reduce = [1, 2, 3, 4, 5]

# Somme avec reduce
somme = reduce(lambda x, y: x + y, nombres_reduce)
print(f"🔄 Reduce - opérations cumulatives :")
print(f"   Nombres : {nombres_reduce}")
print(f"   Somme : {somme}")

# Produit avec reduce
produit = reduce(lambda x, y: x * y, nombres_reduce)
print(f"   Produit : {produit}")

# Maximum avec reduce
maximum = reduce(lambda x, y: x if x > y else y, nombres_reduce)
print(f"   Maximum : {maximum}")

# Réduction de chaînes
mots_reduce = ["Python", "est", "génial"]
phrase = reduce(lambda x, y: x + " " + y, mots_reduce)
print(f"   Phrase : '{phrase}'")

# Réduction avec valeur initiale
somme_avec_init = reduce(lambda x, y: x + y, nombres_reduce, 100)
print(f"   Somme + 100 : {somme_avec_init}")

print("\n🔧 COMBINAISONS MAP/FILTER/REDUCE")
print("-" * 32)

# Pipeline de traitement
donnees = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("🔧 Pipeline de traitement :")
print(f"   Données originales : {donnees}")

# Étape 1 : Garder seulement les nombres pairs
pairs_etape = list(filter(lambda x: x % 2 == 0, donnees))
print(f"   1. Filtrage (pairs) : {pairs_etape}")

# Étape 2 : Élever au carré
carres_etape = list(map(lambda x: x ** 2, pairs_etape))
print(f"   2. Transformation (²) : {carres_etape}")

# Étape 3 : Somme totale
somme_finale = reduce(lambda x, y: x + y, carres_etape)
print(f"   3. Réduction (somme) : {somme_finale}")

# En une seule ligne (style fonctionnel pur)
resultat_compact = reduce(
    lambda x, y: x + y,
    map(lambda x: x ** 2,
        filter(lambda x: x % 2 == 0, donnees)
        )
)
print(f"   Résultat compact : {resultat_compact}")

print("\n" + "=" * 50)
print("3. LAMBDA POUR LE TRI")
print("=" * 50)

print("\n📊 TRI AVEC KEY")
print("-" * 15)

# Tri simple avec lambda comme key
etudiants = [
    {"nom": "Alice", "note": 15, "age": 20},
    {"nom": "Bob", "note": 18, "age": 19},
    {"nom": "Charlie", "note": 12, "age": 21},
    {"nom": "Diana", "note": 16, "age": 18}
]

print("📊 Tri d'objets complexes :")
print("   Étudiants originaux :")
for etudiant in etudiants:
    print(f"     {etudiant}")

# Tri par note (croissant)
par_note = sorted(etudiants, key=lambda etudiant: etudiant["note"])
print("\n   Tri par note (croissant) :")
for etudiant in par_note:
    print(f"     {etudiant['nom']} : {etudiant['note']}")

# Tri par âge (décroissant)
par_age_desc = sorted(
    etudiants, key=lambda etudiant: etudiant["age"], reverse=True)
print("\n   Tri par âge (décroissant) :")
for etudiant in par_age_desc:
    print(f"     {etudiant['nom']} : {etudiant['age']} ans")

# Tri par nom (alphabétique)
par_nom = sorted(etudiants, key=lambda etudiant: etudiant["nom"])
print("\n   Tri par nom (alphabétique) :")
for etudiant in par_nom:
    print(f"     {etudiant['nom']}")

print("\n🎯 TRI MULTICRITÈRES")
print("-" * 20)

# Tri avec plusieurs critères
produits = [
    {"nom": "Laptop", "prix": 800, "stock": 5},
    {"nom": "Mouse", "prix": 25, "stock": 0},
    {"nom": "Keyboard", "prix": 75, "stock": 10},
    {"nom": "Monitor", "prix": 300, "stock": 0},
    {"nom": "Speaker", "prix": 50, "stock": 8}
]

print("🎯 Tri multicritères :")
print("   Produits originaux :")
for produit in produits:
    print(f"     {produit}")

# Tri par stock (disponible d'abord) puis par prix
tri_complexe = sorted(
    produits,
    # False < True, donc stock > 0 d'abord
    key=lambda p: (p["stock"] == 0, p["prix"])
)

print("\n   Tri par disponibilité puis prix :")
for produit in tri_complexe:
    disponible = "✅" if produit["stock"] > 0 else "❌"
    print(
        f"     {disponible} {produit['nom']} : {produit['prix']}€ (stock: {produit['stock']})")

# Tri par longueur de nom puis alphabétique
par_longueur_nom = sorted(
    produits,
    key=lambda p: (len(p["nom"]), p["nom"])
)

print("\n   Tri par longueur de nom puis alphabétique :")
for produit in par_longueur_nom:
    print(f"     {produit['nom']} ({len(produit['nom'])} lettres)")

print("\n🔤 TRI DE CHAÎNES AVANCÉ")
print("-" * 24)

phrases = [
    "Python est génial",
    "j'aime programmer",
    "Les lambda sont utiles",
    "Tri par longueur"
]

print("🔤 Tri avancé de chaînes :")
print(f"   Phrases originales : {phrases}")

# Tri par longueur
par_longueur = sorted(phrases, key=lambda s: len(s))
print(f"   Par longueur : {par_longueur}")

# Tri par nombre de mots
par_mots = sorted(phrases, key=lambda s: len(s.split()))
print(f"   Par nombre de mots : {par_mots}")

# Tri par dernière lettre
par_derniere_lettre = sorted(phrases, key=lambda s: s[-1].lower())
print(f"   Par dernière lettre : {par_derniere_lettre}")

# Tri case-insensitive
mots_casse = ["Apple", "banana", "Cherry", "date"]
tri_insensible = sorted(mots_casse, key=lambda s: s.lower())
print(f"   Tri insensible à la casse : {tri_insensible}")

print("\n" + "=" * 50)
print("4. LAMBDA DANS LES STRUCTURES DE DONNÉES")
print("=" * 50)

print("\n📋 LAMBDA DANS LES LISTES")
print("-" * 25)

# Stockage de lambdas dans une liste
operations = [
    lambda x: x + 1,
    lambda x: x * 2,
    lambda x: x ** 2,
    lambda x: x // 2
]

print("📋 Liste de fonctions lambda :")
nombre_test = 8
for i, operation in enumerate(operations):
    resultat = operation(nombre_test)
    print(f"   Opération {i} sur {nombre_test} = {resultat}")

# Génération dynamique de lambdas
multiplicateurs = [lambda x, m=mult: x * m for mult in range(1, 6)]
print(f"\n   Multiplicateurs pour {nombre_test} :")
for i, mult_func in enumerate(multiplicateurs, 1):
    print(f"     × {i} = {mult_func(nombre_test)}")

print("\n🗂️ LAMBDA DANS LES DICTIONNAIRES")
print("-" * 29)

# Dictionnaire de fonctions lambda
calculatrice = {
    "add": lambda x, y: x + y,
    "sub": lambda x, y: x - y,
    "mul": lambda x, y: x * y,
    "div": lambda x, y: x / y if y != 0 else "Division par zéro",
    "pow": lambda x, y: x ** y,
    "mod": lambda x, y: x % y if y != 0 else 0
}

print("🗂️ Calculatrice avec lambdas :")
test_a, test_b = 15, 4

for operation, func in calculatrice.items():
    resultat = func(test_a, test_b)
    print(f"   {test_a} {operation} {test_b} = {resultat}")

# Dispatch basé sur conditions
strategies = {
    "rapide": lambda data: f"Traitement rapide de {len(data)} éléments",
    "precis": lambda data: f"Traitement précis de {sum(data) if data else 0}",
    "economique": lambda data: f"Traitement économique (batch de {max(data) if data else 0} max)"
}

donnees_test = [1, 5, 3, 8, 2]
strategie_choisie = "precis"

print(
    f"\n   Stratégie '{strategie_choisie}' : {strategies[strategie_choisie](donnees_test)}")

print("\n🎛️ CALLBACKS ET EVENT HANDLERS")
print("-" * 32)


class EventManager:
    """Gestionnaire d'événements simple avec callbacks lambda"""

    def __init__(self):
        self.handlers = {}

    def on(self, event, callback):
        """Enregistre un callback pour un événement"""
        if event not in self.handlers:
            self.handlers[event] = []
        self.handlers[event].append(callback)

    def emit(self, event, data=None):
        """Déclenche un événement"""
        if event in self.handlers:
            for handler in self.handlers[event]:
                handler(data)
        else:
            print(f"   Aucun handler pour l'événement '{event}'")

    def list_events(self):
        """Liste les événements enregistrés"""
        return list(self.handlers.keys())


# Test du gestionnaire d'événements
print("🎛️ Système d'événements avec lambdas :")
em = EventManager()

# Enregistrement de handlers avec lambda
em.on("user_login", lambda user: print(f"   🔑 Utilisateur connecté : {user}"))
em.on("user_logout", lambda user: print(
    f"   🚪 Utilisateur déconnecté : {user}"))
em.on("error", lambda error: print(f"   ❌ Erreur : {error}"))

# Handler plus complexe
em.on("data_processed", lambda data: print(
    f"   📊 {len(data)} éléments traités, somme = {sum(data)}"))

# Test des événements
print(f"   Événements disponibles : {em.list_events()}")

em.emit("user_login", "Alice")
em.emit("data_processed", [1, 2, 3, 4, 5])
em.emit("user_logout", "Alice")
em.emit("error", "Connexion timeout")
em.emit("inexistant", "test")

print("\n" + "=" * 50)
print("5. CLOSURES ET LAMBDA")
print("=" * 50)

print("\n🪆 LAMBDA AVEC CLOSURE")
print("-" * 21)


def creer_multiplicateur_lambda(facteur):
    """Crée une lambda avec closure"""
    return lambda x: x * facteur


def creer_validateur_lambda(min_val, max_val):
    """Crée un validateur avec lambda et closure"""
    return lambda x: min_val <= x <= max_val


print("🪆 Lambdas avec closures :")

# Création de multiplicateurs spécialisés
double = creer_multiplicateur_lambda(2)
triple = creer_multiplicateur_lambda(3)
dizaine = creer_multiplicateur_lambda(10)

test_nombre = 7
print(f"   {test_nombre} × 2 = {double(test_nombre)}")
print(f"   {test_nombre} × 3 = {triple(test_nombre)}")
print(f"   {test_nombre} × 10 = {dizaine(test_nombre)}")

# Création de validateurs
age_adulte = creer_validateur_lambda(18, 65)
note_valide = creer_validateur_lambda(0, 20)
temperature_normale = creer_validateur_lambda(36, 38)

tests_validation = [
    ("Âge 25", age_adulte(25)),
    ("Âge 15", age_adulte(15)),
    ("Note 15", note_valide(15)),
    ("Note 25", note_valide(25)),
    ("Temp 37", temperature_normale(37)),
    ("Temp 40", temperature_normale(40))
]

print("\n   Tests de validation :")
for nom, resultat in tests_validation:
    statut = "✅" if resultat else "❌"
    print(f"     {statut} {nom}")

print("\n🏭 FACTORY DE LAMBDAS")
print("-" * 21)


def creer_comparateur_lambda(operation):
    """Factory de lambdas de comparaison"""
    operations = {
        "eq": lambda x, y: x == y,
        "ne": lambda x, y: x != y,
        "lt": lambda x, y: x < y,
        "le": lambda x, y: x <= y,
        "gt": lambda x, y: x > y,
        "ge": lambda x, y: x >= y
    }
    return operations.get(operation, lambda x, y: None)


def creer_transformateur_lambda(transformation):
    """Factory de lambdas de transformation"""
    transformations = {
        "upper": lambda s: s.upper() if isinstance(s, str) else str(s).upper(),
        "lower": lambda s: s.lower() if isinstance(s, str) else str(s).lower(),
        "reverse": lambda s: s[::-1] if isinstance(s, str) else str(s)[::-1],
        "length": lambda s: len(s) if hasattr(s, '__len__') else len(str(s)),
        "first_char": lambda s: s[0] if s else "",
        "last_char": lambda s: s[-1] if s else ""
    }
    return transformations.get(transformation, lambda x: x)


print("🏭 Factory de lambdas :")

# Test des comparateurs
greater_than = creer_comparateur_lambda("gt")
equal_to = creer_comparateur_lambda("eq")

print(f"   10 > 5 = {greater_than(10, 5)}")
print(f"   10 == 10 = {equal_to(10, 10)}")

# Test des transformateurs
uppercase = creer_transformateur_lambda("upper")
get_length = creer_transformateur_lambda("length")
reverse = creer_transformateur_lambda("reverse")

test_strings = ["hello", "Python", "lambda"]
print("\n   Transformations :")
for s in test_strings:
    print(
        f"     '{s}' -> upper: '{uppercase(s)}', length: {get_length(s)}, reverse: '{reverse(s)}'")

print("\n🔄 COMPOSITION DE LAMBDAS")
print("-" * 25)


def composer_lambdas(*functions):
    """Compose plusieurs lambdas en une seule"""
    return lambda x: reduce(lambda acc, f: f(acc), functions, x)


# Fonctions de transformation
def nettoyer(s): return s.strip().lower()
def remplacer_espaces(s): return s.replace(" ", "_")
def ajouter_prefix(s): return f"user_{s}"


# Composition
transformer_nom_utilisateur = composer_lambdas(
    nettoyer,
    remplacer_espaces,
    ajouter_prefix
)

print("🔄 Composition de lambdas :")
noms_test = ["  Alice Marie  ", " Bob-Smith ", "Charlie_Brown"]

for nom in noms_test:
    resultat = transformer_nom_utilisateur(nom)
    print(f"   '{nom}' -> '{resultat}'")

# Pipeline de traitement de données
traiter_nombre = composer_lambdas(
    lambda x: abs(x),  # Valeur absolue
    lambda x: x ** 2,  # Carré
    lambda x: x + 1,   # +1
    lambda x: x / 10   # Normalisation
)

print("\n   Pipeline numérique :")
nombres_test = [-3, 0, 2, -5, 4]
for nombre in nombres_test:
    resultat = traiter_nombre(nombre)
    print(f"     {nombre} -> {resultat:.2f}")

print("\n" + "=" * 50)
print("6. APPLICATIONS PRATIQUES")
print("=" * 50)

print("\n📊 ANALYSE DE DONNÉES")
print("-" * 20)

# Données de ventes
ventes = [
    {"produit": "Laptop", "prix": 800, "quantite": 2, "mois": "Jan"},
    {"produit": "Mouse", "prix": 25, "quantite": 10, "mois": "Jan"},
    {"produit": "Keyboard", "prix": 75, "quantite": 5, "mois": "Feb"},
    {"produit": "Monitor", "prix": 300, "quantite": 3, "mois": "Feb"},
    {"produit": "Speaker", "prix": 50, "quantite": 8, "mois": "Mar"}
]

print("📊 Analyse de données avec lambdas :")

# Calcul du chiffre d'affaires par vente
with_ca = list(map(lambda v: {**v, "ca": v["prix"] * v["quantite"]}, ventes))
print("   Ventes avec CA :")
for vente in with_ca:
    print(f"     {vente['produit']} : {vente['ca']}€")

# Filtrage des ventes importantes (> 100€)
ventes_importantes = list(filter(lambda v: v["ca"] > 100, with_ca))
print(f"\n   Ventes > 100€ : {len(ventes_importantes)} ventes")

# Calcul du CA total
ca_total = reduce(lambda acc, v: acc + v["ca"], with_ca, 0)
print(f"   CA total : {ca_total}€")

# Groupement par mois (simulation simple)
mois_uniques = list(set(map(lambda v: v["mois"], ventes)))
ca_par_mois = {
    mois: reduce(
        lambda acc, v: acc + v["ca"],
        filter(lambda v: v["mois"] == mois, with_ca),
        0
    )
    for mois in mois_uniques
}
print(f"   CA par mois : {ca_par_mois}")

print("\n🔗 CONFIGURATION ET DISPATCH")
print("-" * 30)

# Système de configuration avec lambdas
config_handlers = {
    "development": lambda: {
        "debug": True,
        "database_url": "sqlite:///dev.db",
        "log_level": "DEBUG"
    },
    "production": lambda: {
        "debug": False,
        "database_url": "postgresql://prod-server/db",
        "log_level": "WARNING"
    },
    "testing": lambda: {
        "debug": True,
        "database_url": ":memory:",
        "log_level": "INFO"
    }
}

# Middleware avec lambdas
middleware_stack = [
    # Ajouter timestamp
    lambda req: {**req, "timestamp": "2024-01-01T10:00:00"},
    # Authentification
    lambda req: {**req, "user_id": req.get("token", "anonymous")},
    lambda req: {**req, "processed": True}  # Marquer comme traité
]

print("🔗 Configuration et middleware :")

# Test de configuration
env = "development"
config = config_handlers[env]()
print(f"   Config {env} : {config}")

# Test de middleware
requete_initiale = {"path": "/api/users", "method": "GET", "token": "user123"}
requete_finale = reduce(lambda req, middleware: middleware(
    req), middleware_stack, requete_initiale)

print(f"   Requête initiale : {requete_initiale}")
print(f"   Requête finale : {requete_finale}")

print("\n🎮 SYSTÈME DE RÈGLES")
print("-" * 20)

# Système de règles métier avec lambdas
regles_remise = [
    {
        "nom": "Première commande",
        "condition": lambda commande: commande.get("premiere_fois", False),
        "remise": lambda total: total * 0.1  # 10%
    },
    {
        "nom": "Commande importante",
        "condition": lambda commande: commande.get("total", 0) > 500,
        "remise": lambda total: total * 0.05  # 5%
    },
    {
        "nom": "Client fidèle",
        "condition": lambda commande: commande.get("nb_commandes", 0) > 10,
        "remise": lambda total: total * 0.08  # 8%
    },
    {
        "nom": "Volume important",
        "condition": lambda commande: commande.get("nb_articles", 0) > 20,
        "remise": lambda total: total * 0.03  # 3%
    }
]


def calculer_remises(commande):
    """Calcule toutes les remises applicables"""
    remises_applicables = []

    for regle in regles_remise:
        if regle["condition"](commande):
            montant_remise = regle["remise"](commande["total"])
            remises_applicables.append({
                "nom": regle["nom"],
                "montant": montant_remise
            })

    return remises_applicables


print("🎮 Système de règles de remise :")

# Test avec différentes commandes
commandes_test = [
    {"total": 100, "premiere_fois": True, "nb_commandes": 1, "nb_articles": 5},
    {"total": 600, "premiere_fois": False, "nb_commandes": 15, "nb_articles": 25},
    {"total": 200, "premiere_fois": False, "nb_commandes": 3, "nb_articles": 8}
]

for i, commande in enumerate(commandes_test, 1):
    remises = calculer_remises(commande)
    total_remise = sum(r["montant"] for r in remises)

    print(f"\n   Commande {i} (total: {commande['total']}€) :")
    if remises:
        for remise in remises:
            print(f"     • {remise['nom']} : -{remise['montant']:.2f}€")
        print(f"     Total remise : -{total_remise:.2f}€")
        print(f"     Prix final : {commande['total'] - total_remise:.2f}€")
    else:
        print("     Aucune remise applicable")

print("\n" + "=" * 50)
print("7. BONNES PRATIQUES")
print("=" * 50)

print("\n✅ QUAND UTILISER LAMBDA")
print("-" * 25)

print("""
🎯 UTILISEZ LAMBDA QUAND :

✅ Fonction simple et courte (une ligne)
✅ Usage ponctuel (callback, key de tri)
✅ Transformation simple dans map/filter
✅ Configuration ou dispatch simple
✅ Fonction "jetable" sans réutilisation
✅ Style fonctionnel approprié

❌ ÉVITEZ LAMBDA QUAND :

❌ Logique complexe (plusieurs conditions)
❌ Fonction réutilisée plusieurs fois
❌ Besoin de documentation/tests
❌ Gestion d'erreurs nécessaire
❌ Lisibilité compromise
❌ Debugging difficile
""")

# Exemples de bon usage
print("✅ Bons usages de lambda :")

# Bon : tri simple
produits_simples = [("Laptop", 800), ("Mouse", 25), ("Keyboard", 75)]
par_prix = sorted(produits_simples, key=lambda p: p[1])
print(f"   Tri par prix : {par_prix}")

# Bon : transformation simple
nombres_simples = [1, 2, 3, 4, 5]
doubles = list(map(lambda x: x * 2, nombres_simples))
print(f"   Doubles : {doubles}")

# Bon : filtrage simple
ages_simples = [15, 22, 17, 30, 16, 25]
majeurs = list(filter(lambda age: age >= 18, ages_simples))
print(f"   Majeurs : {majeurs}")

print("\n❌ Mauvais usages (à éviter) :")

# Mauvais : trop complexe
print("   # lambda x: x if x > 0 else (-x if x < -10 else 0)  # Trop complexe")

# Mauvais : logique métier importante
print(
    "   # lambda user: user['active'] and user['verified'] and user['subscription'] != 'free'")

# Mieux avec def pour les cas complexes


def utilisateur_premium(user):
    """Détermine si un utilisateur est premium"""
    return (user.get('active', False) and
            user.get('verified', False) and
            user.get('subscription') != 'free')


print("   ✅ Mieux avec def pour logique complexe")

print("\n🔧 ALTERNATIVES AUX LAMBDA")
print("-" * 26)

# Au lieu de lambda complexe
donnees_complexes = [
    {"nom": "Alice", "age": 25, "actif": True, "score": 85},
    {"nom": "Bob", "age": 30, "actif": False, "score": 92},
    {"nom": "Charlie", "age": 22, "actif": True, "score": 78}
]

print("🔧 Alternatives aux lambda complexes :")

# Mauvais : lambda complexe
# tri_complexe = sorted(donnees_complexes,
#                      key=lambda x: (not x["actif"], -x["score"], x["age"]))

# Bon : fonction nommée


def cle_tri_utilisateur(utilisateur):
    """Clé de tri : actifs d'abord, puis par score décroissant, puis par âge"""
    return (not utilisateur["actif"], -utilisateur["score"], utilisateur["age"])


tri_propre = sorted(donnees_complexes, key=cle_tri_utilisateur)
print("   Tri avec fonction nommée :")
for user in tri_propre:
    statut = "🟢" if user["actif"] else "🔴"
    print(
        f"     {statut} {user['nom']} (score: {user['score']}, âge: {user['age']})")

# Alternative : operator module pour cas courants

# Au lieu de lambda x: x[1]
par_deuxieme_element = sorted(produits_simples, key=itemgetter(1))
print(f"\n   Avec itemgetter : {par_deuxieme_element}")

# Au lieu de lambda x: x.attribute


class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def __repr__(self):
        return f"Personne('{self.nom}', {self.age})"


personnes = [Personne("Alice", 25), Personne(
    "Bob", 20), Personne("Charlie", 30)]
par_age = sorted(personnes, key=attrgetter('age'))
print(f"   Avec attrgetter : {par_age}")

print("\n📝 DOCUMENTATION ET LISIBILITÉ")
print("-" * 31)

# Problème : lambda non documentée


def operation_mysterieuse(x, y): return x * 2 + y // 3 - 1

# Solution : fonction documentée


def calculer_score_ajuste(base, bonus):
    """
    Calcule un score ajusté selon la formule :
    score = base * 2 + bonus // 3 - 1

    Args:
        base: Score de base
        bonus: Points bonus

    Returns:
        Score ajusté
    """
    return base * 2 + bonus // 3 - 1


print("📝 Importance de la documentation :")
test_base, test_bonus = 10, 15

print(
    f"   Fonction mystérieuse : {operation_mysterieuse(test_base, test_bonus)}")
print(
    f"   Fonction documentée : {calculer_score_ajuste(test_base, test_bonus)}")
print("   -> Même résultat, mais la seconde est claire et maintenable")

print("\n" + "=" * 50)
print("8. PERFORMANCES ET OPTIMISATIONS")
print("=" * 50)

print("\n⚡ PERFORMANCE DES LAMBDA")
print("-" * 25)


def mesurer_temps(func, iterations=100000):
    """Mesure le temps d'exécution d'une fonction"""
    start = time.time()
    for _ in range(iterations):
        func()
    end = time.time()
    return (end - start) * 1000  # en millisecondes

# Comparaison lambda vs def


def fonction_def():
    return 42


def lambda_func(): return 42


print("⚡ Comparaison de performances :")
temps_def = mesurer_temps(fonction_def)
temps_lambda = mesurer_temps(lambda_func)

print(f"   Fonction def : {temps_def:.2f}ms")
print(f"   Lambda : {temps_lambda:.2f}ms")
print(f"   Ratio : {temps_lambda/temps_def:.2f}x")

# Test avec transformations
donnees_perf = list(range(10000))

# Avec lambda
start = time.time()
resultat_lambda = list(map(lambda x: x * x + 1, donnees_perf))
temps_map_lambda = (time.time() - start) * 1000

# Avec def


def transformer_def(x):
    return x * x + 1


start = time.time()
resultat_def = list(map(transformer_def, donnees_perf))
temps_map_def = (time.time() - start) * 1000

# Avec list comprehension
start = time.time()
resultat_comp = [x * x + 1 for x in donnees_perf]
temps_comp = (time.time() - start) * 1000

print(f"\n   Transformation de {len(donnees_perf)} éléments :")
print(f"   map + lambda : {temps_map_lambda:.2f}ms")
print(f"   map + def : {temps_map_def:.2f}ms")
print(f"   list comprehension : {temps_comp:.2f}ms")

print("\n🧠 OPTIMISATIONS AVEC LAMBDA")
print("-" * 28)

# Mémoïsation avec lambda


def memoize_lambda(func):
    """Décorateur de mémoïsation pour lambda"""
    cache = {}
    return lambda *args: cache.setdefault(args, func(*args))


# Lambda coûteuse (simulation)
def calcul_couteux(n): return sum(i**2 for i in range(n))


calcul_memoize = memoize_lambda(calcul_couteux)

print("🧠 Test de mémoïsation :")

# Premier appel (calcul)
start = time.time()
resultat1 = calcul_memoize(1000)
temps1 = (time.time() - start) * 1000

# Second appel (cache)
start = time.time()
resultat2 = calcul_memoize(1000)
temps2 = (time.time() - start) * 1000

print(f"   Premier appel : {temps1:.2f}ms -> {resultat1}")
print(f"   Second appel : {temps2:.2f}ms -> {resultat2}")
print(f"   Accélération : {temps1/temps2:.0f}x")

print("\n" + "=" * 50)
print("1-1. RÉSUMÉ FINAL")
print("=" * 50)

print("""
🎯 POINTS CLÉS À RETENIR :

1. 🎯 SYNTAXE LAMBDA :
   • lambda paramètres: expression
   • Une seule expression (pas de statements)
   • Fonction anonyme et jetable
   • Même objet que def mais plus limité

2. 🔧 USAGES PRINCIPAUX :
   • map(), filter(), reduce()
   • Fonctions de tri (key parameter)
   • Callbacks et event handlers
   • Configuration et dispatch
   • Transformations simples

3. 🪆 CLOSURES AVEC LAMBDA :
   • Capture des variables externes
   • Factory de fonctions spécialisées
   • État encapsulé
   • Composition de fonctions

4. 📊 APPLICATIONS PRATIQUES :
   • Analyse de données
   • Systèmes de règles métier
   • Pipeline de traitement
   • Configuration dynamique
   • Event-driven programming

5. ✅ BONNES PRATIQUES :
   • Utiliser pour fonctions simples uniquement
   • Préférer def pour logique complexe
   • Documenter les lambda complexes
   • Considérer les alternatives (operator)
   • Prioriser la lisibilité

💡 AVANTAGES :
✅ Concision du code
✅ Style fonctionnel
✅ Callbacks inline
✅ Pas de pollution d'espace de noms
✅ Composition facile

⚠️ LIMITATIONS :
❌ Une seule expression
❌ Pas de statements
❌ Debugging difficile
❌ Pas de documentation
❌ Moins lisible si complexe

🎯 ALTERNATIVES :
• operator module (itemgetter, attrgetter)
• functools (partial, reduce)
• Fonctions nommées pour complexité
• List/dict comprehensions
• Générateurs

⚡ PERFORMANCES :
• Comparable aux fonctions def
• Mémoïsation possible
• List comprehensions souvent plus rapides
• Considérer le contexte d'usage

🎨 PATTERNS AVANCÉS :
• Factory de lambdas
• Composition fonctionnelle
• Curry et partial application
• Pipeline de données
• Configuration déclarative
• Event systems

🎉 Félicitations ! Fonctions lambda maîtrisées !
💡 Prochaine étape : Fonctions built-in avancées !
📚 Lambdas maîtrisées, explorez les built-ins !
""")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE - FONCTIONS LAMBDA MAÎTRISÉES !")
print("=" * 70)
