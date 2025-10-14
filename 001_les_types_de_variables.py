"""
Les Types de Variables en Python - Guide Complet pour Débutants
===============================================================

Ce fichier présente tous les types de données de base en Python avec des 
explications détaillées et des exemples pratiques.

Python est un langage à typage dynamique : vous n'avez pas besoin de déclarer
le type d'une variable, Python le devine automatiquement !
"""

# =============================================================================
# 1. LES CHAÎNES DE CARACTÈRES (STRINGS) - TYPE : str
# =============================================================================

print("=" * 60)
print("1. LES CHAÎNES DE CARACTÈRES (STRINGS)")
print("=" * 60)

# Qu'est-ce qu'une chaîne de caractères ?
# C'est du TEXTE : lettres, chiffres, symboles, espaces...
# En Python, on les écrit entre guillemets

# 📝 Méthode 1 : Guillemets doubles (recommandé)
chaine_double = "Bonjour le monde !"
print(f"Guillemets doubles : {chaine_double}")
print(f"Type : {type(chaine_double)}")  # Affiche <class 'str'>

# 📝 Méthode 2 : Guillemets simples (équivalent)
chaine_simple = 'Hello World !'
print(f"Guillemets simples : {chaine_simple}")

# 🤔 QUESTION : Quand utiliser quoi ?
# - Utilisez " quand votre texte contient des apostrophes
phrase_avec_apostrophe = "Je m'appelle Pierre"
print(f"Avec apostrophe : {phrase_avec_apostrophe}")

# - Utilisez ' quand votre texte contient des guillemets
phrase_avec_guillemets = 'Il a dit : "Bonjour !"'
print(f"Avec guillemets : {phrase_avec_guillemets}")

# 📝 Méthode 3 : Échappement avec backslash (\)
# Le backslash "échappe" le caractère suivant
chaine_echappee = 'Je m\'appelle Pierre et il a dit : "Salut !"'
print(f"Avec échappement : {chaine_echappee}")

# 💡 ASTUCE : Caractères spéciaux avec échappement
exemples_echappement = "Nouvelle ligne : \nTabulation : \tGuillemet : \""
print(f"Caractères spéciaux :\n{exemples_echappement}")

# 📝 Méthode 4 : Chaînes multi-lignes avec ''' ou """
# Parfait pour de longs textes ou de la documentation
poeme = '''Roses are red,
Violets are blue,
Python is awesome,
And so are you !'''
print(f"Poème :\n{poeme}")

# Alternative avec guillemets doubles
description = """Ceci est une description
très longue qui s'étend
sur plusieurs lignes."""
print(f"Description :\n{description}")

# 📝 Méthode 5 : Raw strings (chaînes brutes) avec r""
# Le 'r' signifie "raw" = brut, pas d'interprétation des \
chemin_fichier = r"C:\Users\nom_utilisateur\Documents\fichier.txt"
print(f"Chemin de fichier : {chemin_fichier}")

# 📝 Méthode 6 : Concaténation implicite (chaînes longues)
# Python joint automatiquement les chaînes adjacentes
message_long = ("Ceci est un message très long "
                "qui est écrit sur plusieurs lignes "
                "pour une meilleure lisibilité du code.")
print(f"Message long : {message_long}")

# 🔍 VÉRIFICATION DU TYPE
print(f"\nType de 'Bonjour' : {type('Bonjour')}")
# False car 'Bonjour' n'est pas l'objet str
print(f"Est-ce une chaîne ? {'Bonjour' is str}")
print(f"Est-ce une instance de str ? {isinstance('Bonjour', str)}")  # True !

# =============================================================================
# 2. LES NOMBRES ENTIERS (INTEGERS) - TYPE : int
# =============================================================================

print("\n" + "=" * 60)
print("2. LES NOMBRES ENTIERS (INTEGERS)")
print("=" * 60)

