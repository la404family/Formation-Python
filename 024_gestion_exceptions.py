#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
======================================================================
GESTION DES EXCEPTIONS EN PYTHON - GUIDE COMPLET
======================================================================

🎯 Ce fichier couvre la gestion des exceptions en détail :
   • Types d'exceptions et hiérarchie
   • Try, except, else, finally
   • Exceptions personnalisées
   • Bonnes pratiques de gestion d'erreurs
   • Logging et debugging
   • Patterns avancés

📚 Concepts abordés :
   • Exceptions built-in
   • Propagation d'exceptions
   • Context managers et cleanup
   • Assertions et validation
   • Error handling patterns
   • Performance et exceptions

💡 Objectif : Maîtriser la gestion robuste des erreurs
"""

import logging
import random
import time
import traceback
print("=" * 70)
print("GESTION DES EXCEPTIONS EN PYTHON - GUIDE COMPLET")
print("=" * 70)

print("\n" + "=" * 50)
print("1. FONDAMENTAUX DES EXCEPTIONS")
print("=" * 50)

print("\n🚨 QU'EST-CE QU'UNE EXCEPTION ?")
print("-" * 30)

print("""
🎯 DÉFINITION :
Une exception est un événement qui se produit pendant l'exécution
d'un programme et qui interrompt le flux normal des instructions.

🔄 MÉCANISME :
1. Une erreur se produit
2. Python "lève" (raise) une exception
3. Le programme s'arrête SAUF si l'exception est "attrapée" (catch)
4. L'exception remonte la pile d'appels jusqu'à être gérée

⚡ AVANTAGES :
• Séparation logique métier / gestion d'erreurs
• Propagation automatique des erreurs
• Code plus lisible et maintenable
• Gestion centralisée des erreurs
""")

print("\n🎯 EXCEPTIONS COURANTES")
print("-" * 23)

# Démonstration des exceptions les plus courantes
exceptions_courantes = [
    ("NameError", "print(variable_inexistante)", "Variable non définie"),
    ("TypeError", "len(42)", "Mauvais type pour l'opération"),
    ("ValueError", "int('hello')", "Valeur inappropriée pour le type"),
    ("IndexError", "[1, 2, 3][5]", "Index hors limites"),
    ("KeyError", "{'a': 1}['b']", "Clé inexistante dans dictionnaire"),
    ("AttributeError", "'hello'.inexistant", "Attribut inexistant"),
    ("ZeroDivisionError", "10 / 0", "Division par zéro"),
    ("FileNotFoundError", "open('inexistant.txt')", "Fichier non trouvé"),
]

print("🚨 Exceptions Python courantes :")
for nom, code, description in exceptions_courantes:
    print(f"   {nom:<18} : {description}")
    print(f"     Exemple : {code}")

print("\n🏗️ HIÉRARCHIE DES EXCEPTIONS")
print("-" * 28)

print("""
🌳 HIÉRARCHIE SIMPLIFIÉE :

BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   ├── OverflowError
    │   └── FloatingPointError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── ValueError
    ├── TypeError
    ├── NameError
    ├── AttributeError
    ├── ImportError
    ├── OSError
    │   └── FileNotFoundError
    └── RuntimeError

💡 RÈGLE : Toujours capturer Exception ou ses sous-classes,
          jamais BaseException directement !
""")

print("\n" + "=" * 50)
print("2. SYNTAXE TRY/EXCEPT")
print("=" * 50)

print("\n🎯 STRUCTURE DE BASE")
print("-" * 19)

print("🎯 Syntaxe try/except fondamentale :")

# Exemple simple de try/except


def division_simple(a, b):
    """Division avec gestion d'erreur basique"""
    try:
        resultat = a / b
        print(f"   ✅ {a} ÷ {b} = {resultat}")
        return resultat
    except ZeroDivisionError:
        print(f"   ❌ Division par zéro impossible : {a} ÷ {b}")
        return None


# Tests
print("Tests de division :")
division_simple(10, 2)
division_simple(10, 0)
division_simple(15, 3)

print("\n🎭 EXCEPT MULTIPLES")
print("-" * 19)


def conversion_robuste(valeur):
    """Conversion avec gestion d'erreurs multiples"""
    try:
        # Tentative de conversion en nombre
        if isinstance(valeur, str):
            if '.' in valeur:
                resultat = float(valeur)
            else:
                resultat = int(valeur)
        else:
            resultat = float(valeur)

        print(f"   ✅ Conversion réussie : '{valeur}' -> {resultat}")
        return resultat

    except ValueError:
        print(
            f"   ❌ ValueError : Impossible de convertir '{valeur}' en nombre")
        return None
    except TypeError:
        print(f"   ❌ TypeError : Type non supporté pour '{valeur}'")
        return None


# Tests de conversion
print("🎭 Tests de conversion avec except multiples :")
valeurs_test = ["123", "45.67", "hello", 42, [1, 2, 3], None]
for val in valeurs_test:
    conversion_robuste(val)

print("\n🎪 EXCEPT AVEC TUPLE")
print("-" * 21)


