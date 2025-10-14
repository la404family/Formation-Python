"""
======================================================================
LES NOMBRES DÉCIMAUX (FLOAT) EN PYTHON - GUIDE COMPLET
======================================================================

🔢 Les nombres à virgule flottante (float) permettent de représenter
les nombres décimaux. Ce guide couvre leur utilisation, leurs pièges,
l'arrondi, la précision, et toutes les techniques avancées !

"""

from decimal import Decimal, getcontext
import math
print("=" * 70)
print("LES NOMBRES DÉCIMAUX (FLOAT) EN PYTHON - GUIDE COMPLET")
print("=" * 70)

print("\n" + "=" * 50)
print("1. CONCEPT DE BASE : QU'EST-CE QU'UN FLOAT ?")
print("=" * 50)

# 🔢 Les fonctions de manipulation de nombres à virgule flottante
variable_float = 3.14156456489
print(f"🔢 Nombre décimal d'exemple : {variable_float}")
print(f"   Type : {type(variable_float)}")
print(f"   Taille en mémoire : {variable_float.__sizeof__()} bytes")

print("\n💡 ANALOGIE - Les floats comme des mesures :")
print("""
    Entiers : 1, 2, 3, 42 (comptage exact)
    Floats : 1.5, 3.14, 2.718, 0.001 (mesures approximatives)
    
    ⚠️ IMPORTANT : Les floats sont des APPROXIMATIONS !
    Ils ne peuvent pas toujours représenter exactement tous les nombres décimaux.
""")

# Démonstration du problème de précision
print(f"🚨 PIÈGE DE PRÉCISION :")
resultat = 0.1 + 0.2
print(f"   0.1 + 0.2 = {resultat}")
print(f"   Est-ce égal à 0.3 ? {resultat == 0.3}")
print(f"   Représentation exacte : {resultat:.17f}")

print("\n🎯 DIFFÉRENTS TYPES DE NOMBRES DÉCIMAUX")
exemples_floats = [3.14, -2.7, 0.0, 1e5, 1e-5, float('inf'), float('-inf')]
for exemple in exemples_floats:
    if str(exemple) not in ['inf', '-inf', 'nan']:
        print(f"   {exemple} → Type: {type(exemple).__name__}")
    else:
        print(f"   {exemple} → Valeur spéciale")

print("\n" + "=" * 50)
print("2. CRÉATION ET CONVERSION")
print("=" * 50)

print("\n🔄 DIFFÉRENTES FAÇONS DE CRÉER DES FLOATS")
print("-" * 40)

# Création directe
print("✅ Création directe :")
decimaux_directs = [3.14, -2.5, 0.001, 42.0]
for val in decimaux_directs:
    print(f"   {val}")

# Notation scientifique
print("✅ Notation scientifique :")
scientifiques = [1e3, 1.5e-4, 2.3e+2, 6.022e23]
for val in scientifiques:
    print(f"   {val} ({val:.2e})")

# Conversion depuis d'autres types
print("✅ Conversion depuis chaînes :")
chaines_a_convertir = ["3.14", "-2.7", "1e5", ".5", "42"]
for chaine in chaines_a_convertir:
    try:
        resultat = float(chaine)
        print(f"   float('{chaine}') = {resultat}")
    except ValueError as e:
        print(f"   float('{chaine}') → ERREUR : {e}")

# Conversion depuis entiers
print("✅ Conversion depuis entiers :")
entiers = [42, -5, 0]
for entier in entiers:
    resultat = float(entier)
    print(f"   float({entier}) = {resultat}")

print("\n" + "=" * 50)
print("3. ARRONDI ET PRÉCISION")
print("=" * 50)

print("\n🎯 FONCTION round() - ARRONDI INTELLIGENT")
print("-" * 35)

# Arrondir la valeur à différentes précisions
nombre_test = 3.14156456489
print(f"🔢 Nombre original : {nombre_test}")

precisions = [0, 1, 2, 3, 4, 5]
for precision in precisions:
    variable_arrondie = round(nombre_test, precision)
    print(f"   round({nombre_test}, {precision}) = {variable_arrondie}")

print("\n🎯 AUTRES TECHNIQUES D'ARRONDI")
print("-" * 30)


nombres_arrondi = [3.2, 3.7, -2.1, -2.8, 3.5, 4.5]
print("📊 Comparaison des méthodes d'arrondi :")
print(f"{'Nombre':<8} {'round()':<8} {'floor()':<8} {'ceil()':<8} {'trunc()':<8}")
print("-" * 40)

for nombre in nombres_arrondi:
    print(f"{nombre:<8} {round(nombre):<8} {math.floor(nombre):<8} {math.ceil(nombre):<8} {math.trunc(nombre):<8}")

