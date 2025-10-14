#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
======================================================================
ARGUMENTS ET PARAMÈTRES AVANCÉS EN PYTHON - GUIDE COMPLET
======================================================================

🎯 Ce fichier couvre les paramètres et arguments avancés :
   • *args et **kwargs
   • Paramètres positionnels seuls
   • Paramètres par mot-clé seuls
   • Déballage d'arguments
   • Paramètres par défaut complexes
   • Validation et transformation

📚 Concepts abordés :
   • Arguments variables
   • Forçage de paramètres nommés
   • Unpacking d'arguments
   • Introspection de paramètres
   • Signatures dynamiques

💡 Objectif : Maîtriser toutes les formes de paramètres Python
"""

import time
import inspect

print("=" * 70)
print("ARGUMENTS ET PARAMÈTRES AVANCÉS - GUIDE COMPLET")
print("=" * 70)

print("\n" + "=" * 50)
print("1. ARGUMENTS VARIABLES (*args)")
print("=" * 50)

print("\n📦 *ARGS - ARGUMENTS POSITIONNELS VARIABLES")
print("-" * 43)


def additionner_tous(*nombres):
    """Additionne un nombre variable d'arguments"""
    total = 0
    for nombre in nombres:
        total += nombre
    return total


print("🔢 Utilisation de *args :")
print(f"   additionner_tous(1, 2, 3) = {additionner_tous(1, 2, 3)}")
print(f"   additionner_tous(10, 20) = {additionner_tous(10, 20)}")
print(
    f"   additionner_tous(1, 2, 3, 4, 5, 6) = {additionner_tous(1, 2, 3, 4, 5, 6)}")

# *args capture tous les arguments positionnels dans un tuple


def analyser_args(*args):
    """Analyse les arguments reçus"""
    print(f"📊 Type de args : {type(args)}")
    print(f"📊 Nombre d'arguments : {len(args)}")
    print(f"📊 Arguments reçus : {args}")

    for i, arg in enumerate(args):
        print(f"   Argument {i} : {arg} (type: {type(arg).__name__})")


print("\n🔍 Analyse des *args :")
analyser_args("hello", 42, [1, 2, 3], True)

print("\n🎯 FONCTION AVEC PARAMÈTRES FIXES ET *ARGS")
print("-" * 43)


def message_avec_details(titre, *details):
    """Affiche un titre suivi de détails variables"""
    print(f"📋 {titre}")
    for i, detail in enumerate(details, 1):
        print(f"   {i}. {detail}")


print("📝 Message avec détails variables :")
message_avec_details(
    "Liste de courses",
    "Pain",
    "Lait",
    "Œufs",
    "Fromage"
)

message_avec_details("Tâches à faire", "Laver la vaisselle",
                     "Sortir les poubelles")

print("\n🔧 APPLICATIONS PRATIQUES DE *ARGS")
print("-" * 34)


