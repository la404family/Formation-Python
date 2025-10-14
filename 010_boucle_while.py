#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
======================================================================
BOUCLE WHILE EN PYTHON - GUIDE COMPLET
======================================================================

🎯 Ce fichier couvre la boucle while en détail :
   • Syntaxe et fonctionnement
   • Conditions de contrôle
   • Boucles infinies et protection
   • While avec else
   • Applications pratiques
   • Optimisations et bonnes pratiques

📚 Concepts abordés :
   • while condition:
   • Compteurs et accumulateurs
   • Validation de saisie
   • Menus interactifs
   • Algorithmes de recherche

💡 Objectif : Maîtriser les répétitions conditionnelles
"""

print("=" * 70)
print("BOUCLE WHILE EN PYTHON - GUIDE COMPLET")
print("=" * 70)

print("\n" + "=" * 50)
print("1. SYNTAXE ET PRINCIPES DE BASE")
print("=" * 50)

print("\n🔄 SYNTAXE FONDAMENTALE")
print("-" * 22)

print("💡 Structure d'une boucle while :")
print("""
while condition:
    # Instructions à répéter
    # Modification de la condition
""")

print("\n🧮 EXEMPLE SIMPLE - COMPTEUR")
print("-" * 27)

compteur = 1
print(f"🎯 Comptage de 1 à 5 :")

while compteur <= 5:
    print(f"   Compteur : {compteur}")
    compteur += 1  # Important : modifier la condition !

print(f"✅ Fin de boucle, compteur = {compteur}")

print("\n📈 ACCUMULATION DE VALEURS")
print("-" * 25)

nombre = 1
somme = 0
print(f"🧮 Somme des nombres de 1 à 10 :")

while nombre <= 10:
    somme += nombre
    print(f"   {nombre} → somme = {somme}")
    nombre += 1

print(f"✅ Somme totale : {somme}")

print("\n" + "=" * 50)
print("2. CONDITIONS DE CONTRÔLE")
print("=" * 50)

print("\n🎯 CONDITION AVEC VARIABLES")
print("-" * 26)

# Recherche d'un nombre
nombre_cherche = 7
nombre_actuel = 1
trouve = False

print(f"🔍 Recherche du nombre {nombre_cherche} :")

while nombre_actuel <= 10 and not trouve:
    if nombre_actuel == nombre_cherche:
        trouve = True
        print(
            f"✅ Nombre {nombre_cherche} trouvé à la position {nombre_actuel}")
    else:
        print(f"   Vérification de {nombre_actuel}... Non")
    nombre_actuel += 1

if not trouve:
    print(f"❌ Nombre {nombre_cherche} non trouvé")

print("\n🔢 CONDITION AVEC CALCULS")
print("-" * 24)

# Suite de Fibonacci jusqu'à 100
a, b = 0, 1
print("🌀 Suite de Fibonacci (< 100) :")
print(f"   {a}, {b}", end="")

while b < 100:
    suivant = a + b
    if suivant < 100:
        print(f", {suivant}", end="")
    a, b = b, suivant

print(f"\n✅ Dernier terme de la suite : {b}")

print("\n" + "=" * 50)
print("3. VALIDATION DE SAISIE")
print("=" * 50)

print("\n✅ SAISIE SÉCURISÉE")
print("-" * 18)


def saisie_nombre_securisee():
    """Simule une saisie sécurisée d'un nombre"""
    # Simulation de saisies utilisateur
    saisies_test = ["abc", "25.5", "-10", "42"]
    index_saisie = 0

    print("🎯 Entrez un nombre entier positif :")

    while index_saisie < len(saisies_test):
        saisie = saisies_test[index_saisie]
        print(f"   Simulation saisie : '{saisie}'")

        try:
            nombre = int(saisie)
            if nombre > 0:
                print(f"✅ Nombre valide : {nombre}")
                return nombre
            else:
                print("❌ Le nombre doit être positif !")
        except ValueError:
            print("❌ Veuillez entrer un nombre entier !")

        index_saisie += 1

    print("❌ Échec après plusieurs tentatives")
    return None


resultat = saisie_nombre_securisee()

print("\n🎮 MENU INTERACTIF")
print("-" * 17)