def acces_donnees(dictionnaire, cle, index=None):
    """Accès aux données avec gestion d'erreurs groupées"""
    try:
        valeur = dictionnaire[cle]
        if index is not None:
            valeur = valeur[index]
        print(f"   ✅ Succès : {cle}[{index}] = {valeur}")
        return valeur

    except (KeyError, IndexError, TypeError) as e:
        type_erreur = type(e).__name__
        print(f"   ❌ {type_erreur} : Erreur d'accès aux données")
        return None


# Tests d'accès
print("🎪 Tests d'accès avec except groupés :")
donnees_test = {"liste": [1, 2, 3], "nom": "Alice", "vide": []}

acces_donnees(donnees_test, "liste", 1)    # Succès
acces_donnees(donnees_test, "inexistant")  # KeyError
acces_donnees(donnees_test, "liste", 10)   # IndexError
# TypeError (str pas subscriptable comme ça)
acces_donnees(donnees_test, "nom", 0)

print("\n🎯 CAPTURE DE L'EXCEPTION")
print("-" * 26)


def analyser_erreur(operation, a, b):
    """Analyse détaillée des erreurs"""
    try:
        if operation == "div":
            resultat = a / b
        elif operation == "index":
            resultat = a[b]  # a doit être une séquence
        elif operation == "attr":
            resultat = getattr(a, b)
        else:
            raise ValueError(f"Opération '{operation}' non supportée")

        print(f"   ✅ {operation}({a}, {b}) = {resultat}")
        return resultat

    except Exception as e:
        print(f"   ❌ {type(e).__name__} : {e}")
        print(f"      Arguments de l'exception : {e.args}")
        return None


print("🎯 Tests avec capture d'exception :")
analyser_erreur("div", 10, 2)
analyser_erreur("div", 10, 0)
analyser_erreur("index", [1, 2, 3], 1)
analyser_erreur("index", [1, 2, 3], 5)
analyser_erreur("attr", "hello", "upper")
analyser_erreur("attr", "hello", "inexistant")
analyser_erreur("inconnu", 1, 2)

print("\n" + "=" * 50)
print("3. ELSE ET FINALLY")
print("=" * 50)

print("\n✅ CLAUSE ELSE")
print("-" * 14)


def traitement_avec_else(fichier_nom):
    """Démonstration de la clause else"""
    try:
        # Simulation d'ouverture de fichier
        if fichier_nom == "inexistant.txt":
            raise FileNotFoundError(f"Fichier '{fichier_nom}' non trouvé")

        print(f"   📂 Ouverture réussie de '{fichier_nom}'")

    except FileNotFoundError as e:
        print(f"   ❌ Erreur : {e}")
        return False

    else:
        # Cette partie s'exécute SEULEMENT si aucune exception
        print(f"   ✅ Traitement du fichier '{fichier_nom}' en cours...")
        print(f"   📊 Analyse terminée avec succès")
        return True

    finally:
        # Cette partie s'exécute TOUJOURS
        print(f"   🧹 Nettoyage des ressources pour '{fichier_nom}'")


print("✅ Tests avec clause else :")
traitement_avec_else("document.txt")  # Succès
print()
traitement_avec_else("inexistant.txt")  # Échec

print("\n🔒 CLAUSE FINALLY")
print("-" * 17)


def connexion_base_donnees(host, utilisateur):
    """Simulation de connexion avec finally pour cleanup"""
    connexion = None

    try:
        # Simulation de connexion
        if host == "serveur_inexistant":
            raise ConnectionError(f"Impossible de se connecter à {host}")

        print(f"   🔗 Connexion établie à {host} pour {utilisateur}")
        connexion = f"connexion_vers_{host}"

        # Simulation de travail
        if utilisateur == "utilisateur_invalide":
            raise PermissionError(f"Accès refusé pour {utilisateur}")

        print(f"   ✅ Travail effectué pour {utilisateur}")
        return "Succès"

    except ConnectionError as e:
        print(f"   ❌ Erreur de connexion : {e}")
        return "Erreur connexion"

    except PermissionError as e:
        print(f"   ❌ Erreur de permission : {e}")
        return "Erreur permission"

    finally:
        # Nettoyage OBLIGATOIRE
        if connexion:
            print(f"   🔌 Fermeture de la connexion : {connexion}")
        else:
            print(f"   🧹 Nettoyage : aucune connexion à fermer")


print("🔒 Tests avec clause finally :")
print("Test 1 - Succès complet :")
connexion_base_donnees("serveur_principal", "admin")

print("\nTest 2 - Erreur de connexion :")
connexion_base_donnees("serveur_inexistant", "admin")

print("\nTest 3 - Erreur de permission :")
connexion_base_donnees("serveur_principal", "utilisateur_invalide")

print("\n🔄 ORDRE D'EXÉCUTION COMPLET")
print("-" * 29)


def demonstration_ordre_execution(scenario):
    """Démonstration complète de l'ordre try/except/else/finally"""
    print(f"   📋 Scénario : {scenario}")

    try:
        print("   1️⃣ Bloc TRY : Début")

        if scenario == "succes":
            print("   ✅ TRY : Opération réussie")
        elif scenario == "erreur_geree":
            print("   ⚠️ TRY : Problème détecté")
            raise ValueError("Erreur simulée gérée")
        elif scenario == "erreur_non_geree":
            print("   💥 TRY : Problème critique")
            raise RuntimeError("Erreur non gérée")

        print("   1️⃣ Bloc TRY : Fin")

    except ValueError as e:
        print(f"   2️⃣ Bloc EXCEPT ValueError : {e}")

    else:
        print("   3️⃣ Bloc ELSE : Exécuté car aucune exception")

    finally:
        print("   4️⃣ Bloc FINALLY : Toujours exécuté")

    print("   ✅ Fonction terminée\n")


