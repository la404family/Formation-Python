#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
======================================================================
LES LISTES EN PYTHON - GUIDE COMPLET
======================================================================

🎯 Ce fichier couvre les listes en détail :
   • Création et initialisation
   • Accès aux éléments et slicing
   • Modification et manipulation
   • Méthodes essentielles
   • Listes multidimensionnelles
   • Performances et bonnes pratiques

📚 Concepts abordés :
   • list() et []
   • Indexation positive et négative
   • Tranches (slices)
   • Mutabilité des listes
   • Copie superficielle vs profonde
   • List comprehensions (introduction)

💡 Objectif : Maîtriser la structure de données la plus utilisée
"""

import time
import copy

print("=" * 70)
print("LES LISTES EN PYTHON - GUIDE COMPLET")
print("=" * 70)

print("\n" + "=" * 50)
print("1. CRÉATION ET INITIALISATION")
print("=" * 50)

print("\n📝 DIFFÉRENTES FAÇONS DE CRÉER UNE LISTE")
print("-" * 37)

# Création d'une liste vide
liste_vide1 = []
liste_vide2 = list()

print(f"📋 Liste vide avec [] : {liste_vide1}")
print(f"📋 Liste vide avec list() : {liste_vide2}")

# Création avec des éléments
fruits = ["pomme", "banane", "orange"]
nombres = [1, 2, 3, 4, 5]
mixte = ["texte", 42, 3.14, True]

print(f"🍎 Liste de fruits : {fruits}")
print(f"🔢 Liste de nombres : {nombres}")
print(f"🎭 Liste mixte : {mixte}")

print("\n🔄 CRÉATION AVEC RÉPÉTITION")
print("-" * 26)

# Répétition d'éléments
zeros = [0] * 5
motif = ["A", "B"] * 3

print(f"0️⃣ Cinq zéros : {zeros}")
print(f"🔤 Motif répété : {motif}")

print("\n🏗️ CRÉATION AVEC RANGE ET LIST")
print("-" * 29)

# Conversion de range en liste
nombres_1_10 = list(range(1, 11))
pairs = list(range(0, 21, 2))
inverse = list(range(10, 0, -1))

print(f"📈 Nombres 1 à 10 : {nombres_1_10}")
print(f"📊 Nombres pairs : {pairs}")
print(f"📉 Compte à rebours : {inverse}")

print("\n" + "=" * 50)
print("2. ACCÈS AUX ÉLÉMENTS")
print("=" * 50)

print("\n🎯 INDEXATION POSITIVE ET NÉGATIVE")
print("-" * 33)

animaux = ["chat", "chien", "oiseau", "poisson", "lapin"]
print(f"🐾 Liste d'animaux : {animaux}")

print("📍 Indexation positive :")
print(f"   animaux[0] = {animaux[0]} (premier)")
print(f"   animaux[2] = {animaux[2]} (troisième)")
print(f"   animaux[4] = {animaux[4]} (dernier)")

print("📍 Indexation négative :")
print(f"   animaux[-1] = {animaux[-1]} (dernier)")
print(f"   animaux[-2] = {animaux[-2]} (avant-dernier)")
print(f"   animaux[-5] = {animaux[-5]} (premier)")

print("\n🔪 SLICING (TRANCHES)")
print("-" * 20)

print("✂️ Exemples de slicing :")
print(f"   animaux[1:4] = {animaux[1:4]} (indices 1 à 3)")
print(f"   animaux[:3] = {animaux[:3]} (début jusqu'à 2)")
print(f"   animaux[2:] = {animaux[2:]} (indice 2 jusqu'à la fin)")
print(f"   animaux[:] = {animaux[:]} (copie complète)")

print("\n⚡ SLICING AVEC PAS")
print("-" * 18)
print(f"   animaux[::2] = {animaux[::2]} (un élément sur deux)")
print(f"   animaux[::-1] = {animaux[::-1]} (liste inversée)")
print(f"   animaux[1::2] = {animaux[1::2]} (depuis indice 1, un sur deux)")

print("\n" + "=" * 50)
print("3. MODIFICATION DES LISTES")
print("=" * 50)

print("\n✏️ MODIFICATION D'ÉLÉMENTS")
print("-" * 25)

couleurs = ["rouge", "vert", "bleu"]
print(f"🎨 Couleurs initiales : {couleurs}")

# Modification d'un élément
couleurs[1] = "jaune"
print(f"🎨 Après couleurs[1] = 'jaune' : {couleurs}")

# Modification par slice
couleurs[0:2] = ["violet", "orange"]
print(f"🎨 Après couleurs[0:2] = ['violet', 'orange'] : {couleurs}")

print("\n➕ AJOUT D'ÉLÉMENTS")
print("-" * 19)

ma_liste = [1, 2, 3]
print(f"📋 Liste initiale : {ma_liste}")

# Ajout à la fin
ma_liste.append(4)
print(f"📋 Après append(4) : {ma_liste}")

# Insertion à une position
ma_liste.insert(1, 1.5)
print(f"📋 Après insert(1, 1.5) : {ma_liste}")

# Extension avec une autre liste
ma_liste.extend([5, 6, 7])
print(f"📋 Après extend([5, 6, 7]) : {ma_liste}")

print("\n➖ SUPPRESSION D'ÉLÉMENTS")
print("-" * 24)

legumes = ["carotte", "brocoli", "épinard", "tomate", "salade"]
print(f"🥬 Légumes initiaux : {legumes}")

# Suppression par valeur
legumes.remove("brocoli")
print(f"🥬 Après remove('brocoli') : {legumes}")

# Suppression par index
element_supprime = legumes.pop(2)
print(f"🥬 Après pop(2) : {legumes}")
print(f"🗑️ Élément supprimé : {element_supprime}")

# Suppression du dernier
dernier = legumes.pop()
print(f"🥬 Après pop() : {legumes}")
print(f"🗑️ Dernier élément : {dernier}")

# Suppression par slice
legumes[1:] = []
print(f"🥬 Après legumes[1:] = [] : {legumes}")

print("\n" + "=" * 50)
print("4. MÉTHODES ESSENTIELLES DES LISTES")
print("=" * 50)

print("\n🔍 RECHERCHE ET COMPTAGE")
print("-" * 24)

notes = [85, 92, 78, 85, 90, 85, 88]
print(f"📊 Notes : {notes}")

# Recherche d'index
try:
    index_85 = notes.index(85)
    print(f"🎯 Première occurrence de 85 à l'index : {index_85}")
except ValueError:
    print("❌ Valeur non trouvée")

# Comptage d'occurrences
count_85 = notes.count(85)
print(f"🔢 Nombre d'occurrences de 85 : {count_85}")

# Vérification de présence
print(f"❓ 90 dans la liste ? {90 in notes}")
print(f"❓ 95 dans la liste ? {95 in notes}")

print("\n📊 TRI ET ORGANISATION")
print("-" * 22)

lettres = ['d', 'a', 'c', 'b', 'e']
print(f"🔤 Lettres initiales : {lettres}")

# Tri sur place (modifie la liste originale)
lettres.sort()
print(f"🔤 Après sort() : {lettres}")

# Tri inverse
lettres.sort(reverse=True)
print(f"🔤 Après sort(reverse=True) : {lettres}")

# Fonction sorted() (crée une nouvelle liste)
nombres_desordre = [5, 2, 8, 1, 9, 3]
nombres_tries = sorted(nombres_desordre)
print(f"🔢 Original : {nombres_desordre}")
print(f"🔢 Trié (nouvelle liste) : {nombres_tries}")

print("\n🔄 INVERSION ET MÉLANGE")
print("-" * 24)

sequence = [1, 2, 3, 4, 5]
print(f"📋 Séquence initiale : {sequence}")

# Inversion sur place
sequence.reverse()
print(f"📋 Après reverse() : {sequence}")

# Fonction reversed() (retourne un itérateur)
sequence_inverse = list(reversed([1, 2, 3, 4, 5]))
print(f"📋 Avec reversed() : {sequence_inverse}")

print("\n" + "=" * 50)
print("5. LISTES MULTIDIMENSIONNELLES")
print("=" * 50)

print("\n📊 MATRICES ET TABLEAUX 2D")
print("-" * 25)

# Création d'une matrice 3x3
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("🔢 Matrice 3x3 :")
for i, ligne in enumerate(matrice):
    print(f"   Ligne {i}: {ligne}")

# Accès aux éléments
print(f"📍 matrice[1][2] = {matrice[1][2]} (ligne 1, colonne 2)")
print(f"📍 matrice[0] = {matrice[0]} (première ligne)")

# Modification d'un élément
matrice[1][1] = 99
print(f"🔧 Après matrice[1][1] = 99 :")
for ligne in matrice:
    print(f"   {ligne}")

print("\n🏗️ CRÉATION DYNAMIQUE DE MATRICES")
print("-" * 32)

# Création d'une matrice vide 4x3
lignes, colonnes = 4, 3
matrice_vide = []

for i in range(lignes):
    ligne = []
    for j in range(colonnes):
        ligne.append(0)
    matrice_vide.append(ligne)

print(f"🔲 Matrice {lignes}x{colonnes} remplie de zéros :")
for ligne in matrice_vide:
    print(f"   {ligne}")

# Méthode avec list comprehension (plus concise)
matrice_comprehension = [[0 for _ in range(colonnes)] for _ in range(lignes)]
print(f"✨ Même matrice avec comprehension :")
for ligne in matrice_comprehension:
    print(f"   {ligne}")

print("\n" + "=" * 50)
print("6. COPIE DE LISTES")
print("=" * 50)

print("\n📋 COPIE SUPERFICIELLE VS PROFONDE")
print("-" * 32)

# Liste originale
liste_originale = [1, 2, [3, 4], 5]
print(f"📋 Liste originale : {liste_originale}")

print("\n🔗 ASSIGNATION (MÊME RÉFÉRENCE)")
print("-" * 34)
# Assignation simple - même objet !
liste_assignee = liste_originale
liste_assignee[0] = 99
print(f"📋 Après liste_assignee[0] = 99 :")
print(f"   Original : {liste_originale}")
print(f"   Assignée : {liste_assignee}")
print(f"   Même objet ? {liste_originale is liste_assignee}")

# Restaurer pour les tests suivants
liste_originale[0] = 1

print("\n📄 COPIE SUPERFICIELLE")
print("-" * 21)
# Copie superficielle - objets différents, sous-listes partagées
liste_copie_shallow = liste_originale.copy()
liste_copie_shallow[0] = 88
liste_copie_shallow[2][0] = 999  # Modifie la sous-liste partagée !

print(f"📋 Après modifications sur copie superficielle :")
print(f"   Original : {liste_originale}")
print(f"   Copie : {liste_copie_shallow}")
print(f"   Même objet ? {liste_originale is liste_copie_shallow}")

print("\n🔄 COPIE PROFONDE")
print("-" * 16)

# Restaurer
liste_originale[2][0] = 3

# Copie profonde - tout est dupliqué
liste_copie_deep = copy.deepcopy(liste_originale)
liste_copie_deep[0] = 77
liste_copie_deep[2][0] = 888

print(f"📋 Après modifications sur copie profonde :")
print(f"   Original : {liste_originale}")
print(f"   Copie profonde : {liste_copie_deep}")

print("\n" + "=" * 50)
print("7. PERFORMANCES ET OPTIMISATIONS")
print("=" * 50)

print("\n⚡ COMPARAISON DE MÉTHODES")
print("-" * 26)


def mesurer_temps(func, description):
    """Mesure le temps d'exécution d'une fonction"""
    start = time.time()
    resultat = func()
    fin = time.time()
    duree = (fin - start) * 1000  # en millisecondes
    print(f"   {description}: {duree:.4f}ms")
    return resultat


print("🏃 Test de performance (création de liste 1-1000) :")

# Méthode 1: append dans une boucle


def methode_append():
    liste = []
    for i in range(1000):
        liste.append(i)
    return liste

# Méthode 2: list comprehension


def methode_comprehension():
    return [i for i in range(1000)]

# Méthode 3: list(range())


def methode_range():
    return list(range(1000))


# Tests
_ = mesurer_temps(methode_append, "Append en boucle")
_ = mesurer_temps(methode_comprehension, "List comprehension")
_ = mesurer_temps(methode_range, "list(range())")

print("\n💡 BONNES PRATIQUES POUR LES PERFORMANCES")
print("-" * 43)

# Pré-allocation vs croissance dynamique
print("📊 Comparaison pré-allocation vs append :")


def avec_append():
    liste = []
    for i in range(10000):
        liste.append(i)
    return liste


def avec_preallocation():
    liste = [None] * 10000
    for i in range(10000):
        liste[i] = i
    return liste


_ = mesurer_temps(avec_append, "Croissance dynamique (append)")
_ = mesurer_temps(avec_preallocation, "Pré-allocation")

print("\n" + "=" * 50)
print("8. APPLICATIONS PRATIQUES")
print("=" * 50)

print("\n📊 GESTION DE DONNÉES D'ÉTUDIANTS")
print("-" * 30)

# Base de données simple d'étudiants
etudiants = [
    ["Alice", 85, "Informatique"],
    ["Bob", 78, "Mathématiques"],
    ["Charlie", 92, "Physique"],
    ["Diana", 88, "Informatique"],
    ["Eve", 76, "Mathématiques"]
]

print("🎓 Base de données étudiants :")
for etudiant in etudiants:
    nom, note, matiere = etudiant
    print(f"   {nom:<8} : {note:2d}/100 en {matiere}")

# Calculs statistiques
notes = [etudiant[1] for etudiant in etudiants]
moyenne = sum(notes) / len(notes)
note_max = max(notes)
note_min = min(notes)

print(f"\n📈 Statistiques :")
print(f"   Moyenne : {moyenne:.1f}/100")
print(f"   Note max : {note_max}/100")
print(f"   Note min : {note_min}/100")

# Filtrage par matière
informatique = [
    etudiant for etudiant in etudiants if etudiant[2] == "Informatique"]
print(f"\n💻 Étudiants en Informatique :")
for etudiant in informatique:
    print(f"   {etudiant[0]} : {etudiant[1]}/100")

print("\n🛒 GESTION DE PANIER D'ACHAT")
print("-" * 27)


class PanierAchats:
    def __init__(self):
        self.articles = []  # [nom, prix, quantite]

    def ajouter_article(self, nom, prix, quantite=1):
        """Ajoute un article au panier"""
        # Vérifier si l'article existe déjà
        for article in self.articles:
            if article[0] == nom:
                article[2] += quantite
                print(f"   ➕ Quantité mise à jour pour {nom}")
                return

        # Nouvel article
        self.articles.append([nom, prix, quantite])
        print(f"   ✅ {nom} ajouté au panier")

    def supprimer_article(self, nom):
        """Supprime un article du panier"""
        for i, article in enumerate(self.articles):
            if article[0] == nom:
                del self.articles[i]
                print(f"   🗑️ {nom} supprimé du panier")
                return
        print(f"   ❌ {nom} non trouvé dans le panier")

    def afficher_panier(self):
        """Affiche le contenu du panier"""
        if not self.articles:
            print("   🛒 Panier vide")
            return

        print("   🛒 Contenu du panier :")
        total = 0
        for nom, prix, quantite in self.articles:
            sous_total = prix * quantite
            total += sous_total
            print(
                f"      {nom:<15} : {quantite} × {prix:.2f}€ = {sous_total:.2f}€")
        print(f"      {'-'*40}")
        print(f"      {'TOTAL':<15} : {total:.2f}€")


# Test du panier
panier = PanierAchats()
print("🛒 Test du panier d'achats :")

panier.ajouter_article("Pain", 1.20, 2)
panier.ajouter_article("Lait", 0.95, 1)
panier.ajouter_article("Œufs", 2.50, 1)
panier.ajouter_article("Pain", 1.20, 1)  # Mise à jour quantité

panier.afficher_panier()

panier.supprimer_article("Lait")
print("\n🛒 Après suppression du lait :")
panier.afficher_panier()

print("\n" + "=" * 50)
print("9. INTRODUCTION AUX LIST COMPREHENSIONS")
print("=" * 50)

print("\n✨ SYNTAXE DE BASE")
print("-" * 17)

# Méthode traditionnelle
carres_traditionnel = []
for x in range(1, 6):
    carres_traditionnel.append(x**2)

# List comprehension
carres_comprehension = [x**2 for x in range(1, 6)]

print(f"🔢 Méthode traditionnelle : {carres_traditionnel}")
print(f"✨ List comprehension : {carres_comprehension}")

print("\n🎯 AVEC CONDITIONS")
print("-" * 17)

# Nombres pairs seulement
pairs = [x for x in range(1, 21) if x % 2 == 0]
print(f"📊 Nombres pairs 1-20 : {pairs}")

# Transformation conditionnelle
mots = ["python", "java", "C++", "javascript", "go"]
mots_majuscules = [mot.upper() if len(mot) > 4 else mot for mot in mots]
print(f"🔤 Mots transformés : {mots_majuscules}")

print("\n🔄 COMPREHENSIONS IMBRIQUÉES")
print("-" * 27)

# Matrice aplatie
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
aplatie = [element for ligne in matrice for element in ligne]
print(f"📊 Matrice : {matrice}")
print(f"📏 Aplatie : {aplatie}")

print("\n" + "=" * 50)
print("10. RÉSUMÉ FINAL")
print("=" * 50)

print("""
🎯 POINTS CLÉS À RETENIR :

