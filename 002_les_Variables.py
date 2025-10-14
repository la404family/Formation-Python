"""
Les Variables en Python - Guide Complet pour Débutants
======================================================

Ce fichier explique tout sur les variables en Python : création, nommage,
conventions, bonnes pratiques, et mécanismes internes.

Qu'est-ce qu'une variable ?
- Une variable est comme une "boîte" avec un nom qui contient une valeur
- Elle permet de stocker des données en mémoire et de les réutiliser
- Le nom de la variable fait référence à l'adresse où la valeur est stockée

"""

import keyword
print("=" * 70)
print("LES VARIABLES EN PYTHON - GUIDE COMPLET")
print("=" * 70)

# =============================================================================
# 1. QU'EST-CE QU'UNE VARIABLE ? - CONCEPT FONDAMENTAL
# =============================================================================

print("\n" + "=" * 50)
print("1. CONCEPT DE BASE : QU'EST-CE QU'UNE VARIABLE ?")
print("=" * 50)

# 📦 Une variable = un nom + une valeur
mon_age = 25
mon_nom = "Pierre"

print(f"ma variable 'mon_age' contient : {mon_age}")
print(f"ma variable 'mon_nom' contient : {mon_nom}")

# 🧠 Analogie : Une variable est comme une boîte étiquetée
print("""
🧠 ANALOGIE - Les variables comme des boîtes :

    [mon_age]     [mon_nom]      [pi]
       |            |            |
       ▼            ▼            ▼
      25         "Pierre"       3.14

Chaque boîte (variable) a :
- Un NOM (étiquette) : mon_age, mon_nom, pi
- Une VALEUR (contenu) : 25, "Pierre", 3.14
""")

# =============================================================================
# 2. CONVENTIONS DE NOMMAGE - STYLES D'ÉCRITURE
# =============================================================================

print("\n" + "=" * 50)
print("2. CONVENTIONS DE NOMMAGE")
print("=" * 50)

# 🐍 SNAKE_CASE (Recommandé en Python)
# Mots séparés par des underscores, tout en minuscules
mon_nom_complet = "Jean Dupont"
age_utilisateur = 30
nombre_de_tentatives = 3

print(f"✅ snake_case (recommandé) : {mon_nom_complet}")

# 🐪 camelCase (Moins courant en Python)
# Premier mot en minuscule, les suivants commencent par une majuscule
monNomComplet = "Marie Martin"
ageUtilisateur = 25

print(f"⚠️ camelCase (moins courant) : {monNomComplet}")

# 🏛️ PascalCase (Pour les classes)
# Chaque mot commence par une majuscule
MaClasse = "Exemple de classe"
MonModule = "Exemple de module"

print(f"🏛️ PascalCase (pour classes) : {MaClasse}")

# 📢 SCREAMING_SNAKE_CASE (Pour les constantes)
# Tout en majuscules avec underscores
PI = 3.14159
VITESSE_LUMIERE = 299792458  # m/s
NOM_APPLICATION = "Mon Super Programme"

print(f"📢 SCREAMING_SNAKE_CASE (constantes) : {PI}")

# ❌ kebab-case (INTERDIT en Python)
# Les tirets ne sont pas autorisés dans les noms de variables
# mon-nom = "Erreur"  # ❌ Ceci génère une erreur de syntaxe !

print("❌ kebab-case INTERDIT : mon-nom (génère une erreur)")

# 🏷️ Hungarian Notation (Déconseillée en Python moderne)
# Préfixer le nom avec le type (pratique ancienne)
int_age = 25
str_nom = "Pierre"
bool_est_majeur = True
float_taille = 1.75
list_scores = [10, 15, 20]

print(f"🏷️ Hungarian notation (déconseillée) : {str_nom}")

print("""
📋 RÉSUMÉ DES CONVENTIONS :
✅ snake_case       → Variables et fonctions (RECOMMANDÉ)
exemple de snake_case : ma_variable_exemple = 42
⚠️ camelCase        → Acceptable mais moins pythonique
exemple de camelCase : maVariableExemple = 42
🏛️ PascalCase       → Classes et exceptions
exemple de PascalCase : MaClasse = "Exemple de classe"
📢 UPPER_CASE       → Constantes
exemple de UPPER_CASE : PI = 3.14159
❌ kebab-case       → INTERDIT (erreur de syntaxe)
exemple de kebab-case : mon-nom = "Erreur" 
🏷️ hungarianNotation → Déconseillée (non pythonique)
exemple de hungarianNotation : int_age = 25
""")