print("🔄 Démonstrations d'ordre d'exécution :")
demonstration_ordre_execution("succes")
demonstration_ordre_execution("erreur_geree")

try:
    demonstration_ordre_execution("erreur_non_geree")
except RuntimeError as e:
    print(f"   ❌ Erreur non gérée capturée à l'extérieur : {e}\n")

print("\n" + "=" * 50)
print("4. LEVER DES EXCEPTIONS (RAISE)")
print("=" * 50)

print("\n🚀 RAISE - LEVER UNE EXCEPTION")
print("-" * 28)


def valider_age(age):
    """Validation d'âge avec exceptions personnalisées"""
    print(f"   🔍 Validation de l'âge : {age}")

    # Validation du type
    if not isinstance(age, int):
        raise TypeError(
            f"L'âge doit être un entier, reçu : {type(age).__name__}")

    # Validation de la plage
    if age < 0:
        raise ValueError(f"L'âge ne peut pas être négatif : {age}")

    if age > 150:
        raise ValueError(f"L'âge semble irréaliste : {age}")

    print(f"   ✅ Âge valide : {age}")
    return age


print("🚀 Tests de validation avec raise :")
ages_test = [25, -5, 200, "vingt", 150]

for age in ages_test:
    try:
        valider_age(age)
    except (TypeError, ValueError) as e:
        print(f"   ❌ {type(e).__name__} : {e}")

print("\n🔄 RE-RAISE D'EXCEPTIONS")
print("-" * 25)


def traitement_donnees_complexe(donnees):
    """Traitement avec re-raise pour ajout de contexte"""
    try:
        print(f"   📊 Traitement de {len(donnees)} éléments")

        # Simulation de traitement qui peut échouer
        for i, item in enumerate(donnees):
            if item == "ERREUR":
                raise RuntimeError(f"Élément invalide à l'index {i}")

            # Traitement normal
            processed = str(item).upper()

        print(f"   ✅ Traitement terminé avec succès")
        return True

    except Exception as e:
        print(f"   ⚠️ Erreur lors du traitement des données")
        print(f"   📍 Contexte : {len(donnees)} éléments en cours")
        # Re-raise avec le contexte original
        raise  # Re-lance la même exception


def gestionnaire_principal(donnees):
    """Gestionnaire principal avec gestion d'erreurs"""
    try:
        traitement_donnees_complexe(donnees)
        print("   🎉 Succès complet du traitement\n")

    except Exception as e:
        print(f"   ❌ Échec du traitement principal : {e}")
        print(f"   🔧 Action : Notification aux administrateurs\n")


print("🔄 Tests de re-raise :")
gestionnaire_principal(["a", "b", "c"])  # Succès
gestionnaire_principal(["a", "ERREUR", "c"])  # Échec

print("\n🎯 RAISE FROM - CHAÎNAGE D'EXCEPTIONS")
print("-" * 37)


def convertir_avec_contexte(valeur):
    """Conversion avec chaînage d'exceptions"""
    try:
        return int(valeur)
    except ValueError as e:
        # Chaîner l'exception originale avec une nouvelle
        raise ValueError(
            f"Impossible de convertir '{valeur}' en entier") from e


def traitement_avec_chainement(valeurs):
    """Traitement avec chaînage d'exceptions pour debugging"""
    try:
        resultats = []
        for valeur in valeurs:
            resultat = convertir_avec_contexte(valeur)
            resultats.append(resultat)
        return resultats

    except ValueError as e:
        print(f"   ❌ Erreur de conversion : {e}")
        print(f"   🔗 Cause originale : {e.__cause__}")
        return None


print("🎯 Tests de chaînage d'exceptions :")
traitement_avec_chainement(["123", "45", "hello"])

print("\n" + "=" * 50)
print("5. EXCEPTIONS PERSONNALISÉES")
print("=" * 50)

print("\n🎨 CRÉATION D'EXCEPTIONS PERSONNALISÉES")
print("-" * 38)

# Exceptions métier personnalisées


class ErreurMetier(Exception):
    """Exception de base pour les erreurs métier"""
    pass


class ErreurValidation(ErreurMetier):
    """Erreur de validation des données"""

    def __init__(self, champ, valeur, message="Validation échouée"):
        self.champ = champ
        self.valeur = valeur
        self.message = message
        super().__init__(f"{message} : {champ}='{valeur}'")


class ErreurAutorisation(ErreurMetier):
    """Erreur d'autorisation"""

    def __init__(self, utilisateur, action, ressource):
        self.utilisateur = utilisateur
        self.action = action
        self.ressource = ressource
        message = f"Utilisateur '{utilisateur}' non autorisé pour '{action}' sur '{ressource}'"
        super().__init__(message)