1. 📋 CRÉATION DE LISTES :
   • [] ou list() pour listes vides
   • [1, 2, 3] pour initialisation directe
   • list(range()) pour séquences numériques

2. 🎯 ACCÈS AUX ÉLÉMENTS :
   • Index positifs : 0, 1, 2...
   • Index négatifs : -1, -2, -3...
   • Slicing : liste[start:stop:step]

3. ✏️ MODIFICATION :
   • append() pour ajouter à la fin
   • insert() pour insérer à une position
   • remove() et pop() pour supprimer

4. 🔍 MÉTHODES ESSENTIELLES :
   • index(), count(), in pour recherche
   • sort() et sorted() pour tri
   • reverse() et reversed() pour inversion

5. 📊 LISTES 2D :
   • [[1,2], [3,4]] pour matrices
   • Attention aux références partagées
   • list comprehension pour création

6. 📋 COPIE :
   • = : même référence
   • copy() : copie superficielle
   • deepcopy() : copie profonde

💡 FORMULE MAGIQUE pour les listes :
   Création → Manipulation → Optimisation → Applications

🎉 Félicitations ! Vous maîtrisez les listes !
💡 Prochaine étape : Méthodes avancées des listes !
📚 Listes maîtrisées, passez aux méthodes avancées !
""")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE - LISTES MAÎTRISÉES !")
print("=" * 70)
