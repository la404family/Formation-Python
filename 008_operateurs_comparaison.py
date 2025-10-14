#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
======================================================================
LES OPÉRATEURS DE COMPARAISON EN PYTHON - GUIDE COMPLET
======================================================================

🎯 Ce fichier couvre tous les opérateurs de comparaison en Python :
   • Égalité et inégalité
   • Comparaisons numériques
   • Comparaisons de chaînes
   • Comparaisons avancées
   • Opérateurs d'identité et d'appartenance
   • Combinaisons logiques

📚 Concepts abordés :
   • ==, !=, <, >, <=, >=
   • is, is not
   • in, not in
   • and, or, not
   • Priorité des opérateurs
   • Comparaisons chaînées

💡 Objectif : Maîtriser tous les types de comparaisons en Python
"""

print("=" * 70)
print("LES OPÉRATEURS DE COMPARAISON EN PYTHON - GUIDE COMPLET")
print("=" * 70)

print("\n" + "=" * 50)
print("1. OPÉRATEURS DE COMPARAISON BASIQUES")
print("=" * 50)

print("\n⚖️ ÉGALITÉ ET INÉGALITÉ")
print("-" * 24)

a = 10
b = 10
c = 5

print(f"🔢 Variables : a = {a}, b = {b}, c = {c}")
print(f"   a == b : {a == b} (égal à)")
print(f"   a != c : {a != c} (différent de)")
print(f"   a == c : {a == c}")
print(f"   b != c : {b != c}")

print("\n📊 COMPARAISONS NUMÉRIQUES")
print("-" * 26)

x = 15
y = 20
print(f"🔢 Variables : x = {x}, y = {y}")
print(f"   x < y  : {x < y} (inférieur à)")
print(f"   x > y  : {x > y} (supérieur à)")
print(f"   x <= y : {x <= y} (inférieur ou égal)")
print(f"   x >= y : {x >= y} (supérieur ou égal)")

print("\n" + "=" * 50)
print("2. COMPARAISONS DE CHAÎNES")
print("=" * 50)

print("\n🔤 COMPARAISON ALPHABÉTIQUE")
print("-" * 27)

str1 = "apple"
str2 = "banana"
str3 = "apple"

print(f"📝 Chaînes : '{str1}', '{str2}', '{str3}'")
print(f"   '{str1}' == '{str3}' : {str1 == str3}")
print(f"   '{str1}' < '{str2}'  : {str1 < str2} (ordre alphabétique)")
print(f"   '{str1}' > '{str2}'  : {str1 > str2}")

print("\n🔡 SENSIBILITÉ À LA CASSE")
print("-" * 25)

mot1 = "Python"
mot2 = "python"
print(f"📝 Mots : '{mot1}', '{mot2}'")
print(f"   '{mot1}' == '{mot2}' : {mot1 == mot2} (sensible à la casse)")
print(f"   Comparaison insensible : {mot1.lower() == mot2.lower()}")

print("\n" + "=" * 50)
print("3. OPÉRATEURS D'IDENTITÉ")
print("=" * 50)

print("\n🆔 IS ET IS NOT")
print("-" * 16)

liste1 = [1, 2, 3]
liste2 = [1, 2, 3]
liste3 = liste1

print(f"📋 Listes :")
print(f"   liste1 = {liste1}")
print(f"   liste2 = {liste2}")
print(f"   liste3 = liste1 (même référence)")

print(f"\n🔍 Comparaisons :")
print(f"   liste1 == liste2 : {liste1 == liste2} (même contenu)")
print(f"   liste1 is liste2 : {liste1 is liste2} (même objet ?)")
print(f"   liste1 is liste3 : {liste1 is liste3} (même référence)")

print(f"\n📍 Adresses mémoire :")
print(f"   id(liste1) : {id(liste1)}")
print(f"   id(liste2) : {id(liste2)}")
print(f"   id(liste3) : {id(liste3)}")

print("\n💡 CAS SPÉCIAUX AVEC NONE")
print("-" * 26)

valeur = None
print(f"   valeur is None     : {valeur is None}")
print(f"   valeur is not None : {valeur is not None}")

print("\n" + "=" * 50)
print("4. OPÉRATEURS D'APPARTENANCE")
print("=" * 50)

print("\n🔍 IN ET NOT IN")
print("-" * 16)

ma_liste = [1, 2, 3, 4, 5]
mon_texte = "Formation Python"

print(f"📋 Liste : {ma_liste}")
print(f"📝 Texte : '{mon_texte}'")

print(f"\n🎯 Tests d'appartenance :")
print(f"   3 in ma_liste        : {3 in ma_liste}")
print(f"   10 in ma_liste       : {10 in ma_liste}")
print(f"   6 not in ma_liste    : {6 not in ma_liste}")
print(f"   'Python' in mon_texte : {'Python' in mon_texte}")
print(f"   'Java' in mon_texte   : {'Java' in mon_texte}")

print("\n" + "=" * 50)
print("5. COMBINAISONS LOGIQUES")
print("=" * 50)

print("\n🔗 AND, OR, NOT")
print("-" * 16)

age = 25
salaire = 35000
experience = 3

print(
    f"🧑 Profil : âge = {age}, salaire = {salaire}€, expérience = {experience} ans")

# Conditions composées
condition1 = age >= 18 and age <= 65
condition2 = salaire > 30000 or experience >= 5
condition3 = not (age < 18)

print(f"\n✅ Évaluations :")
print(f"   Âge de travail (18-65) : {condition1}")
print(f"   Bon profil (salaire OU exp) : {condition2}")
print(f"   Pas mineur : {condition3}")

print("\n" + "=" * 50)
print("6. COMPARAISONS CHAÎNÉES")
print("=" * 50)

print("\n⛓️ CHAÎNAGE D'OPÉRATEURS")
print("-" * 24)

note = 85
print(f"📊 Note : {note}")

# Comparaisons chaînées
resultat1 = 0 <= note <= 100
resultat2 = 80 <= note < 90
resultat3 = note > 70 and note < 95

print(f"   Note valide (0-100) : {resultat1}")
print(f"   Mention B (80-90) : {resultat2}")
print(f"   Équivalent avec AND : {resultat3}")

print(f"\n🔢 Autres exemples :")
x, y, z = 1, 5, 10
print(f"   Variables : x={x}, y={y}, z={z}")
print(f"   x < y < z : {x < y < z}")
print(f"   x < y > z : {x < y > z}")

print("\n" + "=" * 50)
print("7. PRIORITÉ DES OPÉRATEURS")
print("=" * 50)

print("\n📋 ORDRE DE PRIORITÉ (du plus fort au plus faible)")
print("-" * 48)

print("""
🎯 ORDRE D'ÉVALUATION :

