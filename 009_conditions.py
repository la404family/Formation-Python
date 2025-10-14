#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
======================================================================
STRUCTURES CONDITIONNELLES EN PYTHON - GUIDE COMPLET
======================================================================

🎯 Ce fichier couvre toutes les structures conditionnelles :
   • if simple
   • if/else
   • if/elif/else
   • Conditions imbriquées
   • Opérateur ternaire
   • Match/case (Python 3.10+)

📚 Concepts abordés :
   • Syntaxe des conditions
   • Expressions booléennes
   • Conditions multiples
   • Bonnes pratiques
   • Cas d'usage avancés

💡 Objectif : Maîtriser toutes les structures de branchement
"""

print("=" * 70)
print("STRUCTURES CONDITIONNELLES EN PYTHON - GUIDE COMPLET")
print("=" * 70)

print("\n" + "=" * 50)
print("1. CONDITION IF SIMPLE")
print("=" * 50)

print("\n🎯 SYNTAXE DE BASE")
print("-" * 18)

age = 20
print(f"👤 Âge de l'utilisateur : {age} ans")

if age >= 18:
    print("✅ Vous êtes majeur !")
    print("   Vous pouvez voter.")

print("\n🔍 CONDITION AVEC VARIABLE BOOLÉENNE")
print("-" * 36)

est_connecte = True
print(f"🔐 Statut de connexion : {est_connecte}")

if est_connecte:
    print("✅ Bienvenue dans votre espace personnel !")

print("\n" + "=" * 50)
print("2. STRUCTURE IF/ELSE")
print("=" * 50)

print("\n⚖️ ALTERNATIVE BINAIRE")
print("-" * 21)

temperature = 15
print(f"🌡️ Température : {temperature}°C")

if temperature > 20:
    print("🌞 Il fait chaud, portez des vêtements légers")
else:
    print("🧥 Il fait frais, pensez à prendre un pull")

print("\n🎮 EXEMPLE AVEC SAISIE UTILISATEUR")
print("-" * 32)

# Simulation d'une entrée utilisateur
reponse = "oui"  # Remplace input("Voulez-vous continuer ? (oui/non) : ")
print(f"💬 Réponse de l'utilisateur : '{reponse}'")

if reponse.lower() == "oui":
    print("➡️ Continuation du programme...")
else:
    print("⏹️ Arrêt du programme.")

print("\n" + "=" * 50)
print("3. STRUCTURE IF/ELIF/ELSE")
print("=" * 50)

print("\n🎓 SYSTÈME DE NOTES")
print("-" * 18)

note = 85
print(f"📊 Note obtenue : {note}/100")

if note >= 90:
    mention = "Excellent"
    emoji = "🏆"
elif note >= 80:
    mention = "Très Bien"
    emoji = "🥇"
elif note >= 70:
    mention = "Bien"
    emoji = "🥈"
elif note >= 60:
    mention = "Assez Bien"
    emoji = "🥉"
elif note >= 50:
    mention = "Passable"
    emoji = "✅"
else:
    mention = "Insuffisant"
    emoji = "❌"

print(f"{emoji} Mention : {mention}")

print("\n🌤️ PRÉVISIONS MÉTÉO")
print("-" * 19)

temperature = 25
humidite = 60
vent = 15

print(f"🌡️ Température : {temperature}°C")
print(f"💧 Humidité : {humidite}%")
print(f"🌪️ Vent : {vent} km/h")

if temperature > 30 and humidite > 70:
    conseil = "Journée très chaude et humide - Restez hydratés !"
    icone = "🥵"
elif temperature > 25 and vent < 10:
    conseil = "Belle journée ensoleillée - Parfait pour sortir !"
    icone = "☀️"
elif temperature < 10 or vent > 30:
    conseil = "Temps difficile - Restez au chaud !"
    icone = "🌨️"
elif 15 <= temperature <= 25:
    conseil = "Temps agréable - Idéal pour les activités !"
    icone = "🌤️"
else:
    conseil = "Temps variable - Adaptez-vous !"
    icone = "🌥️"

print(f"{icone} Conseil : {conseil}")

print("\n" + "=" * 50)
print("4. CONDITIONS IMBRIQUÉES")
print("=" * 50)

print("\n🏪 SYSTÈME DE REMISE")
print("-" * 19)

montant_achat = 150
est_membre_vip = True
premiere_commande = False

print(f"💰 Montant : {montant_achat}€")
print(f"⭐ Membre VIP : {est_membre_vip}")
print(f"🆕 Première commande : {premiere_commande}")

if montant_achat >= 100:
    if est_membre_vip:
        if premiere_commande:
            remise = 25  # 25% pour VIP première commande
            type_remise = "VIP + Première commande"
        else:
            remise = 15  # 15% pour VIP normal
            type_remise = "VIP standard"
    else:
        if premiere_commande:
            remise = 10  # 10% pour première commande
            type_remise = "Première commande"
        else:
            remise = 5   # 5% remise standard
            type_remise = "Standard"
else:
    remise = 0
    type_remise = "Aucune"

if remise > 0:
    montant_final = montant_achat * (1 - remise/100)
    print(f"🎉 Remise : {remise}% ({type_remise})")
    print(f"💸 Montant final : {montant_final:.2f}€")
else:
    print("❌ Aucune remise applicable")

print("\n" + "=" * 50)
print("5. OPÉRATEUR TERNAIRE")
print("=" * 50)

print("\n❓ SYNTAXE CONDENSÉE")
print("-" * 19)

age = 16
print(f"👤 Âge : {age} ans")

# Opérateur ternaire (expression conditionnelle)
statut = "Majeur" if age >= 18 else "Mineur"
print(f"📋 Statut : {statut}")

# Comparaison avec if/else classique
if age >= 18:
    statut_classique = "Majeur"
else:
    statut_classique = "Mineur"
print(f"📋 Statut (méthode classique) : {statut_classique}")

print("\n💡 EXEMPLES PRATIQUES")
print("-" * 21)

# Déterminer le maximum
a, b = 15, 23
maximum = a if a > b else b
print(f"🔢 Maximum entre {a} et {b} : {maximum}")

# Pluriel automatique
nb_articles = 3
texte = f"{nb_articles} article{'s' if nb_articles > 1 else ''}"
print(f"📦 {texte}")

# Validation de saisie
email = "user@example.com"
validation = "✅ Email valide" if "@" in email else "❌ Email invalide"
print(f"📧 {validation}")

print("\n" + "=" * 50)
print("6. MATCH/CASE (PYTHON 3.10+)")
print("=" * 50)

print("\n🔄 NOUVELLE SYNTAXE MATCH")
print("-" * 25)

# Note : Cette section est informationnelle car match/case nécessite Python 3.10+
jour = "lundi"
print(f"📅 Jour de la semaine : {jour}")

print("""
💡 Avec match/case (Python 3.10+) :