def menu_calculatrice():
    """Simule un menu de calculatrice"""
    continuer = True
    choix_test = ["1", "2", "3", "0"]  # Simulation des choix
    index_choix = 0

    while continuer and index_choix < len(choix_test):
        print(f"\n📊 CALCULATRICE")
        print("1. Addition")
        print("2. Soustraction")
        print("3. Multiplication")
        print("0. Quitter")

        choix = choix_test[index_choix]
        print(f"   Choix simulé : {choix}")
        index_choix += 1

        if choix == "1":
            print("➕ Mode addition sélectionné")
        elif choix == "2":
            print("➖ Mode soustraction sélectionné")
        elif choix == "3":
            print("✖️ Mode multiplication sélectionné")
        elif choix == "0":
            print("👋 Au revoir !")
            continuer = False
        else:
            print("❌ Choix invalide, recommencez")


menu_calculatrice()

print("\n" + "=" * 50)
print("4. WHILE AVEC ELSE")
print("=" * 50)

print("\n🔍 CLAUSE ELSE AVEC WHILE")
print("-" * 26)

# Recherche d'un élément
liste_nombres = [2, 4, 6, 8, 10]
nombre_cherche = 7
i = 0

print(f"🔍 Recherche de {nombre_cherche} dans {liste_nombres}")

while i < len(liste_nombres):
    if liste_nombres[i] == nombre_cherche:
        print(f"✅ {nombre_cherche} trouvé à l'index {i}")
        break
    i += 1
else:
    # Cette clause s'exécute si la boucle se termine normalement
    print(f"❌ {nombre_cherche} non trouvé dans la liste")

print("\n💡 EXEMPLE AVEC BREAK")
print("-" * 21)

# Test de nombres premiers


def est_premier(n):
    """Teste si un nombre est premier avec while...else"""
    if n < 2:
        return False

    diviseur = 2
    while diviseur * diviseur <= n:
        if n % diviseur == 0:
            return False  # Pas premier
        diviseur += 1
    else:
        return True  # Premier (boucle terminée normalement)


nombres_test = [2, 3, 4, 15, 17, 25, 29]
print("🔢 Test de nombres premiers :")
for nombre in nombres_test:
    resultat = "premier" if est_premier(nombre) else "composé"
    emoji = "✅" if est_premier(nombre) else "❌"
    print(f"   {nombre} : {emoji} {resultat}")

print("\n" + "=" * 50)
print("5. BOUCLES INFINIES ET PROTECTION")
print("=" * 50)

print("\n⚠️ ÉVITER LES BOUCLES INFINIES")
print("-" * 30)

print("❌ EXEMPLE DE PIÈGE :")
print("""
# DANGER - Boucle infinie !
i = 0
while i < 10:
    print(i)
    # Oubli d'incrémenter i !
    # i += 1  <- Cette ligne manque !
""")

print("✅ PROTECTION AVEC COMPTEUR :")


def fonction_avec_protection():
    """Fonction avec protection contre boucle infinie"""
    tentatives = 0
    max_tentatives = 5
    succes = False

    while not succes and tentatives < max_tentatives:
        tentatives += 1
        print(f"🔄 Tentative {tentatives}/{max_tentatives}")

        # Simulation d'une opération qui peut échouer
        import random
        if random.random() > 0.7:  # 30% de chance de succès
            succes = True
            print("✅ Opération réussie !")
        else:
            print("❌ Échec, nouvelle tentative...")

    if not succes:
        print("⚠️ Échec après toutes les tentatives")


# Test de la protection
print("🛡️ Test avec protection :")
fonction_avec_protection()

print("\n" + "=" * 50)
print("6. PATTERNS ALGORITHMIQUES")
print("=" * 50)

print("\n🎯 ALGORITHME DE RECHERCHE")
print("-" * 25)


def recherche_lineaire(liste, element):
    """Recherche linéaire avec while"""
    index = 0

    while index < len(liste):
        if liste[index] == element:
            return index
        index += 1

    return -1  # Non trouvé


# Test de recherche
ma_liste = [3, 7, 1, 9, 4, 6, 8]
element = 9

print(f"📋 Liste : {ma_liste}")
resultat = recherche_lineaire(ma_liste, element)

if resultat != -1:
    print(f"✅ Élément {element} trouvé à l'index {resultat}")
else:
    print(f"❌ Élément {element} non trouvé")

print("\n🔍 ALGORITHME DE DICHOTOMIE")
print("-" * 26)