1. **Parenthèses** : ( )
2. **Puissance** : **
3. **Unaire** : +x, -x, not x
4. **Multiplication, Division** : *, /, //, %
5. **Addition, Soustraction** : +, -
6. **Comparaisons** : ==, !=, <, >, <=, >=, is, in
7. **NOT logique** : not
8. **AND logique** : and
9. **OR logique** : or
""")

print("💡 EXEMPLES PRATIQUES")
print("-" * 20)

# Sans parenthèses
resultat1 = 5 + 3 * 2 > 10 and not False
print(f"   5 + 3 * 2 > 10 and not False = {resultat1}")
print(f"   Étapes : 5 + 6 > 10 and True = 11 > 10 and True = True")

# Avec parenthèses pour clarifier
resultat2 = (5 + 3) * 2 > 10 and (not False)
print(f"   (5 + 3) * 2 > 10 and (not False) = {resultat2}")

print("\n" + "=" * 50)
print("8. APPLICATIONS PRATIQUES")
print("=" * 50)

print("\n🎯 VALIDATION DE DONNÉES")
print("-" * 24)


def valider_utilisateur(nom, age, email):
    """Valide les données d'un utilisateur"""
    nom_valide = nom and len(nom) >= 2
    age_valide = 0 <= age <= 120
    email_valide = email and "@" in email and "." in email

    return nom_valide and age_valide and email_valide


