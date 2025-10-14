"""
======================================================================
LES NOMBRES ENTIERS EN PYTHON - GUIDE COMPLET
======================================================================

🔢 Les nombres entiers (int) sont fondamentaux en programmation.
Ce guide vous apprend tout sur leur manipulation : opérations mathématiques,
conversions, comparaisons, formatage, et techniques avancées !

"""

import math
print("=" * 70)
print("LES NOMBRES ENTIERS EN PYTHON - GUIDE COMPLET")
print("=" * 70)

print("\n" + "=" * 50)
print("1. CONCEPT DE BASE : QU'EST-CE QU'UN ENTIER ?")
print("=" * 50)

# 🔢 Les fonctions relatives aux entiers
int_d_exemple = 42
print(f"🔢 Nombre entier d'exemple : {int_d_exemple}")
print(f"   Type : {type(int_d_exemple)}")
print(f"   Taille en mémoire : {int_d_exemple.__sizeof__()} bytes")

print("\n💡 ANALOGIE - Les entiers comme des compteurs :")
print("""
    Positifs : 1, 2, 3, 42, 1000, 999999...
    Négatifs : -1, -10, -42, -1000...
    Zéro : 0 (ni positif ni négatif)
    
    Python peut gérer des entiers de taille ILLIMITÉE !
""")

# Démonstration avec de très grands nombres
grand_nombre = 123456789012345678901234567890
print(f"🚀 Python gère les TRÈS grands nombres :")
print(f"   Nombre : {grand_nombre}")
print(f"   Type : {type(grand_nombre)}")
print(f"   Nombre de chiffres : {len(str(grand_nombre))}")

print("\n" + "=" * 50)
print("2. OPÉRATIONS MATHÉMATIQUES DE BASE")
print("=" * 50)

print("\n🧮 OPÉRATIONS ARITHMÉTIQUES")
print("-" * 28)

a, b = 15, 4
print(f"💡 Avec a = {a} et b = {b} :")
print(f"   Addition : {a} + {b} = {a + b}")
print(f"   Soustraction : {a} - {b} = {a - b}")
print(f"   Multiplication : {a} * {b} = {a * b}")
print(f"   Division réelle : {a} / {b} = {a / b}")
print(f"   Division entière : {a} // {b} = {a // b}")
print(f"   Modulo (reste) : {a} % {b} = {a % b}")
print(f"   Puissance : {a} ** {b} = {a ** b}")

print("\n🔢 FONCTIONS MATHÉMATIQUES INTÉGRÉES")
print("-" * 35)

nombres_test = [42, -17, 0, -5]
for nombre in nombres_test:
    print(f"\n📊 Analyse du nombre {nombre} :")
    # Afficher la valeur absolue d'un entier
    valeur_absolue = abs(nombre)
    print(f"   abs({nombre}) = {valeur_absolue}")

    print(
        f"   Signe : {'Positif' if nombre > 0 else 'Négatif' if nombre < 0 else 'Zéro'}")

    if nombre != 0:
        print(f"   Opposé : -({nombre}) = {-nombre}")

print("\n🎯 FONCTIONS UTILES")
print("-" * 18)

liste_nombres = [5, 12, 3, 8, 1, 15]
print(f"📋 Liste de nombres : {liste_nombres}")
print(f"   min() : {min(liste_nombres)}")
print(f"   max() : {max(liste_nombres)}")
print(f"   sum() : {sum(liste_nombres)}")
print(f"   len() : {len(liste_nombres)} éléments")

# Calculs dérivés
moyenne = sum(liste_nombres) / len(liste_nombres)
print(f"   Moyenne : {moyenne:.2f}")

print("\n" + "=" * 50)
print("3. SYSTÈMES DE NUMÉRATION")
print("=" * 50)

print("\n🔄 CONVERSIONS ENTRE BASES")
print("-" * 26)

nombre_decimal = 42
print(f"🔢 Nombre décimal : {nombre_decimal}")

# Convertir un entier en binaire
binaire = bin(nombre_decimal)
print(f"✅ Binaire (base 2) : {binaire}")
print(f"   Sans préfixe : {binaire[2:]}")

