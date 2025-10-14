#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
======================================================================
DÉFINITION DE FONCTIONS EN PYTHON - GUIDE COMPLET
======================================================================

🎯 Ce fichier couvre la définition des fonctions en détail :
   • Syntaxe et création de fonctions
   • Paramètres et arguments
   • Valeurs de retour
   • Documentation et annotations
   • Fonctions imbriquées
   • Bonnes pratiques et design

📚 Concepts abordés :
   • def et return
   • Paramètres positionnels et nommés
   • Valeurs par défaut
   • Docstrings et annotations
   • Fonctions comme objets
   • Scope et visibilité

💡 Objectif : Maîtriser la création et l'organisation du code en fonctions
"""

print("=" * 70)
print("DÉFINITION DE FONCTIONS EN PYTHON - GUIDE COMPLET")
print("=" * 70)

print("\n" + "=" * 50)
print("1. SYNTAXE FONDAMENTALE")
print("=" * 50)

print("\n📝 STRUCTURE DE BASE")
print("-" * 19)

# Fonction la plus simple


def dire_bonjour():
    """Fonction sans paramètre ni retour"""
    print("Bonjour !")


# Appel de la fonction
print("🔧 Fonction simple :")
dire_bonjour()

# Fonction avec paramètre


def saluer(nom):
    """Fonction avec un paramètre"""
    print(f"Bonjour {nom} !")


print("\n🔧 Fonction avec paramètre :")
saluer("Alice")
saluer("Bob")

# Fonction avec retour


def additionner(a, b):
    """Fonction qui retourne une valeur"""
    return a + b


print("\n🔧 Fonction avec retour :")
resultat = additionner(5, 3)
print(f"5 + 3 = {resultat}")

print("\n📊 ANATOMIE D'UNE FONCTION")
print("-" * 26)


def fonction_complete(parametre1, parametre2="valeur_defaut"):
    """
    Documentation de la fonction (docstring).

    Args:
        parametre1: Description du premier paramètre
        parametre2: Description du second paramètre (optionnel)

    Returns:
        Description de ce que retourne la fonction
    """
    # Corps de la fonction
    resultat = parametre1 + parametre2
    return resultat


print("🏗️ Éléments d'une fonction :")
print("   • def : mot-clé de définition")
print("   • nom_fonction : identifiant unique")
print("   • (paramètres) : liste des paramètres")
print("   • : début du bloc de code")
print("   • docstring : documentation optionnelle")
print("   • corps : instructions à exécuter")
print("   • return : valeur de retour (optionnel)")

print("\n" + "=" * 50)
print("2. PARAMÈTRES ET ARGUMENTS")
print("=" * 50)

print("\n🎯 PARAMÈTRES POSITIONNELS")
print("-" * 26)


def calculer_rectangle(longueur, largeur):
    """Calcule l'aire et le périmètre d'un rectangle"""
    aire = longueur * largeur
    perimetre = 2 * (longueur + largeur)
    return aire, perimetre


# Appel avec arguments positionnels
aire, perimetre = calculer_rectangle(5, 3)
print(f"📐 Rectangle 5×3 : aire = {aire}, périmètre = {perimetre}")

# L'ordre des arguments est important !
aire2, perimetre2 = calculer_rectangle(3, 5)  # Différent !
print(f"📐 Rectangle 3×5 : aire = {aire2}, périmètre = {perimetre2}")

print("\n🏷️ PARAMÈTRES NOMMÉS (KEYWORD)")
print("-" * 32)


def presenter_personne(nom, age, ville="Non spécifiée", profession="Non spécifiée"):
    """Présente une personne avec ses informations"""
    print(f"👤 {nom}, {age} ans")
    print(f"   Ville : {ville}")
    print(f"   Profession : {profession}")


print("🔧 Appels avec paramètres nommés :")

# Appel mixte (positionnel puis nommé)
presenter_personne("Alice", 25, ville="Paris")

# Appel entièrement nommé (ordre libre)
presenter_personne(profession="Développeuse", nom="Bob", age=30, ville="Lyon")

# Appel avec valeurs par défaut
presenter_personne("Charlie", 28)

print("\n⭐ VALEURS PAR DÉFAUT")
print("-" * 20)


def configurer_serveur(host="localhost", port=8080, debug=False):
    """Configure un serveur avec des valeurs par défaut"""
    config = {
        "host": host,
        "port": port,
        "debug": debug
    }
    return config


print("⚙️ Configurations serveur :")

# Toutes les valeurs par défaut
config1 = configurer_serveur()
print(f"   Défaut : {config1}")

# Quelques modifications
config2 = configurer_serveur(port=3000, debug=True)
print(f"   Modifié : {config2}")

# Configuration complète
config3 = configurer_serveur("prod-server.com", 443, False)
print(f"   Production : {config3}")

print("\n⚠️ PIÈGE DES VALEURS MUTABLES")
print("-" * 30)

# MAUVAIS : valeur par défaut mutable


def mauvaise_fonction(element, liste=[]):  # PIÈGE !
    """Ne jamais faire ça !"""
    liste.append(element)
    return liste


print("❌ Problème avec valeur mutable par défaut :")
resultat1 = mauvaise_fonction("a")
resultat2 = mauvaise_fonction("b")  # Utilise la même liste !
print(f"   Premier appel : {resultat1}")
print(f"   Second appel : {resultat2}")  # Contient "a" et "b" !

# CORRECT : utiliser None et créer une nouvelle liste


def bonne_fonction(element, liste=None):
    """Version correcte"""
    if liste is None:
        liste = []
    liste.append(element)
    return liste


print("\n✅ Version corrigée :")
resultat3 = bonne_fonction("x")
resultat4 = bonne_fonction("y")
print(f"   Premier appel : {resultat3}")
print(f"   Second appel : {resultat4}")

print("\n" + "=" * 50)
print("3. VALEURS DE RETOUR")
print("=" * 50)

print("\n↩️ RETURN SIMPLE")
print("-" * 15)


def calculer_carre(nombre):
    """Retourne le carré d'un nombre"""
    return nombre ** 2


