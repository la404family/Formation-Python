#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
======================================================================
PORTÉE DES VARIABLES EN PYTHON - GUIDE COMPLET
======================================================================

🎯 Ce fichier couvre la portée (scope) des variables :
   • Règle LEGB (Local, Enclosing, Global, Built-in)
   • Variables locales et globales
   • Variables d'enclosure (closure)
   • Mot-clé global et nonlocal
   • Espaces de noms (namespaces)
   • Bonnes pratiques de portée

📚 Concepts abordés :
   • Portée locale vs globale
   • Fermetures (closures)
   • Variables d'instance et de classe
   • Résolution de noms
   • Évitement de la pollution globale

💡 Objectif : Comprendre et maîtriser la portée des variables
"""

print("=" * 70)
print("PORTÉE DES VARIABLES EN PYTHON - GUIDE COMPLET")
print("=" * 70)

print("\n" + "=" * 50)
print("1. RÈGLE LEGB - RÉSOLUTION DE NOMS")
print("=" * 50)

print("\n🔍 LA RÈGLE LEGB")
print("-" * 16)

print("""
🎯 ORDRE DE RÉSOLUTION DES NOMS (LEGB) :

L - LOCAL : Dans la fonction actuelle
E - ENCLOSING : Dans les fonctions englobantes
G - GLOBAL : Au niveau du module
B - BUILT-IN : Noms intégrés Python

Python cherche dans cet ordre et s'arrête au premier trouvé.
""")

# Variables pour démonstration LEGB
nom_builtin = len  # B - Built-in (fonction len)
nom_global = "Global"  # G - Global


def fonction_externe():
    nom_enclosing = "Enclosing"  # E - Enclosing

    def fonction_interne():
        nom_local = "Local"  # L - Local

        print("🔍 Résolution LEGB dans fonction_interne :")
        print(f"   L - Local : {nom_local}")
        print(f"   E - Enclosing : {nom_enclosing}")
        print(f"   G - Global : {nom_global}")
        print(f"   B - Built-in : {nom_builtin.__name__}")

        # Test de priorité : Local masque Enclosing
        nom_enclosing = "Local masque Enclosing"
        print(f"   Après redéfinition locale : {nom_enclosing}")

    fonction_interne()
    print(f"🔄 Dans fonction_externe, nom_enclosing = {nom_enclosing}")


print("🎯 Démonstration de la règle LEGB :")
fonction_externe()

print("\n📊 INSPECTION DES ESPACES DE NOMS")
print("-" * 33)


def inspecter_namespaces():
    """Inspecte les différents espaces de noms"""
    import builtins

    var_locale = "locale"

    print("📊 Espaces de noms disponibles :")
    print(f"   🏠 Locales : {list(locals().keys())}")
    print(f"   🌍 Globales (échantillon) : {list(globals().keys())[:5]}...")
    print(
        f"   🔧 Built-ins (échantillon) : {list(vars(builtins).keys())[:10]}...")

    # Taille des espaces de noms
    print(f"\n📏 Tailles des espaces :")
    print(f"   Locales : {len(locals())} variables")
    print(f"   Globales : {len(globals())} variables")
    print(f"   Built-ins : {len(vars(builtins))} variables")


inspecter_namespaces()

print("\n" + "=" * 50)
print("2. PORTÉE LOCALE")
print("=" * 50)

print("\n🏠 VARIABLES LOCALES")
print("-" * 19)


def demonstration_locale():
    """Démonstration des variables locales"""

    # Variables créées dans la fonction = locales
    nom = "Alice"
    age = 25
    actif = True

    print("🏠 Variables locales créées :")
    print(f"   nom = {nom}")
    print(f"   age = {age}")
    print(f"   actif = {actif}")

    # Modification locale
    def modifier_locales():
        nom = "Bob"  # Nouvelle variable locale (masque la précédente)
        age = 30     # Nouvelle variable locale
        print(f"   📝 Dans modifier_locales : nom = {nom}, age = {age}")

    modifier_locales()
    print(f"   🔄 Après modifier_locales : nom = {nom}, age = {age}")
    # Les variables de demonstration_locale ne sont pas modifiées !


demonstration_locale()

print("\n🔒 ISOLATION DES FONCTIONS")
print("-" * 25)


def fonction_a():
    """Première fonction avec ses variables"""
    variable = "Je suis dans fonction_a"
    nombre = 100

    print(f"🅰️ fonction_a : variable = {variable}")
    print(f"🅰️ fonction_a : nombre = {nombre}")

    return variable, nombre


def fonction_b():
    """Seconde fonction avec variables du même nom"""
    variable = "Je suis dans fonction_b"
    nombre = 200

    print(f"🅱️ fonction_b : variable = {variable}")
    print(f"🅱️ fonction_b : nombre = {nombre}")

    return variable, nombre


print("🔒 Test d'isolation :")
result_a = fonction_a()
result_b = fonction_b()
print(f"   Résultats indépendants : A={result_a}, B={result_b}")

print("\n⚠️ ERREURS DE PORTÉE LOCALE")
print("-" * 27)


def erreur_portee_locale():
    """Démonstration d'erreurs communes de portée"""

    print("⚠️ Tentative d'accès à variable non définie :")
    try:
        # Simulation d'accès à variable inexistante
        globals()['variable_inexistante']  # Cette clé n'existe pas
    except KeyError:
        print(f"   ❌ NameError : name 'variable_inexistante' is not defined")

    # Erreur subtile : utilisation avant définition
    def erreur_subtile():
        print("⚠️ Utilisation avant définition locale :")
        try:
            # x existe dans la fonction mais pas encore définie
            print(f"x = {x}")
            x = 10
        except UnboundLocalError as e:
            print(f"   ❌ UnboundLocalError : {e}")

    erreur_subtile()


