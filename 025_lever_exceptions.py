#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
======================================================================
LEVER DES EXCEPTIONS EN PYTHON - GUIDE COMPLET
======================================================================

🎯 Ce fichier couvre comment lever des exceptions :
   • Instruction raise
   • Exceptions personnalisées
   • Re-lever des exceptions
   • Chaînage d'exceptions
   • Assertions et debugging

📚 Concepts abordés :
   • raise Exception("message")
   • Création de classes d'exception
   • raise...from pour chaînage
   • assert pour conditions
   • Debugging avec exceptions

💡 Objectif : Maîtriser la création et le lever d'exceptions
"""

print("=" * 70)
print("LEVER DES EXCEPTIONS EN PYTHON - GUIDE COMPLET")
print("=" * 70)

print("\n" + "=" * 50)
print("1. INSTRUCTION RAISE DE BASE")
print("=" * 50)

print("\n🚀 LEVER DES EXCEPTIONS SIMPLES")
print("-" * 30)


def demo_raise_simple():
    """Démonstration de l'instruction raise de base"""

    print("🚀 Lever des exceptions simples :")

    def valider_age(age):
        """Valider un âge avec raise"""
        if not isinstance(age, int):
            raise TypeError(
                f"L'âge doit être un entier, reçu {type(age).__name__}")

        if age < 0:
            raise ValueError(f"L'âge ne peut pas être négatif : {age}")

        if age > 150:
            raise ValueError(f"L'âge semble irréaliste : {age}")

        return True

    def calculer_racine_carree(x):
        """Calculer la racine carrée avec validation"""
        if not isinstance(x, (int, float)):
            raise TypeError("Le paramètre doit être un nombre")

        if x < 0:
            raise ValueError(
                "Impossible de calculer la racine d'un nombre négatif")

        return x ** 0.5

    # Tests de validation d'âge
    print("\n   1️⃣ Tests de validation d'âge :")
    ages_test = [25, -5, 200, "trente", 45.5]

    for age in ages_test:
        print(f"      Test age {age} :", end=" ")
        try:
            valider_age(age)
            print("✅ Valide")
        except (TypeError, ValueError) as e:
            print(f"❌ {type(e).__name__}: {e}")

    # Tests de racine carrée
    print("\n   2️⃣ Tests de racine carrée :")
    valeurs_test = [9, -4, "abc", 16.0, 0]

    for valeur in valeurs_test:
        print(f"      Racine de {valeur} :", end=" ")
        try:
            resultat = calculer_racine_carree(valeur)
            print(f"✅ {resultat:.2f}")
        except (TypeError, ValueError) as e:
            print(f"❌ {type(e).__name__}: {e}")


demo_raise_simple()

print("\n🔄 RE-LEVER DES EXCEPTIONS")
print("-" * 26)


def demo_re_raise():
    """Démonstration du re-lever d'exceptions"""

    print("🔄 Re-lever des exceptions :")

    def diviser_avec_log(a, b):
        """Division avec logging et re-raise"""
        print(f"      🧮 Tentative de division : {a} / {b}")

        try:
            resultat = a / b
            print(f"      ✅ Résultat : {resultat}")
            return resultat
        except ZeroDivisionError as e:
            print(f"      📝 Log : Division par zéro détectée à {__name__}")
            # Re-lever l'exception après logging
            raise  # Équivalent à : raise e
        except TypeError as e:
            print(f"      📝 Log : Erreur de type dans la division")
            # Modifier et re-lever
            raise TypeError(
                f"Types invalides pour division : {type(a)}, {type(b)}") from e

    def traitement_avec_gestion(donnees):
        """Traitement qui gère et transforme les exceptions"""
        try:
            return diviser_avec_log(donnees[0], donnees[1])
        except (ZeroDivisionError, TypeError) as e:
            print(f"      🚨 Gestion niveau supérieur : {type(e).__name__}")
            # Transformer en exception métier
            raise RuntimeError(
                f"Impossible de traiter les données {donnees}") from e

    # Tests de re-raise
    print("\n   Tests de re-raise :")
    tests = [
        ([10, 2], "Division normale"),
        ([10, 0], "Division par zéro"),
        ([10, "abc"], "Type invalide"),
        (["hello", 5], "Types incompatibles"),
    ]

    for donnees, description in tests:
        print(f"\n   📋 Test : {description}")
        try:
            resultat = traitement_avec_gestion(donnees)
            print(f"   🎉 Succès : {resultat}")
        except RuntimeError as e:
            print(f"   💀 Échec final : {e}")
            # Afficher la chaîne d'exceptions
            cause = e.__cause__
            if cause:
                print(f"   🔗 Causé par : {type(cause).__name__}: {cause}")


