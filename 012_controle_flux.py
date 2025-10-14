#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
======================================================================
CONTRÔLE DE FLUX : BREAK, CONTINUE, PASS - GUIDE COMPLET
======================================================================

🎯 Ce fichier couvre les instructions de contrôle de flux :
   • break : sortir d'une boucle
   • continue : passer à l'itération suivante
   • pass : instruction vide (placeholder)
   • Applications dans for et while
   • Boucles imbriquées et contrôle
   • Bonnes pratiques et cas d'usage

📚 Concepts abordés :
   • Interruption de boucles
   • Saut d'itérations
   • Structures temporaires
   • Optimisation des performances
   • Patterns de programmation

💡 Objectif : Maîtriser le contrôle fin des boucles
"""

print("=" * 70)
print("CONTRÔLE DE FLUX : BREAK, CONTINUE, PASS - GUIDE COMPLET")
print("=" * 70)

print("\n" + "=" * 50)
print("1. L'INSTRUCTION BREAK")
print("=" * 50)

print("\n🛑 SORTIR D'UNE BOUCLE FOR")
print("-" * 24)

print("🔍 Recherche du premier nombre pair :")
nombres = [1, 3, 5, 8, 9, 11, 12, 15]
print(f"📋 Liste : {nombres}")

for nombre in nombres:
    print(f"   Vérification de {nombre}...")
    if nombre % 2 == 0:
        print(f"✅ Premier nombre pair trouvé : {nombre}")
        break
    print(f"   {nombre} est impair, on continue")
else:
    print("❌ Aucun nombre pair trouvé")

print("\n🛑 SORTIR D'UNE BOUCLE WHILE")
print("-" * 25)

print("🎯 Jeu de devinette avec break :")
nombre_secret = 42
tentative = 0
essais = [25, 50, 40, 42, 35]  # Simulation des essais

while tentative < len(essais):
    guess = essais[tentative]
    tentative += 1

    print(f"   Essai {tentative}: {guess}")

    if guess == nombre_secret:
        print(f"🎉 Bravo ! Trouvé en {tentative} tentatives !")
        break
    elif guess < nombre_secret:
        print("   📈 Trop petit !")
    else:
        print("   📉 Trop grand !")
else:
    print("😞 Nombre d'essais épuisé !")

print("\n" + "=" * 50)
print("2. L'INSTRUCTION CONTINUE")
print("=" * 50)

print("\n⏭️ IGNORER CERTAINES VALEURS")
print("-" * 26)

print("🔢 Affichage des nombres pairs seulement :")
for i in range(1, 11):
    if i % 2 != 0:  # Si impair
        continue    # Passer à l'itération suivante
    print(f"   Nombre pair : {i}")

print("\n📊 TRAITEMENT CONDITIONNEL")
print("-" * 25)

etudiants = [
    {"nom": "Alice", "note": 85},
    {"nom": "Bob", "note": -1},      # Note invalide
    {"nom": "Charlie", "note": 92},
    {"nom": "Diana", "note": 150},   # Note invalide
    {"nom": "Eve", "note": 78}
]

print("🎓 Traitement des notes valides (0-100) :")
for etudiant in etudiants:
    note = etudiant["note"]
    nom = etudiant["nom"]

    # Ignorer les notes invalides
    if note < 0 or note > 100:
        print(f"   ⚠️ {nom} : note invalide ({note}) - ignorée")
        continue

    # Traitement normal pour les notes valides
    if note >= 90:
        mention = "Excellent"
        emoji = "🏆"
    elif note >= 80:
        mention = "Très Bien"
        emoji = "🥇"
    elif note >= 70:
        mention = "Bien"
        emoji = "🥈"
    else:
        mention = "Assez Bien"
        emoji = "📚"

    print(f"   {emoji} {nom} : {note}/100 - {mention}")

print("\n" + "=" * 50)
print("3. L'INSTRUCTION PASS")
print("=" * 50)

print("\n📝 PLACEHOLDER POUR CODE FUTUR")
print("-" * 28)

print("💡 Utilisation de pass dans les structures :")

# Exemple de fonction temporaire


def fonction_a_implementer():
    """Cette fonction sera implémentée plus tard"""
    pass  # Évite l'erreur de syntaxe

# Exemple de classe temporaire


class MaClasseFuture:
    """Classe à développer"""
    pass


# Exemple de condition temporaire
age = 25
if age >= 18:
    pass  # TODO: implémenter la logique pour majeur
else:
    print("Mineur")

print("   ✅ Code sans erreur grâce à pass")

print("\n🔧 GESTION D'EXCEPTIONS TEMPORAIRE")
print("-" * 32)


def diviser_nombres():
    """Exemple avec gestion d'exception temporaire"""
    nombres = [10, 5, 0, 20]

    for nombre in nombres:
        try:
            resultat = 100 / nombre
            print(f"   100 / {nombre} = {resultat}")
        except ZeroDivisionError:
            pass  # Ignorer silencieusement la division par zéro
            print(f"   ⚠️ Division par zéro ignorée ({nombre})")