erreur_portee_locale()

print("\n🎯 PARAMÈTRES SONT LOCAUX")
print("-" * 25)


def parameters_sont_locaux(param1, param2="défaut"):
    """Les paramètres de fonction sont des variables locales"""

    print("🎯 Paramètres reçus (variables locales) :")
    print(f"   param1 = {param1}")
    print(f"   param2 = {param2}")

    # Modification des paramètres (locales)
    param1 = "modifié"
    param2 = "changé"

    print("🔄 Après modification locale :")
    print(f"   param1 = {param1}")
    print(f"   param2 = {param2}")

    return param1, param2


# Test des paramètres locaux
print("🧪 Test de paramètres locaux :")
original_var = "original"
result = parameters_sont_locaux(original_var, "initial")
print(f"   Variable originale inchangée : {original_var}")
print(f"   Résultat de la fonction : {result}")

print("\n" + "=" * 50)
print("3. PORTÉE GLOBALE")
print("=" * 50)

print("\n🌍 VARIABLES GLOBALES")
print("-" * 20)

# Variables globales (définies au niveau module)
compteur_global = 0
configuration_globale = {
    "debug": True,
    "version": "1.0.0",
    "max_users": 1000
}


def utiliser_variables_globales():
    """Utilisation (lecture) de variables globales"""

    print("🌍 Lecture de variables globales :")
    print(f"   compteur_global = {compteur_global}")
    print(f"   configuration_globale = {configuration_globale}")

    # On peut lire et utiliser les globales
    if configuration_globale["debug"]:
        print("   🐛 Mode debug activé")

    return compteur_global * 2


resultat_global = utiliser_variables_globales()
print(f"   Résultat utilisant globale : {resultat_global}")

print("\n🔧 MOT-CLÉ GLOBAL")
print("-" * 17)


def modifier_avec_global():
    """Modification de variables globales avec le mot-clé global"""
    global compteur_global, configuration_globale

    print("🔧 Avant modification :")
    print(f"   compteur_global = {compteur_global}")

    # Maintenant on peut modifier
    compteur_global += 1
    configuration_globale["max_users"] = 2000

    print("🔄 Après modification :")
    print(f"   compteur_global = {compteur_global}")
    print(f"   max_users = {configuration_globale['max_users']}")


print("🧪 Test de modification globale :")
print(f"Avant : compteur_global = {compteur_global}")
modifier_avec_global()
print(f"Après : compteur_global = {compteur_global}")

print("\n⚠️ PIÈGE GLOBAL SANS DÉCLARATION")
print("-" * 33)


def piege_global():
    """Démonstration d'un piège courant"""

    print("⚠️ Tentative de modification sans global :")
    try:
        # Cette ligne va créer une erreur !
        # compteur_global = compteur_global + 1  # UnboundLocalError !
        print("   (Code commenté pour éviter l'erreur)")
        print("   ❌ UnboundLocalError : can't access local variable before assignment")
    except UnboundLocalError as e:
        print(f"   ❌ {e}")


piege_global()

print("\n🏗️ CRÉATION DE GLOBALES DYNAMIQUES")
print("-" * 33)


def creer_globale_dynamique():
    """Création dynamique de variables globales"""
    global nouvelle_globale

    nouvelle_globale = "Créée dynamiquement"
    print(f"🏗️ Variable globale créée : {nouvelle_globale}")