def recherche_dichotomique(liste_triee, element):
    """Recherche dichotomique avec while"""
    gauche = 0
    droite = len(liste_triee) - 1
    comparaisons = 0

    print(f"🎯 Recherche de {element} dans {liste_triee}")

    while gauche <= droite:
        comparaisons += 1
        milieu = (gauche + droite) // 2
        valeur_milieu = liste_triee[milieu]

        print(
            f"   Étape {comparaisons}: gauche={gauche}, droite={droite}, milieu={milieu} (valeur={valeur_milieu})")

        if valeur_milieu == element:
            print(f"✅ Trouvé en {comparaisons} comparaisons !")
            return milieu
        elif valeur_milieu < element:
            gauche = milieu + 1
        else:
            droite = milieu - 1

    print(f"❌ Non trouvé après {comparaisons} comparaisons")
    return -1


# Test de dichotomie
liste_triee = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
recherche_dichotomique(liste_triee, 11)

print("\n" + "=" * 50)
print("7. APPLICATIONS PRATIQUES")
print("=" * 50)

print("\n💰 SIMULATION DE COMPTE BANCAIRE")
print("-" * 31)


class CompteBancaire:
    def __init__(self, solde_initial=0):
        self.solde = solde_initial
        self.transactions = []

    def crediter(self, montant):
        self.solde += montant
        self.transactions.append(f"+{montant}€")
        return True

    def debiter(self, montant):
        if self.solde >= montant:
            self.solde -= montant
            self.transactions.append(f"-{montant}€")
            return True
        return False

    def afficher_solde(self):
        return self.solde


def simuler_guichet():
    """Simule un guichet automatique"""
    compte = CompteBancaire(1000)  # Solde initial 1000€

    # Simulation d'opérations
    operations = [
        ("retrait", 200),
        ("depot", 150),
        ("retrait", 2000),  # Devrait échouer
        ("retrait", 300),
        ("fin", 0)
    ]

    operation_index = 0

    while operation_index < len(operations):
        operation, montant = operations[operation_index]

        print(f"\n💳 Solde actuel : {compte.afficher_solde()}€")

        if operation == "retrait":
            print(f"🏧 Tentative de retrait : {montant}€")
            if compte.debiter(montant):
                print(f"✅ Retrait effectué")
            else:
                print(f"❌ Solde insuffisant")

        elif operation == "depot":
            print(f"💰 Dépôt : {montant}€")
            compte.crediter(montant)
            print(f"✅ Dépôt effectué")

        elif operation == "fin":
            print("👋 Session terminée")
            break

        operation_index += 1

    print(f"💰 Solde final : {compte.afficher_solde()}€")
    print(f"📋 Transactions : {', '.join(compte.transactions)}")


simuler_guichet()

print("\n🎲 JEU DE DEVINETTE")
print("-" * 18)


def jeu_devinette():
    """Jeu de devinette de nombre"""
    import random

    nombre_secret = random.randint(1, 100)
    tentatives = 0
    max_tentatives = 7
    trouve = False

    # Simulation de tentatives
    tentatives_test = [50, 75, 88, 82, 85, 87, 86]

    print("🎯 Devinez le nombre entre 1 et 100 !")
    print(f"🎮 Vous avez {max_tentatives} tentatives")
    print(f"🤫 (Nombre secret : {nombre_secret})")

    tentative_index = 0

    while tentatives < max_tentatives and not trouve and tentative_index < len(tentatives_test):
        tentatives += 1
        proposition = tentatives_test[tentative_index]

        print(f"\n🎯 Tentative {tentatives}: {proposition}")

        if proposition == nombre_secret:
            trouve = True
            print("🎉 BRAVO ! Vous avez trouvé !")
        elif proposition < nombre_secret:
            print("📈 Trop petit !")
        else:
            print("📉 Trop grand !")

        tentative_index += 1

    if not trouve:
        print(f"😞 Perdu ! Le nombre était {nombre_secret}")

    return trouve, tentatives


# Lancer le jeu
victoire, nb_tentatives = jeu_devinette()
performance = "Excellent" if nb_tentatives <= 3 else "Bien" if nb_tentatives <= 5 else "Peut mieux faire"
print(f"📊 Performance : {performance} ({nb_tentatives} tentatives)")

print("\n" + "=" * 50)
print("8. OPTIMISATIONS ET BONNES PRATIQUES")
print("=" * 50)

print("\n⚡ ÉVITER LES CALCULS RÉPÉTITIFS")
print("-" * 31)

# ❌ Mauvaise pratique
print("❌ MAUVAIS - Calcul répétitif :")
print("""
i = 0
while i < len(ma_liste):  # len() calculé à chaque itération !
    print(ma_liste[i])
    i += 1
""")

# ✅ Bonne pratique
print("✅ BON - Calcul une seule fois :")
ma_liste = [1, 2, 3, 4, 5]
longueur = len(ma_liste)  # Calculé une seule fois
i = 0