diviser_nombres()

print("\n" + "=" * 50)
print("4. CONTRÔLE DANS BOUCLES IMBRIQUÉES")
print("=" * 50)

print("\n🎯 BREAK DANS BOUCLES IMBRIQUÉES")
print("-" * 29)

print("🔍 Recherche dans matrice 2D :")
matrice = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

valeur_cherchee = 7
trouve = False

print(f"🎯 Recherche de {valeur_cherchee} :")

for i, ligne in enumerate(matrice):
    for j, valeur in enumerate(ligne):
        print(f"   Position ({i},{j}) : {valeur}")
        if valeur == valeur_cherchee:
            print(f"✅ {valeur_cherchee} trouvé en position ({i},{j}) !")
            trouve = True
            break
    if trouve:  # Sortir aussi de la boucle externe
        break

if not trouve:
    print(f"❌ {valeur_cherchee} non trouvé dans la matrice")

print("\n🔄 CONTINUE DANS BOUCLES IMBRIQUÉES")
print("-" * 33)

print("🎨 Génération de motif avec continue :")
for ligne in range(5):
    print(f"Ligne {ligne}: ", end="")
    for colonne in range(8):
        # Ignorer certaines positions pour créer un motif
        if (ligne + colonne) % 3 == 0:
            continue
        print("*", end="")
    print()  # Nouvelle ligne

print("\n" + "=" * 50)
print("5. PATTERNS DE PROGRAMMATION")
print("=" * 50)

print("\n🔍 PATTERN : RECHERCHE AVEC BREAK")
print("-" * 30)


def chercher_utilisateur(utilisateurs, email_cherche):
    """Recherche un utilisateur par email"""
    print(f"🔍 Recherche de l'email : {email_cherche}")

    for utilisateur in utilisateurs:
        print(f"   Vérification : {utilisateur['email']}")
        if utilisateur['email'] == email_cherche:
            print(f"✅ Utilisateur trouvé : {utilisateur['nom']}")
            return utilisateur

    print("❌ Utilisateur non trouvé")
    return None


# Test du pattern
users = [
    {"nom": "Alice", "email": "alice@example.com"},
    {"nom": "Bob", "email": "bob@example.com"},
    {"nom": "Charlie", "email": "charlie@example.com"}
]

resultat = chercher_utilisateur(users, "bob@example.com")

print("\n📊 PATTERN : FILTRAGE AVEC CONTINUE")
print("-" * 33)


def filtrer_donnees_valides(donnees):
    """Filtre et traite seulement les données valides"""
    resultats = []

    print("📋 Filtrage des données :")
    for item in donnees:
        # Ignorer les données nulles ou vides
        if not item or not isinstance(item, dict):
            print(f"   ⚠️ Donnée invalide ignorée : {item}")
            continue

        # Ignorer les données sans champ obligatoire
        if 'valeur' not in item:
            print(f"   ⚠️ Champ 'valeur' manquant : {item}")
            continue

        # Ignorer les valeurs négatives
        if item['valeur'] < 0:
            print(f"   ⚠️ Valeur négative ignorée : {item['valeur']}")
            continue

        # Traitement de la donnée valide
        item['valeur_traitee'] = item['valeur'] * 2
        resultats.append(item)
        print(f"   ✅ Traité : {item}")

    return resultats


# Test du filtrage
donnees_test = [
    {"nom": "A", "valeur": 10},
    None,
    {"nom": "B", "valeur": -5},
    {"nom": "C"},  # Sans valeur
    {"nom": "D", "valeur": 20},
    "donnée_invalide"
]

