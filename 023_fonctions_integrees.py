#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
======================================================================
FONCTIONS BUILT-IN DE PYTHON - GUIDE COMPLET
======================================================================

🎯 Ce fichier couvre les fonctions intégrées de Python :
   • Fonctions mathématiques et numériques
   • Fonctions de conversion et casting
   • Fonctions d'itération et séquences
   • Fonctions d'introspection
   • Fonctions d'I/O et système
   • Fonctions avancées et spécialisées

📚 Concepts abordés :
   • Built-ins les plus utilisées
   • Combinaisons et patterns
   • Performance et optimisation
   • Cas d'usage spécifiques
   • Alternatives et bonnes pratiques

💡 Objectif : Maîtriser l'arsenal des fonctions intégrées Python
"""

import time
import sys
import io

print("=" * 70)
print("FONCTIONS BUILT-IN DE PYTHON - GUIDE COMPLET")
print("=" * 70)

print("\n" + "=" * 50)
print("1. FONCTIONS MATHÉMATIQUES ET NUMÉRIQUES")
print("=" * 50)

print("\n🔢 FONCTIONS NUMÉRIQUES DE BASE")
print("-" * 29)

# Données de test
nombres_test = [-5, -3.7, 0, 2.8, 7, 12.5]
print(f"📊 Données de test : {nombres_test}")

print("\n🧮 Fonctions mathématiques essentielles :")

# abs() - Valeur absolue
valeurs_absolues = [abs(x) for x in nombres_test]
print(f"   abs() : {valeurs_absolues}")

# round() - Arrondi
arrondis = [round(x) for x in nombres_test]
print(f"   round() : {arrondis}")

# round() avec précision
arrondis_precis = [round(x, 1) for x in nombres_test]
print(f"   round(x, 1) : {arrondis_precis}")

# min() et max()
minimum = min(nombres_test)
maximum = max(nombres_test)
print(f"   min() : {minimum}")
print(f"   max() : {maximum}")

# sum()
somme_totale = sum(nombres_test)
print(f"   sum() : {somme_totale}")

# pow() - Puissance
print(f"   pow(2, 3) : {pow(2, 3)}")
print(f"   pow(2, 3, 5) : {pow(2, 3, 5)}")  # (2³) mod 5

print("\n🔤 FONCTIONS DE CONVERSION")
print("-" * 25)

# Données mixtes pour conversion
donnees_mixtes = [42, 3.14, "123", "45.67", True, False]
print(f"📊 Données mixtes : {donnees_mixtes}")

print("\n🔄 Conversions de types :")

# int() - Conversion en entier
print("   int() conversions :")
for donnee in donnees_mixtes:
    try:
        resultat = int(donnee) if isinstance(
            donnee, (str, float, bool)) else int(float(str(donnee)))
        print(f"     int({donnee}) = {resultat}")
    except ValueError as e:
        print(f"     int({donnee}) = Erreur : {e}")

# float() - Conversion en flottant
print("\n   float() conversions :")
for donnee in donnees_mixtes:
    try:
        if isinstance(donnee, str):
            resultat = float(donnee)
        else:
            resultat = float(donnee)
        print(f"     float({donnee}) = {resultat}")
    except ValueError as e:
        print(f"     float({donnee}) = Erreur : {e}")

# str() - Conversion en chaîne
conversions_str = [str(x) for x in donnees_mixtes]
print(f"\n   str() : {conversions_str}")

# bool() - Conversion en booléen
print("\n   bool() conversions (valeurs falsy/truthy) :")
valeurs_test_bool = [0, 1, "", "hello", [], [1, 2], {}, {"a": 1}, None]
for valeur in valeurs_test_bool:
    resultat = bool(valeur)
    print(f"     bool({valeur}) = {resultat}")

print("\n🎯 FONCTIONS NUMÉRIQUES AVANCÉES")
print("-" * 31)

# divmod() - Division et modulo
print("🎯 divmod() - Division euclidienne :")
divisions_test = [(17, 5), (23, 7), (100, 13)]
for a, b in divisions_test:
    quotient, reste = divmod(a, b)
    print(
        f"   divmod({a}, {b}) = ({quotient}, {reste}) -> {a} = {b}×{quotient} + {reste}")

# bin(), oct(), hex() - Conversions de base
nombre_conv = 42
print(f"\n🔢 Conversions de base pour {nombre_conv} :")
print(f"   bin({nombre_conv}) = {bin(nombre_conv)}")
print(f"   oct({nombre_conv}) = {oct(nombre_conv)}")
print(f"   hex({nombre_conv}) = {hex(nombre_conv)}")

# Conversion inverse
print(f"\n🔄 Conversions inverses :")
print(f"   int('0b101010', 2) = {int('0b101010', 2)}")
print(f"   int('0o52', 8) = {int('0o52', 8)}")
print(f"   int('0x2a', 16) = {int('0x2a', 16)}")

print("\n" + "=" * 50)
print("2. FONCTIONS D'ITÉRATION ET SÉQUENCES")
print("=" * 50)

print("\n📋 ENUMERATE() - INDEXATION")
print("-" * 26)

fruits = ["pomme", "banane", "orange", "kiwi"]
print(f"📋 Liste : {fruits}")

print("\n🔢 enumerate() ajoute des indices :")
for index, fruit in enumerate(fruits):
    print(f"   {index} : {fruit}")

print("\n🎯 enumerate() avec start personnalisé :")
for index, fruit in enumerate(fruits, start=1):
    print(f"   #{index} : {fruit}")

# Utilisation pratique : trouver l'index d'un élément


def trouver_index(liste, element):
    """Trouve l'index d'un élément avec enumerate"""
    for index, item in enumerate(liste):
        if item == element:
            return index
    return -1


index_orange = trouver_index(fruits, "orange")
print(f"\n   Index de 'orange' : {index_orange}")

print("\n🔗 ZIP() - COMBINAISON DE SÉQUENCES")
print("-" * 33)

noms = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
villes = ["Paris", "Lyon", "Marseille"]

print(f"📊 Données parallèles :")
print(f"   Noms : {noms}")
print(f"   Âges : {ages}")
print(f"   Villes : {villes}")

print("\n🔗 zip() combine les séquences :")
for nom, age, ville in zip(noms, ages, villes):
    print(f"   {nom}, {age} ans, vit à {ville}")

# zip() avec longueurs différentes
scores = [85, 92]  # Plus court
print(f"\n⚠️ zip() s'arrête au plus court :")
print(f"   Scores : {scores}")
for nom, score in zip(noms, scores):
    print(f"   {nom} : {score}")

# Création de dictionnaire avec zip
profils = dict(zip(noms, ages))
print(f"\n📖 Dictionnaire créé avec zip : {profils}")

# Déballage avec zip (transposition)
donnees_transposees = list(zip(*zip(noms, ages, villes)))
print(f"\n🔄 Transposition avec zip(*zip(...)) :")
print(f"   Originale : {list(zip(noms, ages, villes))}")
print(f"   Transposée : {donnees_transposees}")

print("\n📏 RANGE() - GÉNÉRATION DE SÉQUENCES")
print("-" * 35)

print("📏 range() génère des séquences numériques :")

# range() basique
print(f"   range(5) : {list(range(5))}")
print(f"   range(2, 8) : {list(range(2, 8))}")
print(f"   range(0, 10, 2) : {list(range(0, 10, 2))}")
print(f"   range(10, 0, -1) : {list(range(10, 0, -1))}")

# Utilisation avec autres fonctions
print(f"\n🔢 Combinaisons avec range() :")
print(f"   sum(range(1, 6)) : {sum(range(1, 6))}")  # 1+2+3+4+5
print(f"   max(range(10, 0, -2)) : {max(range(10, 0, -2))}")

# Génération de coordonnées
coordonnees = [(x, y) for x in range(3) for y in range(3)]
print(f"   Coordonnées 3×3 : {coordonnees}")

print("\n🔄 REVERSED() - INVERSION")
print("-" * 24)

# reversed() sur différents types
donnees_reverse = [1, 2, 3, 4, 5]
chaine_reverse = "Python"

print("🔄 reversed() inverse les séquences :")
print(f"   Liste originale : {donnees_reverse}")
print(f"   Liste inversée : {list(reversed(donnees_reverse))}")
print(f"   Chaîne originale : {chaine_reverse}")
print(f"   Chaîne inversée : {''.join(reversed(chaine_reverse))}")

# reversed() avec enumerate
print(f"\n📋 enumerate() + reversed() :")
for index, valeur in enumerate(reversed(donnees_reverse)):
    print(f"   Position {index} (depuis la fin) : {valeur}")

print("\n📊 SORTED() - TRI AVANCÉ")
print("-" * 22)

# Données complexes pour tri
etudiants = [
    {"nom": "Alice", "note": 15, "age": 20},
    {"nom": "Bob", "note": 18, "age": 19},
    {"nom": "Charlie", "note": 12, "age": 21},
    {"nom": "Diana", "note": 16, "age": 18}
]

print("📊 sorted() avec données complexes :")
print("   Étudiants originaux :")
for etudiant in etudiants:
    print(f"     {etudiant}")

# Tri par note
par_note = sorted(etudiants, key=lambda e: e["note"])
print(
    f"\n   Tri par note : {[e['nom'] + ':' + str(e['note']) for e in par_note]}")

# Tri par âge décroissant
par_age_desc = sorted(etudiants, key=lambda e: e["age"], reverse=True)
print(
    f"   Tri par âge ↓ : {[e['nom'] + ':' + str(e['age']) for e in par_age_desc]}")

# Tri par multiple critères
par_criteres = sorted(etudiants, key=lambda e: (-e["note"], e["age"]))
print(
    f"   Tri note ↓, âge ↑ : {[e['nom'] + ':' + str(e['note']) + ':' + str(e['age']) for e in par_criteres]}")

print("\n" + "=" * 50)
print("3. FONCTIONS D'ENTRÉE/SORTIE")
print("=" * 50)

print("\n💬 INPUT() - SAISIE UTILISATEUR")
print("-" * 27)

print("""
💬 input() capture la saisie utilisateur :