demo_re_raise()

print("\n" + "=" * 50)
print("2. EXCEPTIONS PERSONNALISÉES")
print("=" * 50)

print("\n🎨 CRÉER DES EXCEPTIONS CUSTOM")
print("-" * 30)

# Définition d'exceptions personnalisées


class ValidationError(Exception):
    """Exception pour les erreurs de validation"""

    def __init__(self, message, field=None, value=None):
        super().__init__(message)
        self.field = field
        self.value = value
        self.message = message


class BusinessLogicError(Exception):
    """Exception pour les erreurs de logique métier"""

    def __init__(self, message, error_code=None, context=None):
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.context = context or {}


class ConfigurationError(Exception):
    """Exception pour les erreurs de configuration"""
    pass


class DatabaseError(Exception):
    """Exception pour les erreurs de base de données"""

    def __init__(self, message, query=None, connection_info=None):
        super().__init__(message)
        self.message = message
        self.query = query
        self.connection_info = connection_info


def demo_exceptions_personnalisees():
    """Démonstration des exceptions personnalisées"""

    print("🎨 Exceptions personnalisées :")

    def valider_utilisateur(donnees):
        """Validation d'utilisateur avec exceptions custom"""

        # Validation du nom
        if "nom" not in donnees:
            raise ValidationError("Le nom est requis", field="nom")

        nom = donnees["nom"]
        if not isinstance(nom, str) or len(nom.strip()) < 2:
            raise ValidationError(
                "Le nom doit être une chaîne d'au moins 2 caractères",
                field="nom",
                value=nom
            )

        # Validation de l'email
        if "email" not in donnees:
            raise ValidationError("L'email est requis", field="email")

        email = donnees["email"]
        if "@" not in email or "." not in email:
            raise ValidationError(
                "Format d'email invalide",
                field="email",
                value=email
            )

        # Validation de l'âge
        if "age" in donnees:
            age = donnees["age"]
            if not isinstance(age, int) or age < 0 or age > 150:
                raise ValidationError(
                    "L'âge doit être un entier entre 0 et 150",
                    field="age",
                    value=age
                )

        return True

    def creer_compte_utilisateur(donnees):
        """Création de compte avec logique métier"""

        # Validation des données
        try:
            valider_utilisateur(donnees)
        except ValidationError as e:
            # Transformer en erreur métier
            raise BusinessLogicError(
                f"Impossible de créer le compte : {e.message}",
                error_code="INVALID_USER_DATA",
                context={"field": e.field, "value": e.value}
            ) from e

        # Simulation de logique métier
        email = donnees["email"]
        if email.endswith("@spam.com"):
            raise BusinessLogicError(
                "Domaine email non autorisé",
                error_code="FORBIDDEN_DOMAIN",
                context={"domain": "spam.com"}
            )

        # Simulation d'erreur de base de données
        if donnees["nom"].lower() == "error":
            raise DatabaseError(
                "Erreur de base de données lors de l'insertion",
                query="INSERT INTO users (nom, email) VALUES (?, ?)",
                connection_info="localhost:5432"
            )

        return {"id": 12345, "nom": donnees["nom"], "email": email}

    # Tests avec exceptions personnalisées
    print("\n   Tests de validation et création de compte :")

    utilisateurs_test = [
        ({"nom": "Alice Dupont", "email": "alice@test.com",
         "age": 25}, "Utilisateur valide"),
        ({"email": "bob@test.com"}, "Nom manquant"),
        ({"nom": "A", "email": "alice@test.com"}, "Nom trop court"),
        ({"nom": "Charlie", "email": "email-invalide"}, "Email invalide"),
        ({"nom": "Diane", "email": "diane@test.com", "age": -5}, "Âge invalide"),
        ({"nom": "Eve", "email": "eve@spam.com"}, "Domaine interdit"),
        ({"nom": "error", "email": "test@test.com"}, "Erreur base de données"),
    ]

    for donnees, description in utilisateurs_test:
        print(f"\n   📋 Test : {description}")
        print(f"      Données : {donnees}")

        try:
            utilisateur = creer_compte_utilisateur(donnees)
            print(f"      ✅ Compte créé : {utilisateur}")
        except ValidationError as e:
            print(f"      ❌ Validation : {e.message}")
            if e.field:
                print(f"         Champ : {e.field}")
            if e.value:
                print(f"         Valeur : {e.value}")
        except BusinessLogicError as e:
            print(f"      ❌ Logique métier : {e.message}")
            print(f"         Code : {e.error_code}")
            print(f"         Contexte : {e.context}")
        except DatabaseError as e:
            print(f"      ❌ Base de données : {e.message}")
            if e.query:
                print(f"         Requête : {e.query}")


