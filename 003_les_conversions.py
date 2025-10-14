"""
======================================================================
LES CONVERSIONS DE TYPES EN PYTHON - GUIDE COMPLET
======================================================================

🔄 Les conversions permettent de changer le type d'une donnée.
C'est essentiel quand on travaille avec des inputs utilisateur,
des fichiers, ou quand on mélange différents types de données.
"""

print("=" * 70)
print("LES CONVERSIONS DE TYPES EN PYTHON - GUIDE COMPLET")
print("=" * 70)

print("\n" + "=" * 50)
print("1. CONCEPT DE BASE : POURQUOI CONVERTIR ?")
print("=" * 50)

# 🎯 Exemple concret : input() retourne TOUJOURS une chaîne
print("🎯 PROBLÈME COURANT :")
print("   input() retourne toujours une chaîne, même pour les nombres")
print()

# Simulation d'un input utilisateur
age_saisi = "25"  # Simule input("Quel est votre âge ?")
print(f"   Age saisi : {age_saisi}")
print(f"   Type : {type(age_saisi)}")
print(f"   Est-ce un nombre ? Non, c'est du texte !")

# Pour faire des calculs, il faut convertir
age_numerique = int(age_saisi)
age_dans_10_ans = age_numerique + 10
print(f"   Après conversion : {age_numerique} (type: {type(age_numerique)})")
print(f"   Dans 10 ans : {age_dans_10_ans} ans")

print("\n💡 ANALOGIE - Les conversions comme des traducteurs :")
print("""
    TEXTE "123"  →  [TRADUCTEUR int()]  →  NOMBRE 123
    NOMBRE 45    →  [TRADUCTEUR str()]  →  TEXTE "45"
    TEXTE "3.14" →  [TRADUCTEUR float()] → NOMBRE 3.14
""")

print("\n" + "=" * 50)
print("2. CONVERSIONS VERS LES NOMBRES (int, float)")
print("=" * 50)

print("\n🔢 CONVERSION VERS ENTIER - int()")
print("-" * 30)

# Exemple de base : convertir une chaîne en nombre entier
# int('123') # 123
ma_variable_entiere = "123"
print(
    f"Avant conversion : '{ma_variable_entiere}' (type: {type(ma_variable_entiere)})")

# convertir la chaine de caractères en nombre entier
ma_variable_entiere = int(ma_variable_entiere)
print(
    f"Après conversion : {ma_variable_entiere} (type: {type(ma_variable_entiere)})")

# 💡 La fonction type() renvoie la classe de l'objet, c'est-à-dire son type en tant qu'objet Python.

# Float vers entier (ATTENTION : perte de précision)
nombre_decimal = 3.7
nombre_tronque = int(nombre_decimal)
print(f"Float vers int : {nombre_decimal} → {nombre_tronque} (TRONCATURE !)")

# Booléen vers entier
print(f"True → {int(True)}")
print(f"False → {int(False)}")

print("\n🔢 CONVERSION VERS FLOTTANT - float()")
print("-" * 35)

# Les autres conversions
# convertir une chaîne en nombre flottant
ma_variable_flottante = "123.456"
print(
    f"Avant : '{ma_variable_flottante}' (type: {type(ma_variable_flottante)})")
ma_variable_flottante = float(ma_variable_flottante)
print(f"Après : {ma_variable_flottante} (type: {type(ma_variable_flottante)})")

# Entier vers float
entier = 42
flottant = float(entier)
print(f"Int vers float : {entier} → {flottant}")

print("\n⚠️ ERREURS COURANTES À ÉVITER :")
print("   ❌ int('12.5')     # ERREUR ! Utiliser float() d'abord")
print("   ❌ int('abc')      # ERREUR ! Texte non numérique")
print("   ❌ float('hello')  # ERREUR ! Texte non numérique")

print("\n" + "=" * 50)
print("3. CONVERSIONS VERS LE TEXTE - str()")
print("=" * 50)

print("\n📝 TOUT PEUT DEVENIR DU TEXTE")
print("-" * 25)

# convertir un nombre entier en chaîne de caractères
ma_variable_entiere = 123
print(f"Entier → Texte : {ma_variable_entiere} → '{str(ma_variable_entiere)}'")
ma_variable_entiere = str(ma_variable_entiere)

# convertir un nombre flottant en chaîne de caractères
ma_variable_flottante = 123.456
print(
    f"Float → Texte : {ma_variable_flottante} → '{str(ma_variable_flottante)}'")
ma_variable_flottante = str(ma_variable_flottante)

# convertir un booléen en chaîne de caractères
ma_variable_booleenne = True
print(
    f"Boolean → Texte : {ma_variable_booleenne} → '{str(ma_variable_booleenne)}'")