# Les entiers sont des nombres SANS virgule : ..., -2, -1, 0, 1, 2, ...
nombre_entier = 42
print(f"Nombre entier : {nombre_entier}")
print(f"Type : {type(nombre_entier)}")

# 💡 ASTUCE : Python gère les TRÈS grands nombres automatiquement !
petit_nombre = 5
grand_nombre = 123456789012345678901234567890
tres_grand_nombre = 1_000_000_000  # Les _ rendent plus lisible !

print(f"Petit nombre : {petit_nombre}")
print(f"Grand nombre : {grand_nombre}")
print(f"Très grand nombre : {tres_grand_nombre}")

# 🔢 Différentes bases numériques
nombre_binaire = 0b1010      # Base 2 (binaire) = 10 en décimal
nombre_octal = 0o12          # Base 8 (octal) = 10 en décimal
nombre_hexadecimal = 0xFF    # Base 16 (hexadécimal) = 255 en décimal

print(f"Binaire 0b1010 = {nombre_binaire}")
print(f"Octal 0o12 = {nombre_octal}")
print(f"Hexadécimal 0xFF = {nombre_hexadecimal}")

# =============================================================================
# 3. LES NOMBRES DÉCIMAUX (FLOATS) - TYPE : float
# =============================================================================

print("\n" + "=" * 60)
print("3. LES NOMBRES DÉCIMAUX (FLOATS)")
print("=" * 60)

# Les floats sont des nombres AVEC virgule (décimaux)
nombre_decimal = 3.14159
prix = 19.99
temperature = -5.2

print(f"Pi approximatif : {nombre_decimal}")
print(f"Prix : {prix}€")
print(f"Température : {temperature}°C")
print(f"Type : {type(nombre_decimal)}")

# 💡 IMPORTANT : Même avec .0, c'est un float !
nombre_entier_en_float = 5.0
print(f"5.0 est de type : {type(nombre_entier_en_float)}")

# 🔬 Notation scientifique
nombre_scientifique = 1.5e-4  # 1.5 × 10^-4 = 0.00015
print(f"Notation scientifique 1.5e-4 = {nombre_scientifique}")

# ⚠️ ATTENTION : Précision limitée des floats
resultat = 0.1 + 0.2
print(f"0.1 + 0.2 = {resultat}")  # Attention : pas exactement 0.3 !
print(f"Est-ce égal à 0.3 ? {resultat == 0.3}")  # False !

# =============================================================================
# 4. LES BOOLÉENS (BOOLEANS) - TYPE : bool
# =============================================================================

print("\n" + "=" * 60)
print("4. LES BOOLÉENS (BOOLEANS)")
print("=" * 60)

# Les booléens n'ont que 2 valeurs possibles : True ou False
est_majeur = True
a_permis = False

print(f"Est majeur : {est_majeur}")
print(f"A un permis : {a_permis}")
print(f"Type : {type(est_majeur)}")

# 🔄 CONVERSION EN BOOLÉEN avec bool()
print("\n🔄 Conversion en booléens :")

# Ces valeurs sont considérées comme FALSE (falsy) :
print(f"bool(0) = {bool(0)}")              # 0 = False
print(f"bool(0.0) = {bool(0.0)}")          # 0.0 = False
print(f"bool('') = {bool('')}")            # Chaîne vide = False
print(f"bool([]) = {bool([])}")            # Liste vide = False
print(f"bool(None) = {bool(None)}")        # None = False

# Toutes les autres valeurs sont TRUE (truthy) :
print(f"bool(1) = {bool(1)}")              # Nombre non-zéro = True
print(f"bool(-5) = {bool(-5)}")            # Nombre négatif = True
print(f"bool('Bonjour') = {bool('Bonjour')}")  # Chaîne non-vide = True
print(f"bool([1, 2]) = {bool([1, 2])}")    # Liste non-vide = True

# 💡 UTILISATION PRATIQUE
age = 25
if age:  # age est truthy car c'est un nombre non-zéro
    print(f"L'âge {age} est considéré comme True")