def est_pair(nombre):
    """Retourne True si le nombre est pair"""
    return nombre % 2 == 0


print("🔢 Retours simples :")
print(f"   Carré de 7 : {calculer_carre(7)}")
print(f"   8 est pair ? {est_pair(8)}")
print(f"   7 est pair ? {est_pair(7)}")

print("\n📦 RETOURS MULTIPLES")
print("-" * 20)


def analyser_nombre(n):
    """Analyse un nombre et retourne plusieurs informations"""
    carre = n ** 2
    cube = n ** 3
    est_positif = n > 0
    est_pair = n % 2 == 0

    return carre, cube, est_positif, est_pair


# Déballage des retours multiples
nombre_test = 4
carre, cube, positif, pair = analyser_nombre(nombre_test)

print(f"🔍 Analyse de {nombre_test} :")
print(f"   Carré : {carre}")
print(f"   Cube : {cube}")
print(f"   Positif : {positif}")
print(f"   Pair : {pair}")

# On peut aussi récupérer le tuple complet
resultats = analyser_nombre(-3)
print(f"🔍 Analyse de -3 (tuple) : {resultats}")

print("\n🔄 RETURN CONDITIONNEL")
print("-" * 21)


def classifier_age(age):
    """Classifie une personne selon son âge"""
    if age < 0:
        return "Âge invalide"
    elif age < 13:
        return "Enfant"
    elif age < 20:
        return "Adolescent"
    elif age < 60:
        return "Adulte"
    else:
        return "Senior"


print("👥 Classification par âge :")
ages_test = [5, 16, 30, 65, -2]
for age in ages_test:
    classification = classifier_age(age)
    print(f"   {age} ans → {classification}")

print("\n🔚 RETURN PRÉCOCE (EARLY RETURN)")
print("-" * 33)


def valider_email(email):
    """Valide un email avec returns précoces"""

    # Vérifications avec returns précoces
    if not email:
        return False, "Email vide"

    if "@" not in email:
        return False, "Pas de symbole @"

    if "." not in email.split("@")[-1]:
        return False, "Pas de point dans le domaine"

    if len(email) < 5:
        return False, "Email trop court"

    # Si toutes les vérifications passent
    return True, "Email valide"


print("📧 Validation d'emails :")
emails_test = ["alice@test.com", "bob@", "invalid", "", "ok@site.fr"]
for email in emails_test:
    valide, message = valider_email(email)
    statut = "✅" if valide else "❌"
    print(f"   {email:<15} : {statut} {message}")

print("\n" + "=" * 50)
print("4. DOCUMENTATION DES FONCTIONS")
print("=" * 50)

print("\n📚 DOCSTRINGS")
print("-" * 12)


def calculer_moyenne(nombres):
    """
    Calcule la moyenne arithmétique d'une liste de nombres.

    Cette fonction prend une liste de nombres et retourne leur moyenne.
    Si la liste est vide, retourne 0.

    Args:
        nombres (list): Liste de nombres (int ou float)

    Returns:
        float: La moyenne des nombres, ou 0 si liste vide

    Raises:
        TypeError: Si la liste contient des éléments non numériques

    Examples:
        >>> calculer_moyenne([1, 2, 3, 4, 5])
        3.0
        >>> calculer_moyenne([])
        0
    """
    if not nombres:
        return 0

    return sum(nombres) / len(nombres)


# Accès à la documentation
print("📖 Documentation de la fonction :")
print(f"   Nom : {calculer_moyenne.__name__}")
print(f"   Doc : {calculer_moyenne.__doc__[:100]}...")

# Test de la fonction
test_nombres = [10, 20, 30, 40, 50]
moyenne = calculer_moyenne(test_nombres)
print(f"🔢 Moyenne de {test_nombres} : {moyenne}")

print("\n🏷️ ANNOTATIONS DE TYPE (TYPE HINTS)")
print("-" * 35)


def multiplier_prix(prix: float, quantite: int, remise: float = 0.0) -> float:
    """
    Calcule le prix total avec remise éventuelle.

    Args:
        prix: Prix unitaire
        quantite: Nombre d'articles
        remise: Pourcentage de remise (0.0 à 1.0)

    Returns:
        Prix total après remise
    """
    prix_brut = prix * quantite
    prix_net = prix_brut * (1 - remise)
    return prix_net


print("💰 Calcul de prix avec annotations :")
print(f"   10€ × 3, remise 10% : {multiplier_prix(10.0, 3, 0.1):.2f}€")

# Les annotations sont accessibles
print(f"🏷️ Annotations : {multiplier_prix.__annotations__}")

print("\n📝 STYLES DE DOCSTRINGS")
print("-" * 24)