class ErreurRessource(ErreurMetier):
    """Erreur de ressource non disponible"""

    def __init__(self, ressource, raison="Ressource non disponible"):
        self.ressource = ressource
        self.raison = raison
        super().__init__(f"{raison} : {ressource}")


print("🎨 Définition d'exceptions personnalisées terminée")

print("\n🏗️ UTILISATION D'EXCEPTIONS PERSONNALISÉES")
print("-" * 41)


class GestionnaireUtilisateurs:
    """Gestionnaire d'utilisateurs avec exceptions personnalisées"""

    def __init__(self):
        self.utilisateurs = {
            "admin": {"role": "administrateur", "actif": True},
            "user1": {"role": "utilisateur", "actif": True},
            "user2": {"role": "utilisateur", "actif": False}
        }

    def valider_utilisateur(self, nom_utilisateur):
        """Validation avec exception personnalisée"""
        if not nom_utilisateur:
            raise ErreurValidation(
                "nom_utilisateur", nom_utilisateur, "Nom utilisateur requis")

        if not isinstance(nom_utilisateur, str):
            raise ErreurValidation(
                "nom_utilisateur", nom_utilisateur, "Nom utilisateur doit être une chaîne")

        if len(nom_utilisateur) < 3:
            raise ErreurValidation(
                "nom_utilisateur", nom_utilisateur, "Nom utilisateur trop court")

    def verifier_autorisation(self, utilisateur, action, ressource):
        """Vérification d'autorisation"""
        if utilisateur not in self.utilisateurs:
            raise ErreurRessource(
                f"utilisateur:{utilisateur}", "Utilisateur inexistant")

        user_info = self.utilisateurs[utilisateur]

        if not user_info["actif"]:
            raise ErreurAutorisation(utilisateur, action, ressource)

        if action == "supprimer" and user_info["role"] != "administrateur":
            raise ErreurAutorisation(utilisateur, action, ressource)

    def executer_action(self, utilisateur, action, ressource):
        """Exécution d'action avec gestion d'erreurs complète"""
        try:
            print(
                f"   🎯 Tentative : {utilisateur} -> {action} sur {ressource}")

            # Validation
            self.valider_utilisateur(utilisateur)

            # Autorisation
            self.verifier_autorisation(utilisateur, action, ressource)

            # Exécution (simulation)
            print(f"   ✅ Succès : {action} sur {ressource} par {utilisateur}")
            return True

        except ErreurValidation as e:
            print(f"   ❌ Validation : {e}")
            print(f"      Champ : {e.champ}, Valeur : {e.valeur}")
            return False

        except ErreurAutorisation as e:
            print(f"   ❌ Autorisation : {e}")
            print(f"      Utilisateur : {e.utilisateur}, Action : {e.action}")
            return False

        except ErreurRessource as e:
            print(f"   ❌ Ressource : {e}")
            print(f"      Ressource : {e.ressource}, Raison : {e.raison}")
            return False


# Tests du gestionnaire
print("🏗️ Tests avec exceptions personnalisées :")
gestionnaire = GestionnaireUtilisateurs()

# Scénarios de test
scenarios = [
    ("admin", "supprimer", "fichier_important"),  # Succès
    ("user1", "lire", "document"),               # Succès
    ("user1", "supprimer", "fichier"),           # Erreur autorisation
    ("user2", "lire", "document"),               # Erreur utilisateur inactif
    # Erreur utilisateur inexistant
    ("inexistant", "lire", "document"),
    ("", "lire", "document"),                    # Erreur validation
    # Erreur validation (trop court)
    ("xy", "lire", "document"),
]

for utilisateur, action, ressource in scenarios:
    gestionnaire.executer_action(utilisateur, action, ressource)
    print()

print("\n" + "=" * 50)
print("6. ASSERTIONS ET DEBUGGING")
print("=" * 50)

print("\n🔍 ASSERTIONS POUR LE DEBUGGING")
print("-" * 31)


def calculer_moyenne(notes):
    """Calcul de moyenne avec assertions pour le debugging"""

    # Assertions pour valider les préconditions
    assert isinstance(
        notes, list), f"Les notes doivent être une liste, reçu : {type(notes)}"
    assert len(notes) > 0, "La liste de notes ne peut pas être vide"
    assert all(isinstance(note, (int, float))
               for note in notes), "Toutes les notes doivent être numériques"
    assert all(
        0 <= note <= 20 for note in notes), "Les notes doivent être entre 0 et 20"

    # Calcul
    moyenne = sum(notes) / len(notes)

    # Assertion pour valider la postcondition
    assert 0 <= moyenne <= 20, f"Moyenne invalide calculée : {moyenne}"

    print(f"   ✅ Moyenne calculée : {moyenne:.2f} pour {notes}")
    return moyenne


print("🔍 Tests avec assertions :")

# Tests valides
try:
    calculer_moyenne([15, 18, 12, 16])
    calculer_moyenne([20, 19, 18])
except AssertionError as e:
    print(f"   ❌ Assertion échouée : {e}")

# Tests invalides
tests_invalides = [
    ([], "Liste vide"),
    ([15, "18", 12], "Note non numérique"),
    ([15, 25, 12], "Note hors limites"),
    ("notes", "Mauvais type")
]

