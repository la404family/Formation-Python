"""
======================================================================
LE MODULE MATH EN PYTHON - GUIDE COMPLET
======================================================================

🧮 Le module math est la boîte à outils mathématique de Python.
Il contient toutes les fonctions mathématiques avancées : trigonométrie,
logarithmes, racines, constantes, et bien plus encore !

"""

import math

print("=" * 70)
print("LE MODULE MATH EN PYTHON - GUIDE COMPLET")
print("=" * 70)

print("\n" + "=" * 50)
print("1. INTRODUCTION : MATH VS OPÉRATEURS DE BASE")
print("=" * 50)

print("\n🧮 OPÉRATEURS ARITHMÉTIQUES INTÉGRÉS")
print("-" * 35)

# Les opérateurs mathématiques de base (sans import)
print("✅ Opérateurs de base (intégrés à Python) :")
# Addition
addition = 5 + 3
print(f"   Addition : 5 + 3 = {addition}")
# Soustraction
soustraction = 10 - 4
print(f"   Soustraction : 10 - 4 = {soustraction}")
# Multiplication
multiplication = 6 * 7
print(f"   Multiplication : 6 * 7 = {multiplication}")
# Division (elle renvoie un float)
division = 20 / 4
print(f"   Division : 20 / 4 = {division}")
# Division entière
division_entiere = 20 // 3
print(f"   Division entière : 20 // 3 = {division_entiere}")
# Modulo
modulo = 20 % 3
print(f"   Modulo : 20 % 3 = {modulo}")
# Puissance
puissance = 2 ** 3
print(f"   Puissance : 2 ** 3 = {puissance}")

print("\n🔬 POURQUOI LE MODULE MATH ?")
print("-" * 27)

print("""
💡 Les opérateurs de base suffisent pour :
   • Calculs simples (+, -, *, /, //, %, **)
   • Opérations de tous les jours

🧮 Le module math apporte :
   • Fonctions trigonométriques (sin, cos, tan)
   • Logarithmes et exponentielles
   • Racines et puissances avancées
   • Constantes mathématiques précises
   • Fonctions spécialisées (factoriel, combinaisons)
""")

print("\n" + "=" * 50)
print("2. CONSTANTES MATHÉMATIQUES")
print("=" * 50)

print("\n🎯 CONSTANTES ESSENTIELLES")
print("-" * 26)

# Présentation des fonctions du module math
variable_float = 3.14658468
variable_int = 427

print("📊 Constantes disponibles dans math :")
# Afficher la valeur de pi
print(f"   π (pi) = {math.pi:.15f}")
print(f"   Utilisation : circumférence = 2 * π * rayon")

# Afficher la valeur de e
print(f"   e (euler) = {math.e:.15f}")
print(f"   Utilisation : croissance exponentielle")

# Autres constantes importantes
print(f"   τ (tau = 2π) = {math.tau:.15f}")
print(f"   Utilisation : angle complet en radians")

print(f"   ∞ (infini) = {math.inf}")
print(f"   -∞ (moins infini) = {-math.inf}")
print(f"   NaN (Not a Number) = {math.nan}")

print("\n💡 USAGE PRATIQUE DES CONSTANTES")
print("-" * 32)

# Exemples concrets
rayon = 5
circumference = 2 * math.pi * rayon
aire = math.pi * rayon ** 2
print(f"🔵 Cercle de rayon {rayon} :")
print(f"   Circonférence : 2πr = {circumference:.2f}")
print(f"   Aire : πr² = {aire:.2f}")

# Croissance exponentielle
capital_initial = 1000
taux = 0.05
temps = 10
capital_final = capital_initial * math.e ** (taux * temps)
print(f"📈 Croissance continue :")
print(f"   Capital après {temps} ans : {capital_final:.2f}€")
print("\n" + "=" * 50)
print("3. FONCTIONS D'ARRONDI ET DE TRONCATURE")
print("=" * 50)

print("\n📐 ARRONDI DIRECTIONNEL")
print("-" * 23)

nombre_test = 3.14658468
print(f"🔢 Nombre de test : {nombre_test}")

# Arrondir la valeur à l'entier supérieur
variable_arrondie_haut = math.ceil(nombre_test)
print(f"   ceil({nombre_test}) = {variable_arrondie_haut} (plafond)")

# Arrondir la valeur à l'entier inférieur
variable_arrondie_bas = math.floor(nombre_test)
print(f"   floor({nombre_test}) = {variable_arrondie_bas} (plancher)")

# Troncature (supprime la partie décimale)
variable_tronquee = math.trunc(nombre_test)
print(f"   trunc({nombre_test}) = {variable_tronquee} (troncature)")

# Comparaison avec round() intégré
variable_arrondie_round = round(nombre_test)
print(
    f"   round({nombre_test}) = {variable_arrondie_round} (arrondi classique)")