def fonction_style_google(param1: str, param2: int) -> bool:
    """Docstring style Google.

    Description détaillée de la fonction.

    Args:
        param1: Description du premier paramètre
        param2: Description du second paramètre

    Returns:
        Description de la valeur de retour

    Raises:
        ValueError: Quand et pourquoi cette exception est levée
    """
    return len(param1) > param2


def fonction_style_numpy(param1, param2):
    """
    Docstring style NumPy.

    Description détaillée de la fonction.

    Parameters
    ----------
    param1 : str
        Description du premier paramètre
    param2 : int
        Description du second paramètre

    Returns
    -------
    bool
        Description de la valeur de retour
    """
    return len(param1) > param2


print("📄 Différents styles de documentation disponibles")
print("   • Google Style (recommandé pour simplicité)")
print("   • NumPy Style (pour projets scientifiques)")
print("   • Sphinx Style (pour documentation avancée)")

print("\n" + "=" * 50)
print("5. FONCTIONS COMME OBJETS")
print("=" * 50)

print("\n🎭 FONCTIONS SONT DES OBJETS")
print("-" * 27)


def dire_bonjour_fr():
    return "Bonjour !"


def dire_bonjour_en():
    return "Hello !"


def dire_bonjour_es():
    return "¡Hola !"


# Stocker des fonctions dans des variables
salutation = dire_bonjour_fr
print(f"🗣️ Salutation française : {salutation()}")

# Stocker des fonctions dans une liste
salutations = [dire_bonjour_fr, dire_bonjour_en, dire_bonjour_es]
print("🌍 Salutations multilingues :")
for i, func in enumerate(salutations):
    print(f"   Langue {i+1} : {func()}")

# Stocker des fonctions dans un dictionnaire
salutations_dict = {
    "français": dire_bonjour_fr,
    "anglais": dire_bonjour_en,
    "espagnol": dire_bonjour_es
}

print("🗺️ Salutations par langue :")
for langue, func in salutations_dict.items():
    print(f"   {langue.capitalize()} : {func()}")

print("\n🔄 FONCTIONS COMME PARAMÈTRES")
print("-" * 29)


def appliquer_operation(nombres, operation):
    """Applique une opération à une liste de nombres"""
    return [operation(x) for x in nombres]


def au_carre(x):
    return x ** 2


def au_cube(x):
    return x ** 3


def doubler(x):
    return x * 2


# Test avec différentes opérations
nombres_test = [1, 2, 3, 4, 5]
print(f"🔢 Nombres originaux : {nombres_test}")

resultats_carre = appliquer_operation(nombres_test, au_carre)
print(f"🔢 Au carré : {resultats_carre}")

resultats_cube = appliquer_operation(nombres_test, au_cube)
print(f"🔢 Au cube : {resultats_cube}")

resultats_double = appliquer_operation(nombres_test, doubler)
print(f"🔢 Doublés : {resultats_double}")

print("\n🏭 FONCTIONS QUI RETOURNENT DES FONCTIONS")
print("-" * 38)


def creer_multiplicateur(facteur):
    """Crée une fonction qui multiplie par un facteur donné"""
    def multiplicateur(x):
        return x * facteur
    return multiplicateur


# Création de fonctions spécialisées
double = creer_multiplicateur(2)
triple = creer_multiplicateur(3)
dizaine = creer_multiplicateur(10)

print("🏭 Fonctions générées :")
nombre_test = 7
print(f"   {nombre_test} × 2 = {double(nombre_test)}")
print(f"   {nombre_test} × 3 = {triple(nombre_test)}")
print(f"   {nombre_test} × 10 = {dizaine(nombre_test)}")

print("\n" + "=" * 50)
print("6. FONCTIONS IMBRIQUÉES")
print("=" * 50)

print("\n🪆 DÉFINITION DE FONCTIONS INTERNES")
print("-" * 33)


def calculateur_avance():
    """Fonction conteneur avec fonctions internes"""

    def additionner(a, b):
        """Fonction interne pour additionner"""
        return a + b

    def soustraire(a, b):
        """Fonction interne pour soustraire"""
        return a - b

    def multiplier(a, b):
        """Fonction interne pour multiplier"""
        return a * b

    def diviser(a, b):
        """Fonction interne pour diviser"""
        if b == 0:
            return "Division par zéro impossible"
        return a / b

    # Retourner un dictionnaire de fonctions
    return {
        "add": additionner,
        "sub": soustraire,
        "mul": multiplier,
        "div": diviser
    }


# Utilisation
calc = calculateur_avance()
print("🧮 Calculateur avancé :")
print(f"   10 + 5 = {calc['add'](10, 5)}")
print(f"   10 - 5 = {calc['sub'](10, 5)}")
print(f"   10 × 5 = {calc['mul'](10, 5)}")
print(f"   10 ÷ 5 = {calc['div'](10, 5)}")

print("\n🔒 ENCAPSULATION ET FERMETURE")
print("-" * 30)


def creer_compteur(initial=0):
    """Crée un compteur avec état encapsulé"""

    # Variable privée (encapsulée)
    count = initial

    def incrementer():
        nonlocal count  # Modifier la variable de la portée externe
        count += 1
        return count

    def decrementer():
        nonlocal count
        count -= 1
        return count

    def obtenir_valeur():
        return count

    def reinitialiser():
        nonlocal count
        count = initial
        return count

    # Retourner les fonctions (closure)
    return {
        "inc": incrementer,
        "dec": decrementer,
        "get": obtenir_valeur,
        "reset": reinitialiser
    }