resultats_filtres = filtrer_donnees_valides(donnees_test)
print(f"📊 Résultats finaux : {len(resultats_filtres)} éléments traités")

print("\n" + "=" * 50)
print("6. OPTIMISATION AVEC CONTRÔLE DE FLUX")
print("=" * 50)

print("\n⚡ ÉVITER LES CALCULS INUTILES")
print("-" * 29)


def calculer_statistiques_optimise(nombres):
    """Calcul optimisé avec break et continue"""
    print(f"📊 Analyse de {len(nombres)} nombres...")

    positifs = 0
    negatifs = 0
    zeros = 0
    somme = 0

    for i, nombre in enumerate(nombres):
        # Arrêter si on a analysé assez d'échantillons
        if i >= 100:  # Limite pour de gros datasets
            print(f"   ⚡ Analyse limitée aux 100 premiers éléments")
            break

        # Ignorer les valeurs non numériques
        if not isinstance(nombre, (int, float)):
            print(f"   ⚠️ Valeur non numérique ignorée : {nombre}")
            continue

        # Calculs statistiques
        if nombre > 0:
            positifs += 1
        elif nombre < 0:
            negatifs += 1
        else:
            zeros += 1

        somme += nombre

    total_analyses = positifs + negatifs + zeros

    if total_analyses > 0:
        moyenne = somme / total_analyses
        print(f"📈 Statistiques :")
        print(f"   Positifs : {positifs}")
        print(f"   Négatifs : {negatifs}")
        print(f"   Zéros : {zeros}")
        print(f"   Moyenne : {moyenne:.2f}")
    else:
        print("❌ Aucune donnée valide à analyser")


# Test avec données mixtes
donnees_mixtes = [1, 2, -3, 0, 4, "abc", 5, None, 6, -7, 8, 0, 9]
calculer_statistiques_optimise(donnees_mixtes)

print("\n" + "=" * 50)
print("7. VALIDATION ET CONTRÔLE DE QUALITÉ")
print("=" * 50)

print("\n✅ VALIDATION AVEC CONTINUE")
print("-" * 26)


def valider_mots_de_passe(mots_de_passe):
    """Valide une liste de mots de passe"""
    mots_valides = []

    print("🔐 Validation des mots de passe :")

    for i, mdp in enumerate(mots_de_passe, 1):
        print(f"\n   Mot de passe #{i}: '{mdp}'")

        # Vérification longueur minimum
        if len(mdp) < 8:
            print("   ❌ Trop court (< 8 caractères)")
            continue

        # Vérification caractères
        a_majuscule = False
        a_minuscule = False
        a_chiffre = False
        a_special = False

        for char in mdp:
            if char.isupper():
                a_majuscule = True
            elif char.islower():
                a_minuscule = True
            elif char.isdigit():
                a_chiffre = True
            elif char in "!@#$%^&*()_+-=[]{}|;:,.<>?":
                a_special = True

        # Vérifications des critères
        if not a_majuscule:
            print("   ❌ Manque une majuscule")
            continue

        if not a_minuscule:
            print("   ❌ Manque une minuscule")
            continue

        if not a_chiffre:
            print("   ❌ Manque un chiffre")
            continue

        if not a_special:
            print("   ❌ Manque un caractère spécial")
            continue

        # Mot de passe valide
        print("   ✅ Mot de passe VALIDE")
        mots_valides.append(mdp)

    print(
        f"\n📊 Résumé : {len(mots_valides)}/{len(mots_de_passe)} mots de passe valides")
    return mots_valides


# Test de validation
mdp_test = [
    "motdepasse",           # Trop simple
    "MotDePasse123!",       # Valide
    "abc",                  # Trop court
    "PASSWORD123!",         # Pas de minuscule
    "password123!",         # Pas de majuscule
    "MotDePasse!",          # Pas de chiffre
    "MotDePasse123",        # Pas de spécial
    "SecurE2024@"           # Valide
]

mots_valides = valider_mots_de_passe(mdp_test)

print("\n" + "=" * 50)
print("8. APPLICATIONS PRATIQUES")
print("=" * 50)