# Exemples (code non exécuté ici) :
# nom = input("Votre nom : ")
# age = int(input("Votre âge : "))
# prix = float(input("Prix : "))

⚠️ input() retourne toujours une chaîne !
➡️ Conversion nécessaire pour nombres
""")

# Simulation de saisies utilisateur


def simuler_input(prompt, valeur_simulee):
    """Simule input() pour les démonstrations"""
    print(f"{prompt}{valeur_simulee}")
    return valeur_simulee


print("🎯 Simulation de saisies :")
nom_simule = simuler_input("Nom : ", "Alice")
age_simule = int(simuler_input("Âge : ", "25"))
actif_simule = simuler_input("Actif (oui/non) : ", "oui").lower() == "oui"

print(
    f"   Résultats : nom='{nom_simule}', âge={age_simule}, actif={actif_simule}")

print("\n🖨️ PRINT() - SORTIE FORMATÉE")
print("-" * 25)

print("🖨️ print() options avancées :")

# Séparateur personnalisé
print("Option sep :", end="")
print("A", "B", "C", sep=" | ")

# Terminaison personnalisée
print("Option end :", end="")
print("Ligne 1", end=" -> ")
print("Suite de la ligne")

# Redirection vers fichier (simulation)

buffer = io.StringIO()
print("Redirection vers buffer", file=buffer)
contenu_buffer = buffer.getvalue()
print(f"   Contenu capturé : '{contenu_buffer.strip()}'")

# Formatage avec f-strings
nom, age, salaire = "Bob", 30, 45000.50
print(f"   f-string : {nom} a {age} ans et gagne {salaire:.2f}€")

# Print avec flush (force l'écriture immédiate)
print("   flush=True force l'écriture immédiate", flush=True)

print("\n📄 FORMAT() - FORMATAGE AVANCÉ")
print("-" * 28)

# Exemples de formatage
valeur = 1234.5678
print("📄 format() - formatage de nombres :")
print(f"   format({valeur}, '.2f') = {format(valeur, '.2f')}")
print(f"   format({valeur}, '.2e') = {format(valeur, '.2e')}")
print(f"   format({valeur}, '.2%') = {format(valeur/100, '.2%')}")
print(f"   format({int(valeur)}, 'b') = {format(int(valeur), 'b')}")
print(f"   format({int(valeur)}, 'x') = {format(int(valeur), 'x')}")

# Formatage avec largeur et alignement
texte = "Python"
print(f"\n📐 Formatage avec alignement :")
print(f"   format('{texte}', '<10') = '{format(texte, '<10')}'")  # Gauche
print(f"   format('{texte}', '^10') = '{format(texte, '^10')}'")  # Centre
print(f"   format('{texte}', '>10') = '{format(texte, '>10')}'")  # Droite
# Remplissage
print(f"   format('{texte}', '*^10') = '{format(texte, '*^10')}'")

print("\n" + "=" * 50)
print("4. FONCTIONS D'INTROSPECTION")
print("=" * 50)

print("\n🔍 TYPE() ET ISINSTANCE()")
print("-" * 24)

# Différents types d'objets
objets_test = [42, 3.14, "hello", [1, 2, 3], {"a": 1}, (1, 2), {1, 2, 3}, None]

print("🔍 Introspection de types :")
for obj in objets_test:
    type_obj = type(obj)
    nom_type = type_obj.__name__
    print(f"   {obj} -> type: {nom_type}")

# isinstance() vs type()
print(f"\n🎯 isinstance() vs type() :")
nombre = 42
print(f"   type({nombre}) == int : {type(nombre) == int}")
print(f"   isinstance({nombre}, int) : {isinstance(nombre, int)}")
print(
    f"   isinstance({nombre}, (int, float)) : {isinstance(nombre, (int, float))}")

# isinstance() avec héritage


class Animal:
    pass


class Chien(Animal):
    pass


mon_chien = Chien()
print(f"\n🐕 Test d'héritage :")
print(f"   isinstance(chien, Chien) : {isinstance(mon_chien, Chien)}")
print(f"   isinstance(chien, Animal) : {isinstance(mon_chien, Animal)}")
print(f"   type(chien) == Animal : {type(mon_chien) == Animal}")

print("\n📖 DIR() - EXPLORATION D'OBJETS")
print("-" * 29)

# dir() sur différents objets
print("📖 dir() liste les attributs et méthodes :")

# String
methodes_str = [m for m in dir("") if not m.startswith('_')]
print(f"   Méthodes str (échantillon) : {methodes_str[:8]}...")

# List
methodes_list = [m for m in dir([]) if not m.startswith('_')]
print(f"   Méthodes list : {methodes_list}")

# Objet personnalisé


class Exemple:
    attribut_classe = "classe"

    def __init__(self):
        self.attribut_instance = "instance"

    def methode_exemple(self):
        pass


obj_exemple = Exemple()
attributs_exemple = [attr for attr in dir(
    obj_exemple) if not attr.startswith('_')]
print(f"   Attributs Exemple : {attributs_exemple}")

print("\n🏷️ HASATTR(), GETATTR(), SETATTR()")
print("-" * 35)

print("🏷️ Manipulation d'attributs dynamique :")

# hasattr() - Test d'existence
print(
    f"   hasattr(obj_exemple, 'attribut_instance') : {hasattr(obj_exemple, 'attribut_instance')}")
print(
    f"   hasattr(obj_exemple, 'inexistant') : {hasattr(obj_exemple, 'inexistant')}")

# getattr() - Récupération avec défaut
valeur_existante = getattr(obj_exemple, 'attribut_instance', 'défaut')
valeur_inexistante = getattr(obj_exemple, 'inexistant', 'défaut')
print(f"   getattr(obj, 'attribut_instance', 'défaut') : {valeur_existante}")
print(f"   getattr(obj, 'inexistant', 'défaut') : {valeur_inexistante}")

# setattr() - Définition dynamique
setattr(obj_exemple, 'nouvel_attribut', 'nouvelle_valeur')
print(f"   Après setattr() : {obj_exemple.nouvel_attribut}")

# delattr() - Suppression
# delattr(obj_exemple, 'nouvel_attribut')  # Décommentez pour tester

print("\n🆔 ID() ET HASH()")
print("-" * 16)

# id() - Identité d'objet
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("🆔 Identité d'objets avec id() :")
print(f"   a = {a}, id = {id(a)}")
print(f"   b = a, id = {id(b)} -> même objet ? {id(a) == id(b)}")
print(f"   c = [1,2,3], id = {id(c)} -> même objet ? {id(a) == id(c)}")

# hash() - Empreinte
objets_hashables = [42, "hello", (1, 2, 3), frozenset([1, 2, 3])]
print(f"\n🔐 Hash d'objets :")
for obj in objets_hashables:
    try:
        h = hash(obj)
        print(f"   hash({obj}) = {h}")
    except TypeError as e:
        print(f"   hash({obj}) = Erreur : {e}")

print("\n" + "=" * 50)
print("5. FONCTIONS DE MANIPULATION D'OBJETS")
print("=" * 50)

print("\n📦 LEN() - TAILLE D'OBJETS")
print("-" * 22)

# len() sur différents types
objets_taille = [
    [1, 2, 3, 4, 5],
    "Python",
    {"a": 1, "b": 2, "c": 3},
    (1, 2, 3, 4),
    {1, 2, 3, 4, 5, 6},
    range(10)
]

print("📦 len() mesure la taille :")
for obj in objets_taille:
    taille = len(obj)
    type_nom = type(obj).__name__
    print(f"   len({obj}) = {taille} ({type_nom})")

print("\n🧮 ALL() ET ANY()")
print("-" * 17)

# Données pour tests logiques
tests_bool = [
    [True, True, True],
    [True, False, True],
    [False, False, False],
    [],
    [1, 2, 3, 4],
    [0, 1, 2, 3],
    ["", "hello", "world"],
    ["hello", "world"]
]

print("🧮 all() et any() - tests logiques :")
for test in tests_bool:
    all_result = all(test)
    any_result = any(test)
    print(f"   {test}")
    print(f"     all() = {all_result}, any() = {any_result}")

# Utilisation pratique
notes = [12, 15, 18, 14, 16]
print(f"\n🎯 Applications pratiques :")
print(f"   Notes : {notes}")
print(f"   Toutes >= 10 ? {all(note >= 10 for note in notes)}")
print(f"   Au moins une >= 15 ? {any(note >= 15 for note in notes)}")

# Validation de données
users = [
    {"nom": "Alice", "actif": True, "age": 25},
    {"nom": "Bob", "actif": True, "age": 30},
    {"nom": "Charlie", "actif": False, "age": 22}
]

tous_actifs = all(user["actif"] for user in users)
au_moins_un_majeur = any(user["age"] >= 18 for user in users)
print(f"   Tous actifs ? {tous_actifs}")
print(f"   Au moins un majeur ? {au_moins_un_majeur}")

print("\n🔀 ITER() ET NEXT()")
print("-" * 18)

# Création d'itérateur
ma_liste = [1, 2, 3, 4, 5]
iterateur = iter(ma_liste)

print("🔀 iter() et next() - itération manuelle :")
print(f"   Liste : {ma_liste}")
print(f"   Itérateur créé : {iterateur}")

# Consommation avec next()
print("   Consommation avec next() :")
try:
    for i in range(len(ma_liste) + 1):  # +1 pour tester StopIteration
        valeur = next(iterateur)
        print(f"     next() = {valeur}")
except StopIteration:
    print("     StopIteration atteinte")

# next() avec valeur par défaut
nouvel_iterateur = iter([10, 20])
print(f"\n   next() avec défaut :")
print(f"     next(iter, 'fini') = {next(nouvel_iterateur, 'fini')}")
print(f"     next(iter, 'fini') = {next(nouvel_iterateur, 'fini')}")
print(f"     next(iter, 'fini') = {next(nouvel_iterateur, 'fini')}")

print("\n🎯 CALLABLE() - TEST DE FONCTION")
print("-" * 31)

# Différents objets à tester


def ma_fonction():
    pass


class MaClasse:
    def __call__(self):
        pass


instance_callable = MaClasse()
objets_test_callable = [
    ma_fonction,
    MaClasse,
    instance_callable,
    lambda x: x,
    print,
    42,
    "hello",
    []
]

print("🎯 callable() teste si un objet est appelable :")
for obj in objets_test_callable:
    is_callable = callable(obj)
    nom = getattr(obj, '__name__', str(obj))
    print(f"   callable({nom}) = {is_callable}")

print("\n" + "=" * 50)
print("6. FONCTIONS AVANCÉES")
print("=" * 50)

print("\n⚡ EVAL() ET EXEC() - ÉVALUATION DYNAMIQUE")
print("-" * 40)

print("⚡ eval() évalue des expressions :")

# eval() - Évaluation d'expressions
expressions = [
    "2 + 3 * 4",
    "len('Python')",
    "max([1, 5, 3, 9, 2])",
    "'Hello' + ' ' + 'World'"
]

for expr in expressions:
    try:
        resultat = eval(expr)
        print(f"   eval('{expr}') = {resultat}")
    except Exception as e:
        print(f"   eval('{expr}') = Erreur : {e}")

# eval() avec contexte
contexte = {"x": 10, "y": 20, "fruits": ["pomme", "banane"]}
expressions_contexte = [
    "x + y",
    "x ** 2",
    "len(fruits)",
    "fruits[0].upper()"
]

print(f"\n🎯 eval() avec contexte {contexte} :")
for expr in expressions_contexte:
    try:
        resultat = eval(expr, {"__builtins__": {}}, contexte)
        print(f"   eval('{expr}') = {resultat}")
    except Exception as e:
        print(f"   eval('{expr}') = Erreur : {e}")

print(f"\n⚠️ exec() exécute du code (attention à la sécurité) :")
code_simple = """
resultat_exec = 0
for i in range(5):
    resultat_exec += i ** 2