# Test du compteur
compteur = creer_compteur(10)
print("📊 Compteur avec fermeture :")
print(f"   Valeur initiale : {compteur['get']()}")
print(f"   Après inc() : {compteur['inc']()}")
print(f"   Après inc() : {compteur['inc']()}")
print(f"   Après dec() : {compteur['dec']()}")
print(f"   Après reset() : {compteur['reset']()}")

print("\n🔄 DÉCORATEURS SIMPLES")
print("-" * 22)


def mesurer_temps(func):
    """Décorateur simple pour mesurer le temps d'exécution"""
    import time

    def wrapper(*args, **kwargs):
        debut = time.time()
        resultat = func(*args, **kwargs)
        fin = time.time()
        duree = (fin - debut) * 1000  # en millisecondes
        print(f"⏱️ {func.__name__} exécutée en {duree:.2f}ms")
        return resultat

    return wrapper

# Utilisation du décorateur


@mesurer_temps
def calcul_lent():
    """Fonction qui simule un calcul lent"""
    import time
    time.sleep(0.1)  # Simulation de 100ms
    return sum(range(10000))


print("🐌 Test de fonction avec mesure de temps :")
resultat = calcul_lent()
print(f"   Résultat : {resultat}")

print("\n" + "=" * 50)
print("7. APPLICATIONS PRATIQUES")
print("=" * 50)

print("\n🧰 BOÎTE À OUTILS MATHÉMATIQUES")
print("-" * 31)


def outils_math():
    """Collection d'outils mathématiques"""

    def factorielle(n):
        """Calcule la factorielle de n"""
        if n < 0:
            return None
        if n <= 1:
            return 1
        return n * factorielle(n - 1)

    def pgcd(a, b):
        """Calcule le PGCD de deux nombres (algorithme d'Euclide)"""
        while b:
            a, b = b, a % b
        return a

    def ppcm(a, b):
        """Calcule le PPCM de deux nombres"""
        return abs(a * b) // pgcd(a, b)

    def est_premier(n):
        """Vérifie si un nombre est premier"""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def fibonacci(n):
        """Calcule le n-ième terme de Fibonacci"""
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    return {
        "factorielle": factorielle,
        "pgcd": pgcd,
        "ppcm": ppcm,
        "est_premier": est_premier,
        "fibonacci": fibonacci
    }


# Test des outils mathématiques
math_tools = outils_math()

print("🔢 Tests d'outils mathématiques :")
print(f"   5! = {math_tools['factorielle'](5)}")
print(f"   PGCD(48, 18) = {math_tools['pgcd'](48, 18)}")
print(f"   PPCM(48, 18) = {math_tools['ppcm'](48, 18)}")
print(f"   17 est premier ? {math_tools['est_premier'](17)}")
print(f"   10ème Fibonacci : {math_tools['fibonacci'](10)}")

print("\n💰 SYSTÈME DE CALCUL DE PRIX")
print("-" * 29)


def systeme_prix():
    """Système de calcul de prix avec différentes stratégies"""

    def prix_standard(prix_base, quantite):
        """Prix standard sans remise"""
        return prix_base * quantite

    def prix_avec_remise_quantite(prix_base, quantite):
        """Remise progressive selon la quantité"""
        total = prix_base * quantite

        if quantite >= 100:
            remise = 0.15  # 15% pour 100+
        elif quantite >= 50:
            remise = 0.10  # 10% pour 50+
        elif quantite >= 20:
            remise = 0.05  # 5% pour 20+
        else:
            remise = 0     # Pas de remise

        return total * (1 - remise)

    def prix_avec_tva(prix_base, quantite, taux_tva=0.20):
        """Prix avec TVA"""
        prix_ht = prix_base * quantite
        prix_ttc = prix_ht * (1 + taux_tva)
        return {
            "prix_ht": prix_ht,
            "tva": prix_ht * taux_tva,
            "prix_ttc": prix_ttc
        }

    def calculer_remise_fidelite(prix_total, niveau_fidelite):
        """Calcule la remise fidélité"""
        remises = {
            "bronze": 0.02,   # 2%
            "argent": 0.05,   # 5%
            "or": 0.08,       # 8%
            "platine": 0.12   # 12%
        }

        remise = remises.get(niveau_fidelite.lower(), 0)
        return prix_total * (1 - remise)

    return {
        "standard": prix_standard,
        "quantite": prix_avec_remise_quantite,
        "tva": prix_avec_tva,
        "fidelite": calculer_remise_fidelite
    }


# Test du système de prix
prix_calc = systeme_prix()

print("💸 Tests de calcul de prix :")
prix_unitaire = 10.0
quantite = 25

prix_std = prix_calc["standard"](prix_unitaire, quantite)
prix_qty = prix_calc["quantite"](prix_unitaire, quantite)
prix_tva = prix_calc["tva"](prix_unitaire, quantite)
prix_fid = prix_calc["fidelite"](prix_std, "or")

print(f"   Prix standard : {prix_std:.2f}€")
print(f"   Prix avec remise quantité : {prix_qty:.2f}€")
print(f"   Prix avec TVA : {prix_tva}")
print(f"   Prix avec fidélité OR : {prix_fid:.2f}€")

print("\n📊 GÉNÉRATEUR DE RAPPORTS")
print("-" * 26)