# Tests
utilisateurs = [
    ("Alice", 25, "alice@email.com"),
    ("", 30, "bob@email.com"),
    ("Charlie", -5, "charlie@email.com"),
    ("Diana", 40, "diana.email.com"),
    ("Eve", 35, "eve@email.com")
]

print("👥 Validation des utilisateurs :")
for nom, age, email in utilisateurs:
    valide = valider_utilisateur(nom, age, email)
    status = "✅ VALIDE" if valide else "❌ INVALIDE"
    print(f"   {nom:<8} ({age}, {email:<20}) : {status}")

print("\n🏆 SYSTÈME DE NOTES")
print("-" * 19)


def evaluer_note(note):
    """Évalue une note et retourne la mention"""
    if note >= 90:
        return "Excellent"
    elif note >= 80:
        return "Très Bien"
    elif note >= 70:
        return "Bien"
    elif note >= 60:
        return "Assez Bien"
    elif note >= 50:
        return "Passable"
    else:
        return "Insuffisant"


notes = [95, 82, 67, 54, 43, 88]
print("📊 Évaluation des notes :")
for note in notes:
    mention = evaluer_note(note)
    print(f"   Note {note:2d}/100 : {mention}")

print("\n" + "=" * 50)
print("9. TABLEAU RÉCAPITULATIF")
print("=" * 50)

print("""
📊 GUIDE DE RÉFÉRENCE RAPIDE

⚖️ COMPARAISONS NUMÉRIQUES :
   • == : égal à
   • != : différent de
   • <  : inférieur à
   • >  : supérieur à
   • <= : inférieur ou égal à
   • >= : supérieur ou égal à

🆔 IDENTITÉ :
   • is     : même objet
   • is not : objets différents

🔍 APPARTENANCE :
   • in     : appartient à
   • not in : n'appartient pas à

🔗 LOGIQUES :
   • and : ET logique
   • or  : OU logique
   • not : NON logique

⛓️ CHAÎNAGE :
   • a < b < c : comparaisons chaînées
   • Plus lisible que a < b and b < c
""")

print("\n" + "=" * 50)
print("10. RÉSUMÉ FINAL")
print("=" * 50)

print("""
🎯 POINTS CLÉS À RETENIR :

1. ⚖️ COMPARAISONS DE BASE :
   • == pour l'égalité de valeur
   • is pour l'identité d'objet
   • Attention à la différence !

2. 🔤 CHAÎNES DE CARACTÈRES :
   • Comparaison alphabétique
   • Sensible à la casse
   • Utilisez .lower() pour ignorer la casse

3. 🔗 OPÉRATEURS LOGIQUES :
   • and : toutes les conditions vraies
   • or : au moins une condition vraie
   • not : inverse le résultat

4. ⛓️ COMPARAISONS CHAÎNÉES :
   • Plus lisibles : a < b < c
   • Plus efficaces que plusieurs and

5. 🎯 BONNES PRATIQUES :
   • Utilisez des parenthèses pour clarifier
   • is None plutôt que == None
   • Attention à la priorité des opérateurs

💡 FORMULE MAGIQUE pour les comparaisons :
   Lisibilité → Parenthèses → Tests → Validation

🎉 Félicitations ! Vous maîtrisez les comparaisons !
💡 Prochaine étape : Structures conditionnelles !
📚 Comparaisons maîtrisées, passez aux conditions !
""")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE - OPÉRATEURS DE COMPARAISON MAÎTRISÉS !")
print("=" * 70)