# Convertir un entier en octal
octal = oct(nombre_decimal)
print(f"✅ Octal (base 8) : {octal}")
print(f"   Sans préfixe : {octal[2:]}")

# Convertir un entier en hexadécimal
hexadecimal = hex(nombre_decimal)
print(f"✅ Hexadécimal (base 16) : {hexadecimal}")
print(f"   Sans préfixe : {hexadecimal[2:]}")
print(f"   En majuscules : {hexadecimal[2:].upper()}")

print("\n🔄 CONVERSIONS INVERSES")
print("-" * 23)

# Conversion depuis d'autres bases vers décimal
print("✅ Conversion vers décimal :")
print(f"   int('101010', 2) = {int('101010', 2)} (binaire)")
print(f"   int('52', 8) = {int('52', 8)} (octal)")
print(f"   int('2a', 16) = {int('2a', 16)} (hexadécimal)")

print("\n💡 USAGE PRATIQUE - Couleurs web")
couleur_rouge = 255
couleur_vert = 128
couleur_bleu = 64
couleur_hex = f"#{couleur_rouge:02x}{couleur_vert:02x}{couleur_bleu:02x}"
print(f"   RGB({couleur_rouge}, {couleur_vert}, {couleur_bleu}) = {couleur_hex}")
print("\n" + "=" * 50)
print("4. COMPARAISONS ET OPÉRATEURS LOGIQUES")
print("=" * 50)

print("\n⚖️ COMPARAISONS DE BASE")
print("-" * 23)

# Comparer deux entiers
int_a = 10
int_b = 20
int_c = 10

print(f"💡 Avec a = {int_a}, b = {int_b}, c = {int_c} :")

# Égalité et inégalité
est_egal = int_a == int_b
print(f"   {int_a} == {int_b} : {est_egal}")
est_egal_c = int_a == int_c
print(f"   {int_a} == {int_c} : {est_egal_c}")
est_different = int_a != int_b
print(f"   {int_a} != {int_b} : {est_different}")

# Comparaisons d'ordre
# Comparer deux entiers (plus grand que)
est_plus_grand = int_a > int_b
print(f"   {int_a} > {int_b} : {est_plus_grand}")
# Comparer deux entiers (plus petit que)
est_plus_petit = int_a < int_b
print(f"   {int_a} < {int_b} : {est_plus_petit}")
# Comparer deux entiers (plus grand ou égal)
est_plus_grand_ou_egal = int_a >= int_c
print(f"   {int_a} >= {int_c} : {est_plus_grand_ou_egal}")
# Comparer deux entiers (plus petit ou égal)
est_plus_petit_ou_egal = int_a <= int_b
print(f"   {int_a} <= {int_b} : {est_plus_petit_ou_egal}")

print("\n🎯 COMPARAISONS MULTIPLES")
print("-" * 25)

nombre = 15
print(f"📊 Nombre testé : {nombre}")
print(f"   Entre 10 et 20 ? {10 <= nombre <= 20}")
print(f"   Nombre pair ? {nombre % 2 == 0}")
print(f"   Nombre impair ? {nombre % 2 == 1}")
print(f"   Multiple de 3 ? {nombre % 3 == 0}")
print(f"   Multiple de 5 ? {nombre % 5 == 0}")

# Tests avec différents nombres
nombres_test = [12, 15, 20, 7, 30]
print(f"\n🔍 Analyse de plusieurs nombres : {nombres_test}")
for n in nombres_test:
    pair = "pair" if n % 2 == 0 else "impair"
    signe = "positif" if n > 0 else "négatif" if n < 0 else "zéro"
    print(f"   {n} : {pair}, {signe}")

print("\n" + "=" * 50)
print("5. FORMATAGE ET AFFICHAGE")
print("=" * 50)

print("\n📐 FORMATAGE DE NOMBRES")
print("-" * 23)

# Compléter un entier avec des zéros à gauche
nombre_court = 5
nombre_long = 42
nombre_tres_long = 1234

print("✅ Formatage avec zéros (zfill) :")
int_a_zfill = str(nombre_court).zfill(3)
int_b_zfill = str(nombre_long).zfill(3)
print(f"   {nombre_court} avec zfill(3) : '{int_a_zfill}'")
print(f"   {nombre_long} avec zfill(3) : '{int_b_zfill}'")