def generateur_rapports():
    """Générateur de rapports avec formatage"""

    def rapport_ventes(donnees_ventes):
        """Génère un rapport de ventes"""
        total_ventes = sum(vente["montant"] for vente in donnees_ventes)
        nb_ventes = len(donnees_ventes)
        vente_moyenne = total_ventes / nb_ventes if nb_ventes > 0 else 0

        # Trouve la meilleure vente
        meilleure_vente = max(
            donnees_ventes, key=lambda x: x["montant"]) if donnees_ventes else None

        rapport = f"""
📊 RAPPORT DE VENTES
==================
• Nombre de ventes : {nb_ventes}
• Total des ventes : {total_ventes:.2f}€
• Vente moyenne : {vente_moyenne:.2f}€
• Meilleure vente : {meilleure_vente["montant"]:.2f}€ ({meilleure_vente["client"]})
"""
        return rapport.strip()

    def rapport_inventaire(stock):
        """Génère un rapport d'inventaire"""
        total_articles = sum(stock.values())
        nb_produits = len(stock)
        stock_moyen = total_articles / nb_produits if nb_produits > 0 else 0

        # Produits en rupture
        ruptures = [produit for produit,
                    quantite in stock.items() if quantite == 0]
        stock_faible = [produit for produit,
                        quantite in stock.items() if 0 < quantite <= 5]

        rapport = f"""
📦 RAPPORT D'INVENTAIRE
=====================
• Nombre de produits : {nb_produits}
• Total articles : {total_articles}
• Stock moyen : {stock_moyen:.1f}
• Ruptures : {len(ruptures)} ({', '.join(ruptures) if ruptures else 'Aucune'})
• Stock faible : {len(stock_faible)} ({', '.join(stock_faible) if stock_faible else 'Aucun'})
"""
        return rapport.strip()

    return {
        "ventes": rapport_ventes,
        "inventaire": rapport_inventaire
    }


# Test du générateur de rapports
rapports = generateur_rapports()

# Données de test
ventes_test = [
    {"client": "Alice", "montant": 150.0},
    {"client": "Bob", "montant": 89.5},
    {"client": "Charlie", "montant": 220.0},
    {"client": "Diana", "montant": 95.0}
]

stock_test = {
    "Laptop": 5,
    "Souris": 0,
    "Clavier": 15,
    "Écran": 3,
    "Casque": 8
}

print("📈 Rapport de ventes :")
print(rapports["ventes"](ventes_test))

print("\n📦 Rapport d'inventaire :")
print(rapports["inventaire"](stock_test))

print("\n" + "=" * 50)
print("8. BONNES PRATIQUES")
print("=" * 50)

print("\n✅ RÈGLES DE CONCEPTION")
print("-" * 24)

print("""
💡 Principes de conception des fonctions :

🎯 RESPONSABILITÉ UNIQUE :
• Une fonction = une tâche spécifique
• Éviter les fonctions "fourre-tout"
• Facilite les tests et la maintenance

📏 TAILLE APPROPRIÉE :
• Maximum 20-30 lignes de code
• Si plus long, découper en sous-fonctions
• Une fonction doit tenir sur un écran

🏷️ NOMMAGE EXPLICITE :
• Noms descriptifs (verbes pour actions)
• calculer_prix() plutôt que calc()
• est_valide() pour les prédicats

📝 DOCUMENTATION :
• Docstring pour toute fonction publique
• Expliquer le "pourquoi", pas le "comment"
• Exemples d'utilisation utiles

🔧 PARAMÈTRES :
• Maximum 3-4 paramètres
• Valeurs par défaut pour l'optionnel
• Éviter les flags booléens multiples
""")

print("\n🚨 ANTI-PATTERNS À ÉVITER")
print("-" * 26)

print("""
❌ PROBLÈMES COURANTS :

🔄 EFFETS DE BORD CACHÉS :
• Modifier les paramètres mutables
• Accéder aux variables globales
• Imprimer dans une fonction de calcul

🎭 FONCTIONS TROP COMPLEXES :
• Trop d'if/else imbriqués
• Logique métier mélangée
• Responsabilités multiples

🔗 COUPLAGE FORT :
• Dépendre d'autres fonctions spécifiques
• Hardcoder des valeurs
• Assumer un contexte particulier

💣 GESTION D'ERREURS :
• Return silencieux en cas d'erreur
• Mélanger None et faux positifs
• Ignorer les cas limites

🐌 PERFORMANCES :
• Calculs répétés inutiles
• Récursion sans limite
• Créer des objets volumineux
""")

print("\n🎯 EXEMPLES DE REFACTORING")
print("-" * 27)

# AVANT : fonction mal conçue


def mauvaise_fonction(data, flag1, flag2, flag3):
    """Exemple de ce qu'il ne faut PAS faire"""
    if flag1:
        if flag2:
            if flag3:
                result = []
                for item in data:
                    if item > 0:
                        result.append(item * 2)
                print(f"Résultat: {result}")  # Effet de bord !
                return result
            else:
                # Code dupliqué...
                result = []
                for item in data:
                    if item > 0:
                        result.append(item)
                return result
    return []

# APRÈS : version refactorisée


def filtrer_positifs(donnees):
    """Filtre les nombres positifs d'une liste"""
    return [x for x in donnees if x > 0]


def doubler_nombres(nombres):
    """Double tous les nombres d'une liste"""
    return [x * 2 for x in nombres]