demo_exceptions_personnalisees()

print("\n🏗️ HIÉRARCHIE D'EXCEPTIONS")
print("-" * 27)


def demo_hierarchie_exceptions():
    """Démonstration d'une hiérarchie d'exceptions"""

    print("🏗️ Hiérarchie d'exceptions :")

    # Hiérarchie d'exceptions pour une application
    class AppError(Exception):
        """Exception de base de l'application"""
        pass

    class UserError(AppError):
        """Erreurs liées aux utilisateurs"""
        pass

    class AuthenticationError(UserError):
        """Erreurs d'authentification"""
        pass

    class AuthorizationError(UserError):
        """Erreurs d'autorisation"""
        pass

    class DataError(AppError):
        """Erreurs liées aux données"""
        pass

    class ValidationError(DataError):
        """Erreurs de validation des données"""
        pass

    class IntegrityError(DataError):
        """Erreurs d'intégrité des données"""
        pass

    def simuler_operations():
        """Simuler différentes opérations avec exceptions"""

        operations = [
            ("login", "user_inexistant", AuthenticationError, "Utilisateur inexistant"),
            ("access_admin", "user_normal",
             AuthorizationError, "Droits insuffisants"),
            ("validate_data", "data_invalid", ValidationError, "Données invalides"),
            ("save_data", "constraint_violation",
             IntegrityError, "Violation contrainte"),
            ("normal_op", "success", None, "Opération réussie"),
        ]

        for operation, scenario, exception_type, message in operations:
            print(f"\n      🔧 Opération : {operation} ({scenario})")

            try:
                if exception_type:
                    raise exception_type(message)
                else:
                    print(f"         ✅ {message}")
            except AuthenticationError as e:
                print(f"         🔐 Erreur d'authentification : {e}")
            except AuthorizationError as e:
                print(f"         🚫 Erreur d'autorisation : {e}")
            except ValidationError as e:
                print(f"         📝 Erreur de validation : {e}")
            except IntegrityError as e:
                print(f"         🔗 Erreur d'intégrité : {e}")
            except UserError as e:
                print(f"         👤 Erreur utilisateur générique : {e}")
            except DataError as e:
                print(f"         📊 Erreur de données générique : {e}")
            except AppError as e:
                print(f"         🏠 Erreur application générique : {e}")

    simuler_operations()