# Avant l'appel, la variable n'existe pas
print("🧪 Test de création dynamique :")
print("Avant :", 'nouvelle_globale' in globals())

creer_globale_dynamique()

print("Après :", 'nouvelle_globale' in globals())
print(f"Valeur : {nouvelle_globale}")

print("\n" + "=" * 50)
print("4. PORTÉE D'ENCLOSURE (CLOSURES)")
print("=" * 50)

print("\n🪆 FONCTIONS IMBRIQUÉES ET CLOSURES")
print("-" * 35)


def fonction_externe_closure(multiplicateur):
    """Fonction externe qui retourne une closure"""

    # Variable de la fonction englobante
    message = f"Multiplicateur : {multiplicateur}"

    def fonction_interne_closure(nombre):
        """Fonction interne qui capture les variables externes"""
        # Accès aux variables de la fonction englobante
        print(f"🪆 {message}")
        return nombre * multiplicateur

    return fonction_interne_closure


# Création de closures
doubler = fonction_externe_closure(2)
tripler = fonction_externe_closure(3)

print("🪆 Test de closures :")
print(f"   doubler(5) = {doubler(5)}")
print(f"   tripler(4) = {tripler(4)}")

# Les closures conservent leur environnement !
print(f"   doubler(10) = {doubler(10)}")

print("\n🔍 INSPECTION DES CLOSURES")
print("-" * 26)


def inspecter_closure():
    """Inspection détaillée d'une closure"""
    x = 100
    y = "closure_var"

    def closure_func(z):
        return f"{y}_{x}_{z}"

    return closure_func


ma_closure = inspecter_closure()

print("🔍 Informations sur la closure :")
print(f"   Nom de la fonction : {ma_closure.__name__}")
print(f"   Variables capturées : {ma_closure.__code__.co_freevars}")
print(
    f"   Valeurs des cellules : {[cell.cell_contents for cell in ma_closure.__closure__]}")
print(f"   Test de la closure : {ma_closure('test')}")

print("\n🔧 MOT-CLÉ NONLOCAL")
print("-" * 19)


def demonstration_nonlocal():
    """Démonstration du mot-clé nonlocal"""

    compteur = 0
    message = "Compteur initial"

    def incrementer():
        nonlocal compteur, message
        compteur += 1
        message = f"Compteur à {compteur}"
        print(f"🔧 Dans incrementer : {message}")

    def obtenir_compteur():
        return compteur, message

    print("🧪 Test de nonlocal :")
    print(f"   Initial : {obtenir_compteur()}")

    incrementer()
    print(f"   Après inc : {obtenir_compteur()}")

    incrementer()
    print(f"   Après inc : {obtenir_compteur()}")

    return incrementer, obtenir_compteur


# Test de nonlocal
inc_func, get_func = demonstration_nonlocal()
print("🔄 Fonctions retournées conservent leur état :")
inc_func()
print(f"   État final : {get_func()}")

print("\n🏭 FACTORY DE CLOSURES")
print("-" * 22)


def creer_accumulateur(valeur_initiale=0):
    """Factory qui crée des accumulateurs avec closure"""

    # État privé de l'accumulateur
    total = valeur_initiale
    historique = []

    def accumuler(valeur):
        nonlocal total
        total += valeur
        historique.append(valeur)
        return total

    def obtenir_total():
        return total

    def obtenir_historique():
        return historique.copy()  # Copie pour éviter modifications externes

    def reinitialiser():
        nonlocal total
        total = valeur_initiale
        historique.clear()
        return total

    # Retourner un dictionnaire de fonctions
    return {
        "add": accumuler,
        "total": obtenir_total,
        "history": obtenir_historique,
        "reset": reinitialiser
    }


print("🏭 Test de factory d'accumulateurs :")

# Créer deux accumulateurs indépendants
acc1 = creer_accumulateur(100)
acc2 = creer_accumulateur(0)

print(f"   Acc1 initial : {acc1['total']()}")
print(f"   Acc2 initial : {acc2['total']()}")

print(f"   Acc1 + 10 : {acc1['add'](10)}")
print(f"   Acc1 + 5 : {acc1['add'](5)}")
print(f"   Acc2 + 20 : {acc2['add'](20)}")

print(f"   Acc1 final : {acc1['total']()}, historique : {acc1['history']()}")
print(f"   Acc2 final : {acc2['total']()}, historique : {acc2['history']()}")

print("\n" + "=" * 50)
print("5. ESPACES DE NOMS AVANCÉS")
print("=" * 50)

print("\n📦 MANIPULATION D'ESPACES DE NOMS")
print("-" * 33)