def traiter_donnees(donnees, doit_doubler=False):
    """Traite les données selon les options"""
    nombres_positifs = filtrer_positifs(donnees)

    if doit_doubler:
        return doubler_nombres(nombres_positifs)
    else:
        return nombres_positifs


# Test de la version améliorée
donnees_test = [-2, 1, -1, 3, 0, 5]
print("🔧 Refactoring en action :")
print(f"   Données : {donnees_test}")
print(f"   Filtrées : {traiter_donnees(donnees_test)}")
print(f"   Doublées : {traiter_donnees(donnees_test, True)}")

print("\n" + "=" * 50)
print("9. DEBUGGING ET TESTS")
print("=" * 50)

print("\n🐛 TECHNIQUES DE DEBUGGING")
print("-" * 27)


def fonction_avec_debug(nombres):
    """Exemple de fonction avec debugging intégré"""

    # Vérification des entrées
    if not isinstance(nombres, list):
        raise TypeError("Le paramètre doit être une liste")

    if not nombres:
        print("⚠️ Debug: Liste vide reçue")
        return 0

    # Debug intermédiaire
    print(f"🔍 Debug: Traitement de {len(nombres)} éléments")

    # Filtrage avec debug
    nombres_valides = []
    for i, n in enumerate(nombres):
        if isinstance(n, (int, float)):
            nombres_valides.append(n)
        else:
            print(f"⚠️ Debug: Élément invalide à l'index {i}: {n}")

    if not nombres_valides:
        print("⚠️ Debug: Aucun nombre valide trouvé")
        return 0

    # Calcul avec debug
    moyenne = sum(nombres_valides) / len(nombres_valides)
    print(f"✅ Debug: Moyenne calculée: {moyenne}")

    return moyenne


# Test avec debugging
print("🐛 Test avec debugging :")
test_data = [1, 2, "trois", 4, None, 5.5]
resultat = fonction_avec_debug(test_data)
print(f"   Résultat final : {resultat}")

print("\n✅ TESTS UNITAIRES SIMPLES")
print("-" * 28)


def test_calculer_moyenne():
    """Tests unitaires pour la fonction calculer_moyenne"""

    # Test cas normal
    assert calculer_moyenne([1, 2, 3, 4, 5]) == 3.0, "Test cas normal échoué"

    # Test liste vide
    assert calculer_moyenne([]) == 0, "Test liste vide échoué"

    # Test un seul élément
    assert calculer_moyenne([42]) == 42, "Test un élément échoué"

    # Test nombres négatifs
    assert calculer_moyenne([-1, -2, -3]) == - \
        2.0, "Test nombres négatifs échoué"

    print("✅ Tous les tests sont passés !")


# Exécution des tests
print("🧪 Exécution des tests unitaires :")
test_calculer_moyenne()

print("\n🔍 ASSERTIONS ET VALIDATIONS")
print("-" * 30)


def division_securisee(a, b):
    """Division avec validations complètes"""

    # Validation des types
    assert isinstance(
        a, (int, float)), f"a doit être numérique, reçu {type(a)}"
    assert isinstance(
        b, (int, float)), f"b doit être numérique, reçu {type(b)}"

    # Validation des valeurs
    assert b != 0, "Division par zéro impossible"

    # Calcul et validation du résultat
    resultat = a / b

    # Post-condition (optionnel)
    assert isinstance(resultat, float), "Le résultat doit être un float"

    return resultat


print("🛡️ Tests de division sécurisée :")
try:
    print(f"   10 ÷ 2 = {division_securisee(10, 2)}")
    print(f"   15 ÷ 3 = {division_securisee(15, 3)}")
    # division_securisee(10, 0)  # Décommentez pour voir l'erreur
except AssertionError as e:
    print(f"   ❌ Erreur : {e}")

print("\n" + "=" * 50)
print("10. EXERCICES PRATIQUES")
print("=" * 50)