"""

espace_exec = {}
exec(code_simple, espace_exec)
print(f"   Code exécuté, résultat : {espace_exec.get('resultat_exec')}")

print("\n🔨 COMPILE() - COMPILATION DE CODE")
print("-" * 31)

# compile() pour optimiser l'exécution répétée
expression_compilee = compile("x ** 2 + 2 * x + 1", "<string>", "eval")
code_compile = compile("print('Code compilé exécuté')", "<string>", "exec")

print("🔨 compile() pré-compile le code :")
print(f"   Expression compilée : {expression_compilee}")

# Utilisation du code compilé
x = 5
resultat_compile = eval(expression_compilee, {"x": x})
print(f"   eval(code_compilé) avec x={x} = {resultat_compile}")

exec(code_compile)

print("\n🏗️ VARS() - VARIABLES LOCALES/GLOBALES")
print("-" * 37)


def demonstration_vars():
    """Démonstration de vars()"""
    var_locale_1 = "valeur1"
    var_locale_2 = 42

    print("🏗️ vars() retourne les variables :")
    variables_locales = vars()
    print(f"   Variables locales : {list(variables_locales.keys())}")

    # vars() avec objet
    class ExempleVars:
        attr1 = "attribut1"
        attr2 = 123

    obj_vars = ExempleVars()
    obj_vars.attr3 = "attribut3"

    print(f"   vars(objet) : {vars(obj_vars)}")


demonstration_vars()

# vars() sans argument = locals()
print(f"   vars() globales (échantillon) : {list(vars().keys())[:5]}...")

print("\n🎲 GLOBALS() ET LOCALS()")
print("-" * 24)

variable_globale_demo = "Je suis globale"


def demo_globals_locals():
    """Démonstration de globals() et locals()"""
    variable_locale_demo = "Je suis locale"

    print("🎲 globals() et locals() :")

    # Accès aux espaces de noms
    print(
        f"   Variable globale via globals() : {globals()['variable_globale_demo']}")
    print(
        f"   Variable locale via locals() : {locals()['variable_locale_demo']}")

    # Modification via globals()
    globals()['nouvelle_globale'] = "Créée dynamiquement"

    # Comparaison des tailles
    print(f"   Nombre de variables globales : {len(globals())}")
    print(f"   Nombre de variables locales : {len(locals())}")


demo_globals_locals()
if 'nouvelle_globale' in globals():
    print(f"   Variable créée dynamiquement : {globals()['nouvelle_globale']}")
else:
    print("   Variable globale non créée")

print("\n" + "=" * 50)
print("7. APPLICATIONS PRATIQUES")
print("=" * 50)

print("\n🔧 UTILITAIRES DE DÉVELOPPEMENT")
print("-" * 32)


def debug_helper(obj, nom="objet"):
    """Utilitaire de debugging avec built-ins"""
    print(f"🔧 Debug de {nom} :")
    print(f"   Type : {type(obj).__name__}")
    print(f"   Valeur : {obj}")
    print(f"   ID : {id(obj)}")
    print(f"   Taille : {len(obj) if hasattr(obj, '__len__') else 'N/A'}")
    print(f"   Hashable : {hash(obj) if hashable_safe(obj) else 'Non'}")
    print(f"   Callable : {callable(obj)}")

    # Attributs (sans les privés)
    if hasattr(obj, '__dict__') or not isinstance(obj, (int, float, str, bool, type(None))):
        attrs = [attr for attr in dir(obj) if not attr.startswith('_')]
        print(
            f"   Attributs publics : {attrs[:5] if len(attrs) > 5 else attrs}")


def hashable_safe(obj):
    """Test sécurisé de hashabilité"""
    try:
        hash(obj)
        return True
    except TypeError:
        return False


# Test de l'utilitaire
print("🔧 Test de l'utilitaire de debug :")
debug_helper([1, 2, 3], "ma_liste")
debug_helper({"a": 1, "b": 2}, "mon_dict")

print("\n📊 ANALYSE DE DONNÉES AVEC BUILT-INS")
print("-" * 35)


def analyser_donnees(donnees, nom="dataset"):
    """Analyse statistique avec fonctions built-in"""
    print(f"📊 Analyse de {nom} :")

    if not donnees:
        print("   Dataset vide")
        return

    # Statistiques de base
    taille = len(donnees)
    minimum = min(donnees)
    maximum = max(donnees)
    somme = sum(donnees)
    moyenne = somme / taille

    print(f"   Taille : {taille}")
    print(f"   Min/Max : {minimum} / {maximum}")
    print(f"   Somme : {somme}")
    print(f"   Moyenne : {moyenne:.2f}")

    # Analyse des types
    types_presents = set(type(x).__name__ for x in donnees)
    print(f"   Types présents : {types_presents}")

    # Comptage des valeurs
    if taille <= 20:  # Afficher seulement pour petits datasets
        valeurs_uniques = set(donnees)
        print(f"   Valeurs uniques : {len(valeurs_uniques)}")

        # Fréquences simples
        if len(valeurs_uniques) <= 10:
            for valeur in sorted(valeurs_uniques):
                compte = sum(1 for x in donnees if x == valeur)
                print(f"     {valeur} : {compte} fois")


# Tests d'analyse
donnees_test_1 = [1, 2, 3, 4, 5, 3, 2, 4, 1, 5]
donnees_test_2 = [10.5, 20.3, 15.7, 30.1, 25.8]

analyser_donnees(donnees_test_1, "entiers")
print()
analyser_donnees(donnees_test_2, "flottants")

print("\n🎯 VALIDATION DE DONNÉES")
print("-" * 24)


def validateur_universel(donnees, regles):
    """Validateur utilisant les built-ins"""
    resultats = {
        "valide": True,
        "erreurs": [],
        "warnings": [],
        "statistiques": {}
    }

    # Règles de validation
    if "non_vide" in regles and regles["non_vide"]:
        if not donnees:
            resultats["erreurs"].append("Données vides")
            resultats["valide"] = False

    if "type_attendu" in regles:
        type_attendu = regles["type_attendu"]
        if not all(isinstance(x, type_attendu) for x in donnees):
            types_trouves = set(type(x).__name__ for x in donnees)
            resultats["erreurs"].append(
                f"Types incorrects. Attendu: {type_attendu.__name__}, trouvés: {types_trouves}")
            resultats["valide"] = False

    if "min_taille" in regles:
        if len(donnees) < regles["min_taille"]:
            resultats["erreurs"].append(
                f"Taille insuffisante: {len(donnees)} < {regles['min_taille']}")
            resultats["valide"] = False

    if "max_taille" in regles:
        if len(donnees) > regles["max_taille"]:
            resultats["warnings"].append(
                f"Taille importante: {len(donnees)} > {regles['max_taille']}")

    if donnees and "valeur_min" in regles:
        min_trouvee = min(donnees)
        if min_trouvee < regles["valeur_min"]:
            resultats["erreurs"].append(
                f"Valeur trop petite: {min_trouvee} < {regles['valeur_min']}")
            resultats["valide"] = False

    if donnees and "valeur_max" in regles:
        max_trouvee = max(donnees)
        if max_trouvee > regles["valeur_max"]:
            resultats["erreurs"].append(
                f"Valeur trop grande: {max_trouvee} > {regles['valeur_max']}")
            resultats["valide"] = False

    # Statistiques
    if donnees:
        resultats["statistiques"] = {
            "taille": len(donnees),
            "min": min(donnees) if all(isinstance(x, (int, float)) for x in donnees) else None,
            "max": max(donnees) if all(isinstance(x, (int, float)) for x in donnees) else None,
            "types": list(set(type(x).__name__ for x in donnees))
        }

    return resultats


# Tests de validation
print("🎯 Tests de validation :")

donnees_valides = [10, 20, 30, 40, 50]
regles_test = {
    "non_vide": True,
    "type_attendu": int,
    "min_taille": 3,
    "max_taille": 10,
    "valeur_min": 0,
    "valeur_max": 100
}

resultat_validation = validateur_universel(donnees_valides, regles_test)
print(f"   Données valides : {resultat_validation['valide']}")
if resultat_validation["erreurs"]:
    print(f"   Erreurs : {resultat_validation['erreurs']}")
if resultat_validation["warnings"]:
    print(f"   Warnings : {resultat_validation['warnings']}")
print(f"   Stats : {resultat_validation['statistiques']}")

# Test avec données invalides
donnees_invalides = [200, -10, "hello"]
resultat_invalid = validateur_universel(donnees_invalides, regles_test)
print(f"\n   Données invalides : {resultat_invalid['valide']}")
print(f"   Erreurs : {resultat_invalid['erreurs']}")

print("\n" + "=" * 50)
print("8. PERFORMANCES ET OPTIMISATIONS")
print("=" * 50)

print("\n⚡ COMPARAISON DE PERFORMANCES")
print("-" * 31)


def mesurer_performance(func, *args, iterations=10000):
    """Mesure la performance d'une fonction"""
    start = time.time()
    for _ in range(iterations):
        func(*args)
    end = time.time()
    return (end - start) * 1000  # en millisecondes