print("\n🎮 JEU AVEC CONTRÔLE DE FLUX")
print("-" * 26)


def jeu_nombre_mystere():
    """Jeu du nombre mystère avec contrôle de flux"""
    import random

    nombre_secret = random.randint(1, 100)
    tentatives_max = 7
    tentative = 0

    # Simulation des essais
    essais_joueur = [50, 75, 62, 68, 71, 69, 70]

    print("🎯 JEU DU NOMBRE MYSTÈRE")
    print(f"🎮 Devinez le nombre entre 1 et 100 ({tentatives_max} tentatives)")
    print(f"🤫 (Nombre secret: {nombre_secret})")

    for essai in essais_joueur:
        tentative += 1
        print(f"\n🎯 Tentative {tentative}: {essai}")

        if essai == nombre_secret:
            print("🎉 FÉLICITATIONS ! Vous avez trouvé !")
            score = (tentatives_max - tentative + 1) * 10
            print(f"🏆 Score: {score} points")
            break
        elif essai < nombre_secret:
            print("📈 Trop petit !")
        else:
            print("📉 Trop grand !")

        # Vérifier s'il reste des tentatives
        if tentative >= tentatives_max:
            print(f"😞 PERDU ! Le nombre était {nombre_secret}")
            break
        else:
            reste = tentatives_max - tentative
            print(
                f"💡 Il vous reste {reste} tentative{'s' if reste > 1 else ''}")


jeu_nombre_mystere()

print("\n🏪 SYSTÈME DE CAISSE")
print("-" * 19)


def traiter_commandes(commandes):
    """Traite les commandes avec gestion d'erreurs"""
    total_ca = 0
    commandes_traitees = 0

    print("🛒 Traitement des commandes :")

    for i, commande in enumerate(commandes, 1):
        print(f"\n📦 Commande #{i}: {commande}")

        # Vérifier la structure de la commande
        if not isinstance(commande, dict):
            print("   ❌ Format de commande invalide - ignorée")
            continue

        # Vérifier les champs obligatoires
        if 'produit' not in commande or 'quantite' not in commande or 'prix' not in commande:
            print("   ❌ Champs manquants - commande ignorée")
            continue

        # Vérifier la quantité
        if commande['quantite'] <= 0:
            print("   ❌ Quantité invalide - commande ignorée")
            continue

        # Vérifier le prix
        if commande['prix'] <= 0:
            print("   ❌ Prix invalide - commande ignorée")
            continue

        # Calculer le montant
        montant = commande['quantite'] * commande['prix']

        # Vérifier le montant maximum
        if montant > 1000:
            print(f"   ⚠️ Montant élevé ({montant}€) - validation requise")
            # Dans un vrai système, on pourrait demander une validation
            print("   ✅ Validation accordée")

        # Traitement réussi
        total_ca += montant
        commandes_traitees += 1
        print(
            f"   ✅ {commande['produit']} - {commande['quantite']} × {commande['prix']}€ = {montant}€")

    print(f"\n📊 BILAN :")
    print(f"   Commandes traitées : {commandes_traitees}/{len(commandes)}")
    print(f"   Chiffre d'affaires : {total_ca}€")


# Test du système
commandes_test = [
    {"produit": "Ordinateur", "quantite": 1, "prix": 800},
    {"produit": "Souris", "quantite": -2, "prix": 25},  # Quantité invalide
    {"produit": "Clavier", "prix": 60},                 # Quantité manquante
    None,                                               # Commande nulle
    {"produit": "Écran", "quantite": 2, "prix": 300},
    {"produit": "Serveur", "quantite": 1, "prix": 1200},  # Montant élevé
    "commande_invalide"                                 # Format invalide
]

traiter_commandes(commandes_test)

print("\n" + "=" * 50)
print("9. EXERCICES PRATIQUES")
print("=" * 50)