print("\n🎯 TESTS AVEC NOMBRES NÉGATIFS")
print("-" * 30)

nombres_negatifs = [-2.3, -2.7, -0.1, -0.9]
print(f"{'Nombre':<8} {'ceil':<6} {'floor':<6} {'trunc':<6} {'round':<6}")
print("-" * 35)
for n in nombres_negatifs:
    print(f"{n:<8} {math.ceil(n):<6} {math.floor(n):<6} {math.trunc(n):<6} {round(n):<6}")

print("\n💡 APPLICATIONS PRATIQUES")
print("-" * 25)

# Calcul de pages
articles_par_page = 10
total_articles = 47
pages_necessaires = math.ceil(total_articles / articles_par_page)
print(
    f"📄 Pagination : {total_articles} articles, {articles_par_page} par page")
print(f"   Pages nécessaires : {pages_necessaires}")

# Calcul de temps
duree_secondes = 125
minutes = math.floor(duree_secondes / 60)
secondes_restantes = duree_secondes % 60
print(
    f"⏱️ Conversion temps : {duree_secondes}s = {minutes}min {secondes_restantes}s")

print("\n" + "=" * 50)
print("4. PUISSANCES ET RACINES")
print("=" * 50)

print("\n🔋 FONCTIONS DE PUISSANCE")
print("-" * 25)

base = 2.5
exposant = 3.2
print(f"🔢 Base : {base}, Exposant : {exposant}")

# Calculer la puissance de la valeur
variable_puissance = math.pow(base, exposant)
print(f"   pow({base}, {exposant}) = {variable_puissance:.4f}")

# Comparaison avec l'opérateur **
puissance_operateur = base ** exposant
print(f"   {base} ** {exposant} = {puissance_operateur:.4f}")
print(
    f"   Identiques ? {abs(variable_puissance - puissance_operateur) < 1e-10}")

print("\n🌱 FONCTIONS DE RACINE")
print("-" * 22)

# Calculer la racine carrée de la valeur
nombre_racine = 16.0
variable_racine_carre = math.sqrt(nombre_racine)
print(f"   sqrt({nombre_racine}) = {variable_racine_carre}")

# Racine cubique (pow avec exposant fractionnaire)
racine_cubique = math.pow(27, 1/3)
print(f"   ∛27 = pow(27, 1/3) = {racine_cubique:.4f}")

# Racine n-ième
nombre = 32
racine_5 = math.pow(nombre, 1/5)
print(f"   ⁵√{nombre} = pow({nombre}, 1/5) = {racine_5:.4f}")

print("\n🎯 VÉRIFICATIONS ET TESTS")
print("-" * 24)

# Tests avec différents nombres
nombres_test = [4, 9, 16, 25, 100]
print("Vérification : (√x)² = x")
for n in nombres_test:
    racine = math.sqrt(n)
    verification = racine ** 2
    print(f"   √{n} = {racine:.1f}, ({racine:.1f})² = {verification:.1f}")

print("\n" + "=" * 50)
print("5. LOGARITHMES ET EXPONENTIELLES")
print("=" * 50)

print("\n📈 FONCTIONS EXPONENTIELLES")
print("-" * 27)

x = 2.0
print(f"🔢 Valeur : {x}")

# Exponentielle (e^x)
exp_x = math.exp(x)
print(f"   exp({x}) = e^{x} = {exp_x:.4f}")

# Puissances de 2 et 10
exp2_x = math.pow(2, x)
exp10_x = math.pow(10, x)
print(f"   2^{x} = {exp2_x:.4f}")
print(f"   10^{x} = {exp10_x:.4f}")

print("\n📉 FONCTIONS LOGARITHMIQUES")
print("-" * 27)

# Calculer le logarithme naturel de la valeur
variable_logarithme = math.log(variable_float)
print(
    f"   log({variable_float}) = ln({variable_float}) = {variable_logarithme:.4f}")

# Calculer le logarithme en base 10 de la valeur
variable_logarithme_base_10 = math.log10(variable_float)
print(f"   log10({variable_float}) = {variable_logarithme_base_10:.4f}")

# Logarithme en base 2
log2_val = math.log2(8)
print(f"   log2(8) = {log2_val:.1f}")

# Logarithme en base quelconque
log_base = math.log(1000, 10)  # log10(1000)
print(f"   log(1000, 10) = {log_base:.1f}")

print("\n🔄 PROPRIÉTÉS DES LOGARITHMES")
print("-" * 29)

# Vérification des propriétés
a, b = 8, 2
print(f"💡 Propriétés avec a = {a}, b = {b} :")
print(f"   log(a * b) = {math.log(a * b):.4f}")
print(f"   log(a) + log(b) = {math.log(a) + math.log(b):.4f}")
print(f"   log(a / b) = {math.log(a / b):.4f}")
print(f"   log(a) - log(b) = {math.log(a) - math.log(b):.4f}")