# Données de test
grandes_donnees = list(range(1000))

print("⚡ Comparaison map() vs comprehension :")

# Test map vs comprehension


def avec_map():
    return list(map(lambda x: x * 2, grandes_donnees))


def avec_comprehension():
    return [x * 2 for x in grandes_donnees]


temps_map = mesurer_performance(avec_map)
temps_comp = mesurer_performance(avec_comprehension)

print(f"   map() : {temps_map:.2f}ms")
print(f"   comprehension : {temps_comp:.2f}ms")
print(f"   Ratio : {temps_map/temps_comp:.2f}x")

# Test filter vs comprehension
print(f"\n🔍 Comparaison filter() vs comprehension :")


def avec_filter():
    return list(filter(lambda x: x % 2 == 0, grandes_donnees))


def avec_comprehension_filter():
    return [x for x in grandes_donnees if x % 2 == 0]


temps_filter = mesurer_performance(avec_filter)
temps_comp_filter = mesurer_performance(avec_comprehension_filter)

print(f"   filter() : {temps_filter:.2f}ms")
print(f"   comprehension : {temps_comp_filter:.2f}ms")
print(f"   Ratio : {temps_filter/temps_comp_filter:.2f}x")

print("\n🧠 OPTIMISATIONS AVEC BUILT-INS")
print("-" * 30)