def manipuler_namespaces():
    """Manipulation avancée des espaces de noms"""

    # Variables locales
    var_a = "locale_a"
    var_b = "locale_b"

    print("📦 Espace de noms local :")
    espace_local = locals()
    print(f"   Clés : {list(espace_local.keys())}")

    # Modification dynamique (attention : pas toujours fiable)
    espace_local['var_c'] = "créée_dynamiquement"
    print(f"   Après ajout : var_c existe ? {'var_c' in espace_local}")

    # Accès à l'espace global
    print("\n🌍 Espace de noms global :")
    espace_global = globals()
    print(
        f"   Modules importés : {[k for k in espace_global.keys() if not k.startswith('_')][:5]}")

    # Modification de l'espace global
    espace_global['variable_dynamique_globale'] = "créée depuis fonction"

    return espace_local


resultat_ns = manipuler_namespaces()
# Vérifier si la variable globale a été créée
if 'variable_dynamique_globale' in globals():
    print(
        f"📊 Variable créée dynamiquement : {globals()['variable_dynamique_globale']}")
else:
    print("📊 Variable dynamique non créée")

print("\n🔍 RÉSOLUTION DE NOMS PERSONNALISÉE")
print("-" * 35)


class EspaceNomPersonnalise:
    """Espace de noms personnalisé avec résolution customisée"""

    def __init__(self):
        self.variables = {}
        self.historique = []

    def definir(self, nom, valeur):
        """Définit une variable"""
        ancienne_valeur = self.variables.get(nom)
        self.variables[nom] = valeur
        self.historique.append(f"SET {nom}: {ancienne_valeur} -> {valeur}")
        return valeur

    def obtenir(self, nom, defaut=None):
        """Obtient une variable avec fallback"""
        if nom in self.variables:
            self.historique.append(f"GET {nom}: {self.variables[nom]}")
            return self.variables[nom]

        # Fallback vers globals
        if nom in globals():
            valeur = globals()[nom]
            self.historique.append(f"GET {nom} (global): {valeur}")
            return valeur

        # Fallback vers défaut
        self.historique.append(f"GET {nom} (défaut): {defaut}")
        return defaut

    def lister(self):
        """Liste toutes les variables"""
        return self.variables.copy()

    def historique_operations(self):
        """Retourne l'historique des opérations"""
        return self.historique.copy()


# Test de l'espace personnalisé
print("🔍 Test d'espace de noms personnalisé :")
espace = EspaceNomPersonnalise()

espace.definir("nom", "Alice")
espace.definir("age", 25)

print(f"   nom = {espace.obtenir('nom')}")
print(f"   age = {espace.obtenir('age')}")
print(f"   ville = {espace.obtenir('ville', 'Non définie')}")  # Défaut
print(f"   compteur_global = {espace.obtenir('compteur_global')}")  # Global

print(f"   Variables : {espace.lister()}")
print(f"   Historique : {espace.historique_operations()[-3:]}")  # 3 dernières

print("\n" + "=" * 50)
print("6. PORTÉE DANS LES CLASSES")
print("=" * 50)

print("\n🏛️ VARIABLES DE CLASSE VS INSTANCE")
print("-" * 33)


class DemonstrationPortee:
    """Classe pour démontrer la portée dans les classes"""

    # Variable de classe (partagée)
    compteur_classe = 0
    config_classe = {"debug": True}

    def __init__(self, nom):
        # Variables d'instance (spécifiques à chaque objet)
        self.nom = nom
        self.compteur_instance = 0

        # Incrémenter le compteur de classe
        DemonstrationPortee.compteur_classe += 1

    def incrementer_instance(self):
        """Incrémente le compteur d'instance"""
        self.compteur_instance += 1
        return self.compteur_instance

    @classmethod
    def incrementer_classe(cls):
        """Incrémente le compteur de classe"""
        cls.compteur_classe += 1
        return cls.compteur_classe

    def afficher_portees(self):
        """Affiche les différentes portées disponibles"""
        print(f"🏛️ Portées dans {self.nom} :")
        print(f"   Instance - nom : {self.nom}")
        print(f"   Instance - compteur : {self.compteur_instance}")
        print(f"   Classe - compteur : {DemonstrationPortee.compteur_classe}")
        print(f"   Classe - config : {DemonstrationPortee.config_classe}")

    def modifier_config_attention(self):
        """Attention au piège de modification de classe"""
        # PIÈGE : ceci crée une variable d'instance !
        self.config_classe = {"debug": False, "instance": True}
        print("⚠️ Config modifiée (mais crée une variable d'instance !)")