print("\n💰 APPLICATION : INTÉRÊTS COMPOSÉS")
print("-" * 33)

capital = 1000
taux = 0.05  # 5%
duree = 10
# Formule : A = P * e^(rt)
montant_continu = capital * math.exp(taux * duree)
print(f"   Capital initial : {capital}€")
print(f"   Taux : {taux*100}% par an")
print(f"   Durée : {duree} ans")
print(f"   Montant final (continu) : {montant_continu:.2f}€")

print("\n" + "=" * 50)
print("6. TRIGONOMÉTRIE")
print("=" * 50)

print("\n🔺 FONCTIONS TRIGONOMÉTRIQUES DE BASE")
print("-" * 37)

# Angles en radians
angle_rad = math.pi / 4  # 45 degrés
print(f"🔢 Angle : {angle_rad:.4f} radians = {math.degrees(angle_rad)}°")

# Calculer le sinus de la valeur
variable_sinus = math.sin(angle_rad)
print(f"   sin({angle_rad:.4f}) = {variable_sinus:.4f}")

# Calculer le cosinus de la valeur
variable_cosinus = math.cos(angle_rad)
print(f"   cos({angle_rad:.4f}) = {variable_cosinus:.4f}")

# Calculer la tangente de la valeur
variable_tangente = math.tan(angle_rad)
print(f"   tan({angle_rad:.4f}) = {variable_tangente:.4f}")

print("\n🔄 CONVERSIONS RADIANS/DEGRÉS")
print("-" * 31)

# Conversion degrés vers radians
degres = 90
radians = math.radians(degres)
print(f"   {degres}° = {radians:.4f} radians")

# Conversion radians vers degrés
radians_val = math.pi / 2
degres_val = math.degrees(radians_val)
print(f"   {radians_val:.4f} radians = {degres_val:.1f}°")

print("\n📊 TABLEAU TRIGONOMÉTRIQUE")
print("-" * 27)

angles_degres = [0, 30, 45, 60, 90, 180, 270, 360]
print(f"{'Degrés':<8} {'Radians':<8} {'sin':<8} {'cos':<8} {'tan':<8}")
print("-" * 45)

for deg in angles_degres:
    rad = math.radians(deg)
    sin_val = math.sin(rad)
    cos_val = math.cos(rad)

    # Gestion de la tangente pour 90° et 270°
    if abs(cos_val) < 1e-10:  # cos ≈ 0
        tan_str = "∞"
    else:
        tan_val = math.tan(rad)
        tan_str = f"{tan_val:.3f}"

    print(f"{deg:<8} {rad:<8.3f} {sin_val:<8.3f} {cos_val:<8.3f} {tan_str:<8}")

print("\n🔺 FONCTIONS TRIGONOMÉTRIQUES INVERSES")
print("-" * 38)

# Arcsinus, arccosinus, arctangente
valeur = 0.5
print(f"🔢 Valeur : {valeur}")
print(
    f"   arcsin({valeur}) = {math.asin(valeur):.4f} rad = {math.degrees(math.asin(valeur)):.1f}°")
print(
    f"   arccos({valeur}) = {math.acos(valeur):.4f} rad = {math.degrees(math.acos(valeur)):.1f}°")
print(
    f"   arctan({valeur}) = {math.atan(valeur):.4f} rad = {math.degrees(math.atan(valeur)):.1f}°")

# atan2 pour gestion des quadrants
x, y = 3, 4
angle_atan2 = math.atan2(y, x)
print(
    f"   atan2({y}, {x}) = {angle_atan2:.4f} rad = {math.degrees(angle_atan2):.1f}°")

print("\n" + "=" * 50)
print("7. FONCTIONS HYPERBOLIQUES")
print("=" * 50)

print("\n🌊 FONCTIONS HYPERBOLIQUES")
print("-" * 26)

x = 1.0
print(f"🔢 Valeur : {x}")

# Fonctions hyperboliques
sinh_x = math.sinh(x)
cosh_x = math.cosh(x)
tanh_x = math.tanh(x)

print(f"   sinh({x}) = {sinh_x:.4f}")
print(f"   cosh({x}) = {cosh_x:.4f}")
print(f"   tanh({x}) = {tanh_x:.4f}")

# Vérification de l'identité cosh²(x) - sinh²(x) = 1
identite = cosh_x**2 - sinh_x**2
print(f"   Vérification : cosh²({x}) - sinh²({x}) = {identite:.4f}")