print("\n   Tests d'assertions avec données invalides :")
for donnees, description in tests_invalides:
    try:
        calculer_moyenne(donnees)
    except AssertionError as e:
        print(f"   ❌ {description} : {e}")
    except Exception as e:
        print(f"   ❌ Autre erreur ({description}) : {e}")

print("\n🐛 DEBUGGING AVEC TRACEBACK")
print("-" * 29)


def fonction_niveau_3():
    """Fonction qui génère une erreur"""
    x = 10
    y = 0
    return x / y  # Division par zéro


def fonction_niveau_2():
    """Fonction intermédiaire"""
    data = [1, 2, 3]
    result = fonction_niveau_3()
    return data + [result]


def fonction_niveau_1():
    """Fonction de niveau supérieur"""
    try:
        return fonction_niveau_2()
    except Exception as e:
        print("   🐛 Erreur capturée dans fonction_niveau_1")
        print(f"   ❌ Type : {type(e).__name__}")
        print(f"   📝 Message : {e}")

        # Affichage de la stack trace
        print("   📊 Stack trace complète :")
        traceback.print_exc()

        # Récupération de la stack trace comme string
        stack_trace = traceback.format_exc()
        print(f"   📋 Stack trace formatée :\n{stack_trace}")

        return None


print("🐛 Test de debugging avec traceback :")
fonction_niveau_1()

print("\n📊 INFORMATIONS D'EXCEPTION DÉTAILLÉES")
print("-" * 39)


def analyser_exception_detaillee():
    """Analyse détaillée d'une exception"""
    try:
        # Simulation d'une erreur complexe
        donnees = {"utilisateurs": [{"nom": "Alice"}, {"nom": "Bob"}]}
        # Double erreur !
        utilisateur_inexistant = donnees["utilisateurs"][5]["nom"]

    except Exception as e:
        print("   📊 Analyse détaillée de l'exception :")
        print(f"      Type : {type(e).__name__}")
        print(f"      Message : {e}")
        print(f"      Arguments : {e.args}")

        # Informations sur l'exception
        exc_type, exc_value, exc_traceback = traceback.sys.exc_info()
        print(f"      Type système : {exc_type}")
        print(f"      Valeur : {exc_value}")

        # Dernière frame de la stack trace
        if exc_traceback:
            frame = exc_traceback.tb_frame
            print(f"      Fichier : {frame.f_code.co_filename}")
            print(f"      Fonction : {frame.f_code.co_name}")
            print(f"      Ligne : {exc_traceback.tb_lineno}")

            # Variables locales au moment de l'erreur
            print(f"      Variables locales : {list(frame.f_locals.keys())}")


analyser_exception_detaillee()

print("\n" + "=" * 50)
print("7. PATTERNS AVANCÉS")
print("=" * 50)

print("\n🔄 RETRY PATTERN")
print("-" * 15)


def operation_instable():
    """Simulation d'opération qui peut échouer"""
    if random.random() < 0.3:  # 30% de chance de succès
        return "Opération réussie"
    else:
        raise ConnectionError("Connexion temporairement indisponible")


def retry_pattern(operation, max_tentatives=3, delai=1):
    """Pattern de retry avec backoff"""
    for tentative in range(1, max_tentatives + 1):
        try:
            print(f"   🎯 Tentative {tentative}/{max_tentatives}")
            resultat = operation()
            print(f"   ✅ Succès à la tentative {tentative}")
            return resultat

        except Exception as e:
            print(f"   ❌ Échec tentative {tentative} : {e}")

            if tentative == max_tentatives:
                print(
                    f"   💥 Échec définitif après {max_tentatives} tentatives")
                raise  # Re-raise la dernière exception

            # Attendre avant la prochaine tentative (backoff)
            temps_attente = delai * tentative
            print(f"   ⏳ Attente de {temps_attente}s avant nouvelle tentative")
            time.sleep(temps_attente / 100)  # Divisé par 100 pour la démo


print("🔄 Test du pattern retry :")
try:
    resultat = retry_pattern(operation_instable, max_tentatives=5, delai=0.1)
    print(f"   🎉 Résultat final : {resultat}")
except Exception as e:
    print(f"   💀 Échec définitif : {e}")

print("\n🏭 FACTORY PATTERN AVEC EXCEPTIONS")
print("-" * 34)


class ProcesseurBase:
    """Classe de base pour les processeurs"""

    def traiter(self, donnees):
        raise NotImplementedError("Méthode traiter() doit être implémentée")


class ProcesseurTexte(ProcesseurBase):
    def traiter(self, donnees):
        if not isinstance(donnees, str):
            raise TypeError("ProcesseurTexte nécessite des données texte")
        return donnees.upper()


class ProcesseurNombre(ProcesseurBase):
    def traiter(self, donnees):
        if not isinstance(donnees, (int, float)):
            raise TypeError(
                "ProcesseurNombre nécessite des données numériques")
        return donnees ** 2


class ProcesseurListe(ProcesseurBase):
    def traiter(self, donnees):
        if not isinstance(donnees, list):
            raise TypeError("ProcesseurListe nécessite une liste")
        return sorted(donnees)


class ErreurProcesseur(Exception):
    """Exception pour les erreurs de processeur"""
    pass