print("""
💪 EXERCICES À FAIRE (décommentez pour tester) :

# Exercice 1 : Gestionnaire de mots de passe
# def gestionnaire_mots_de_passe():
#     \"\"\"Système complet de gestion de mots de passe\"\"\"
#     
#     def generer_mot_de_passe(longueur=12, inclure_symboles=True):
#         import random
#         import string
#         
#         caracteres = string.ascii_letters + string.digits
#         if inclure_symboles:
#             caracteres += "!@#$%^&*"
#         
#         return ''.join(random.choices(caracteres, k=longueur))
#     
#     def evaluer_force(mot_de_passe):
#         score = 0
#         
#         # Longueur
#         if len(mot_de_passe) >= 8:
#             score += 1
#         if len(mot_de_passe) >= 12:
#             score += 1
#         
#         # Diversité des caractères
#         if any(c.islower() for c in mot_de_passe):
#             score += 1
#         if any(c.isupper() for c in mot_de_passe):
#             score += 1
#         if any(c.isdigit() for c in mot_de_passe):
#             score += 1
#         if any(c in "!@#$%^&*" for c in mot_de_passe):
#             score += 1
#         
#         niveaux = {
#             0: "Très faible",
#             1: "Faible", 
#             2: "Faible",
#             3: "Moyen",
#             4: "Fort",
#             5: "Très fort",
#             6: "Excellent"
#         }
#         
#         return niveaux.get(score, "Inconnu"), score
#     
#     def chiffrer_simple(texte, decalage=3):
#         # Chiffrement César simple
#         resultat = ""
#         for char in texte:
#             if char.isalpha():
#                 ascii_offset = 65 if char.isupper() else 97
#                 resultat += chr((ord(char) - ascii_offset + decalage) % 26 + ascii_offset)
#             else:
#                 resultat += char
#         return resultat
#     
#     def dechiffrer_simple(texte_chiffre, decalage=3):
#         return chiffrer_simple(texte_chiffre, -decalage)
#     
#     return {
#         'generer': generer_mot_de_passe,
#         'evaluer': evaluer_force,
#         'chiffrer': chiffrer_simple,
#         'dechiffrer': dechiffrer_simple
#     }
# 
# # Test du gestionnaire
# mdp_manager = gestionnaire_mots_de_passe()
# 
# # Génération et évaluation
# nouveau_mdp = mdp_manager['generer'](16)
# force, score = mdp_manager['evaluer'](nouveau_mdp)
# print(f"Mot de passe généré : {nouveau_mdp}")
# print(f"Force : {force} (score: {score}/6)")
# 
# # Test de chiffrement
# texte_secret = "MonMotDePasseSecret123"
# texte_chiffre = mdp_manager['chiffrer'](texte_secret)
# texte_dechiffre = mdp_manager['dechiffrer'](texte_chiffre)
# print(f"Original : {texte_secret}")
# print(f"Chiffré : {texte_chiffre}")
# print(f"Déchiffré : {texte_dechiffre}")

# Exercice 2 : Calculatrice scientifique
# def calculatrice_scientifique():
#     \"\"\"Calculatrice avec fonctions scientifiques\"\"\"
#     import math
#     
#     def operations_base():
#         return {
#             'add': lambda a, b: a + b,
#             'sub': lambda a, b: a - b,
#             'mul': lambda a, b: a * b,
#             'div': lambda a, b: a / b if b != 0 else float('inf'),
#             'pow': lambda a, b: a ** b,
#             'mod': lambda a, b: a % b if b != 0 else 0
#         }
#     
#     def operations_scientifiques():
#         return {
#             'sqrt': lambda x: math.sqrt(x) if x >= 0 else complex(0, math.sqrt(-x)),
#             'sin': math.sin,
#             'cos': math.cos,
#             'tan': math.tan,
#             'log': lambda x: math.log(x) if x > 0 else float('-inf'),
#             'log10': lambda x: math.log10(x) if x > 0 else float('-inf'),
#             'exp': math.exp,
#             'factorial': lambda n: math.factorial(int(n)) if n >= 0 and n == int(n) else None
#         }
#     
#     def evaluer_expression(expression):
#         # Évaluateur simple d'expressions mathématiques
#         # ATTENTION : eval() est dangereux en production !
#         operateurs_autorises = {
#             '+', '-', '*', '/', '**', '(', ')', '.',
#             'sin', 'cos', 'tan', 'sqrt', 'log', 'exp'
#         }
#         
#         # Vérification basique de sécurité
#         import re
#         if re.search(r'[a-zA-Z_][a-zA-Z0-9_]*(?!\()', expression):
#             # Contient des variables non autorisées
#             return "Expression non sécurisée"
#         
#         try:
#             # Remplacer les fonctions par leurs équivalents math
#             expression_safe = expression.replace('sqrt', 'math.sqrt')
#             expression_safe = expression_safe.replace('sin', 'math.sin')
#             expression_safe = expression_safe.replace('cos', 'math.cos')
#             expression_safe = expression_safe.replace('tan', 'math.tan')
#             expression_safe = expression_safe.replace('log', 'math.log')
#             expression_safe = expression_safe.replace('exp', 'math.exp')
#             
#             return eval(expression_safe)
#         except Exception as e:
#             return f"Erreur : {e}"
#     
#     def convertir_angle(angle, de_unite, vers_unite):
#         # Conversion entre degrés et radians
#         if de_unite == vers_unite:
#             return angle
#         
#         if de_unite == 'deg' and vers_unite == 'rad':
#             return math.radians(angle)
#         elif de_unite == 'rad' and vers_unite == 'deg':
#             return math.degrees(angle)
#         else:
#             return None
#     
#     return {
#         'base': operations_base(),
#         'sci': operations_scientifiques(),
#         'eval': evaluer_expression,
#         'convert_angle': convertir_angle
#     }
# 
# # Test de la calculatrice
# calc = calculatrice_scientifique()
# 
# print("Opérations de base :")
# print(f"5 + 3 = {calc['base']['add'](5, 3)}")
# print(f"10 / 3 = {calc['base']['div'](10, 3):.3f}")
# 
# print("\\nOpérations scientifiques :")
# print(f"sqrt(16) = {calc['sci']['sqrt'](16)}")
# print(f"sin(π/2) = {calc['sci']['sin'](math.pi/2):.3f}")
# print(f"5! = {calc['sci']['factorial'](5)}")
# 
# print("\\nÉvaluation d'expressions :")
# print(f"2**3 + sqrt(9) = {calc['eval']('2**3 + sqrt(9)')}")

# Exercice 3 : Système de validation de données
# def systeme_validation():
#     \"\"\"Système complet de validation de données\"\"\"
#     
#     def valider_email(email):
#         import re
#         pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
#         return re.match(pattern, email) is not None
#     
#     def valider_telephone(numero):
#         import re
#         # Format français : 01.23.45.67.89 ou 01 23 45 67 89 ou 0123456789
#         pattern = r'^(?:(?:\\+33|0)[1-9])(?:[0-9]{8})$'
#         numero_nettoye = re.sub(r'[\\s.-]', '', numero)
#         return re.match(pattern, numero_nettoye) is not None
#     
#     def valider_age(age):
#         try:
#             age_int = int(age)
#             return 0 <= age_int <= 150
#         except ValueError:
#             return False
#     
#     def valider_mot_de_passe(mot_de_passe):
#         # Au moins 8 caractères, 1 majuscule, 1 minuscule, 1 chiffre
#         if len(mot_de_passe) < 8:
#             return False, "Trop court (min 8 caractères)"
#         
#         if not any(c.isupper() for c in mot_de_passe):
#             return False, "Doit contenir au moins une majuscule"
#         
#         if not any(c.islower() for c in mot_de_passe):
#             return False, "Doit contenir au moins une minuscule"
#         
#         if not any(c.isdigit() for c in mot_de_passe):
#             return False, "Doit contenir au moins un chiffre"
#         
#         return True, "Mot de passe valide"
#     
#     def valider_formulaire(donnees):
#         erreurs = []
#         
#         # Validation de chaque champ
#         if 'email' in donnees:
#             if not valider_email(donnees['email']):
#                 erreurs.append("Email invalide")
#         
#         if 'telephone' in donnees:
#             if not valider_telephone(donnees['telephone']):
#                 erreurs.append("Numéro de téléphone invalide")
#         
#         if 'age' in donnees:
#             if not valider_age(donnees['age']):
#                 erreurs.append("Âge invalide")
#         
#         if 'mot_de_passe' in donnees:
#             valide, message = valider_mot_de_passe(donnees['mot_de_passe'])
#             if not valide:
#                 erreurs.append(f"Mot de passe : {message}")
#         
#         return len(erreurs) == 0, erreurs
#     
#     return {
#         'email': valider_email,
#         'telephone': valider_telephone,
#         'age': valider_age,
#         'mot_de_passe': valider_mot_de_passe,
#         'formulaire': valider_formulaire
#     }
# 
# # Test du système de validation
# validateur = systeme_validation()
# 
# # Tests individuels
# print("Tests de validation :")
# print(f"Email 'test@example.com' : {validateur['email']('test@example.com')}")
# print(f"Téléphone '01.23.45.67.89' : {validateur['telephone']('01.23.45.67.89')}")
# print(f"Âge '25' : {validateur['age']('25')}")
# 
# # Test du mot de passe
# valide, msg = validateur['mot_de_passe']('MonMotDePasse123')
# print(f"Mot de passe 'MonMotDePasse123' : {valide} - {msg}")
# 
# # Test de formulaire complet
# formulaire_test = {
#     'email': 'alice@example.com',
#     'telephone': '01 23 45 67 89',
#     'age': '28',
#     'mot_de_passe': 'MdP123!'
# }
# 
# valide, erreurs = validateur['formulaire'](formulaire_test)
# print(f"\\nFormulaire valide : {valide}")
# if erreurs:
#     print("Erreurs :", erreurs)
""")