def calculer_statistiques(*valeurs):
    """Calcule diverses statistiques sur des valeurs"""
    if not valeurs:
        return {"erreur": "Aucune valeur fournie"}

    total = sum(valeurs)
    nombre = len(valeurs)
    moyenne = total / nombre
    minimum = min(valeurs)
    maximum = max(valeurs)

    # Médiane
    valeurs_triees = sorted(valeurs)
    if nombre % 2 == 0:
        mediane = (valeurs_triees[nombre//2 - 1] +
                   valeurs_triees[nombre//2]) / 2
    else:
        mediane = valeurs_triees[nombre//2]

    return {
        "nombre": nombre,
        "somme": total,
        "moyenne": moyenne,
        "médiane": mediane,
        "minimum": minimum,
        "maximum": maximum
    }


# Test avec différents nombres de valeurs
print("📊 Statistiques sur différents datasets :")

stats1 = calculer_statistiques(1, 2, 3, 4, 5)
print(f"   Dataset 1 : {stats1}")

stats2 = calculer_statistiques(10, 15, 12, 18, 14, 16, 11)
print(f"   Dataset 2 : {stats2}")

stats3 = calculer_statistiques(100)
print(f"   Dataset 3 : {stats3}")

print("\n" + "=" * 50)
print("2. ARGUMENTS DE MOT-CLÉ VARIABLES (**kwargs)")
print("=" * 50)

print("\n🏷️ **KWARGS - ARGUMENTS NOMMÉS VARIABLES")
print("-" * 40)


def creer_profil(**informations):
    """Crée un profil utilisateur avec informations variables"""
    profil = {}

    # Informations obligatoires par défaut
    profil["nom"] = informations.get("nom", "Anonyme")
    profil["age"] = informations.get("age", "Non spécifié")

    # Ajouter toutes les autres informations
    for cle, valeur in informations.items():
        if cle not in ["nom", "age"]:
            profil[cle] = valeur

    return profil


print("👤 Création de profils avec **kwargs :")

profil1 = creer_profil(
    nom="Alice",
    age=25,
    ville="Paris",
    profession="Développeuse",
    loisirs=["lecture", "programmation"]
)
print(f"   Profil 1 : {profil1}")

profil2 = creer_profil(
    nom="Bob",
    pays="France",
    email="bob@example.com"
)
print(f"   Profil 2 : {profil2}")

# **kwargs capture tous les arguments nommés dans un dictionnaire


def analyser_kwargs(**kwargs):
    """Analyse les arguments nommés reçus"""
    print(f"📊 Type de kwargs : {type(kwargs)}")
    print(f"📊 Nombre d'arguments : {len(kwargs)}")
    print(f"📊 Clés disponibles : {list(kwargs.keys())}")

    for cle, valeur in kwargs.items():
        print(f"   {cle} = {valeur} (type: {type(valeur).__name__})")


print("\n🔍 Analyse des **kwargs :")
analyser_kwargs(
    nom="Charlie",
    age=30,
    actif=True,
    scores=[95, 87, 92]
)

print("\n⚙️ CONFIGURATION DYNAMIQUE")
print("-" * 26)


def configurer_serveur(host="localhost", port=8080, **options):
    """Configure un serveur avec options personnalisées"""
    config = {
        "host": host,
        "port": port
    }

    # Ajouter les options personnalisées
    config.update(options)

    # Valeurs par défaut pour certaines options
    config.setdefault("debug", False)
    config.setdefault("timeout", 30)
    config.setdefault("max_connections", 100)

    return config


print("⚙️ Configuration de serveur flexible :")

config1 = configurer_serveur()
print(f"   Config par défaut : {config1}")

config2 = configurer_serveur(
    port=3000,
    debug=True,
    ssl=True,
    cors_enabled=True,
    rate_limiting={"max_requests": 1000, "window": 3600}
)
print(f"   Config personnalisée : {config2}")

print("\n" + "=" * 50)
print("3. COMBINAISON *ARGS ET **KWARGS")
print("=" * 50)

print("\n🎭 FONCTION UNIVERSELLE")
print("-" * 21)


def fonction_universelle(*args, **kwargs):
    """Accepte tous types d'arguments"""
    print(f"📦 Arguments positionnels (*args) : {args}")
    print(f"🏷️ Arguments nommés (**kwargs) : {kwargs}")

    # Traiter les arguments positionnels
    if args:
        print("   Traitement des args :")
        for i, arg in enumerate(args):
            print(f"     Position {i} : {arg}")

    # Traiter les arguments nommés
    if kwargs:
        print("   Traitement des kwargs :")
        for cle, valeur in kwargs.items():
            print(f"     {cle} → {valeur}")


print("🔧 Test de fonction universelle :")
fonction_universelle(
    1, 2, 3,  # args
    nom="Alice", age=25, actif=True  # kwargs
)

print("\n🎯 ORDRE DES PARAMÈTRES")
print("-" * 23)


def fonction_complete(param_fixe, param_defaut="defaut", *args, **kwargs):
    """Fonction avec tous types de paramètres"""
    print(f"📌 Paramètre fixe : {param_fixe}")
    print(f"⭐ Paramètre par défaut : {param_defaut}")
    print(f"📦 Args supplémentaires : {args}")
    print(f"🏷️ Kwargs : {kwargs}")


print("🎼 Ordre des paramètres (param_fixe, defaut, *args, **kwargs) :")
fonction_complete(
    "obligatoire",      # param_fixe
    "modifié",          # param_defaut
    "extra1", "extra2",  # *args
    option1="value1", option2="value2"  # **kwargs
)

print("\n🚀 PROXY ET DÉCORATEURS")
print("-" * 24)


def logger_fonction(func):
    """Décorateur qui log les appels de fonction"""
    def wrapper(*args, **kwargs):
        print(f"📝 Appel de {func.__name__}")
        print(f"   Args : {args}")
        print(f"   Kwargs : {kwargs}")

        # Appeler la fonction originale
        resultat = func(*args, **kwargs)

        print(f"   Résultat : {resultat}")
        return resultat

    return wrapper


@logger_fonction
def calculer(operation, a, b, precision=2):
    """Fonction de calcul simple"""
    if operation == "add":
        return round(a + b, precision)
    elif operation == "mul":
        return round(a * b, precision)
    else:
        return "Opération non supportée"


print("📊 Test de fonction avec décorateur logger :")
resultat = calculer("add", 10, 5, precision=1)
print(f"🎯 Résultat final : {resultat}")

print("\n" + "=" * 50)
print("4. DÉBALLAGE D'ARGUMENTS (UNPACKING)")
print("=" * 50)

print("\n📦 DÉBALLAGE DE LISTES ET TUPLES")
print("-" * 33)


def calculer_rectangle(longueur, largeur, hauteur=1):
    """Calcule volume et surface d'un parallélépipède"""
    volume = longueur * largeur * hauteur
    surface = 2 * (longueur*largeur + longueur*hauteur + largeur*hauteur)
    return volume, surface


# Données dans des structures
dimensions_2d = [5, 3]  # longueur, largeur
dimensions_3d = (4, 6, 2)  # longueur, largeur, hauteur

print("📐 Déballage avec * :")

# Déballage de liste (2D -> 3D avec hauteur par défaut)
volume_2d, surface_2d = calculer_rectangle(*dimensions_2d)
print(
    f"   Rectangle 2D {dimensions_2d} : volume={volume_2d}, surface={surface_2d}")

# Déballage de tuple (3D complet)
volume_3d, surface_3d = calculer_rectangle(*dimensions_3d)
print(
    f"   Parallélépipède {dimensions_3d} : volume={volume_3d}, surface={surface_3d}")

print("\n🏷️ DÉBALLAGE DE DICTIONNAIRES")
print("-" * 30)


def presenter_personne(nom, age, ville="Non spécifiée", profession="Non spécifiée"):
    """Présente une personne"""
    return f"👤 {nom}, {age} ans, vit à {ville}, travaille comme {profession}"


# Données dans un dictionnaire
personne1 = {
    "nom": "Alice",
    "age": 28,
    "ville": "Paris"
}

personne2 = {
    "nom": "Bob",
    "age": 35,
    "ville": "Lyon",
    "profession": "Ingénieur"
}

print("🏷️ Déballage avec ** :")
print(f"   {presenter_personne(**personne1)}")
print(f"   {presenter_personne(**personne2)}")

print("\n🔀 DÉBALLAGE MIXTE")
print("-" * 17)


def fonction_mixte(a, b, c, d=10, e=20, **autres):
    """Fonction avec paramètres mixtes"""
    return {
        "positionnels": [a, b, c],
        "par_defaut": [d, e],
        "autres": autres
    }


# Combinaison de déballages
args_pos = [1, 2, 3]
kwargs_dict = {"d": 100, "f": 300, "g": 400}

resultat_mixte = fonction_mixte(*args_pos, **kwargs_dict)
print(f"🔀 Résultat mixte : {resultat_mixte}")

print("\n🎯 CONSTRUCTION DYNAMIQUE D'APPELS")
print("-" * 35)


def appeler_fonction_dynamique(fonction, args_list=None, kwargs_dict=None):
    """Appelle une fonction avec des arguments dynamiques"""
    args_list = args_list or []
    kwargs_dict = kwargs_dict or {}

    print(f"🎯 Appel de {fonction.__name__}")
    print(f"   Args : {args_list}")
    print(f"   Kwargs : {kwargs_dict}")

    return fonction(*args_list, **kwargs_dict)


# Test avec différentes fonctions
print("🔧 Appels dynamiques :")

# Test 1 : fonction simple
resultat1 = appeler_fonction_dynamique(
    additionner_tous,
    [10, 20, 30, 40]
)
print(f"   Résultat 1 : {resultat1}")

# Test 2 : fonction avec kwargs
resultat2 = appeler_fonction_dynamique(
    creer_profil,
    [],
    {"nom": "Charlie", "age": 40, "email": "charlie@test.com"}
)
print(f"   Résultat 2 : {resultat2}")

print("\n" + "=" * 50)
print("5. PARAMÈTRES POSITIONNELS ET NOMMÉS SEULS")
print("=" * 50)

print("\n🔒 PARAMÈTRES POSITIONNELS SEULS (/)")
print("-" * 35)


def diviser(dividende, diviseur, /, precision=2):
    """
    Division avec paramètres positionnels obligatoires.

    Args:
        dividende: Nombre à diviser (positionnel seul)
        diviseur: Nombre diviseur (positionnel seul)  
        precision: Nombre de décimales (peut être nommé)
    """
    if diviseur == 0:
        return "Division par zéro impossible"

    resultat = dividende / diviseur
    return round(resultat, precision)


print("🔒 Paramètres positionnels seuls (avant /) :")
print(f"   diviser(10, 3) = {diviser(10, 3)}")
print(f"   diviser(10, 3, precision=4) = {diviser(10, 3, precision=4)}")

# Ceci ne marche PAS :
# diviser(dividende=10, diviseur=3)  # TypeError !

print("\n🏷️ PARAMÈTRES NOMMÉS SEULS (*)")
print("-" * 31)


def configurer_base_donnees(host, port, *, database, username, password, ssl=True):
    """
    Configure une connexion base de données.

    Args:
        host: Serveur (positionnel ou nommé)
        port: Port (positionnel ou nommé)
        database: Base de données (nommé obligatoire)
        username: Utilisateur (nommé obligatoire)
        password: Mot de passe (nommé obligatoire)
        ssl: SSL activé (nommé avec défaut)
    """
    config = {
        "host": host,
        "port": port,
        "database": database,
        "username": username,
        "password": password,
        "ssl": ssl
    }

    return f"🔗 Connexion à {database} sur {host}:{port} (SSL: {ssl})"


print("🏷️ Paramètres nommés obligatoires (après *) :")
connexion = configurer_base_donnees(
    "localhost", 5432,  # Positionnels OK
    database="myapp",   # Nommés obligatoires
    username="admin",
    password="secret123"
)
print(f"   {connexion}")

print("\n🔐 COMBINAISON / ET *")
print("-" * 20)


def fonction_stricte(pos_seul, /, pos_ou_nom, *, nom_seul, nom_avec_defaut="defaut"):
    """
    Fonction avec tous types de contraintes de paramètres.

    Args:
        pos_seul: Positionnel obligatoire seulement
        pos_ou_nom: Positionnel ou nommé
        nom_seul: Nommé obligatoire seulement
        nom_avec_defaut: Nommé avec valeur par défaut
    """
    return {
        "pos_seul": pos_seul,
        "pos_ou_nom": pos_ou_nom,
        "nom_seul": nom_seul,
        "nom_avec_defaut": nom_avec_defaut
    }


print("🔐 Fonction avec contraintes strictes :")
resultat_strict = fonction_stricte(
    "valeur1",              # pos_seul (positionnel seulement)
    pos_ou_nom="valeur2",   # pos_ou_nom (nommé ici)
    nom_seul="valeur3"      # nom_seul (nommé obligatoire)
)
print(f"   {resultat_strict}")

print("\n📚 EXEMPLES D'API DESIGN")
print("-" * 25)


def range_ameliore(stop, /, start=0, step=1, *, include_stop=False):
    """
    Version améliorée de range avec options avancées.

    Args:
        stop: Valeur de fin (positionnel seul)
        start: Valeur de début (défaut 0)
        step: Pas (défaut 1)
        include_stop: Inclure la valeur stop (nommé seul)
    """
    if include_stop:
        stop += 1 if step > 0 else -1

    return list(range(start, stop, step))


print("📚 API bien designée :")
print(f"   range_ameliore(5) = {range_ameliore(5)}")
print(
    f"   range_ameliore(10, start=2, step=2) = {range_ameliore(10, start=2, step=2)}")
print(
    f"   range_ameliore(5, include_stop=True) = {range_ameliore(5, include_stop=True)}")

print("\n" + "=" * 50)
print("6. VALIDATION ET TRANSFORMATION D'ARGUMENTS")
print("=" * 50)

print("\n✅ VALIDATION D'ARGUMENTS")
print("-" * 25)


def valider_arguments(func):
    """Décorateur pour valider les arguments d'une fonction"""
    def wrapper(*args, **kwargs):
        # Exemple de validations
        for arg in args:
            if isinstance(arg, str) and not arg.strip():
                raise ValueError("Les chaînes ne peuvent pas être vides")

        for key, value in kwargs.items():
            if key.endswith("_age") and (not isinstance(value, int) or value < 0):
                raise ValueError(f"L'âge {key} doit être un entier positif")

        return func(*args, **kwargs)

    return wrapper


@valider_arguments
def creer_personne(nom, prenom, *, personne_age, email=""):
    """Crée une personne avec validation"""
    return {
        "nom": nom,
        "prenom": prenom,
        "age": personne_age,
        "email": email
    }


print("✅ Test de validation :")
try:
    personne_valide = creer_personne("Dupont", "Jean", personne_age=30)
    print(f"   Personne créée : {personne_valide}")

    # Test avec erreur
    # personne_invalide = creer_personne("", "Jean", personne_age=-5)
except ValueError as e:
    print(f"   ❌ Erreur de validation : {e}")

print("\n🔄 TRANSFORMATION D'ARGUMENTS")
print("-" * 30)


def transformer_arguments(func):
    """Décorateur qui transforme les arguments avant traitement"""
    def wrapper(*args, **kwargs):
        # Transformer les args (exemple : convertir strings en majuscules)
        args_transformes = []
        for arg in args:
            if isinstance(arg, str):
                args_transformes.append(arg.upper())
            else:
                args_transformes.append(arg)

        # Transformer les kwargs (exemple : nettoyer les emails)
        kwargs_transformes = {}
        for key, value in kwargs.items():
            if key.endswith("_email") and isinstance(value, str):
                kwargs_transformes[key] = value.lower().strip()
            else:
                kwargs_transformes[key] = value

        return func(*args_transformes, **kwargs_transformes)

    return wrapper


@transformer_arguments
def enregistrer_utilisateur(nom, prenom, *, user_email):
    """Enregistre un utilisateur avec transformation automatique"""
    return f"👤 {nom} {prenom} ({user_email})"


print("🔄 Test de transformation :")
utilisateur = enregistrer_utilisateur(
    "dupont", "jean",  # Seront mis en majuscules
    user_email="  Jean.DUPONT@Example.COM  "  # Sera nettoyé
)
print(f"   Utilisateur : {utilisateur}")

print("\n🎯 VALIDATION AVEC TYPE HINTS")
print("-" * 30)


def valider_types(func):
    """Décorateur qui valide les types selon les annotations"""
    import inspect

    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()

        for param_name, value in bound_args.arguments.items():
            param = sig.parameters[param_name]
            if param.annotation != inspect.Parameter.empty:
                expected_type = param.annotation
                if not isinstance(value, expected_type):
                    raise TypeError(
                        f"Paramètre '{param_name}' doit être de type {expected_type.__name__}, "
                        f"reçu {type(value).__name__}"
                    )

        return func(*args, **kwargs)

    return wrapper


@valider_types
def calculer_prix_total(prix_unitaire: float, quantite: int, taux_tva: float = 0.20) -> float:
    """Calcule le prix total TTC avec validation de types"""
    prix_ht = prix_unitaire * quantite
    prix_ttc = prix_ht * (1 + taux_tva)
    return round(prix_ttc, 2)


print("🎯 Test de validation de types :")
try:
    prix_correct = calculer_prix_total(10.50, 3)
    print(f"   Prix calculé : {prix_correct}€")

    # Test avec type incorrect
    # prix_incorrect = calculer_prix_total("10.50", 3)  # str au lieu de float
except TypeError as e:
    print(f"   ❌ Erreur de type : {e}")

print("\n" + "=" * 50)
print("7. INTROSPECTION DE PARAMÈTRES")
print("=" * 50)

print("\n🔍 INSPECTION DE SIGNATURES")
print("-" * 28)


def analyser_signature(func):
    """Analyse la signature d'une fonction"""
    sig = inspect.signature(func)

    print(f"🔍 Analyse de {func.__name__} :")
    print(f"   Signature complète : {sig}")

    for nom, param in sig.parameters.items():
        infos = []

        # Type de paramètre
        if param.kind == param.POSITIONAL_ONLY:
            infos.append("positionnel seul")
        elif param.kind == param.POSITIONAL_OR_KEYWORD:
            infos.append("positionnel ou nommé")
        elif param.kind == param.VAR_POSITIONAL:
            infos.append("*args")
        elif param.kind == param.KEYWORD_ONLY:
            infos.append("nommé seul")
        elif param.kind == param.VAR_KEYWORD:
            infos.append("**kwargs")

        # Valeur par défaut
        if param.default != param.empty:
            infos.append(f"défaut: {param.default}")

        # Annotation de type
        if param.annotation != param.empty:
            infos.append(f"type: {param.annotation}")

        print(f"   📌 {nom} : {', '.join(infos)}")

    # Type de retour
    if sig.return_annotation != sig.empty:
        print(f"   🔄 Retour : {sig.return_annotation}")


print("🔍 Inspection de différentes fonctions :")

# Test sur nos fonctions précédentes
analyser_signature(diviser)
print()
analyser_signature(configurer_base_donnees)
print()
analyser_signature(calculer_prix_total)

print("\n🎛️ CRÉATION DYNAMIQUE D'APPELS")
print("-" * 32)


def appel_intelligent(func, **kwargs_fournis):
    """Appelle une fonction en ne passant que les paramètres qu'elle accepte"""
    sig = inspect.signature(func)

    # Filtrer les kwargs pour ne garder que ceux acceptés par la fonction
    kwargs_acceptes = {}
    for nom_param in sig.parameters:
        if nom_param in kwargs_fournis:
            kwargs_acceptes[nom_param] = kwargs_fournis[nom_param]

    print(f"🎛️ Appel de {func.__name__}")
    print(f"   Kwargs fournis : {list(kwargs_fournis.keys())}")
    print(f"   Kwargs utilisés : {list(kwargs_acceptes.keys())}")

    return func(**kwargs_acceptes)

# Fonction de test


def fonction_selective(a, b, c=10):
    """Fonction qui n'accepte que certains paramètres"""
    return a + b + c


print("🎛️ Test d'appel intelligent :")
resultat_intelligent = appel_intelligent(
    fonction_selective,
    a=5,
    b=15,
    c=20,
    d=999,  # Sera ignoré
    e=888   # Sera ignoré
)
print(f"   Résultat : {resultat_intelligent}")

print("\n📊 INFORMATIONS AVANCÉES")
print("-" * 25)


def info_fonction_complete(func):
    """Analyse complète d'une fonction"""
    print(f"📊 Analyse complète de {func.__name__} :")

    # Informations basiques
    print(f"   Module : {func.__module__}")
    print(f"   Nom : {func.__name__}")
    if func.__doc__:
        print(f"   Doc : {func.__doc__[:50]}...")

    # Signature
    sig = inspect.signature(func)
    print(f"   Signature : {sig}")

    # Annotations
    if hasattr(func, '__annotations__') and func.__annotations__:
        print(f"   Annotations : {func.__annotations__}")

    # Code source (si disponible)
    try:
        source_lines = inspect.getsourcelines(func)
        print(f"   Lignes de code : {len(source_lines[0])}")
        print(f"   Première ligne : {source_lines[1]}")
    except OSError:
        print("   Code source non disponible")

    # Paramètres détaillés
    params = sig.parameters
    print(f"   Nombre de paramètres : {len(params)}")

    types_params = {
        inspect.Parameter.POSITIONAL_ONLY: "pos-seul",
        inspect.Parameter.POSITIONAL_OR_KEYWORD: "pos-ou-nom",
        inspect.Parameter.VAR_POSITIONAL: "*args",
        inspect.Parameter.KEYWORD_ONLY: "nom-seul",
        inspect.Parameter.VAR_KEYWORD: "**kwargs"
    }

    for nom, param in params.items():
        type_param = types_params.get(param.kind, "inconnu")
        print(f"     • {nom} ({type_param})")


print("📊 Analyse de fonction complète :")
info_fonction_complete(configurer_base_donnees)

print("\n" + "=" * 50)
print("8. APPLICATIONS PRATIQUES AVANCÉES")
print("=" * 50)

print("\n🏭 FACTORY DE FONCTIONS")
print("-" * 23)


def creer_validateur(**regles):
    """Crée une fonction de validation basée sur des règles"""

    def validateur(**donnees):
        erreurs = []

        for champ, regle in regles.items():
            if champ not in donnees:
                if regle.get("obligatoire", False):
                    erreurs.append(f"{champ} est obligatoire")
                continue

            valeur = donnees[champ]

            # Validation de type
            if "type" in regle:
                if not isinstance(valeur, regle["type"]):
                    erreurs.append(
                        f"{champ} doit être de type {regle['type'].__name__}")
                    continue

            # Validation de longueur (pour strings)
            if isinstance(valeur, str):
                if "min_length" in regle and len(valeur) < regle["min_length"]:
                    erreurs.append(
                        f"{champ} trop court (min {regle['min_length']})")
                if "max_length" in regle and len(valeur) > regle["max_length"]:
                    erreurs.append(
                        f"{champ} trop long (max {regle['max_length']})")

            # Validation de plage (pour nombres)
            if isinstance(valeur, (int, float)):
                if "min_val" in regle and valeur < regle["min_val"]:
                    erreurs.append(
                        f"{champ} trop petit (min {regle['min_val']})")
                if "max_val" in regle and valeur > regle["max_val"]:
                    erreurs.append(
                        f"{champ} trop grand (max {regle['max_val']})")

            # Validation personnalisée
            if "validator" in regle:
                try:
                    if not regle["validator"](valeur):
                        erreurs.append(
                            f"{champ} ne respecte pas la règle personnalisée")
                except Exception as e:
                    erreurs.append(f"Erreur de validation pour {champ}: {e}")

        return len(erreurs) == 0, erreurs

    return validateur


# Création de validateurs spécialisés
validateur_utilisateur = creer_validateur(
    nom={"type": str, "min_length": 2, "max_length": 50, "obligatoire": True},
    age={"type": int, "min_val": 0, "max_val": 150, "obligatoire": True},
    email={"type": str, "validator": lambda x: "@" in x and "." in x},
    score={"type": float, "min_val": 0.0, "max_val": 100.0}
)

print("🏭 Test du validateur créé dynamiquement :")

# Test avec données valides
donnees_valides = {
    "nom": "Alice",
    "age": 25,
    "email": "alice@example.com",
    "score": 85.5
}

valide, erreurs = validateur_utilisateur(**donnees_valides)
print(f"   Données valides : {valide}")
if erreurs:
    print(f"   Erreurs : {erreurs}")

# Test avec données invalides
donnees_invalides = {
    "nom": "A",  # Trop court
    "age": 200,  # Trop grand
    "email": "email-invalide"  # Pas de .
}

valide, erreurs = validateur_utilisateur(**donnees_invalides)
print(f"   Données invalides : {valide}")
if erreurs:
    print("   Erreurs :")
    for erreur in erreurs:
        print(f"     • {erreur}")

print("\n🔗 CHAÎNAGE DE FONCTIONS")
print("-" * 24)


def creer_pipeline(*fonctions):
    """Crée un pipeline de fonctions qui s'enchaînent"""

    def pipeline(donnees):
        resultat = donnees
        historique = [("entrée", donnees)]

        for i, fonction in enumerate(fonctions):
            try:
                resultat = fonction(resultat)
                historique.append(
                    (f"étape_{i+1}_{fonction.__name__}", resultat))
            except Exception as e:
                historique.append((f"erreur_étape_{i+1}", str(e)))
                raise

        return resultat, historique

    return pipeline

# Fonctions de transformation


def nettoyer_texte(texte):
    """Nettoie un texte"""
    return texte.strip().lower()


def remplacer_espaces(texte):
    """Remplace les espaces par des underscores"""
    return texte.replace(" ", "_")


def ajouter_prefix(texte):
    """Ajoute un préfixe"""
    return f"user_{texte}"


# Création d'un pipeline de traitement
pipeline_nom_utilisateur = creer_pipeline(
    nettoyer_texte,
    remplacer_espaces,
    ajouter_prefix
)

print("🔗 Test du pipeline :")
texte_original = "  Alice Marie Dupont  "
resultat, historique = pipeline_nom_utilisateur(texte_original)

print(f"   Texte original : '{texte_original}'")
print(f"   Résultat final : '{resultat}'")
print("   Historique :")
for etape, valeur in historique:
    print(f"     {etape} : '{valeur}'")

print("\n🎯 DISPATCHER DE FONCTIONS")
print("-" * 27)


def creer_dispatcher(**handlers):
    """Crée un dispatcher qui route vers différentes fonctions"""

    def dispatcher(action, *args, **kwargs):
        if action not in handlers:
            raise ValueError(
                f"Action '{action}' non supportée. Actions disponibles : {list(handlers.keys())}")

        handler = handlers[action]

        print(f"🎯 Dispatch vers {action} (fonction: {handler.__name__})")
        return handler(*args, **kwargs)

    # Ajouter une méthode pour lister les actions
    dispatcher.actions = list(handlers.keys())

    return dispatcher

# Fonctions métier


def creer_utilisateur(nom, email):
    return {"id": hash(email) % 10000, "nom": nom, "email": email, "statut": "actif"}


def modifier_utilisateur(user_id, **modifications):
    return {"id": user_id, "modifications": modifications, "timestamp": "2024-01-01"}


def supprimer_utilisateur(user_id):
    return {"id": user_id, "statut": "supprimé"}


def lister_utilisateurs(filtre="tous"):
    return {"filtre": filtre, "count": 42, "utilisateurs": ["Alice", "Bob", "Charlie"]}


# Création du dispatcher
gestionnaire_utilisateurs = creer_dispatcher(
    create=creer_utilisateur,
    update=modifier_utilisateur,
    delete=supprimer_utilisateur,
    list=lister_utilisateurs
)

print("🎯 Test du dispatcher :")
print(f"   Actions disponibles : {gestionnaire_utilisateurs.actions}")

# Test des différentes actions
resultat_create = gestionnaire_utilisateurs(
    "create", "Alice", "alice@test.com")
print(f"   Create : {resultat_create}")

resultat_update = gestionnaire_utilisateurs(
    "update", 1234, nom="Alice Martin", ville="Paris")
print(f"   Update : {resultat_update}")

resultat_list = gestionnaire_utilisateurs("list", filtre="actifs")
print(f"   List : {resultat_list}")

print("\n" + "=" * 50)
print("9. PERFORMANCES ET OPTIMISATIONS")
print("=" * 50)

print("\n⚡ MÉMOÏSATION AVEC ARGUMENTS")
print("-" * 30)


def memoize_args(func):
    """Décorateur de mémoïsation qui gère *args et **kwargs"""
    cache = {}

    def wrapper(*args, **kwargs):
        # Créer une clé de cache à partir des arguments
        # Attention : les kwargs doivent être triés pour une clé stable
        key = (args, tuple(sorted(kwargs.items())))

        if key not in cache:
            print(f"⚡ Calcul pour {func.__name__}{args} {kwargs}")
            cache[key] = func(*args, **kwargs)
        else:
            print(f"📋 Cache hit pour {func.__name__}{args} {kwargs}")

        return cache[key]

    # Ajouter des méthodes utiles
    wrapper.cache = cache
    wrapper.cache_clear = lambda: cache.clear()
    wrapper.cache_info = lambda: {
        "size": len(cache), "keys": list(cache.keys())}

    return wrapper


@memoize_args
def calcul_complexe(n, precision=2, methode="standard"):
    """Calcul simulé complexe"""
    import time
    time.sleep(0.1)  # Simulation de calcul lent

    if methode == "standard":
        resultat = sum(i**2 for i in range(n))
    else:
        resultat = sum(i**3 for i in range(n))

    return round(resultat, precision)


print("⚡ Test de mémoïsation :")

# Premier appel (calcul)
result1 = calcul_complexe(100, precision=2, methode="standard")
print(f"   Résultat 1 : {result1}")

# Second appel (cache)
result2 = calcul_complexe(100, precision=2, methode="standard")
print(f"   Résultat 2 : {result2}")

# Appel différent (calcul)
result3 = calcul_complexe(100, precision=3, methode="standard")
print(f"   Résultat 3 : {result3}")

print(f"   Info cache : {calcul_complexe.cache_info()}")

print("\n🔄 GESTION D'ARGUMENTS PAR DÉFAUT COÛTEUX")
print("-" * 42)


def fonction_avec_defaut_couteux(data, timestamp=None, config=None):
    """Fonction avec calculs de défauts optimisés"""

    # Calculer timestamp seulement si nécessaire
    if timestamp is None:
        print("⏰ Calcul du timestamp par défaut")
        timestamp = time.time()

    # Créer config seulement si nécessaire
    if config is None:
        print("⚙️ Création de la config par défaut")
        config = {
            "timeout": 30,
            "retries": 3,
            "debug": False
        }

    return {
        "data": data,
        "timestamp": timestamp,
        "config": config
    }


print("🔄 Test de défauts optimisés :")

# Premier appel (calcul des défauts)
result1 = fonction_avec_defaut_couteux("data1")
print(f"   Résultat 1 timestamp : {result1['timestamp']:.2f}")

# Second appel avec paramètres fournis (pas de calcul)
result2 = fonction_avec_defaut_couteux(
    "data2", timestamp=1234567890, config={"custom": True})
print(f"   Résultat 2 config : {result2['config']}")

print("\n📊 PROFILAGE D'ARGUMENTS")
print("-" * 26)


def profiler_arguments(func):
    """Décorateur qui profile l'utilisation des arguments"""
    stats = {
        "calls": 0,
        "args_usage": {},
        "kwargs_usage": {},
        "total_time": 0
    }

    def wrapper(*args, **kwargs):
        import time
        start = time.time()

        # Statistiques d'appel
        stats["calls"] += 1

        # Statistiques d'arguments positionnels
        for i, arg in enumerate(args):
            key = f"arg_{i}"
            if key not in stats["args_usage"]:
                stats["args_usage"][key] = {"count": 0, "types": set()}
            stats["args_usage"][key]["count"] += 1
            stats["args_usage"][key]["types"].add(type(arg).__name__)

        # Statistiques d'arguments nommés
        for key, value in kwargs.items():
            if key not in stats["kwargs_usage"]:
                stats["kwargs_usage"][key] = {"count": 0, "types": set()}
            stats["kwargs_usage"][key]["count"] += 1
            stats["kwargs_usage"][key]["types"].add(type(value).__name__)

        # Appel de la fonction
        result = func(*args, **kwargs)

        # Temps d'exécution
        end = time.time()
        stats["total_time"] += (end - start)

        return result

    wrapper.stats = stats
    wrapper.print_stats = lambda: print(
        f"📊 Stats pour {func.__name__}: {stats}")

    return wrapper


@profiler_arguments
def fonction_profilée(a, b=10, **options):
    """Fonction pour tester le profilage"""
    return sum([a, b] + list(options.values()) if options else [a, b])


print("📊 Test de profilage :")

# Différents appels
fonction_profilée(5)
fonction_profilée(10, b=20)
fonction_profilée(15, b=25, extra=5, bonus=10)
fonction_profilée("test", b="world")

# Affichage des statistiques
fonction_profilée.print_stats()

print("\n" + "=" * 50)
print("10. RÉSUMÉ FINAL")
print("=" * 50)

print("""
🎯 POINTS CLÉS À RETENIR :

1. 📦 *ARGS (ARGUMENTS VARIABLES) :
   • Capture arguments positionnels en surplus
   • Type : tuple dans la fonction
   • Utilisation : func(*args)
   • Déballage : func(*ma_liste)

2. 🏷️ **KWARGS (ARGUMENTS NOMMÉS VARIABLES) :
   • Capture arguments nommés en surplus
   • Type : dict dans la fonction
   • Utilisation : func(**kwargs)
   • Déballage : func(**mon_dict)

3. 🎭 COMBINAISONS :
   • Ordre : pos, defaut, *args, nom_seul, **kwargs
   • Flexibilité maximale avec validation
   • Proxy et décorateurs universels

4. 🔒 CONTRAINTES DE PARAMÈTRES :
   • / : paramètres positionnels seuls (avant)
   • * : paramètres nommés seuls (après)
   • Design d'API plus sûr

5. 📦 DÉBALLAGE (UNPACKING) :
   • * pour listes/tuples → arguments positionnels
   • ** pour dicts → arguments nommés
   • Construction d'appels dynamiques

6. ✅ VALIDATION ET TRANSFORMATION :
   • Décorateurs pour validation automatique
   • Transformation des arguments
   • Type checking avec annotations

7. 🔍 INTROSPECTION :
   • inspect.signature() pour analyser
   • Création d'appels intelligents
   • Informations sur les paramètres

8. ⚡ OPTIMISATIONS :
   • Mémoïsation avec arguments complexes
   • Défauts calculés à la demande
   • Profilage d'utilisation

💡 PATTERNS AVANCÉS :
✅ Factory de fonctions avec **config
✅ Pipeline de transformations
✅ Dispatcher d'actions
✅ Système de plugins
✅ Builder patterns
✅ Décorateurs universels

🚨 PIÈGES À ÉVITER :
❌ Trop d'arguments positionnels
❌ Validation insuffisante
❌ Défauts mutables sans None
❌ Signatures trop complexes
❌ Manque de documentation

🎯 DESIGN D'API :
• Cohérence dans les noms
• Validation précoce
• Messages d'erreur clairs
• Documentation complète
• Exemples d'utilisation

🎉 Félicitations ! Arguments avancés maîtrisés !
💡 Prochaine étape : Portée et espaces de noms !
📚 Arguments flexibles, explorez la portée !
""")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE - ARGUMENTS AVANCÉS MAÎTRISÉS !")
print("=" * 70)