print("\n✅ Formatage avec f-strings :")
print(f"   {nombre_court:03d} (format :03d)")
print(f"   {nombre_long:05d} (format :05d)")
print(f"   {nombre_tres_long:08d} (format :08d)")

print("\n✅ Alignement et espacement :")
nombres = [5, 42, 123, 9876]
print("   Aligné à droite :")
for n in nombres:
    print(f"   {n:>6d}")

print("   Aligné à gauche :")
for n in nombres:
    print(f"   {n:<6d}")

print("   Centré :")
for n in nombres:
    print(f"   {n:^6d}")

print("\n🎨 FORMATAGE AVANCÉ")
print("-" * 20)

grand_nombre = 1234567890
print(f"✅ Séparateurs de milliers :")
print(f"   {grand_nombre:,} (virgules)")
print(f"   {grand_nombre:_} (underscores)")

pourcentage = 0.755
print(f"✅ Pourcentages :")
print(f"   {pourcentage:.1%} (1 décimale)")
print(f"   {pourcentage:.2%} (2 décimales)")

print("\n" + "=" * 50)
print("6. OPÉRATIONS AVANCÉES")
print("=" * 50)

print("\n🔢 FONCTIONS MATHÉMATIQUES AVANCÉES")
print("-" * 35)


nombre = 16
print(f"🧮 Avec le nombre {nombre} :")
print(f"   Racine carrée : √{nombre} = {math.sqrt(nombre)}")
print(f"   Logarithme naturel : ln({nombre}) = {math.log(nombre):.3f}")
print(f"   Logarithme base 10 : log₁₀({nombre}) = {math.log10(nombre):.3f}")
print(f"   Logarithme base 2 : log₂({nombre}) = {math.log2(nombre):.1f}")

print(f"\n🎯 Puissances et exponentielles :")
base = 2
exposants = [0, 1, 2, 3, 4, 5, 8, 10]
for exp in exposants:
    resultat = base ** exp
    print(f"   {base}^{exp} = {resultat}")

print(f"\n🔄 Fonctions d'arrondi :")
nombres_decimaux = [3.2, 3.7, -2.1, -2.8, 3.5, 4.5]
for n in nombres_decimaux:
    print(
        f"   {n} → floor: {math.floor(n)}, ceil: {math.ceil(n)}, round: {round(n)}")

print("\n⚙️ OPÉRATIONS BINAIRES (BITS)")
print("-" * 28)

a, b = 12, 7  # 12 = 1100, 7 = 0111 en binaire
print(f"💡 Avec a = {a} ({bin(a)}) et b = {b} ({bin(b)}) :")
print(f"   ET binaire (AND) : {a} & {b} = {a & b} ({bin(a & b)})")
print(f"   OU binaire (OR) : {a} | {b} = {a | b} ({bin(a | b)})")
print(f"   OU exclusif (XOR) : {a} ^ {b} = {a ^ b} ({bin(a ^ b)})")
print(f"   NON binaire (NOT) : ~{a} = {~a}")
print(f"   Décalage gauche : {a} << 2 = {a << 2} ({bin(a << 2)})")
print(f"   Décalage droite : {a} >> 2 = {a >> 2} ({bin(a >> 2)})")

print("\n" + "=" * 50)
print("7. VALIDATION ET VÉRIFICATION")
print("=" * 50)

print("\n✅ TESTS DE PROPRIÉTÉS")
print("-" * 22)


def analyser_nombre(n):
    """Analyse complète d'un nombre"""
    print(f"\n📊 Analyse du nombre {n} :")
    print(f"   Type : {type(n).__name__}")
    print(f"   Valeur absolue : {abs(n)}")
    print(
        f"   Signe : {'Positif' if n > 0 else 'Négatif' if n < 0 else 'Zéro'}")
    print(f"   Pair/Impair : {'Pair' if n % 2 == 0 else 'Impair'}")

    if n > 0:
        print(f"   Est un carré parfait ? {int(math.sqrt(n))**2 == n}")
        # Premiers 10
        print(
            f"   Diviseurs : {[i for i in range(1, n+1) if n % i == 0][:10]}...")

    # Conversion en bases
    if n >= 0:
        print(f"   Binaire : {bin(n)}")
        print(f"   Octal : {oct(n)}")
        print(f"   Hexadécimal : {hex(n)}")