# =============================================================================
# 5. CONVERSIONS DE TYPES (TYPE CASTING)
# =============================================================================

print("\n" + "=" * 60)
print("5. CONVERSIONS DE TYPES")
print("=" * 60)

# 🔄 Conversion vers STRING avec str()
nombre = 42
nombre_en_texte = str(nombre)
print(f"str({nombre}) = '{nombre_en_texte}' (type: {type(nombre_en_texte)})")

# 🔄 Conversion vers INTEGER avec int()
texte_nombre = "123"
texte_en_nombre = int(texte_nombre)
print(f"int('{texte_nombre}') = {texte_en_nombre} (type: {type(texte_en_nombre)})")

# ⚠️ ATTENTION : int() supprime la partie décimale !
decimal = 3.99
decimal_en_entier = int(decimal)
print(f"int({decimal}) = {decimal_en_entier}")  # Résultat : 3 (pas 4 !)

# 🔄 Conversion vers FLOAT avec float()
entier = 10
entier_en_decimal = float(entier)
print(f"float({entier}) = {entier_en_decimal} (type: {type(entier_en_decimal)})")

# 🔄 Conversion vers BOOLEAN avec bool()
print(f"bool(42) = {bool(42)}")
print(f"bool(0) = {bool(0)}")

# ❌ ERREURS COURANTES de conversion
try:
    # Ceci va générer une erreur !
    int("Bonjour")
except ValueError as e:
    print(f"❌ Erreur : {e}")

try:
    # Ceci aussi !
    float("3.14.15")
except ValueError as e:
    print(f"❌ Erreur : {e}")

# =============================================================================
# 6. LES COLLECTIONS - STRUCTURES DE DONNÉES
# =============================================================================

print("\n" + "=" * 60)
print("6. LES COLLECTIONS")
print("=" * 60)

# 📋 LES LISTES (LISTS) - TYPE : list
# Les listes sont MODIFIABLES et ORDONNÉES
ma_liste = [1, 2, 3, "Python", True, 3.14]
print(f"Liste : {ma_liste}")
print(f"Type : {type(ma_liste)}")
print(f"Longueur : {len(ma_liste)} éléments")

# Accès par index (commence à 0)
print(f"Premier élément : {ma_liste[0]}")
print(f"Dernier élément : {ma_liste[-1]}")

# Modification possible
ma_liste[0] = "Nouveau"
print(f"Liste modifiée : {ma_liste}")

# 📦 LES TUPLES (TUPLES) - TYPE : tuple
# Les tuples sont NON-MODIFIABLES et ORDONNÉS
mon_tuple = (1, 2, 3, "Python", True)
print(f"\nTuple : {mon_tuple}")
print(f"Type : {type(mon_tuple)}")

# Accès par index comme les listes
print(f"Deuxième élément : {mon_tuple[1]}")

# ⚠️ Impossible de modifier un tuple !
# mon_tuple[0] = "Nouveau"  # Ceci générerait une erreur !

# 🗂️ LES DICTIONNAIRES (DICTIONARIES) - TYPE : dict
# Les dictionnaires stockent des paires clé-valeur
mon_dictionnaire = {
    "nom": "Dupont",
    "age": 30,
    "ville": "Paris",
    "programmeur": True
}
print(f"\nDictionnaire : {mon_dictionnaire}")
print(f"Type : {type(mon_dictionnaire)}")

# Accès par clé
print(f"Nom : {mon_dictionnaire['nom']}")
print(f"Age : {mon_dictionnaire['age']}")

# Modification possible
mon_dictionnaire["age"] = 31
print(f"Age modifié : {mon_dictionnaire['age']}")

# 🔗 LES ENSEMBLES (SETS) - TYPE : set
# Les ensembles contiennent des éléments UNIQUES (pas de doublons)
mon_ensemble = {1, 2, 3, 3, 3, 4, 5}  # Les 3 en double disparaissent !
print(f"\nEnsemble : {mon_ensemble}")  # Résultat : {1, 2, 3, 4, 5}
print(f"Type : {type(mon_ensemble)}")