print("""
💪 EXERCICES À FAIRE (décommentez pour tester) :

# Exercice 1 : Saisie jusqu'à valeur valide
# def saisie_securisee():
#     while True:
#         try:
#             valeur = input("Entrez un nombre entre 1 et 100 : ")
#             nombre = int(valeur)
#             
#             if 1 <= nombre <= 100:
#                 print(f"Valeur valide : {nombre}")
#                 break
#             else:
#                 print("Nombre hors intervalle !")
#                 continue
#         except ValueError:
#             print("Ce n'est pas un nombre !")
#             continue

# Exercice 2 : Menu avec contrôle
# def menu_principal():
#     while True:
#         print("\\n=== MENU ===")
#         print("1. Option 1")
#         print("2. Option 2") 
#         print("3. Quitter")
#         
#         choix = input("Votre choix : ")
#         
#         if choix == "1":
#             print("Option 1 sélectionnée")
#             continue
#         elif choix == "2":
#             print("Option 2 sélectionnée")
#             continue
#         elif choix == "3":
#             print("Au revoir !")
#             break
#         else:
#             print("Choix invalide !")
#             continue

# Exercice 3 : Nettoyage de données
# def nettoyer_donnees():
#     donnees = [1, 2, "abc", 4, None, 6, -1, 8, "", 10]
#     donnees_propres = []
#     
#     for item in donnees:
#         if item is None or item == "":
#             continue
#         
#         if not isinstance(item, (int, float)):
#             continue
#         
#         if item < 0:
#             continue
#         
#         donnees_propres.append(item)
#     
#     print(f"Données originales : {donnees}")
#     print(f"Données nettoyées : {donnees_propres}")

# Exercice 4 : Recherche multicritères
# def recherche_produits():
#     produits = [
#         {"nom": "Laptop", "prix": 800, "stock": 5},
#         {"nom": "Souris", "prix": 25, "stock": 0},
#         {"nom": "Clavier", "prix": 60, "stock": 10},
#         {"nom": "Écran", "prix": 300, "stock": 3}
#     ]
#     
#     prix_max = 100
#     stock_min = 1
#     
#     print(f"Recherche : prix ≤ {prix_max}€ et stock ≥ {stock_min}")
#     
#     for produit in produits:
#         if produit["prix"] > prix_max:
#             continue
#         
#         if produit["stock"] < stock_min:
#             continue
#         
#         print(f"✅ {produit['nom']} - {produit['prix']}€ (stock: {produit['stock']})")

# Exercice 5 : Génération de rapport
# def generer_rapport():
#     ventes = [100, 150, -50, 200, 0, 300, "abc", 400, None, 250]
#     
#     total_ventes = 0
#     nb_ventes_valides = 0
#     ventes_importantes = []
#     
#     for vente in ventes:
#         if not isinstance(vente, (int, float)):
#             continue
#         
#         if vente <= 0:
#             continue
#         
#         total_ventes += vente
#         nb_ventes_valides += 1
#         
#         if vente >= 200:
#             ventes_importantes.append(vente)
#     
#     if nb_ventes_valides > 0:
#         moyenne = total_ventes / nb_ventes_valides
#         print(f"Total : {total_ventes}€")
#         print(f"Moyenne : {moyenne:.2f}€")
#         print(f"Ventes importantes : {ventes_importantes}")
""")

print("\n" + "=" * 50)
print("10. RÉSUMÉ FINAL")
print("=" * 50)

print("""
🎯 POINTS CLÉS À RETENIR :

1. 🛑 BREAK :
   • Sort immédiatement de la boucle
   • Fonctionne avec for et while
   • Utile pour recherches et conditions d'arrêt

2. ⏭️ CONTINUE :
   • Passe à l'itération suivante
   • Ignore le reste du code de la boucle
   • Parfait pour filtrer des données

3. 📝 PASS :
   • Instruction vide (ne fait rien)
   • Évite les erreurs de syntaxe
   • Placeholder pour code futur

4. 🎯 BOUCLES IMBRIQUÉES :
   • break sort seulement de la boucle courante
   • Utiliser des flags pour sortir complètement
   • continue affecte la boucle courante

5. ⚡ OPTIMISATION :
   • Éviter les calculs inutiles avec continue
   • Arrêter tôt avec break
   • Améliorer les performances

💡 FORMULE MAGIQUE pour le contrôle :
   Condition → Action → Optimisation → Lisibilité

🎉 Félicitations ! Vous maîtrisez le contrôle de flux !
💡 Prochaine étape : Structures de données !
📚 Contrôle de flux maîtrisé, passez aux listes !
""")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE - CONTRÔLE DE FLUX MAÎTRISÉ !")
print("=" * 70)