match jour:
    case "lundi" | "mardi" | "mercredi" | "jeudi" | "vendredi":
        print("📚 Jour de travail")
    case "samedi" | "dimanche":
        print("🏖️ Weekend !")
    case _:
        print("❓ Jour inconnu")
""")

# Équivalent avec if/elif pour tous les Python
if jour in ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]:
    print("📚 Jour de travail (avec if/elif)")
elif jour in ["samedi", "dimanche"]:
    print("🏖️ Weekend ! (avec if/elif)")
else:
    print("❓ Jour inconnu (avec if/elif)")

print("\n" + "=" * 50)
print("7. EXPRESSIONS BOOLÉENNES AVANCÉES")
print("=" * 50)

print("\n🔗 COMBINAISONS COMPLEXES")
print("-" * 24)

utilisateur = {
    "nom": "Alice",
    "age": 28,
    "email": "alice@example.com",
    "actif": True,
    "premium": False
}

print(f"👤 Utilisateur : {utilisateur}")

# Conditions multiples
if (utilisateur["age"] >= 18 and
    utilisateur["actif"] and
        "@" in utilisateur["email"]):

    if utilisateur["premium"]:
        acces = "Accès Premium complet"
        emoji = "👑"
    else:
        acces = "Accès Standard"
        emoji = "👤"

    print(f"{emoji} {acces} accordé à {utilisateur['nom']}")
else:
    print("❌ Accès refusé - Conditions non remplies")

print("\n🎯 VALIDATION EN ÉTAPES")
print("-" * 23)


def valider_connexion(username, password, captcha_ok):
    """Valide une tentative de connexion"""
    print(f"🔐 Tentative de connexion : {username}")

    if not username:
        return "❌ Nom d'utilisateur requis"

    if len(password) < 8:
        return "❌ Mot de passe trop court"

    if not captcha_ok:
        return "❌ Captcha invalide"

    if username.lower() == "admin" and password == "admin123":
        return "⚠️ Identifiants par défaut - Changez le mot de passe !"

    return "✅ Connexion autorisée"


# Tests de validation
tests = [
    ("", "password123", True),
    ("user", "123", True),
    ("user", "password123", False),
    ("admin", "admin123", True),
    ("alice", "motdepasse2024", True)
]

for username, password, captcha in tests:
    resultat = valider_connexion(username, password, captcha)
    print(f"   {resultat}")

print("\n" + "=" * 50)
print("8. GESTION DES ERREURS AVEC CONDITIONS")
print("=" * 50)

print("\n⚠️ VALIDATION DÉFENSIVE")
print("-" * 22)


def calculer_moyenne(notes):
    """Calcule la moyenne avec validation"""
    print(f"📝 Notes reçues : {notes}")

    # Vérifications préalables
    if not notes:
        print("❌ Erreur : Liste de notes vide")
        return None

    if not isinstance(notes, list):
        print("❌ Erreur : Les notes doivent être dans une liste")
        return None

    # Validation de chaque note
    notes_valides = []
    for note in notes:
        if isinstance(note, (int, float)) and 0 <= note <= 20:
            notes_valides.append(note)
        else:
            print(f"⚠️ Note invalide ignorée : {note}")

    if not notes_valides:
        print("❌ Erreur : Aucune note valide")
        return None

    moyenne = sum(notes_valides) / len(notes_valides)
    print(f"✅ Moyenne calculée : {moyenne:.2f}/20")
    return moyenne


# Tests avec différents cas
donnees_test = [
    [15, 12, 18, 14],           # Cas normal
    [],                         # Liste vide
    [15, "abc", 12, -5, 25],   # Notes invalides
    "pas une liste",           # Type incorrect
    [16.5, 14.0, 17.5]         # Notes décimales
]

for donnees in donnees_test:
    print(f"\n🧪 Test avec : {donnees}")
    calculer_moyenne(donnees)

print("\n" + "=" * 50)
print("9. APPLICATIONS PRATIQUES")
print("=" * 50)

print("\n🏧 DISTRIBUTEUR AUTOMATIQUE")
print("-" * 26)


def distributeur_automatique():
    """Simule un distributeur automatique"""
    produits = {
        "1": {"nom": "Coca-Cola", "prix": 2.50, "stock": 5},
        "2": {"nom": "Eau", "prix": 1.00, "stock": 0},
        "3": {"nom": "Sandwich", "prix": 4.50, "stock": 3}
    }

    montant_insere = 3.00
    choix = "1"

    print(f"💰 Montant inséré : {montant_insere}€")
    print(f"🎯 Choix : {choix}")

    if choix not in produits:
        print("❌ Produit inexistant")
        return

    produit = produits[choix]

    if produit["stock"] == 0:
        print(f"❌ {produit['nom']} en rupture de stock")
        return

    if montant_insere < produit["prix"]:
        manque = produit["prix"] - montant_insere
        print(f"❌ Montant insuffisant - Il manque {manque:.2f}€")
        return

    # Achat réussi
    produit["stock"] -= 1
    monnaie = montant_insere - produit["prix"]

    print(f"✅ {produit['nom']} distribué !")
    if monnaie > 0:
        print(f"💰 Monnaie rendue : {monnaie:.2f}€")
    print(f"📦 Stock restant : {produit['stock']}")


distributeur_automatique()

print("\n🎮 SYSTÈME DE JEU")
print("-" * 17)


def evaluer_score_jeu(score, temps, vies_restantes):
    """Évalue la performance dans un jeu"""
    print(f"🎯 Score : {score}")
    print(f"⏱️ Temps : {temps}s")
    print(f"❤️ Vies restantes : {vies_restantes}")

    # Calcul du rang
    if score >= 10000 and temps <= 300 and vies_restantes >= 2:
        rang = "🏆 LÉGENDE"
        bonus = 500
    elif score >= 7500 and temps <= 450:
        rang = "⭐ EXPERT"
        bonus = 300
    elif score >= 5000 and vies_restantes > 0:
        rang = "🥈 AVANCÉ"
        bonus = 150
    elif score >= 2500:
        rang = "🥉 INTERMÉDIAIRE"
        bonus = 50
    elif score >= 1000:
        rang = "📈 DÉBUTANT"
        bonus = 10
    else:
        rang = "📚 NOVICE"
        bonus = 0

    score_final = score + bonus

    print(f"🏅 Rang obtenu : {rang}")
    print(f"🎁 Bonus : +{bonus} points")
    print(f"📊 Score final : {score_final}")


# Tests de performance
performances = [
    (12000, 250, 3),  # Performance exceptionnelle
    (8000, 400, 1),   # Bon joueur
    (3000, 600, 0),   # Joueur moyen
    (500, 800, 0)     # Débutant
]

for score, temps, vies in performances:
    print(f"\n🧪 Test de performance :")
    evaluer_score_jeu(score, temps, vies)

print("\n" + "=" * 50)
print("10. RÉSUMÉ FINAL")
print("=" * 50)

print("""
🎯 POINTS CLÉS À RETENIR :