# Ajout d'élément
mon_ensemble.add(6)
print(f"Après ajout de 6 : {mon_ensemble}")

# 🚫 LA VALEUR NONE - TYPE : NoneType
# None représente "rien", "vide", "absence de valeur"
ma_variable_vide = None
print(f"\nValeur None : {ma_variable_vide}")
print(f"Type : {type(ma_variable_vide)}")

# Utilisation courante de None


def ma_fonction():
    pass  # Ne fait rien, retourne None


resultat = ma_fonction()
print(f"Fonction sans return : {resultat}")

# =============================================================================
# 7. VÉRIFICATION ET IDENTIFICATION DES TYPES
# =============================================================================

print("\n" + "=" * 60)
print("7. VÉRIFICATION DES TYPES")
print("=" * 60)

# 🔍 La fonction type()
exemples = [
    "Bonjour",      # str
    42,             # int
    3.14,           # float
    True,           # bool
    [1, 2, 3],      # list
    (1, 2, 3),      # tuple
    {"a": 1},       # dict
    {1, 2, 3},      # set
    None            # NoneType
]

for exemple in exemples:
    print(f"type({exemple}) = {type(exemple).__name__}")

# 🔍 La fonction isinstance() - Plus robuste
print(f"\nisinstance('Hello', str) = {isinstance('Hello', str)}")
print(f"isinstance(42, int) = {isinstance(42, int)}")
print(f"isinstance(3.14, (int, float)) = {isinstance(3.14, (int, float))}")

# =============================================================================
# 8. BONNES PRATIQUES POUR DÉBUTANTS
# =============================================================================

print("\n" + "=" * 60)
print("8. BONNES PRATIQUES")
print("=" * 60)

# ✅ Nommage des variables (conventions Python)
age_utilisateur = 25        # ✅ snake_case recommandé
nom_complet = "Jean Dupont"  # ✅ Descriptif
PI = 3.14159               # ✅ Constante en MAJUSCULES

# ❌ Évitez ces noms
# l = [1, 2, 3]           # ❌ Trop court
# O = "Bonjour"           # ❌ Peut être confondu avec 0
# class = "Python"        # ❌ Mot-clé réservé

# ✅ Utilisez des f-strings pour l'affichage (Python 3.6+)
nom = "Pierre"
age = 30
message = f"Je m'appelle {nom} et j'ai {age} ans."
print(f"F-string : {message}")

# ✅ Soyez explicite avec les conversions
nombre_str = "42"
nombre_int = int(nombre_str)  # ✅ Conversion explicite
print(f"'{nombre_str}' converti en nombre : {nombre_int}")

# =============================================================================
# 9. RÉSUMÉ RAPIDE - AIDE-MÉMOIRE
# =============================================================================

print("\n" + "=" * 60)
print("9. RÉSUMÉ - AIDE-MÉMOIRE")
print("=" * 60)

aide_memoire = """
📝 TYPES DE BASE :
   str    → "texte" ou 'texte'          → Texte
   int    → 42                          → Nombre entier  
   float  → 3.14                        → Nombre décimal
   bool   → True ou False               → Vrai/Faux

📚 COLLECTIONS :
   list   → [1, 2, 3]                   → Liste modifiable
   tuple  → (1, 2, 3)                   → Liste non-modifiable
   dict   → {"clé": "valeur"}           → Dictionnaire
   set    → {1, 2, 3}                   → Ensemble (unique)
   
🔧 FONCTIONS UTILES :
   type(variable)                       → Affiche le type
   isinstance(variable, type)           → Vérifie le type
   len(collection)                      → Longueur/taille
   
🔄 CONVERSIONS :
   str(42)        → "42"
   int("42")      → 42
   float("3.14")  → 3.14
   bool(1)        → True
"""

print(aide_memoire)