print("🏛️ Test de portée dans les classes :")

# Création d'instances
obj1 = DemonstrationPortee("Objet1")
obj2 = DemonstrationPortee("Objet2")

print(
    f"Compteur classe après création : {DemonstrationPortee.compteur_classe}")

# Test des compteurs
obj1.incrementer_instance()
obj1.incrementer_instance()
obj2.incrementer_instance()

obj1.afficher_portees()
obj2.afficher_portees()

# Test du piège de modification
print("\n⚠️ Piège de modification de variable de classe :")
print(f"Avant - obj1.config_classe : {obj1.config_classe}")
print(f"Avant - obj2.config_classe : {obj2.config_classe}")

obj1.modifier_config_attention()

print(f"Après - obj1.config_classe : {obj1.config_classe}")
print(f"Après - obj2.config_classe : {obj2.config_classe}")
print(
    f"Après - DemonstrationPortee.config_classe : {DemonstrationPortee.config_classe}")

print("\n🔍 INSPECTION D'INSTANCE")
print("-" * 23)


def inspecter_instance(obj):
    """Inspecte les espaces de noms d'une instance"""
    print(f"🔍 Inspection de {obj.nom} :")

    # Espace de noms de l'instance
    instance_vars = vars(obj)
    print(f"   Variables d'instance : {instance_vars}")

    # Espace de noms de la classe
    class_vars = {k: v for k, v in vars(obj.__class__).items()
                  if not callable(v) and not k.startswith('_')}
    print(f"   Variables de classe : {class_vars}")

    # Résolution d'attributs
    print(f"   Résolution obj.compteur_instance : {obj.compteur_instance}")
    print(f"   Résolution obj.compteur_classe : {obj.compteur_classe}")


inspecter_instance(obj1)

print("\n" + "=" * 50)
print("7. BONNES PRATIQUES DE PORTÉE")
print("=" * 50)

print("\n✅ ÉVITER LA POLLUTION GLOBALE")
print("-" * 30)

# MAUVAIS : trop de variables globales
# variable_globale_1 = "mauvais"
# variable_globale_2 = "mauvais"
# variable_globale_3 = "mauvais"

# BON : utiliser des conteneurs ou modules


class Configuration:
    """Conteneur pour la configuration globale"""
    DEBUG = True
    VERSION = "1.0.0"
    MAX_CONNECTIONS = 100

    @classmethod
    def to_dict(cls):
        return {k: v for k, v in vars(cls).items()
                if not k.startswith('_') and not callable(v)}


def obtenir_config():
    """Factory pour la configuration"""
    return {
        "database": {
            "host": "localhost",
            "port": 5432,
            "name": "myapp"
        },
        "cache": {
            "enabled": True,
            "ttl": 3600
        }
    }


print("✅ Configuration bien organisée :")
print(f"   Class config : {Configuration.to_dict()}")
print(f"   Factory config : {obtenir_config()}")

print("\n🔒 ENCAPSULATION AVEC CLOSURES")
print("-" * 31)


def creer_module_prive():
    """Crée un module avec état privé encapsulé"""

    # État privé (invisible de l'extérieur)
    _donnees_privees = {}
    _compteur_prive = 0

    def ajouter_donnee(cle, valeur):
        nonlocal _compteur_prive
        _donnees_privees[cle] = valeur
        _compteur_prive += 1
        return _compteur_prive

    def obtenir_donnee(cle):
        return _donnees_privees.get(cle)

    def statistiques():
        return {
            "nombre_elements": len(_donnees_privees),
            "compteur_operations": _compteur_prive,
            "cles": list(_donnees_privees.keys())
        }

    # Interface publique uniquement
    return {
        "add": ajouter_donnee,
        "get": obtenir_donnee,
        "stats": statistiques
    }


print("🔒 Module avec encapsulation :")
module_prive = creer_module_prive()

module_prive["add"]("nom", "Alice")
module_prive["add"]("age", 25)

print(f"   Données ajoutées : nom = {module_prive['get']('nom')}")
print(f"   Statistiques : {module_prive['stats']()}")
# Les variables _donnees_privees et _compteur_prive sont inaccessibles !

print("\n🎯 INJECTION DE DÉPENDANCES")
print("-" * 28)