print("\n💡 EXPLICATIONS :")
print("   • round() : Arrondi au plus proche (banker's rounding)")
print("   • floor() : Arrondi vers le bas (plancher)")
print("   • ceil() : Arrondi vers le haut (plafond)")
print("   • trunc() : Supprime la partie décimale (troncature)")

print("\n⚠️ PIÈGE DU BANKER'S ROUNDING")
print("-" * 30)
valeurs_ambigues = [0.5, 1.5, 2.5, 3.5, 4.5]
print("   Banker's rounding (arrondi vers le pair) :")
for val in valeurs_ambigues:
    print(f"   round({val}) = {round(val)}")

print("\n" + "=" * 50)
print("4. FORMATAGE ET AFFICHAGE")
print("=" * 50)

print("\n📐 FORMATAGE AVEC F-STRINGS")
print("-" * 26)

# Convertir la valeur en chaîne de caractères
variable_float_str = str(variable_float)
print(
    f"✅ Conversion en chaîne : str({variable_float}) = '{variable_float_str}'")

# Formatage avec différentes précisions
pi = 3.14159265359
print(f"\n🎨 Formatage de π = {pi} :")
print(f"   2 décimales : {pi:.2f}")
print(f"   4 décimales : {pi:.4f}")
print(f"   6 décimales : {pi:.6f}")
print(f"   Notation scientifique : {pi:.2e}")
print(f"   Notation avec % : {pi:.2%}")

print("\n✅ FORMATAGE AVANCÉ")
print("-" * 20)

grand_decimal = 1234567.89012
print(f"🔢 Grand nombre : {grand_decimal}")
print(f"   Avec séparateurs : {grand_decimal:,.2f}")
print(f"   Largeur fixe (15) : {grand_decimal:15.2f}")
print(f"   Aligné à gauche : {grand_decimal:<15.2f}")
print(f"   Aligné à droite : {grand_decimal:>15.2f}")
print(f"   Centré : {grand_decimal:^15.2f}")
print(f"   Avec zéros : {grand_decimal:015.2f}")

print("\n🎯 FORMATAGE SPÉCIALISÉ")
print("-" * 23)

# Pourcentages
taux = 0.1574
print(f"💹 Taux : {taux} = {taux:.1%} = {taux:.2%}")

# Devises
prix = 29.99
print(f"💰 Prix : {prix:.2f}€")

# Coordonnées GPS
latitude, longitude = 48.8566, 2.3522
print(f"📍 Coordonnées : {latitude:.4f}°N, {longitude:.4f}°E")
print("\n" + "=" * 50)
print("5. VÉRIFICATIONS ET TESTS")
print("=" * 50)

print("\n✅ TESTS DE TYPE")
print("-" * 15)

# Vérifier si la valeur est un nombre à virgule flottante
est_float = isinstance(variable_float, float)
print(f"📊 Analyse de {variable_float} :")
print(f"   isinstance(x, float) : {est_float}")

# Vérifier si la valeur est un entier
est_entier = isinstance(variable_float, int)
print(f"   isinstance(x, int) : {est_entier}")

# Vérifier si la valeur est un nombre
est_nombre = isinstance(variable_float, (int, float))
print(f"   isinstance(x, (int, float)) : {est_nombre}")

# Vérifier si la valeur est un nombre entier (valeur)
est_entier_valeur = variable_float.is_integer()
print(f"   x.is_integer() : {est_entier_valeur}")

# Tests avec différents types de nombres
print(f"\n🔍 Tests sur différents nombres :")
test_nombres = [3.0, 3.5, -2.0, 0.0, 1e5]
for nombre in test_nombres:
    print(f"   {nombre} → is_integer(): {nombre.is_integer()}")

print("\n🎯 TESTS DE VALEUR ET SIGNE")
print("-" * 26)

# Vérifier si la valeur est un nombre positif
est_positif = variable_float > 0
print(f"📈 Tests de signe pour {variable_float} :")
print(f"   Positif (> 0) : {est_positif}")

# Vérifier si la valeur est un nombre négatif
est_negatif = variable_float < 0
print(f"   Négatif (< 0) : {est_negatif}")

# Vérifier si la valeur est zéro
est_zero = variable_float == 0
print(f"   Zéro (== 0) : {est_zero}")

print("\n⚠️ COMPARAISON SÉCURISÉE DES FLOATS")
print("-" * 35)

# Problème de la comparaison directe
a, b = 0.1 + 0.2, 0.3
print(f"🚨 Problème classique :")
print(f"   0.1 + 0.2 = {a}")
print(f"   0.3 = {b}")
print(f"   Sont-ils égaux ? {a == b}")

# Solution avec tolérance


def floats_egaux(a, b, tolerance=1e-9):
    return abs(a - b) < tolerance


print(f"✅ Solution avec tolérance :")
print(f"   abs({a} - {b}) < 1e-9 : {floats_egaux(a, b)}")