demo_hierarchie_exceptions()

print("\n" + "=" * 50)
print("3. CHAÎNAGE D'EXCEPTIONS")
print("=" * 50)

print("\n🔗 CHAÎNER DES EXCEPTIONS")
print("-" * 24)


def demo_chainement_exceptions():
    """Démonstration du chaînage d'exceptions"""

    print("🔗 Chaînage d'exceptions avec 'from' :")

    def lire_configuration(fichier):
        """Lire un fichier de configuration avec chaînage"""
        try:
            with open(fichier, 'r') as f:
                contenu = f.read()
        except FileNotFoundError as e:
            raise ConfigurationError(
                f"Fichier de configuration manquant : {fichier}") from e

        try:
            import json
            config = json.loads(contenu)
        except json.JSONDecodeError as e:
            raise ConfigurationError(
                f"Format JSON invalide dans {fichier}") from e

        return config

    def valider_configuration(config):
        """Valider la configuration avec chaînage"""
        try:
            if "database" not in config:
                raise KeyError("Section 'database' manquante")

            db_config = config["database"]
            if "host" not in db_config:
                raise KeyError("Paramètre 'host' manquant dans database")

        except KeyError as e:
            raise ConfigurationError(f"Configuration incomplète : {e}") from e

    def initialiser_application(fichier_config):
        """Initialiser l'application avec chaînage complet"""
        try:
            # Étape 1 : Lire la configuration
            config = lire_configuration(fichier_config)

            # Étape 2 : Valider la configuration
            valider_configuration(config)

            # Étape 3 : Initialiser (simulation)
            if config.get("database", {}).get("host") == "invalid_host":
                raise ConnectionError("Impossible de se connecter à la base")

            return "Application initialisée avec succès"

        except ConfigurationError:
            # Re-lever les erreurs de configuration
            raise
        except ConnectionError as e:
            # Chaîner les erreurs de connexion
            raise RuntimeError(
                "Échec d'initialisation de l'application") from e

    # Tests de chaînage
    print("\n   Tests de chaîne d'exceptions :")

    # Créer des fichiers de test temporaires
    import json
    import os

    # Fichier valide
    config_valide = {"database": {"host": "localhost", "port": 5432}}
    with open("config_valide.json", "w") as f:
        json.dump(config_valide, f)

    # Fichier JSON invalide
    with open("config_invalide.json", "w") as f:
        f.write("{ invalid json }")

    # Fichier avec configuration incomplète
    config_incomplete = {"other": "value"}
    with open("config_incomplete.json", "w") as f:
        json.dump(config_incomplete, f)

    # Fichier avec host invalide
    config_host_invalide = {"database": {"host": "invalid_host"}}
    with open("config_host_invalide.json", "w") as f:
        json.dump(config_host_invalide, f)

    # Tests
    tests_config = [
        ("config_valide.json", "Configuration valide"),
        ("config_inexistant.json", "Fichier inexistant"),
        ("config_invalide.json", "JSON invalide"),
        ("config_incomplete.json", "Configuration incomplète"),
        ("config_host_invalide.json", "Host de base invalide"),
    ]

    for fichier, description in tests_config:
        print(f"\n   📋 Test : {description}")

        try:
            resultat = initialiser_application(fichier)
            print(f"      ✅ Succès : {resultat}")
        except Exception as e:
            print(f"      ❌ {type(e).__name__} : {e}")

            # Afficher la chaîne d'exceptions
            cause = e.__cause__
            niveau = 1
            while cause:
                print(
                    f"      {'  ' * niveau}🔗 Causé par : {type(cause).__name__}: {cause}")
                cause = cause.__cause__
                niveau += 1

    # Nettoyage
    for fichier in ["config_valide.json", "config_invalide.json", "config_incomplete.json", "config_host_invalide.json"]:
        if os.path.exists(fichier):
            os.remove(fichier)


demo_chainement_exceptions()