def creer_service_avec_deps(logger=None, config=None):
    """Service avec dépendances injectées plutôt que globales"""

    # Dépendances par défaut si non fournies
    if logger is None:
        def logger(msg): return print(f"📝 LOG: {msg}")

    if config is None:
        config = {"timeout": 30, "retries": 3}

    def executer_operation(nom_operation, donnees):
        """Exécute une opération avec logging"""
        logger(f"Début {nom_operation}")

        # Simulation d'opération
        try:
            if nom_operation == "process":
                resultat = f"Traité: {donnees}"
            elif nom_operation == "validate":
                resultat = f"Validé: {len(donnees)} éléments"
            else:
                resultat = f"Opération {nom_operation} inconnue"

            logger(f"Succès {nom_operation}: {resultat}")
            return {"success": True, "result": resultat}

        except Exception as e:
            logger(f"Erreur {nom_operation}: {e}")
            return {"success": False, "error": str(e)}

    def obtenir_config():
        return config.copy()

    return {
        "execute": executer_operation,
        "config": obtenir_config
    }

# Test avec dépendances personnalisées


def logger_personnalise(message):
    print(f"🎯 CUSTOM LOG [{message}]")


config_personnalisee = {"timeout": 60, "retries": 5}

print("🎯 Service avec injection de dépendances :")
service = creer_service_avec_deps(logger_personnalise, config_personnalisee)

resultat_op = service["execute"]("process", ["data1", "data2"])
print(f"   Résultat : {resultat_op}")

print("\n🧪 TESTS ET PORTÉE")
print("-" * 17)


def fonction_testable(donnees, processor=None, validator=None):
    """Fonction facilement testable grâce à l'injection"""

    # Processeurs par défaut
    if processor is None:
        def processor(x): return x.upper() if isinstance(x, str) else str(x)

    if validator is None:
        def validator(x): return len(x) > 0

    # Traitement
    resultats = []
    for item in donnees:
        if validator(item):
            processed = processor(item)
            resultats.append(processed)

    return resultats


# Version normale
print("🧪 Tests de fonction injectable :")
donnees_test = ["alice", "bob", "", "charlie"]

resultat_normal = fonction_testable(donnees_test)
print(f"   Normal : {resultat_normal}")

# Version avec mocks pour test


def mock_processor(x):
    return f"MOCK_{x}"


def mock_validator(x):
    return x != "bob"  # Rejeter "bob" pour le test


resultat_test = fonction_testable(donnees_test, mock_processor, mock_validator)
print(f"   Test avec mocks : {resultat_test}")

print("\n" + "=" * 50)
print("8. DEBUGGING DE PORTÉE")
print("=" * 50)

print("\n🐛 OUTILS DE DEBUGGING")
print("-" * 22)


def debugger_portee():
    """Outils pour debugger les problèmes de portée"""

    # Variables pour le test
    var_locale = "locale"

    def debug_vars():
        import inspect

        # Frame actuelle
        frame = inspect.currentframe()

        print("🐛 Debug de portée :")
        print(f"   Fonction actuelle : {frame.f_code.co_name}")
        print(f"   Variables locales : {list(frame.f_locals.keys())}")

        # Frame parent
        if frame.f_back:
            parent_frame = frame.f_back
            print(f"   Fonction parent : {parent_frame.f_code.co_name}")
            print(
                f"   Variables parent : {list(parent_frame.f_locals.keys())}")

        # Nettoyage
        del frame

    debug_vars()


debugger_portee()

print("\n🔍 RECHERCHE DE VARIABLES")
print("-" * 25)


def rechercher_variable(nom_var):
    """Recherche une variable dans tous les espaces de noms"""
    import builtins

    resultats = []

    # Recherche locale
    frame = None
    try:
        import inspect
        frame = inspect.currentframe().f_back
        if nom_var in frame.f_locals:
            resultats.append(("Local", frame.f_locals[nom_var]))
    except:
        pass
    finally:
        del frame

    # Recherche globale
    if nom_var in globals():
        resultats.append(("Global", globals()[nom_var]))

    # Recherche built-in
    if hasattr(builtins, nom_var):
        resultats.append(("Built-in", getattr(builtins, nom_var)))

    return resultats


print("🔍 Test de recherche de variables :")

# Variables de test
test_var = "Je suis locale"


def test_recherche():
    test_var = "Je suis dans test_recherche"

    recherches = [
        ("test_var", rechercher_variable("test_var")),
        ("compteur_global", rechercher_variable("compteur_global")),
        ("len", rechercher_variable("len")),
        ("inexistante", rechercher_variable("inexistante"))
    ]

    for nom, resultats in recherches:
        print(f"   {nom} : {resultats}")


test_recherche()

print("\n⚠️ DÉTECTION DE PROBLÈMES COURANTS")
print("-" * 35)