print("\n" + "=" * 50)
print("11. RÉSUMÉ FINAL")
print("=" * 50)

print("""
🎯 POINTS CLÉS À RETENIR :

1. 📝 DÉFINITION DE FONCTIONS :
   • def nom_fonction(paramètres): corps
   • return pour retourner une valeur
   • Docstring pour documenter
   • Annotations de type recommandées

2. 🎛️ PARAMÈTRES :
   • Positionnels : ordre important
   • Nommés : ordre libre avec nom=valeur
   • Valeurs par défaut : éviter les mutables
   • *args et **kwargs (voir chapitre suivant)

3. ↩️ VALEURS DE RETOUR :
   • return simple ou multiple (tuple)
   • Return précoce pour simplifier
   • None par défaut si pas de return

4. 📚 DOCUMENTATION :
   • Docstring obligatoire pour fonctions publiques
   • Formats Google/NumPy/Sphinx
   • Type hints pour la clarté
   • Exemples d'utilisation

5. 🎭 FONCTIONS COMME OBJETS :
   • Assignables à des variables
   • Passables comme paramètres
   • Stockables dans structures
   • Retournables depuis d'autres fonctions

💡 BONNES PRATIQUES :
✅ Une fonction = une responsabilité
✅ Noms explicites et descriptifs
✅ Maximum 20-30 lignes
✅ Documentation complète
✅ Gestion des cas d'erreur
✅ Tests unitaires

🚨 ERREURS COURANTES :
❌ Fonctions trop complexes
❌ Effets de bord cachés
❌ Valeurs par défaut mutables
❌ Manque de validation
❌ Documentation insuffisante

⚡ PERFORMANCES :
• Éviter les calculs répétés
• Valider tôt, échouer vite
• Utiliser la mémoïsation si besoin
• Profiler les fonctions critiques

🎯 APPLICATIONS :
• Réutilisabilité du code
• Organisation et structure
• Tests et maintenance
• Abstraction de la complexité
• Modularité du programme

🎉 Félicitations ! Vous maîtrisez la définition des fonctions !
💡 Prochaine étape : Arguments avancés et paramètres !
📚 Fonctions définies, explorez les paramètres avancés !
""")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE - DÉFINITION DE FONCTIONS MAÎTRISÉE !")
print("=" * 70)