# =============================================================================
# 3. MÉCANISME INTERNE - COMMENT PYTHON STOCKE LES VARIABLES
# =============================================================================

print("\n" + "=" * 50)
print("3. MÉCANISME INTERNE - STOCKAGE EN MÉMOIRE")
print("=" * 50)

# 🧠 Chaque variable a une adresse mémoire unique (identifiant)
# La fonction id() retourne cette adresse

variable1 = 42
variable2 = variable1  # variable2 pointe vers la même valeur

print(f"Variable1 : {variable1}")
print(f"Variable2 : {variable2}")
print(f"Adresse de variable1 : {id(variable1)}")
print(f"Adresse de variable2 : {id(variable2)}")
print(f"Même adresse ? {id(variable1) == id(variable2)}")

# 🔢 OPTIMISATION PYTHON : Petits entiers (-5 à 256)
# Python réutilise les mêmes objets pour économiser la mémoire
petit_nombre1 = 100
petit_nombre2 = 100

grand_nombre1 = 1000
grand_nombre2 = 1000

print(f"\nPetits nombres (100) :")
print(f"ID de petit_nombre1 : {id(petit_nombre1)}")
print(f"ID de petit_nombre2 : {id(petit_nombre2)}")
print(f"Même adresse ? {id(petit_nombre1) == id(petit_nombre2)}")  # True

print(f"\nGrands nombres (1000) :")
print(f"ID de grand_nombre1 : {id(grand_nombre1)}")
print(f"ID de grand_nombre2 : {id(grand_nombre2)}")
# Peut être False
print(f"Même adresse ? {id(grand_nombre1) == id(grand_nombre2)}")

# 🔍 Vérification du type avec type()
print(f"\nTypes des variables :")
print(f"type(variable1) : {type(variable1)}")
print(f"type('Hello') : {type('Hello')}")
print(f"type([1,2,3]) : {type([1,2,3])}")

# =============================================================================
# 4. ASSIGNATIONS MULTIPLES - TECHNIQUES AVANCÉES
# =============================================================================

print("\n" + "=" * 50)
print("4. ASSIGNATIONS MULTIPLES")
print("=" * 50)

# 📋 Assignation multiple (unpacking)
# Assigner plusieurs valeurs à plusieurs variables en une ligne
nom, age, ville = "Alice", 28, "Paris"

print(f"✅ Assignation multiple :")
print(f"   nom = {nom}")
print(f"   age = {age}")
print(f"   ville = {ville}")

# 🔄 Échange de variables (swap)
# Technique très élégante en Python !
x = 10
y = 20
print(f"\nAvant échange : x={x}, y={y}")

x, y = y, x  # Échange magique !
print(f"Après échange : x={x}, y={y}")

# 📝 Assignation en chaîne
# Donner la même valeur à plusieurs variables
a = b = c = 100
print(f"\nAssignation en chaîne : a={a}, b={b}, c={c}")

# ⚠️ ATTENTION avec les objets mutables !
liste1 = liste2 = [1, 2, 3]  # ⚠️ Même liste partagée !
liste1.append(4)
print(f"liste1 : {liste1}")
print(f"liste2 : {liste2}")  # ⚠️ Aussi modifiée !

# ✅ Solution : Créer des listes séparées
liste3 = [1, 2, 3]
liste4 = [1, 2, 3]  # ✅ Listes indépendantes
liste3.append(4)
print(f"liste3 : {liste3}")
print(f"liste4 : {liste4}")  # ✅ Non modifiée

# =============================================================================
# 5. RÈGLES ET RESTRICTIONS - CE QUI EST INTERDIT
# =============================================================================

print("\n" + "=" * 50)
print("5. RÈGLES ET RESTRICTIONS")
print("=" * 50)

# ✅ NOMS VALIDES
nom_valide = "OK"
_nom_avec_underscore = "OK"
nom2 = "OK"
NomAvecMajuscules = "OK"

print("✅ Noms valides :")
print(f"   nom_valide : {nom_valide}")
print(f"   _nom_avec_underscore : {_nom_avec_underscore}")
print(f"   nom2 : {nom2}")

# ❌ NOMS INVALIDES (commentés pour éviter les erreurs)
print("\n❌ Noms INVALIDES (génèrent des erreurs) :")
print("   2nom = 'Erreur'        # ❌ Commence par un chiffre")
print("   mon-nom = 'Erreur'     # ❌ Contient un tiret")
print("   mon nom = 'Erreur'     # ❌ Contient un espace")
print("   if = 'Erreur'          # ❌ Mot-clé réservé")