# any() vs loop manuel pour recherche


def recherche_manuelle(liste, condition):
    """Recherche manuelle avec boucle"""
    for item in liste:
        if condition(item):
            return True
    return False


def recherche_any(liste, condition):
    """Recherche avec any()"""
    return any(condition(item) for item in liste)


# Test de performance
def condition_test(x): return x > 500


donnees_recherche = list(range(1000))

temps_manuel = mesurer_performance(
    recherche_manuelle, donnees_recherche, condition_test)
temps_any = mesurer_performance(
    recherche_any, donnees_recherche, condition_test)

print(f"🧠 Recherche d'élément :")
print(f"   Boucle manuelle : {temps_manuel:.2f}ms")
print(f"   any() : {temps_any:.2f}ms")
print(
    f"   Amélioration : {temps_manuel/temps_any:.2f}x plus rapide avec any()")

# min/max vs sorted


def min_max_sorted(liste):
    """Min/max avec sorted (inefficace)"""
    triee = sorted(liste)
    return triee[0], triee[-1]


def min_max_builtin(liste):
    """Min/max avec built-ins"""
    return min(liste), max(liste)


temps_sorted = mesurer_performance(min_max_sorted, grandes_donnees)
temps_builtin = mesurer_performance(min_max_builtin, grandes_donnees)