# Tests de seuils
# Vérifier si la valeur est inférieure à un seuil
seuil = 5.0
est_inferieur_seuil = variable_float < seuil
print(f"\n📊 Tests de seuils pour {variable_float} :")
print(f"   < {seuil} : {est_inferieur_seuil}")

# Vérifier si la valeur est supérieure à un seuil
est_superieur_seuil = variable_float > seuil
print(f"   > {seuil} : {est_superieur_seuil}")

# Test de plage
plage_min, plage_max = 1.0, 10.0
dans_plage = plage_min <= variable_float <= plage_max
print(f"   Dans [{plage_min}, {plage_max}] : {dans_plage}")

print("\n" + "=" * 50)
print("6. OPÉRATIONS MATHÉMATIQUES AVANCÉES")
print("=" * 50)

print("\n🧮 FONCTIONS MATHÉMATIQUES")
print("-" * 25)


nombre_math = 2.7182818  # Approximation de e
print(f"🔢 Avec le nombre {nombre_math} :")

# Fonctions de base
print(f"   Valeur absolue : abs({nombre_math}) = {abs(nombre_math)}")
print(f"   Racine carrée : √{nombre_math} = {math.sqrt(nombre_math):.4f}")
print(f"   Puissance : {nombre_math}² = {nombre_math**2:.4f}")

# Fonctions exponentielles et logarithmiques
print(f"   Exponentielle : e^{nombre_math} = {math.exp(nombre_math):.4f}")
print(
    f"   Logarithme naturel : ln({nombre_math}) = {math.log(nombre_math):.4f}")
print(
    f"   Logarithme base 10 : log₁₀({nombre_math}) = {math.log10(nombre_math):.4f}")

# Fonctions trigonométriques
angle = math.pi / 4  # 45 degrés en radians
print(f"\n🔺 Fonctions trigonométriques (angle = π/4 = 45°) :")
print(f"   sin(π/4) = {math.sin(angle):.4f}")
print(f"   cos(π/4) = {math.cos(angle):.4f}")
print(f"   tan(π/4) = {math.tan(angle):.4f}")

# Conversions radians/degrés
degres = 45
radians = math.radians(degres)
print(f"   {degres}° = {radians:.4f} radians")
print(f"   {radians:.4f} radians = {math.degrees(radians)}°")

print("\n🎯 CONSTANTES MATHÉMATIQUES")
print("-" * 27)

print(f"   π (pi) = {math.pi:.6f}")
print(f"   e (euler) = {math.e:.6f}")
print(f"   τ (tau = 2π) = {math.tau:.6f}")
print(f"   φ (golden ratio) = {(1 + math.sqrt(5)) / 2:.6f}")

print("\n" + "=" * 50)
print("7. VALEURS SPÉCIALES ET CAS LIMITES")
print("=" * 50)

print("\n🚨 VALEURS SPÉCIALES")
print("-" * 20)

# Valeurs spéciales
infini_positif = float('inf')
infini_negatif = float('-inf')
pas_un_nombre = float('nan')

print(f"   Infini positif : {infini_positif}")
print(f"   Infini négatif : {infini_negatif}")
print(f"   Not a Number : {pas_un_nombre}")

# Tests sur les valeurs spéciales
print(f"\n🔍 Tests sur les valeurs spéciales :")
print(f"   math.isinf({infini_positif}) = {math.isinf(infini_positif)}")
print(f"   math.isinf({infini_negatif}) = {math.isinf(infini_negatif)}")
print(f"   math.isnan({pas_un_nombre}) = {math.isnan(pas_un_nombre)}")
print(f"   math.isfinite(3.14) = {math.isfinite(3.14)}")

# Opérations qui produisent des valeurs spéciales
print(f"\n⚠️ Opérations dangereuses :")
try:
    division_par_zero = 1.0 / 0.0
except ZeroDivisionError:
    print(f"   1.0 / 0.0 → ZeroDivisionError")

print(f"   float('inf') / float('inf') = {float('inf') / float('inf')}")
print(f"   0.0 * float('inf') = {0.0 * float('inf')}")
print(f"   math.sqrt(-1) → ", end="")
try:
    print(math.sqrt(-1))
except ValueError:
    print("ValueError (nombre négatif)")

print("\n" + "=" * 50)
print("8. TECHNIQUES AVANCÉES")
print("=" * 50)

print("\n🎯 GESTION DE LA PRÉCISION")
print("-" * 25)


# Problème avec les floats standards
print("🚨 Problème de précision des floats :")
somme_float = 0.0
for i in range(10):
    somme_float += 0.1
print(f"   0.1 ajouté 10 fois = {somme_float}")
print(f"   Est-ce égal à 1.0 ? {somme_float == 1.0}")