# 📚 MOTS-CLÉS RÉSERVÉS PYTHON
mots_reserves = keyword.kwlist
print(f"\n📚 Mots-clés réservés Python ({len(mots_reserves)} au total) :")
print("   " + ", ".join(mots_reserves[:10]) + "...")
print("   (Vous ne pouvez pas utiliser ces mots comme noms de variables)")

# 🧪 Test si un nom est valide


def est_nom_valide(nom):
    """Teste si un nom de variable est valide en Python"""
    try:
        # Tentative d'évaluation comme nom de variable
        compile(f'{nom} = 1', '<string>', 'exec')
        return not keyword.iskeyword(nom)
    except SyntaxError:
        return False


tests_noms = ['mon_nom', '2nom', 'mon-nom', 'if', 'nom_valide']
print(f"\n🧪 Test de validité des noms :")
for nom in tests_noms:
    validite = "✅ Valide" if est_nom_valide(nom) else "❌ Invalide"
    print(f"   '{nom}' : {validite}")


# =============================================================================
# 6. BONNES PRATIQUES - NOMMAGE DESCRIPTIF
# =============================================================================

print("\n" + "=" * 50)
print("6. BONNES PRATIQUES POUR LE NOMMAGE")
print("=" * 50)

# ✅ NOMS DESCRIPTIFS ET CLAIRS
utilisateur_connecte = True
nombre_tentatives_restantes = 3
liste_scores_eleves = [15, 18, 12, 20]
dictionnaire_configuration = {"theme": "sombre", "langue": "fr"}

print("✅ Noms descriptifs :")
print(f"   utilisateur_connecte : {utilisateur_connecte}")
print(f"   nombre_tentatives_restantes : {nombre_tentatives_restantes}")

# ❌ NOMS PEU CLAIRS (à éviter)
u = True          # ❌ Trop court, pas clair
n = 3             # ❌ Que représente 'n' ?
l = [15, 18, 12]  # ❌ 'l' ressemble à '1'
d = {"a": 1}      # ❌ Pas descriptif

print("\n❌ Noms peu clairs (à éviter) :")
print(f"   u : {u} (que représente 'u' ?)")
print(f"   n : {n} (que représente 'n' ?)")

# 🎯 CONVENTIONS SPÉCIFIQUES PYTHON

# Variables privées (convention)
_variable_privee = "Ne devrait pas être utilisée directement"
__variable_tres_privee = "Encore plus privée"

# Constantes
TAUX_TVA = 0.20
URL_API_BASE = "https://api.example.com"
COULEURS_AUTORISEES = ["rouge", "vert", "bleu"]

# Variables temporaires ou itérateurs
for i in range(3):  # 'i' est acceptable pour les boucles courtes
    for j in range(2):  # 'j' pour une boucle imbriquée
        pass

# Variables "jetables"
_ = "Variable temporaire ignorée"  # '_' = variable qu'on ignore

print(f"\n🎯 Conventions spéciales :")
print(f"   _variable_privee : '{_variable_privee[:20]}...'")
print(f"   TAUX_TVA : {TAUX_TVA}")

# =============================================================================
# 7. PORTÉE DES VARIABLES (SCOPE) - CONCEPTS AVANCÉS
# =============================================================================

print("\n" + "=" * 50)
print("7. PORTÉE DES VARIABLES (SCOPE)")
print("=" * 50)

# 🌍 Variable globale (accessible partout)
variable_globale = "Je suis globale"


def ma_fonction():
    # 🔄 Déclaration global en premier
    global variable_globale

    # 🏠 Variable locale (accessible seulement dans la fonction)
    variable_locale = "Je suis locale"

    print(f"   Dans la fonction - globale : {variable_globale}")
    print(f"   Dans la fonction - locale : {variable_locale}")

    # 🔄 Modification d'une variable globale
    variable_globale = "Modifiée depuis la fonction"


print("🌍 Avant appel de fonction :")
print(f"   variable_globale : {variable_globale}")

ma_fonction()

print("🔄 Après appel de fonction :")
print(f"   variable_globale : {variable_globale}")

# ❌ variable_locale n'existe pas ici !
# print(variable_locale)  # ❌ Erreur : NameError

# =============================================================================
# 8. MANIPULATION ET OPÉRATIONS SUR LES VARIABLES
# =============================================================================