print(f"\n📊 Min/Max de {len(grandes_donnees)} éléments :")
print(f"   Avec sorted() : {temps_sorted:.2f}ms")
print(f"   Avec min/max : {temps_builtin:.2f}ms")
print(f"   Amélioration : {temps_sorted/temps_builtin:.2f}x plus rapide")


print("\n" + "=" * 50)
print("1-1. RÉSUMÉ FINAL")
print("=" * 50)

print("""
🎯 POINTS CLÉS À RETENIR :

1. 🔢 FONCTIONS MATHÉMATIQUES :
   • abs(), round(), min(), max(), sum()
   • pow(), divmod()
   • bin(), oct(), hex() pour les bases
   • int(), float() pour conversions

2. 🔄 FONCTIONS D'ITÉRATION :
   • enumerate() pour indexation
   • zip() pour combinaison de séquences
   • range() pour génération numérique
   • reversed() pour inversion
   • sorted() pour tri avancé

3. 💬 ENTRÉES/SORTIES :
   • input() pour saisie utilisateur
   • print() avec options avancées
   • format() pour formatage
   • str(), repr() pour représentation

4. 🔍 INTROSPECTION :
   • type(), isinstance() pour types
   • dir() pour exploration
   • hasattr(), getattr(), setattr()
   • id(), hash() pour identité
   • vars(), globals(), locals()

5. 🧮 FONCTIONS LOGIQUES :
   • all(), any() pour tests booléens
   • len() pour taille
   • callable() pour test de fonction
   • iter(), next() pour itération

6. ⚡ FONCTIONS AVANCÉES :
   • eval(), exec() pour évaluation
   • compile() pour optimisation
   • map(), filter(), reduce()
   • Built-ins vs alternatives

💡 AVANTAGES DES BUILT-INS :
✅ Performance optimisée (code C)
✅ Disponibilité immédiate
✅ Comportement standardisé  
✅ Gestion d'erreurs intégrée
✅ Compatibilité multi-types

🚨 BONNES PRATIQUES :
✅ Préférer built-ins aux loops manuels
✅ Combiner pour plus de puissance
✅ Attention à eval()/exec() (sécurité)
✅ Type checking avec isinstance()
✅ Gestion des exceptions
✅ Documentation du comportement

⚡ PERFORMANCES :
• Built-ins généralement plus rapides
• Comprehensions souvent meilleures que map/filter
• any()/all() avec short-circuit
• min()/max() plus rapides que sorted()
• enumerate() plus rapide que range(len())

🎯 PATTERNS COURANTS :
• enumerate() pour index + valeur
• zip() pour données parallèles
• all()/any() pour validation
• sorted() avec key personnalisée
• isinstance() pour polymorphisme
• getattr() avec défauts

🔧 DEBUGGING ET INTROSPECTION :
• dir() pour explorer objets
• type() et isinstance() pour typage
• vars() pour variables
• callable() pour fonctions
• hasattr() pour attributs

🎉 Félicitations ! Fonctions built-in maîtrisées !
💡 Prochaine étape : Gestion des erreurs et exceptions !
📚 Built-ins maîtrisées, gérez les erreurs !
""")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE - FONCTIONS BUILT-IN MAÎTRISÉES !")
print("=" * 70)