ma_variable_booleenne = str(ma_variable_booleenne)

print("\n💡 USAGE PRATIQUE - Concaténation")
nom = "Alice"
age = 25
# Sans conversion : ERREUR !
# message = "Bonjour " + nom + ", vous avez " + age + " ans"  # ❌
# Avec conversion : OK !
message = "Bonjour " + nom + ", vous avez " + str(age) + " ans"
print(f"Message : {message}")

# Méthode moderne (f-strings, plus lisible)
message_moderne = f"Bonjour {nom}, vous avez {age} ans"
print(f"Avec f-string : {message_moderne}")
print("\n" + "=" * 50)
print("4. CONVERSIONS VERS BOOLÉEN - bool()")
print("=" * 50)

print("\n🔍 RÈGLES DE CONVERSION VERS bool()")
print("-" * 35)

print("✅ VALEURS 'VRAIES' (True) :")
# convertir une chaîne de caractères en booléen
ma_variable_chaine = "True"
ma_variable_booleenne = bool(ma_variable_chaine)
print(f"   bool('{ma_variable_chaine}') = {ma_variable_booleenne}  # True, car la chaîne n'est pas vide")

valeurs_vraies = [1, -1, 42, 3.14, "hello", [1, 2], {"a": 1}]
for valeur in valeurs_vraies:
    print(f"   bool({repr(valeur)}) = {bool(valeur)}")

print("\n❌ VALEURS 'FAUSSES' (False) :")
# convertir une chaîne vide en booléen
ma_variable_chaine_vide = ""
ma_variable_booleenne_vide = bool(ma_variable_chaine_vide)
print(f"   bool('{ma_variable_chaine_vide}') = {ma_variable_booleenne_vide}  # False, car la chaîne est vide")

# convertir un nombre entier en booléen
ma_variable_entiere = 0
ma_variable_booleenne = bool(ma_variable_entiere)
print(f"   bool({ma_variable_entiere}) = {ma_variable_booleenne}  # False, car 0 est considéré comme faux")

# convertir un nombre flottant en booléen
ma_variable_flottante = 0.0
ma_variable_booleenne_flottante = bool(ma_variable_flottante)
print(f"   bool({ma_variable_flottante}) = {ma_variable_booleenne_flottante}  # False, car 0.0 est considéré comme faux")

valeurs_fausses = [0, 0.0, "", [], {}, None]
for valeur in valeurs_fausses:
    print(f"   bool({repr(valeur)}) = {bool(valeur)}")

print("\n✅ EXEMPLES POSITIFS :")
# convertir un nombre entier non nul en booléen
ma_variable_entiere_non_nul = 42
ma_variable_booleenne_non_nul = bool(ma_variable_entiere_non_nul)
print(f"   bool({ma_variable_entiere_non_nul}) = {ma_variable_booleenne_non_nul}  # True, car tout nombre entier non nul est considéré comme vrai")

# convertir un nombre flottant non nul en booléen
ma_variable_flottante_non_nul = 3.14
ma_variable_booleenne_flottante_non_nul = bool(ma_variable_flottante_non_nul)
print(f"   bool({ma_variable_flottante_non_nul}) = {ma_variable_booleenne_flottante_non_nul}  # True, car tout nombre flottant non nul est considéré comme vrai")

print("\n💡 MÉMO - Valeurs 'fausses' en Python :")
print("""
   • 0 (zéro entier)
   • 0.0 (zéro flottant)  
   • "" (chaîne vide)
   • [] (liste vide)
   • {} (dictionnaire vide)
   • None (valeur nulle)
   • False (évidemment)
   
   ⚠️ PIÈGE : "False" (texte) = True car c'est une chaîne non vide !
""")

# Démonstration du piège
texte_false = "False"
print(f"bool('{texte_false}') = {bool(texte_false)} (piège !)")

print("\n" + "=" * 50)
print("5. CONVERSIONS AVANCÉES ET CAS PARTICULIERS")
print("=" * 50)

print("\n🎯 CONVERSION DE LISTES")
print("-" * 20)

# convertir une liste en chaîne de caractères
ma_liste = [1, 2, 3]
ma_liste_chaine = str(ma_liste)
print(f"Liste → Texte : {ma_liste} → '{ma_liste_chaine}'")

# Liste de chaînes vers liste de nombres
liste_textes = ["1", "2", "3", "4", "5"]
liste_nombres = [int(x) for x in liste_textes]
print(f"Textes : {liste_textes}")
print(f"Nombres : {liste_nombres}")

# Chaîne vers liste de caractères
phrase = "Python"
caracteres = list(phrase)
print(f"Phrase : '{phrase}'")
print(f"Caractères : {caracteres}")

print("\n🎯 CONVERSION DE NOMBRES AVEC BASES")
print("-" * 35)