print("\n" + "=" * 50)
print("8. MANIPULATION DES VARIABLES")
print("=" * 50)

# 🔢 Opérations sur les nombres
compteur = 0
compteur += 1        # compteur = compteur + 1
compteur *= 2        # compteur = compteur * 2
compteur -= 3        # compteur = compteur - 3

print(f"🔢 Opérations arithmétiques :")
print(f"   Résultat final du compteur : {compteur}")

# 📝 Opérations sur les chaînes
salutation = "Bonjour"
nom_utilisateur = "Alice"
message_complet = salutation + " " + nom_utilisateur + " !"

print(f"📝 Concaténation de chaînes :")
print(f"   message_complet : {message_complet}")

# 📋 Opérations sur les listes
ma_liste = [1, 2, 3]
ma_liste.append(4)
ma_liste.extend([5, 6])

print(f"📋 Manipulation de listes :")
print(f"   ma_liste après modifications : {ma_liste}")

# 🔄 Copie vs Référence (concept important !)
liste_originale = [1, 2, 3]
reference = liste_originale      # ⚠️ Référence (même objet)
copie = liste_originale.copy()   # ✅ Copie (nouvel objet)

liste_originale.append(4)

print(f"\n🔄 Copie vs Référence :")
print(f"   liste_originale : {liste_originale}")
print(f"   reference : {reference}")        # ⚠️ Modifiée aussi !
print(f"   copie : {copie}")               # ✅ Non modifiée

# =============================================================================
# 9. GESTION DYNAMIQUE DES VARIABLES
# =============================================================================

print("\n" + "=" * 50)
print("9. GESTION DYNAMIQUE")
print("=" * 50)

# 🔍 Vérifier l'existence d'une variable
variables_locales = locals()  # Dictionnaire des variables locales
variables_globales = globals()  # Dictionnaire des variables globales

print("🔍 Variables définies dans cette fonction :")
variables_interessantes = {k: v for k, v in variables_locales.items()
                           if not k.startswith('__') and not callable(v)}
for nom, valeur in list(variables_interessantes.items())[:5]:
    print(f"   {nom} : {str(valeur)[:30]}...")

# 🗑️ Supprimer une variable
variable_temporaire = "Je vais disparaître"
print(f"Avant suppression : variable_temporaire = {variable_temporaire}")

del variable_temporaire
# print(variable_temporaire)  # ❌ Erreur : NameError

print("Après suppression : variable_temporaire n'existe plus")

# 🏷️ Variables dynamiques (avancé)
variables_dynamiques = {}
for i in range(3):
    # Création de variables dynamiques (nom généré)
    nom_variable = f"variable_dynamique_{i}"
    valeur = f"Valeur {i}"
    # Stockage dans un dictionnaire pour éviter les erreurs
    variables_dynamiques[nom_variable] = valeur
    # Alternative : créer vraiment la variable globale (décommentez si nécessaire)
    # globals()[nom_variable] = valeur

print(f"\n🏷️ Variables créées dynamiquement :")
for nom, valeur in variables_dynamiques.items():
    print(f"   {nom} : {valeur}")

# Exemple d'accès aux variables dynamiques
print(f"Accès direct : {variables_dynamiques['variable_dynamique_1']}")

# =============================================================================
# 10. CONVENTIONS DE STYLE DÉTAILLÉES (PEP 8)
# =============================================================================

print("\n" + "=" * 50)
print("10. GUIDE DE STYLE PEP 8")
print("=" * 50)

style_guide = """
📖 GUIDE DE STYLE PYTHON (PEP 8) :

🐍 snake_case :
   ✅ Variables : mon_nom, age_utilisateur
   ✅ Fonctions : calculer_moyenne(), obtenir_donnees()
   ✅ Modules : mon_module.py

🏛️ PascalCase :
   ✅ Classes : MaClasse, GestionnaireUtilisateur
   ✅ Exceptions : MonErreurPersonnalisee

📢 UPPER_CASE :
   ✅ Constantes : PI, VITESSE_LUMIERE, URL_API

🔤 Longueur des noms :
   ✅ Descriptifs mais pas trop longs
   ✅ Préférer "nombre_utilisateurs" à "nb_usr"
   ✅ Éviter les abréviations obscures

🚫 À éviter :
   ❌ Noms d'une lettre (sauf i, j, k dans les boucles)
   ❌ Mélanger les conventions (camelCase + snake_case)
   ❌ Caractères spéciaux ou accents
"""

print(style_guide)