class FactoryProcesseur:
    """Factory pour créer des processeurs avec gestion d'erreurs"""

    processeurs = {
        "texte": ProcesseurTexte,
        "nombre": ProcesseurNombre,
        "liste": ProcesseurListe
    }

    @classmethod
    def creer_processeur(cls, type_processeur):
        """Crée un processeur avec gestion d'erreurs"""
        if type_processeur not in cls.processeurs:
            raise ErreurProcesseur(
                f"Type de processeur inconnu : '{type_processeur}'. "
                f"Types disponibles : {list(cls.processeurs.keys())}"
            )

        try:
            return cls.processeurs[type_processeur]()
        except Exception as e:
            raise ErreurProcesseur(
                f"Erreur lors de la création du processeur : {e}") from e

    @classmethod
    def traiter_donnee(cls, type_processeur, donnees):
        """Traite une donnée avec le bon processeur"""
        try:
            processeur = cls.creer_processeur(type_processeur)
            resultat = processeur.traiter(donnees)
            print(f"   ✅ {type_processeur} : '{donnees}' -> '{resultat}'")
            return resultat

        except (ErreurProcesseur, TypeError) as e:
            print(f"   ❌ Erreur de traitement : {e}")
            return None


print("🏭 Tests du factory pattern :")
tests_factory = [
    ("texte", "hello world"),
    ("nombre", 5),
    ("liste", [3, 1, 4, 1, 5]),
    ("inconnu", "test"),
    ("nombre", "pas_un_nombre"),
    ("texte", 123)
]

for type_proc, donnee in tests_factory:
    FactoryProcesseur.traiter_donnee(type_proc, donnee)

print("\n🛡️ PATTERN CIRCUIT BREAKER")
print("-" * 28)


class CircuitBreaker:
    """Circuit breaker pour éviter les cascades de pannes"""

    def __init__(self, seuil_echecs=3, timeout_reset=5):
        self.seuil_echecs = seuil_echecs
        self.timeout_reset = timeout_reset
        self.compteur_echecs = 0
        self.etat = "FERME"  # FERME, OUVERT, SEMI_OUVERT
        self.dernier_echec = None

    def appeler(self, operation, *args, **kwargs):
        """Appelle une opération avec protection circuit breaker"""

        # Vérifier si on peut tenter de fermer le circuit
        if self.etat == "OUVERT":
            temps_ecoule = time.time() - self.dernier_echec
            if temps_ecoule >= self.timeout_reset:
                self.etat = "SEMI_OUVERT"
                print(f"   🔄 Circuit SEMI-OUVERT : tentative de rétablissement")
            else:
                raise RuntimeError(
                    f"Circuit OUVERT : attendre {self.timeout_reset - temps_ecoule:.1f}s")

        try:
            print(f"   🎯 Appel via circuit breaker (état: {self.etat})")
            resultat = operation(*args, **kwargs)

            # Succès : réinitialiser le compteur
            if self.etat == "SEMI_OUVERT":
                self.etat = "FERME"
                print(f"   ✅ Circuit FERMÉ : service rétabli")

            self.compteur_echecs = 0
            return resultat

        except Exception as e:
            self.compteur_echecs += 1
            self.dernier_echec = time.time()

            print(
                f"   ❌ Échec {self.compteur_echecs}/{self.seuil_echecs} : {e}")

            # Ouvrir le circuit si seuil atteint
            if self.compteur_echecs >= self.seuil_echecs:
                self.etat = "OUVERT"
                print(f"   🚨 Circuit OUVERT : service protégé")

            raise


def service_instable(taux_succes=0.5):
    """Service qui échoue parfois"""
    if random.random() < taux_succes:
        return "Service OK"
    else:
        raise RuntimeError("Service temporairement indisponible")


print("🛡️ Test du circuit breaker :")
cb = CircuitBreaker(seuil_echecs=2, timeout_reset=2)

# Simulation de plusieurs appels
for i in range(8):
    try:
        resultat = cb.appeler(
            service_instable, taux_succes=0.2)  # 20% de succès
        print(f"   ✅ Appel {i+1} : {resultat}")
    except Exception as e:
        print(f"   ❌ Appel {i+1} bloqué : {e}")

    time.sleep(0.1)  # Petite pause

print("\n" + "=" * 50)
print("8. BONNES PRATIQUES")
print("=" * 50)

print("\n✅ RÈGLES D'OR DE LA GESTION D'ERREURS")
print("-" * 40)

print("""
🎯 PRINCIPES FONDAMENTAUX :

1. 🎯 SPÉCIFICITÉ :
   ✅ Capturer des exceptions spécifiques (ValueError, TypeError)
   ❌ Éviter except Exception: trop général
   ❌ JAMAIS except: sans type (capture tout, même Ctrl+C)

2. 🔍 INFORMATION :
   ✅ Messages d'erreur informatifs avec contexte
   ✅ Logger les erreurs pour le debugging
   ✅ Inclure les données qui ont causé l'erreur

3. 🚀 FAIL FAST :
   ✅ Échouer rapidement et clairement
   ✅ Valider les entrées en début de fonction
   ✅ Utiliser des assertions pour les invariants

4. 🧹 CLEANUP :
   ✅ Utiliser finally pour le nettoyage obligatoire
   ✅ Context managers (with) pour les ressources
   ✅ Libérer les ressources même en cas d'erreur

5. 📊 MONITORING :
   ✅ Logger les exceptions pour l'analyse
   ✅ Métriques sur les erreurs
   ✅ Alertes sur les erreurs critiques
""")