print("Affichage optimisé :")
while i < longueur:
    print(f"   ma_liste[{i}] = {ma_liste[i]}")
    i += 1

print("\n🎯 UTILISER DES FLAGS EXPLICITES")
print("-" * 30)


def chercher_avec_flag(liste, valeur):
    """Recherche avec flag explicite"""
    trouve = False
    index = 0
    position = -1

    while index < len(liste) and not trouve:
        if liste[index] == valeur:
            trouve = True
            position = index
        index += 1

    return trouve, position


# Test
test_liste = [10, 20, 30, 40, 50]
trouve, pos = chercher_avec_flag(test_liste, 30)
print(
    f"🔍 Recherche de 30 : {'✅ Trouvé' if trouve else '❌ Non trouvé'} à la position {pos}")

print("\n" + "=" * 50)
print("9. EXERCICES PRATIQUES")
print("=" * 50)

print("""
💪 EXERCICES À FAIRE (décommentez pour tester) :

# Exercice 1 : Table de multiplication
# def table_multiplication():
#     nombre = int(input("Table de quel nombre ? "))
#     i = 1
#     while i <= 10:
#         print(f"{nombre} x {i} = {nombre * i}")
#         i += 1

# Exercice 2 : Factorielle
# def calculer_factorielle():
#     n = int(input("Nombre : "))
#     if n < 0:
#         print("Impossible pour un nombre négatif")
#         return
#     
#     factorielle = 1
#     i = 1
#     while i <= n:
#         factorielle *= i
#         i += 1
#     print(f"{n}! = {factorielle}")

# Exercice 3 : Moyenne de notes
# def calculer_moyenne():
#     somme = 0
#     nombre_notes = 0
#     
#     while True:
#         note = input("Note (ou 'fin' pour terminer) : ")
#         if note.lower() == 'fin':
#             break
#         try:
#             note = float(note)
#             if 0 <= note <= 20:
#                 somme += note
#                 nombre_notes += 1
#             else:
#                 print("Note doit être entre 0 et 20")
#         except ValueError:
#             print("Entrez un nombre valide")
#     
#     if nombre_notes > 0:
#         moyenne = somme / nombre_notes
#         print(f"Moyenne : {moyenne:.2f}/20")
#     else:
#         print("Aucune note valide")

# Exercice 4 : PGCD (Plus Grand Commun Diviseur)
# def calculer_pgcd():
#     a = int(input("Premier nombre : "))
#     b = int(input("Deuxième nombre : "))
#     
#     while b != 0:
#         a, b = b, a % b
#     
#     print(f"PGCD : {a}")

# Exercice 5 : Suite de Syracuse
# def suite_syracuse():
#     n = int(input("Nombre de départ : "))
#     etapes = 0
#     
#     print(f"Suite de Syracuse pour {n} :")
#     while n != 1:
#         print(n, end=" → ")
#         if n % 2 == 0:
#             n = n // 2
#         else:
#             n = 3 * n + 1
#         etapes += 1
#     
#     print(f"1")
#     print(f"Nombre d'étapes : {etapes}")
""")

print("\n" + "=" * 50)
print("10. RÉSUMÉ FINAL")
print("=" * 50)

print("""
🎯 POINTS CLÉS À RETENIR :

1. 🔄 SYNTAXE WHILE :
   • while condition:
   • Indentation obligatoire
   • Modifier la condition dans la boucle !

2. ⚠️ ÉVITER LES PIÈGES :
   • Toujours modifier la variable de condition
   • Protéger contre les boucles infinies
   • Tester les cas limites

3. 🎯 APPLICATIONS COURANTES :
   • Validation de saisie
   • Menus interactifs
   • Algorithmes de recherche
   • Calculs itératifs

4. 🔍 WHILE...ELSE :
   • else s'exécute si boucle termine normalement
   • Pas d'exécution si break utilisé
   • Utile pour les recherches

5. ⚡ OPTIMISATIONS :
   • Éviter les calculs répétitifs
   • Utiliser des flags explicites
   • Limiter le nombre d'itérations

💡 FORMULE MAGIQUE pour while :
   Condition → Modification → Protection → Optimisation

🎉 Félicitations ! Vous maîtrisez la boucle while !
💡 Prochaine étape : Boucle for et itérations !
📚 While maîtrisé, passez aux boucles for !
""")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE - BOUCLE WHILE MAÎTRISÉE !")
print("=" * 70)