# Tests sur différents nombres
nombres_analyse = [0, 7, 16, 25, -5, 100]
for nombre in nombres_analyse:
    analyser_nombre(nombre)

print("\n🎯 FONCTIONS DE VALIDATION")
print("-" * 26)


def est_premier(n):
    """Vérifie si un nombre est premier"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def pgcd(a, b):
    """Plus Grand Commun Diviseur"""
    while b:
        a, b = b, a % b
    return a


def ppcm(a, b):
    """Plus Petit Commun Multiple"""
    return abs(a * b) // pgcd(a, b)


# Tests des fonctions
print("🔍 Tests de nombres premiers :")
nombres_premiers_test = [2, 3, 4, 5, 6, 7, 11, 13, 15, 17, 20, 23]
for n in nombres_premiers_test:
    print(f"   {n} : {'Premier' if est_premier(n) else 'Non premier'}")

print(f"\n🔗 PGCD et PPCM :")
couples = [(12, 8), (15, 25), (7, 11)]
for a, b in couples:
    print(f"   PGCD({a}, {b}) = {pgcd(a, b)}, PPCM({a}, {b}) = {ppcm(a, b)}")

print("\n" + "=" * 50)
print("9. TABLEAU RÉCAPITULATIF")
print("=" * 50)

print("""
📊 GUIDE DE RÉFÉRENCE RAPIDE

🧮 OPÉRATIONS ARITHMÉTIQUES :
   • +, -, *, / (division réelle)
   • // (division entière), % (modulo)
   • ** (puissance), abs() (valeur absolue)

⚖️ COMPARAISONS :
   • ==, != (égalité, différence)
   • <, >, <=, >= (ordre)
   • Comparaisons chaînées : 10 <= x <= 20

🔄 CONVERSIONS DE BASES :
   • bin() / oct() / hex() : vers binaire/octal/hexadécimal
   • int(string, base) : depuis une base vers décimal

📐 FORMATAGE :
   • f"{n:03d}" : avec zéros (003)
   • f"{n:,}" : séparateurs de milliers
   • f"{n:>5}" : alignement à droite

🔢 FONCTIONS MATHÉMATIQUES :
   • min(), max(), sum() : extremums et somme
   • math.sqrt(), math.log() : racine, logarithme
   • math.floor(), math.ceil() : arrondi inf/sup

⚙️ OPÉRATIONS BINAIRES :
   • & (AND), | (OR), ^ (XOR), ~ (NOT)
   • << >> : décalages gauche/droite
""")

print("\n" + "=" * 50)
print("10. RÉSUMÉ FINAL")
print("=" * 50)

print("""
🎯 POINTS CLÉS À RETENIR :

1. 🔢 ENTIERS ILLIMITÉS :
   • Python gère des nombres de taille illimitée
   • Pas de problème d'overflow comme d'autres langages
   • Conversion automatique int ↔ float selon besoin

2. 🧮 OPÉRATIONS ESSENTIELLES :
   • // pour division entière, % pour reste
   • ** pour puissances (plus lisible que pow())
   • abs() pour valeur absolue

3. ⚖️ COMPARAISONS INTELLIGENTES :
   • Comparaisons chaînées : 0 <= x <= 100
   • Modulo pour tester parité : n % 2 == 0
   • Opérateurs logiques pour conditions complexes

4. 🔄 BASES NUMÉRIQUES :
   • bin(), oct(), hex() pour convertir
   • int(string, base) pour lire d'autres bases
   • Utile pour programmation système et couleurs

5. 📐 FORMATAGE PROFESSIONNEL :
   • F-strings avec spécificateurs : :03d, :,
   • zfill() pour codes avec zéros
   • Alignement avec >, <, ^

💡 FORMULE MAGIQUE pour les entiers :
   Calculer → Comparer → Formater → Afficher

🎉 Félicitations ! Vous maîtrisez les entiers Python !
💡 Prochaine étape : Les nombres décimaux (float) !
📚 Continuez avec 006_les_fonctions_float.py
""")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE - NOMBRES ENTIERS MAÎTRISÉS !")
print("=" * 70)