print("\n❌ ANTI-PATTERNS À ÉVITER")
print("-" * 26)

print("❌ Exemples de mauvaises pratiques :")

# Anti-pattern 1 : Exception trop générale
print("\n   1. Exception trop générale :")
print("   ❌ Mauvais :")
print("   try:")
print("       # code complexe")
print("   except Exception:")
print("       pass  # Silence toutes les erreurs !")

print("\n   ✅ Bon :")
print("   try:")
print("       resultat = int(valeur)")
print("   except ValueError as e:")
print("       logger.error(f'Conversion échouée pour {valeur}: {e}')")
print("       return None")

# Anti-pattern 2 : Ignorer les erreurs
print("\n   2. Ignorer les erreurs :")
print("   ❌ Mauvais :")
print("   try:")
print("       operation_importante()")
print("   except:")
print("       pass  # Ignore tout !")

print("\n   ✅ Bon :")
print("   try:")
print("       operation_importante()")
print("   except SpecificError as e:")
print("       logger.warning(f'Opération échouée: {e}')")
print("       return valeur_par_defaut")

print("\n📝 LOGGING ET EXCEPTIONS")
print("-" * 25)


# Configuration du logging pour la démo
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def fonction_avec_logging(data):
    """Exemple de fonction avec logging approprié"""
    logger.info(f"Début du traitement de {len(data)} éléments")

    try:
        # Validation
        if not isinstance(data, list):
            raise TypeError(f"Liste attendue, reçu {type(data).__name__}")

        if not data:
            logger.warning("Liste vide reçue")
            return []

        # Traitement
        resultats = []
        for i, item in enumerate(data):
            try:
                resultat = str(item).upper()
                resultats.append(resultat)
            except Exception as e:
                logger.error(f"Erreur sur l'élément {i} ({item}): {e}")
                # Continue avec les autres éléments
                continue

        logger.info(
            f"Traitement terminé : {len(resultats)}/{len(data)} éléments traités")
        return resultats

    except Exception as e:
        logger.exception(f"Erreur critique dans fonction_avec_logging: {e}")
        raise  # Re-raise pour ne pas masquer l'erreur


print("📝 Test avec logging :")
print("   Sortie console :")
fonction_avec_logging(["hello", "world", 123, None])

print("\n🎯 VALIDATION ROBUSTE")
print("-" * 21)


def valider_donnees_robuste(donnees, schema):
    """Validation robuste avec messages d'erreur détaillés"""
    erreurs = []

    try:
        # Validation du type global
        if not isinstance(donnees, dict):
            raise TypeError(
                f"Dictionnaire attendu, reçu {type(donnees).__name__}")

        # Validation de chaque champ
        for champ, regles in schema.items():
            try:
                # Champ requis ?
                if regles.get("requis", False) and champ not in donnees:
                    erreurs.append(f"Champ requis manquant : {champ}")
                    continue

                # Si champ présent, valider
                if champ in donnees:
                    valeur = donnees[champ]

                    # Type
                    if "type" in regles:
                        if not isinstance(valeur, regles["type"]):
                            erreurs.append(
                                f"{champ} : type incorrect. "
                                f"Attendu {regles['type'].__name__}, "
                                f"reçu {type(valeur).__name__}"
                            )
                            continue

                    # Plage pour nombres
                    if isinstance(valeur, (int, float)):
                        if "min" in regles and valeur < regles["min"]:
                            erreurs.append(
                                f"{champ} : valeur trop petite ({valeur} < {regles['min']})")

                        if "max" in regles and valeur > regles["max"]:
                            erreurs.append(
                                f"{champ} : valeur trop grande ({valeur} > {regles['max']})")

                    # Longueur pour chaînes
                    if isinstance(valeur, str):
                        if "min_length" in regles and len(valeur) < regles["min_length"]:
                            erreurs.append(
                                f"{champ} : trop court ({len(valeur)} < {regles['min_length']})")

                        if "max_length" in regles and len(valeur) > regles["max_length"]:
                            erreurs.append(
                                f"{champ} : trop long ({len(valeur)} > {regles['max_length']})")

            except Exception as e:
                erreurs.append(
                    f"Erreur lors de la validation de {champ} : {e}")

        # Résultat
        if erreurs:
            raise ValueError(f"Validation échouée :\n" +
                             "\n".join(f"  • {err}" for err in erreurs))

        print(f"   ✅ Validation réussie pour {list(donnees.keys())}")
        return True

    except Exception as e:
        print(f"   ❌ {e}")
        return False


# Test de validation robuste
print("🎯 Tests de validation robuste :")

schema_utilisateur = {
    "nom": {"requis": True, "type": str, "min_length": 2, "max_length": 50},
    "age": {"requis": True, "type": int, "min": 0, "max": 150},
    "email": {"requis": False, "type": str, "min_length": 5},
    "score": {"requis": False, "type": float, "min": 0.0, "max": 100.0}
}