def detecter_problemes_portee():
    """Détecte des problèmes courants de portée"""

    problemes = []

    # Vérifier les variables globales suspectes
    variables_globales = [k for k in globals().keys()
                          if not k.startswith('_') and not callable(globals()[k])]

    if len(variables_globales) > 20:  # Seuil arbitraire
        problemes.append(
            f"Trop de variables globales ({len(variables_globales)})")

    # Vérifier les noms qui masquent les built-ins
    import builtins
    builtins_masques = []
    for nom in variables_globales:
        if hasattr(builtins, nom):
            builtins_masques.append(nom)

    if builtins_masques:
        problemes.append(f"Built-ins masqués : {builtins_masques}")

    # Vérifier les imports *
    if any('*' in str(globals().get(k, '')) for k in globals()):
        problemes.append(
            "Imports avec * détectés (pollution d'espace de noms)")

    return problemes


print("⚠️ Analyse des problèmes de portée :")
problemes = detecter_problemes_portee()
if problemes:
    for probleme in problemes:
        print(f"   ⚠️ {probleme}")
else:
    print("   ✅ Aucun problème détecté")

print("\n" + "=" * 50)
print("9. APPLICATIONS PRATIQUES")
print("=" * 50)

print("\n🏭 SYSTÈME DE PLUGINS AVEC PORTÉE")
print("-" * 33)


def creer_systeme_plugins():
    """Système de plugins avec espaces de noms isolés"""

    # Registre des plugins (privé)
    _plugins = {}
    _config_globale = {"debug": False, "timeout": 30}

    def enregistrer_plugin(nom, fonction_plugin, config=None):
        """Enregistre un plugin avec sa propre configuration"""
        nonlocal _plugins

        # Configuration du plugin (hérite de la globale)
        config_plugin = _config_globale.copy()
        if config:
            config_plugin.update(config)

        def wrapper_plugin(*args, **kwargs):
            # Contexte d'exécution du plugin
            contexte = {
                "nom_plugin": nom,
                "config": config_plugin,
                "logger": lambda msg: print(f"🔌 [{nom}] {msg}")
            }

            # Injecter le contexte dans le plugin
            return fonction_plugin(contexte, *args, **kwargs)

        _plugins[nom] = {
            "function": wrapper_plugin,
            "config": config_plugin,
            "active": True
        }

        return nom

    def executer_plugin(nom, *args, **kwargs):
        """Exécute un plugin spécifique"""
        if nom not in _plugins:
            raise ValueError(f"Plugin '{nom}' non trouvé")

        plugin_info = _plugins[nom]
        if not plugin_info["active"]:
            raise ValueError(f"Plugin '{nom}' désactivé")

        return plugin_info["function"](*args, **kwargs)

    def lister_plugins():
        """Liste tous les plugins enregistrés"""
        return {nom: {"active": info["active"], "config": info["config"]}
                for nom, info in _plugins.items()}

    def configurer_global(**nouvelle_config):
        """Met à jour la configuration globale"""
        nonlocal _config_globale
        _config_globale.update(nouvelle_config)

    return {
        "register": enregistrer_plugin,
        "execute": executer_plugin,
        "list": lister_plugins,
        "configure": configurer_global
    }


# Création du système
systeme = creer_systeme_plugins()

# Plugins de test


def plugin_salutation(contexte, nom):
    """Plugin qui salue avec logging"""
    contexte["logger"](f"Salutation de {nom}")
    return f"Bonjour {nom} !"


def plugin_calcul(contexte, a, b, operation="add"):
    """Plugin de calcul avec configuration"""
    timeout = contexte["config"]["timeout"]
    contexte["logger"](f"Calcul {operation} avec timeout {timeout}s")

    if operation == "add":
        return a + b
    elif operation == "mul":
        return a * b
    else:
        return None


# Enregistrement des plugins
systeme["register"]("salutation", plugin_salutation)
systeme["register"]("calcul", plugin_calcul, {"precision": 2})

print("🏭 Test du système de plugins :")
print(f"   Plugins : {list(systeme['list']().keys())}")

# Exécution des plugins
salut = systeme["execute"]("salutation", "Alice")
print(f"   Salutation : {salut}")

calcul = systeme["execute"]("calcul", 10, 5, operation="mul")
print(f"   Calcul : {calcul}")

print("\n🎮 MACHINE À ÉTATS AVEC CLOSURES")
print("-" * 33)