print("\n" + "=" * 50)
print("4. ASSERTIONS ET DEBUGGING")
print("=" * 50)

print("\n🐛 ASSERTIONS POUR LE DEBUGGING")
print("-" * 31)


def demo_assertions():
    """Démonstration des assertions"""

    print("🐛 Assertions pour le debugging :")

    def calculer_moyenne(valeurs):
        """Calculer la moyenne avec assertions"""
        # Assertions pour vérifier les préconditions
        assert isinstance(
            valeurs, list), f"Attendu une liste, reçu {type(valeurs)}"
        assert len(valeurs) > 0, "La liste ne peut pas être vide"
        assert all(isinstance(v, (int, float))
                   for v in valeurs), "Tous les éléments doivent être numériques"

        moyenne = sum(valeurs) / len(valeurs)

        # Assertion pour vérifier la postcondition
        assert isinstance(moyenne, (int, float)
                          ), "La moyenne doit être numérique"

        return moyenne

    def diviser_securise(a, b):
        """Division sécurisée avec assertions"""
        assert isinstance(
            a, (int, float)), f"a doit être numérique, reçu {type(a)}"
        assert isinstance(
            b, (int, float)), f"b doit être numérique, reçu {type(b)}"
        assert b != 0, "Division par zéro interdite"

        resultat = a / b

        # Vérification du résultat
        assert isinstance(resultat, (int, float)
                          ), "Le résultat doit être numérique"

        return resultat

    def factorielle(n):
        """Calcul de factorielle avec assertions"""
        assert isinstance(n, int), f"n doit être un entier, reçu {type(n)}"
        assert n >= 0, f"n doit être positif ou nul, reçu {n}"

        if n <= 1:
            return 1

        resultat = 1
        for i in range(2, n + 1):
            resultat *= i
            # Assertion pour vérifier que le résultat grandit
            assert resultat > 0, "Le résultat ne devrait jamais être négatif"

        return resultat

    # Tests des assertions
    print("\n   1️⃣ Tests de calcul de moyenne :")

    tests_moyenne = [
        ([1, 2, 3, 4, 5], "Liste valide"),
        ([], "Liste vide"),
        ("pas une liste", "Type incorrect"),
        ([1, 2, "trois"], "Éléments non numériques"),
        ([10, 20, 30], "Cas valide 2"),
    ]

    for valeurs, description in tests_moyenne:
        print(f"      Test : {description}")
        print(f"      Valeurs : {valeurs}")

        try:
            moyenne = calculer_moyenne(valeurs)
            print(f"      ✅ Moyenne : {moyenne}")
        except AssertionError as e:
            print(f"      ❌ Assertion échouée : {e}")
        except Exception as e:
            print(f"      💥 Autre erreur : {type(e).__name__}: {e}")

    print("\n   2️⃣ Tests de division sécurisée :")

    tests_division = [
        ((10, 2), "Division normale"),
        ((10, 0), "Division par zéro"),
        (("10", 2), "Type incorrect a"),
        ((10, "2"), "Type incorrect b"),
        ((15, 3), "Cas valide 2"),
    ]

    for (a, b), description in tests_division:
        print(f"      Test : {description} - {a} / {b}")

        try:
            resultat = diviser_securise(a, b)
            print(f"      ✅ Résultat : {resultat}")
        except AssertionError as e:
            print(f"      ❌ Assertion échouée : {e}")

    print("\n   3️⃣ Tests de factorielle :")

    tests_factorielle = [5, 0, -1, 3.5, "5"]

    for n in tests_factorielle:
        print(f"      Factorielle de {n} :", end=" ")

        try:
            resultat = factorielle(n)
            print(f"✅ {resultat}")
        except AssertionError as e:
            print(f"❌ {e}")
        except Exception as e:
            print(f"💥 {type(e).__name__}: {e}")


demo_assertions()

print("\n🔧 DEBUGGING AVANCÉ AVEC EXCEPTIONS")
print("-" * 37)