# Nombres en différentes bases
nombre_decimal = 42
print(f"Décimal : {nombre_decimal}")
print(f"Binaire : {bin(nombre_decimal)}")
print(f"Hexadécimal : {hex(nombre_decimal)}")
print(f"Octal : {oct(nombre_decimal)}")

# Conversion depuis d'autres bases
binaire = "101010"
decimal_depuis_binaire = int(binaire, 2)
print(f"'{binaire}' en base 2 = {decimal_depuis_binaire} en décimal")

print("\n" + "=" * 50)
print("6. GESTION DES ERREURS DE CONVERSION")
print("=" * 50)

print("\n⚠️ CONVERSIONS QUI PEUVENT ÉCHOUER")
print("-" * 35)


def tenter_conversion(valeur, type_cible):
    """Fonction pour tester les conversions avec gestion d'erreur"""
    try:
        if type_cible == "int":
            resultat = int(valeur)
        elif type_cible == "float":
            resultat = float(valeur)
        else:
            resultat = type_cible(valeur)

        print(f"✅ {type_cible}('{valeur}') = {resultat}")
        return resultat
    except ValueError as e:
        print(f"❌ {type_cible}('{valeur}') → ERREUR : Conversion impossible")
        return None


# Tests de conversions
print("Tests de conversions sûres :")
tenter_conversion("123", "int")
tenter_conversion("12.5", "float")
tenter_conversion("hello", "int")
tenter_conversion("12.5", "int")

print("\n💡 SOLUTION : Validation avant conversion")


def convertir_securise(texte):
    """Conversion sécurisée avec validation"""
    if texte.isdigit():
        return int(texte)
    elif texte.replace(".", "").replace("-", "").isdigit():
        return float(texte)
    else:
        return texte  # Garder comme texte


# Tests de conversion sécurisée
valeurs_test = ["123", "12.5", "-42", "hello", "3.14159"]
print("\nConversions sécurisées :")
for valeur in valeurs_test:
    resultat = convertir_securise(valeur)
    print(f"'{valeur}' → {resultat} (type: {type(resultat).__name__})")

print("\n" + "=" * 50)
print("7. TABLEAU RÉCAPITULATIF DES CONVERSIONS")
print("=" * 50)

print("\n📊 GUIDE DE CONVERSION RAPIDE")
print("-" * 30)

conversions = [
    ["DE", "VERS", "FONCTION", "EXEMPLE"],
    ["str", "int", "int()", "'123' → 123"],
    ["str", "float", "float()", "'12.5' → 12.5"],
    ["str", "bool", "bool()", "'hello' → True"],
    ["int", "str", "str()", "123 → '123'"],
    ["int", "float", "float()", "42 → 42.0"],
    ["int", "bool", "bool()", "0 → False, autres → True"],
    ["float", "str", "str()", "3.14 → '3.14'"],
    ["float", "int", "int()", "3.7 → 3 (troncature)"],
    ["float", "bool", "bool()", "0.0 → False, autres → True"],
    ["bool", "str", "str()", "True → 'True'"],
    ["bool", "int", "int()", "True → 1, False → 0"],
    ["bool", "float", "float()", "True → 1.0, False → 0.0"],
]

for ligne in conversions:
    print(f"{ligne[0]:<8} {ligne[1]:<8} {ligne[2]:<10} {ligne[3]}")

print("""
🎯 POINTS CLÉS À RETENIR :

1. 🔄 CONVERSIONS DE BASE :
   • int() : Convertit vers entier
   • float() : Convertit vers nombre décimal  
   • str() : Convertit vers texte
   • bool() : Convertit vers booléen

2. ⚠️ PIÈGES À ÉVITER :
   • input() retourne TOUJOURS du texte
   • int() tronque les décimales (3.7 → 3)
   • Chaînes non-vides = True (même "False" !)
   • Vérifier avant de convertir

3. 🛡️ CONVERSION SÉCURISÉE :
   • Utiliser try/except
   • Vérifier avec .isdigit()
   • Valider les données utilisateur

4. 💡 BONNES PRATIQUES :
   • F-strings au lieu de concaténation
   • isinstance() pour vérifier les types
   • Documentation des conversions
   • Gestion des cas d'erreur

5. 🎨 CONVERSIONS AVANCÉES :
   • Bases numériques (bin, hex, oct)
   • List comprehensions pour listes
   • Fonctions personnalisées de validation

✅ FORMULE MAGIQUE pour débuter :
   input() → int()/float() → calculs → str() → affichage

🎉 Félicitations ! Vous maîtrisez les conversions Python !
💡 Prochaine étape : Les opérateurs et les calculs !
📚 Continuez avec 004_les_fonctions_str.py
""")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE")
print("=" * 70)