# Solution avec Decimal
print("✅ Solution avec Decimal :")
getcontext().prec = 50  # 50 chiffres de précision
somme_decimal = Decimal('0')
for i in range(10):
    somme_decimal += Decimal('0.1')
print(f"   0.1 ajouté 10 fois = {somme_decimal}")
print(f"   Est-ce égal à 1 ? {somme_decimal == Decimal('1')}")

print("\n🔄 CONVERSIONS COMPLEXES")
print("-" * 23)

# Conversion de chaînes avec gestion d'erreurs


def convertir_float_securise(chaine):
    try:
        return float(chaine)
    except ValueError:
        return None


chaines_test = ["3.14", "abc", "1e5", "", "inf", "-inf", "nan"]
print("🔍 Conversions sécurisées :")
for chaine in chaines_test:
    resultat = convertir_float_securise(chaine)
    print(f"   '{chaine}' → {resultat}")

print("\n🎨 ALGORITHMES UTILES")
print("-" * 20)


def moyenne(nombres):
    """Calcule la moyenne d'une liste de nombres"""
    if not nombres:
        return 0.0
    return sum(nombres) / len(nombres)


def ecart_type(nombres):
    """Calcule l'écart-type d'une liste de nombres"""
    if len(nombres) < 2:
        return 0.0
    moy = moyenne(nombres)
    variance = sum((x - moy) ** 2 for x in nombres) / (len(nombres) - 1)
    return math.sqrt(variance)


# Tests des algorithmes
donnees = [1.5, 2.3, 1.8, 2.1, 1.9, 2.4, 1.7, 2.0]
print(f"📊 Données : {donnees}")
print(f"   Moyenne : {moyenne(donnees):.3f}")
print(f"   Écart-type : {ecart_type(donnees):.3f}")
print(f"   Min : {min(donnees)}")
print(f"   Max : {max(donnees)}")

print("\n" + "=" * 50)
print("10. TABLEAU RÉCAPITULATIF")
print("=" * 50)

print("""
📊 GUIDE DE RÉFÉRENCE RAPIDE

🔢 CRÉATION ET CONVERSION :
   • float(x) : Conversion vers float
   • Notation scientifique : 1e5, 2.3e-4
   • Valeurs spéciales : float('inf'), float('nan')

🎯 ARRONDI ET PRÉCISION :
   • round(x, n) : Arrondi à n décimales
   • math.floor() / math.ceil() : Arrondi inf/sup
   • math.trunc() : Suppression décimales

📐 FORMATAGE :
   • f"{x:.2f}" : 2 décimales
   • f"{x:.2e}" : Notation scientifique
   • f"{x:.2%}" : Pourcentage
   • f"{x:,.2f}" : Séparateurs de milliers

✅ VÉRIFICATIONS :
   • isinstance(x, float) : Test de type
   • x.is_integer() : Valeur entière ?
   • math.isfinite() / math.isinf() / math.isnan()

🧮 FONCTIONS MATHÉMATIQUES :
   • math.sqrt(), math.pow() : Racine, puissance
   • math.exp(), math.log() : Exponentielle, logarithme
   • math.sin(), math.cos(), math.tan() : Trigonométrie

⚠️ PIÈGES À ÉVITER :
   • 0.1 + 0.2 != 0.3 (problème de précision)
   • Comparaison directe : utiliser tolérance
   • Division par zéro : float('inf')
""")

print("\n" + "=" * 50)
print("11. RÉSUMÉ FINAL")
print("=" * 50)

print("""
🎯 POINTS CLÉS À RETENIR :

1. 🔢 NATURE DES FLOATS :
   • Représentation approximative des décimaux
   • Problèmes de précision inhérents
   • Utilisez Decimal pour la précision exacte

2. 🎯 ARRONDI INTELLIGENT :
   • round() pour l'arrondi standard
   • floor() / ceil() pour direction forcée
   • Attention au banker's rounding (.5)

3. 📐 FORMATAGE PROFESSIONNEL :
   • F-strings avec spécificateurs : :.2f, :.2e
   • Séparateurs de milliers : :,
   • Alignement et largeur fixe

4. ✅ COMPARAISONS SÉCURISÉES :
   • Jamais == pour comparer des floats
   • Toujours utiliser une tolérance
   • abs(a - b) < epsilon

5. 🧮 FONCTIONS MATHÉMATIQUES :
   • Module math pour toutes les fonctions
   • Constantes : math.pi, math.e
   • Gestion des valeurs spéciales (inf, nan)

💡 FORMULE MAGIQUE pour les floats :
   Créer → Calculer → Arrondir → Formater → Comparer avec tolérance

🎉 Félicitations ! Vous maîtrisez les nombres décimaux Python !
💡 Prochaine étape : Le module math complet !
📚 Continuez avec 007_le_module_math.py
""")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE - NOMBRES DÉCIMAUX MAÎTRISÉS !")
print("=" * 70)