1. 🎯 SYNTAXE DES CONDITIONS :
   • if condition:
   • elif autre_condition:
   • else:
   • Indentation obligatoire !

2. ⚖️ EXPRESSIONS BOOLÉENNES :
   • Utilisez and, or, not
   • Parenthèses pour clarifier
   • Attention à la priorité

3. 🔄 CHOIX DE STRUCTURE :
   • if simple : une seule condition
   • if/else : alternative binaire
   • if/elif/else : choix multiples

4. ❓ OPÉRATEUR TERNAIRE :
   • valeur_si_vrai if condition else valeur_si_faux
   • Pour des assignations simples
   • Plus concis mais moins lisible pour du complexe

5. 🏗️ CONDITIONS IMBRIQUÉES :
   • Possible mais attention à la lisibilité
   • Préférez plusieurs elif quand c'est possible
   • Commentez les logiques complexes

💡 FORMULE MAGIQUE pour les conditions :
   Clarté → Lisibilité → Tests → Optimisation

🎉 Félicitations ! Vous maîtrisez les conditions !
💡 Prochaine étape : Boucles et répétitions !
📚 Conditions maîtrisées, passez aux boucles !
""")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE - STRUCTURES CONDITIONNELLES MAÎTRISÉES !")
print("=" * 70)