def creer_machine_etats(etat_initial, transitions):
    """Crée une machine à états avec closures"""

    # État privé
    _etat_actuel = etat_initial
    _historique = [etat_initial]

    def obtenir_etat():
        return _etat_actuel

    def changer_etat(nouvel_etat):
        nonlocal _etat_actuel

        # Vérifier si la transition est autorisée
        etats_autorises = transitions.get(_etat_actuel, [])
        if nouvel_etat not in etats_autorises:
            raise ValueError(
                f"Transition {_etat_actuel} -> {nouvel_etat} non autorisée")

        ancien_etat = _etat_actuel
        _etat_actuel = nouvel_etat
        _historique.append(nouvel_etat)

        print(f"🎮 Transition : {ancien_etat} -> {nouvel_etat}")
        return nouvel_etat

    def obtenir_historique():
        return _historique.copy()

    def etats_disponibles():
        return transitions.get(_etat_actuel, [])

    def reinitialiser():
        nonlocal _etat_actuel
        _etat_actuel = etat_initial
        _historique.clear()
        _historique.append(etat_initial)

    return {
        "state": obtenir_etat,
        "transition": changer_etat,
        "history": obtenir_historique,
        "available": etats_disponibles,
        "reset": reinitialiser
    }


# Machine à états pour un processus de commande
transitions_commande = {
    "nouvelle": ["en_attente", "annulee"],
    "en_attente": ["confirmee", "annulee"],
    "confirmee": ["expediee", "annulee"],
    "expediee": ["livree"],
    "livree": [],
    "annulee": []
}

print("🎮 Test de machine à états :")
machine = creer_machine_etats("nouvelle", transitions_commande)

print(f"   État initial : {machine['state']()}")
print(f"   États disponibles : {machine['available']()}")

# Transitions valides
machine["transition"]("en_attente")
machine["transition"]("confirmee")
machine["transition"]("expediee")
machine["transition"]("livree")

print(f"   État final : {machine['state']()}")
print(f"   Historique : {machine['history']()}")

# Test de transition invalide
try:
    machine["transition"]("nouvelle")  # Pas possible depuis "livree"
except ValueError as e:
    print(f"   ❌ Erreur attendue : {e}")

print("\n" + "=" * 50)
print("10. RÉSUMÉ FINAL")
print("=" * 50)

print("""
🎯 POINTS CLÉS À RETENIR :

1. 🔍 RÈGLE LEGB :
   • L - Local (fonction actuelle)
   • E - Enclosing (fonctions englobantes)
   • G - Global (niveau module)
   • B - Built-in (intégrés Python)

2. 🏠 PORTÉE LOCALE :
   • Variables créées dans fonctions
   • Paramètres sont locaux
   • Isolation entre fonctions
   • Erreurs : NameError, UnboundLocalError

3. 🌍 PORTÉE GLOBALE :
   • Variables au niveau module
   • Mot-clé global pour modification
   • Éviter la pollution globale
   • Préférer l'injection de dépendances

4. 🪆 CLOSURES :
   • Fonctions imbriquées
   • Capture de variables englobantes
   • Mot-clé nonlocal pour modification
   • État encapsulé

5. 🏛️ PORTÉE DANS LES CLASSES :
   • Variables de classe vs instance
   • Résolution d'attributs
   • Méthodes et espaces de noms
   • Pièges de modification

6. 📦 ESPACES DE NOMS :
   • locals() et globals()
   • Manipulation dynamique
   • Résolution personnalisée
   • Introspection avancée

💡 BONNES PRATIQUES :
✅ Éviter les variables globales
✅ Utiliser l'injection de dépendances
✅ Encapsuler avec des closures
✅ Nommer explicitement les scopes
✅ Documenter les portées complexes
✅ Tester l'isolation

🚨 PIÈGES À ÉVITER :
❌ Pollution d'espace global
❌ Modification globale sans déclaration
❌ Masquage des built-ins
❌ Closures avec variables mutables
❌ Confusion classe/instance
❌ Late binding dans les boucles

⚡ PATTERNS AVANCÉS :
• Factory de closures
• Système de plugins isolés
• Machine à états avec closures
• Configuration hiérarchique
• Injection de contexte
• Namespaces personnalisés

🔧 DEBUGGING :
• inspect module pour introspection
• Recherche de variables LEGB
• Détection de problèmes courants
• Outils de visualisation
• Tests d'isolation

🎯 APPLICATIONS :
• Systèmes de configuration
• Plugins et extensions
• State machines
• Frameworks et libraries
• Systèmes de permissions
• Contextes d'exécution

🎉 Félicitations ! Portée des variables maîtrisée !
💡 Prochaine étape : Fonctions lambda et built-in !
📚 Scopes maîtrisés, explorez les lambdas !
""")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE - PORTÉE DES VARIABLES MAÎTRISÉE !")
print("=" * 70)