# Fonctions hyperboliques inverses
print(f"   asinh({sinh_x:.4f}) = {math.asinh(sinh_x):.4f}")
print(f"   acosh({cosh_x:.4f}) = {math.acosh(cosh_x):.4f}")
print(f"   atanh({tanh_x:.4f}) = {math.atanh(tanh_x):.4f}")

print("\n" + "=" * 50)
print("8. FONCTIONS SPÉCIALISÉES")
print("=" * 50)

print("\n🔢 FACTORIELLE ET COMBINATOIRE")
print("-" * 30)

# Factorielle
n = 5
factorielle = math.factorial(n)
print(f"   {n}! = factorial({n}) = {factorielle}")

# Combinaisons et permutations
n, k = 10, 3
combinaisons = math.comb(n, k)
permutations = math.perm(n, k)
print(f"   C({n}, {k}) = {combinaisons}")
print(f"   P({n}, {k}) = {permutations}")

print("\n🎯 FONCTIONS DE DISTANCE")
print("-" * 25)

# Distance euclidienne
x1, y1 = 3, 4
distance = math.hypot(x1, y1)
print(f"   Distance origine à ({x1}, {y1}) = {distance:.4f}")

# Distance entre deux points
x2, y2 = 6, 8
distance_points = math.hypot(x2 - x1, y2 - y1)
print(f"   Distance ({x1}, {y1}) à ({x2}, {y2}) = {distance_points:.4f}")

print("\n✅ FONCTIONS DE VÉRIFICATION")
print("-" * 27)

# Tests sur différents nombres
valeurs_test = [1.5, float('inf'), float('-inf'), float('nan'), 0.0]
print(f"{'Valeur':<10} {'isfinite':<9} {'isinf':<6} {'isnan':<6}")
print("-" * 32)

for val in valeurs_test:
    finite = math.isfinite(val)
    inf = math.isinf(val)
    nan = math.isnan(val)
    print(f"{str(val):<10} {finite:<9} {inf:<6} {nan:<6}")

print("\n" + "=" * 50)
print("10. TABLEAU RÉCAPITULATIF")
print("=" * 50)

print("""
📊 GUIDE DE RÉFÉRENCE RAPIDE

🎯 CONSTANTES :
   • math.pi, math.e, math.tau
   • math.inf, math.nan

📐 ARRONDI :
   • math.ceil() : plafond
   • math.floor() : plancher  
   • math.trunc() : troncature

🔋 PUISSANCES ET RACINES :
   • math.pow(x, y) : x^y
   • math.sqrt(x) : racine carrée
   • x ** (1/n) : racine n-ième

📈 LOGARITHMES ET EXP :
   • math.exp(x) : e^x
   • math.log(x) : ln(x)
   • math.log10(x), math.log2(x)

🔺 TRIGONOMÉTRIE :
   • math.sin(), math.cos(), math.tan()
   • math.asin(), math.acos(), math.atan()
   • math.radians(), math.degrees()

🌊 HYPERBOLIQUES :
   • math.sinh(), math.cosh(), math.tanh()
   • math.asinh(), math.acosh(), math.atanh()

🔢 SPÉCIALISÉES :
   • math.factorial(n) : n!
   • math.comb(n, k), math.perm(n, k)
   • math.hypot(x, y) : distance
   • math.isfinite(), math.isinf(), math.isnan()
""")

print("\n" + "=" * 50)
print("11. RÉSUMÉ FINAL")
print("=" * 50)

print("""
🎯 POINTS CLÉS À RETENIR :

1. 🧮 IMPORT OBLIGATOIRE :
   • import math en début de fichier
   • Toutes les fonctions préfixées par math.
   • Constantes précises et standardisées

2. 📐 ARRONDI INTELLIGENT :
   • ceil() pour le plafond (vers +∞)
   • floor() pour le plancher (vers -∞)
   • trunc() pour supprimer les décimales

3. 🔋 PUISSANCES AVANCÉES :
   • pow() vs ** : pow() plus précis pour certains cas
   • sqrt() optimisé pour racine carrée
   • Racine n-ième : pow(x, 1/n)

4. 📈 LOGARITHMES ESSENTIELS :
   • log() = logarithme naturel (base e)
   • log10() pour base 10, log2() pour base 2
   • Propriétés : log(a*b) = log(a) + log(b)

5. 🔺 TRIGONOMÉTRIE COMPLÈTE :
   • Angles TOUJOURS en radians
   • radians() / degrees() pour conversions
   • atan2() pour gestion des quadrants

💡 FORMULE MAGIQUE pour math :
   Import → Constantes → Fonctions → Applications

🎉 Félicitations ! Vous maîtrisez le module math !
💡 Prochaine étape : Structures de données !
📚 Module math maîtrisé, passez aux listes et dictionnaires !
""")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE - MODULE MATH MAÎTRISÉ !")
print("=" * 70)