def demo_debugging_avance():
    """Démonstration du debugging avancé"""

    print("🔧 Debugging avancé avec exceptions :")

    import traceback
    import sys

    def fonction_avec_erreur(niveau=0):
        """Fonction qui génère une erreur à différents niveaux"""
        if niveau == 0:
            return fonction_avec_erreur(1)
        elif niveau == 1:
            return fonction_avec_erreur(2)
        elif niveau == 2:
            # Générer une erreur ici
            x = 1 / 0  # Division par zéro

    def analyser_exception_detaillee():
        """Analyser une exception en détail"""
        try:
            fonction_avec_erreur()
        except Exception as e:
            print(f"\n      🔍 Analyse détaillée de l'exception :")
            print(f"      Type : {type(e).__name__}")
            print(f"      Message : {e}")
            print(f"      Args : {e.args}")

            print(f"\n      📚 Stack trace complète :")
            traceback.print_exc()

            print(f"\n      📋 Stack trace formatée :")
            tb_lines = traceback.format_exception(type(e), e, e.__traceback__)
            for line in tb_lines:
                print(f"         {line.strip()}")

            print(f"\n      🎯 Informations sur la frame :")
            tb = e.__traceback__
            while tb:
                frame = tb.tb_frame
                print(f"         Fichier : {frame.f_code.co_filename}")
                print(f"         Fonction : {frame.f_code.co_name}")
                print(f"         Ligne : {tb.tb_lineno}")
                print(
                    f"         Variables locales : {list(frame.f_locals.keys())}")
                tb = tb.tb_next
                if tb:
                    print(f"         ---")

    analyser_exception_detaillee()


demo_debugging_avance()

print("\n" + "=" * 50)
print("5. RÉSUMÉ FINAL")
print("=" * 50)

print("""
🎯 POINTS CLÉS À RETENIR :

1. 🚀 INSTRUCTION RAISE :
   • raise Exception("message") pour lever
   • raise sans paramètre pour re-lever
   • raise NewException from old_exception pour chaîner

2. 🎨 EXCEPTIONS PERSONNALISÉES :
   • class MyError(Exception): pass
   • Hériter d'exceptions appropriées
   • Ajouter des attributs spécifiques
   • Créer des hiérarchies logiques

3. 🔗 CHAÎNAGE D'EXCEPTIONS :
   • raise...from pour préserver la cause
   • __cause__ contient l'exception d'origine
   • Facilite le debugging en gardant le contexte

4. 🐛 ASSERTIONS :
   • assert condition, "message"
   • Pour vérifier les invariants
   • Désactivées avec python -O
   • Utiles pour le debugging et les tests

5. 🔧 DEBUGGING AVANCÉ :
   • traceback module pour stack traces
   • Inspection des frames d'exécution
   • Variables locales dans chaque frame
   • Formatage personnalisé des erreurs

💡 BONNES PRATIQUES :
✅ Exceptions spécifiques et informatives
✅ Hiérarchie logique d'exceptions
✅ Chaînage pour préserver le contexte
✅ Messages d'erreur clairs et utiles
✅ Assertions pour invariants et préconditions

🚨 À ÉVITER :
❌ Lever Exception générique
❌ Messages d'erreur vagues
❌ Casser la chaîne d'exceptions
❌ Assertions pour validation utilisateur
❌ Masquer les informations de debug

⚡ PATTERNS AVANCÉS :
• Context managers pour nettoyage automatique
• Décorateurs pour gestion d'erreurs répétitives
• Factory patterns pour création d'exceptions
• Observer pattern pour logging d'erreurs

🎉 Félicitations ! Lever d'exceptions maîtrisé !
💡 Prochaine étape : Lecture de fichiers !
📚 Exceptions levées, fichiers à découvrir !
""")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE - LEVER D'EXCEPTIONS MAÎTRISÉ !")
print("=" * 70)