donnees_test_validation = [
    {"nom": "Alice", "age": 25, "email": "alice@test.com", "score": 85.5},  # Valide
    {"nom": "A", "age": 25},  # Nom trop court
    {"nom": "Bob", "age": -5},  # Âge négatif
    {"age": 30},  # Nom manquant
    {"nom": "Charlie", "age": "trente"},  # Mauvais type pour âge
]

for i, donnees in enumerate(donnees_test_validation, 1):
    print(f"\nTest {i} : {donnees}")
    valider_donnees_robuste(donnees, schema_utilisateur)

print("\n" + "=" * 50)
print("9. EXERCICES PRATIQUES")
print("=" * 50)

print("""
💪 EXERCICES À IMPLÉMENTER :

🎯 Exercice 1 : Système de validation de formulaire web
Créez un validateur complet :
• Exceptions personnalisées par type de champ
• Validation en cascade avec collecte d'erreurs
• Messages d'erreur localisés
• Logging des tentatives de validation
• Métriques de réussite/échec

🔧 Exercice 2 : Client HTTP robuste
Créez un client avec gestion d'erreurs complète :
• Retry automatique avec backoff exponentiel
• Circuit breaker pour éviter les surcharges
• Timeout configurables
• Exceptions spécifiques par code d'erreur HTTP
• Cache des réponses avec invalidation

🏗️ Exercice 3 : Système de traitement de fichiers
Créez un processeur de fichiers :
• Gestion d'erreurs par type de fichier
• Validation de format avec exceptions détaillées
• Nettoyage automatique en cas d'erreur
• Progress reporting avec gestion d'interruption
• Rollback des modifications partielles

🎮 Exercice 4 : Mini-ORM avec exceptions métier
Créez un ORM simplifié :
• Exceptions spécifiques (NotFound, ValidationError, etc.)
• Transaction rollback automatique
• Contraintes de validation avec messages clairs
• Connection pooling avec gestion d'erreurs
• Migrations avec rollback en cas d'échec

🔍 Exercice 5 : Système de monitoring et alertes
Créez un système de monitoring :
• Collecte d'exceptions avec stack traces
• Agrégation par type d'erreur et fréquence
• Alertes configurables par seuil
• Dashboard temps réel des erreurs
• Export des métriques pour analyse
""")

print("\n" + "=" * 50)
print("10. RÉSUMÉ FINAL")
print("=" * 50)

print("""
🎯 POINTS CLÉS À RETENIR :

1. 🚨 TYPES D'EXCEPTIONS :
   • Built-in : ValueError, TypeError, etc.
   • Personnalisées : héritent d'Exception
   • Hiérarchie : spécifique vers général
   • Toujours hériter d'Exception, pas BaseException

2. 🎭 SYNTAXE TRY/EXCEPT :
   • try : code qui peut échouer
   • except : gestion spécifique par type
   • else : exécuté si aucune exception
   • finally : toujours exécuté (cleanup)

3. 🚀 RAISE ET RE-RAISE :
   • raise Exception("message") : lever une exception
   • raise : re-lever l'exception actuelle
   • raise ... from e : chaîner les exceptions
   • Contexte préservé pour debugging

4. 🎨 EXCEPTIONS PERSONNALISÉES :
   • Classes héritant d'Exception
   • Attributs personnalisés pour contexte
   • Messages informatifs
   • Hiérarchie logique métier

5. 🔍 DEBUGGING ET ASSERTIONS :
   • assert pour les invariants (dev/test)
   • traceback pour l'analyse d'erreurs
   • Logging structuré des exceptions
   • Informations de contexte détaillées

💡 BONNES PRATIQUES :
✅ Exceptions spécifiques (pas Exception générale)
✅ Messages d'erreur informatifs avec contexte
✅ Cleanup avec finally ou context managers
✅ Fail fast : validation précoce
✅ Logging approprié des erreurs
✅ Tests des cas d'erreur

🚨 ERREURS COURANTES :
❌ except: sans type spécifique
❌ Ignorer les exceptions (pass)
❌ Messages d'erreur non informatifs
❌ Oublier le cleanup des ressources
❌ Re-raise sans contexte
❌ Exceptions trop générales

⚡ PATTERNS AVANCÉS :
• Retry avec backoff exponentiel
• Circuit breaker pour la résilience
• Factory pattern avec exceptions
• Validation en cascade
• Exception chaining pour le contexte
• Logging structuré

🎯 ARCHITECTURE ROBUSTE :
• Séparation erreurs techniques/métier
• Gestion centralisée des erreurs
• Monitoring et alertes
• Documentation des exceptions
• Tests d'erreurs systématiques
• Graceful degradation

🔧 OUTILS DE DEBUGGING :
• traceback pour stack traces
• logging pour traçabilité
• assertions pour invariants
• pdb pour debugging interactif
• Exception chaining pour contexte

🎉 Félicitations ! Gestion d'exceptions maîtrisée !
💡 Prochaine étape : Manipulation de fichiers !
📚 Exceptions gérées, manipulez les fichiers !
""")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE - GESTION D'EXCEPTIONS MAÎTRISÉE !")
print("=" * 70)
