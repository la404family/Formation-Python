#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
======================================================================
EXCEPTIONS EN PYTHON - GUIDE COMPLET
======================================================================

🎯 Ce fichier couvre la gestion des exceptions de base :
   • try, except, else, finally
   • Types d'exceptions courantes
   • Syntaxe et bonnes pratiques
   • Gestion d'erreurs multiples
   • Debugging avec les exceptions

📚 Concepts abordés :
   • Structure try/except/else/finally
   • Hiérarchie des exceptions Python
   • Capture spécifique vs générale
   • Propagation d'exceptions
   • Messages d'erreur informatifs

💡 Objectif : Maîtriser la gestion d'erreurs de base
"""

print("=" * 70)
print("EXCEPTIONS EN PYTHON - GUIDE COMPLET")
print("=" * 70)

print("\n" + "=" * 50)
print("1. STRUCTURE TRY/EXCEPT DE BASE")
print("=" * 50)

print("\n🚨 GESTION D'ERREURS SIMPLE")
print("-" * 26)


def demo_try_except_simple():
    """Démonstration de la structure try/except de base"""

    print("🚨 Try/except simple :")

    # Exemple 1 : Division par zéro
    print("\n   1️⃣ Division par zéro :")
    try:
        resultat = 10 / 0
        print(f"   Résultat : {resultat}")
    except ZeroDivisionError:
        print("   ❌ Erreur : Division par zéro impossible !")

    # Exemple 2 : Conversion invalide
    print("\n   2️⃣ Conversion invalide :")
    try:
        nombre = int("abc")
        print(f"   Nombre converti : {nombre}")
    except ValueError:
        print("   ❌ Erreur : Impossible de convertir 'abc' en entier !")

    # Exemple 3 : Accès à un index inexistant
    print("\n   3️⃣ Index hors limites :")
    liste = [1, 2, 3]
    try:
        element = liste[10]
        print(f"   Élément à l'index 10 : {element}")
    except IndexError:
        print("   ❌ Erreur : Index 10 hors limites !")

    # Exemple 4 : Accès à une clé inexistante
    print("\n   4️⃣ Clé de dictionnaire inexistante :")
    dictionnaire = {"nom": "Alice", "age": 25}
    try:
        ville = dictionnaire["ville"]
        print(f"   Ville : {ville}")
    except KeyError:
        print("   ❌ Erreur : Clé 'ville' inexistante !")


demo_try_except_simple()

print("\n🔧 GESTION D'EXCEPTIONS MULTIPLES")
print("-" * 32)


def demo_exceptions_multiples():
    """Démonstration de la gestion d'exceptions multiples"""

    print("🔧 Exceptions multiples :")

    def calculer_moyenne(valeurs_str):
        """Calculer la moyenne d'une liste de chaînes numériques"""
        try:
            # Conversion des chaînes en nombres
            valeurs = [float(v) for v in valeurs_str]

            # Calcul de la moyenne
            moyenne = sum(valeurs) / len(valeurs)

            return moyenne

        except ValueError as e:
            print(f"   ❌ Erreur de conversion : {e}")
            return None
        except ZeroDivisionError:
            print("   ❌ Erreur : Liste vide, impossible de calculer la moyenne")
            return None
        except TypeError as e:
            print(f"   ❌ Erreur de type : {e}")
            return None

    # Tests avec différents types d'erreurs
    test_cases = [
        (["10", "20", "30"], "Valeurs valides"),
        (["10", "abc", "30"], "Valeur invalide"),
        ([], "Liste vide"),
        (None, "Type incorrect"),
        (["10.5", "20.7", "15.2"], "Nombres décimaux"),
    ]

    for valeurs, description in test_cases:
        print(f"\n   Test : {description}")
        print(f"   Données : {valeurs}")

        resultat = calculer_moyenne(valeurs)
        if resultat is not None:
            print(f"   ✅ Moyenne : {resultat:.2f}")
        else:
            print("   💀 Calcul impossible")


demo_exceptions_multiples()

print("\n" + "=" * 50)
print("2. STRUCTURE COMPLÈTE TRY/EXCEPT/ELSE/FINALLY")
print("=" * 50)

print("\n🏗️ STRUCTURE COMPLÈTE")
print("-" * 20)


def demo_structure_complete():
    """Démonstration de try/except/else/finally"""

    print("🏗️ Structure complète try/except/else/finally :")

    def traiter_fichier(nom_fichier, contenu=None):
        """Exemple de traitement de fichier avec structure complète"""
        fichier = None

        try:
            print(f"   📂 Tentative d'ouverture du fichier '{nom_fichier}'")

            if contenu is not None:
                # Mode écriture
                fichier = open(nom_fichier, 'w', encoding='utf-8')
                fichier.write(contenu)
            else:
                # Mode lecture
                fichier = open(nom_fichier, 'r', encoding='utf-8')
                contenu_lu = fichier.read()
                return contenu_lu

        except FileNotFoundError:
            print(f"   ❌ Fichier '{nom_fichier}' introuvable")
            return None
        except PermissionError:
            print(f"   ❌ Permissions insuffisantes pour '{nom_fichier}'")
            return None
        except IOError as e:
            print(f"   ❌ Erreur d'E/S : {e}")
            return None
        else:
            # Exécuté seulement si aucune exception n'a été levée
            print(f"   ✅ Opération sur '{nom_fichier}' réussie")
            return "Opération réussie"
        finally:
            # Toujours exécuté, même en cas d'exception
            if fichier:
                fichier.close()
                print(f"   🔒 Fichier '{nom_fichier}' fermé")
            else:
                print(f"   ⚠️ Aucun fichier à fermer")

    # Tests de la structure complète
    print("\n   1️⃣ Test écriture de fichier :")
    traiter_fichier("test_temp.txt", "Contenu de test")

    print("\n   2️⃣ Test lecture de fichier existant :")
    contenu = traiter_fichier("test_temp.txt")
    if contenu:
        print(f"   📖 Contenu lu : {contenu}")

    print("\n   3️⃣ Test lecture de fichier inexistant :")
    traiter_fichier("fichier_inexistant.txt")

    # Nettoyage
    import os
    if os.path.exists("test_temp.txt"):
        os.remove("test_temp.txt")
        print("   🧹 Fichier temporaire supprimé")


demo_structure_complete()

print("\n🎭 EXEMPLE PRATIQUE COMPLET")
print("-" * 26)


def demo_exemple_pratique():
    """Exemple pratique avec calculatrice robuste"""

    print("🎭 Calculatrice robuste avec gestion d'erreurs :")

    def calculatrice_robuste(expression):
        """Calculatrice qui gère les erreurs courantes"""

        print(f"\n   🧮 Calcul de : {expression}")

        try:
            # Tentative d'évaluation de l'expression
            resultat = eval(expression)

        except ZeroDivisionError:
            print("   ❌ Division par zéro détectée")
            return None
        except NameError as e:
            print(f"   ❌ Variable non définie : {e}")
            return None
        except SyntaxError as e:
            print(f"   ❌ Erreur de syntaxe : {e}")
            return None
        except TypeError as e:
            print(f"   ❌ Erreur de type : {e}")
            return None
        except Exception as e:
            # Capture générale pour les autres erreurs
            print(f"   ❌ Erreur inattendue : {type(e).__name__}: {e}")
            return None
        else:
            # Exécuté si aucune exception
            print(f"   ✅ Résultat : {resultat}")
            return resultat
        finally:
            # Toujours exécuté
            print("   📊 Calcul terminé")

    # Tests de la calculatrice
    expressions_test = [
        "2 + 3 * 4",           # Valide
        "10 / 2",              # Valide
        "10 / 0",              # Division par zéro
        "2 + abc",             # Variable non définie
        "2 +",                 # Syntaxe invalide
        "len('hello')",        # Fonction valide
        "'hello' + 5",         # Erreur de type
    ]

    for expression in expressions_test:
        calculatrice_robuste(expression)


demo_exemple_pratique()

print("\n" + "=" * 50)
print("3. TYPES D'EXCEPTIONS COURANTES")
print("=" * 50)

print("\n📚 HIÉRARCHIE DES EXCEPTIONS")
print("-" * 28)


def demo_types_exceptions():
    """Démonstration des types d'exceptions courantes"""

    print("📚 Types d'exceptions Python :")

    exceptions_exemples = [
        # (Type d'exception, Code qui lève l'exception, Description)
        (ValueError, "int('abc')", "Valeur inappropriée pour le type"),
        (TypeError, "'hello' + 5", "Types incompatibles"),
        (IndexError, "[1,2,3][10]", "Index hors limites"),
        (KeyError, "{'a': 1}['b']", "Clé inexistante dans dictionnaire"),
        (AttributeError, "'hello'.non_existant", "Attribut inexistant"),
        (ZeroDivisionError, "10 / 0", "Division par zéro"),
        (FileNotFoundError, "open('inexistant.txt')", "Fichier introuvable"),
        (ImportError, "import module_inexistant", "Module introuvable"),
        (NameError, "print(variable_inexistante)", "Variable non définie"),
        (SyntaxError, "eval('2 +')", "Erreur de syntaxe"),
    ]

    for i, (exception_type, code, description) in enumerate(exceptions_exemples, 1):
        print(f"\n   {i}️⃣ {exception_type.__name__} :")
        print(f"      Code : {code}")
        print(f"      Description : {description}")

        try:
            eval(code)
        except exception_type as e:
            print(f"      ❌ Exception capturée : {e}")
        except Exception as e:
            print(f"      ⚠️ Autre exception : {type(e).__name__}: {e}")


demo_types_exceptions()

print("\n🔍 INFORMATIONS SUR LES EXCEPTIONS")
print("-" * 33)


def demo_infos_exceptions():
    """Démonstration des informations sur les exceptions"""

    print("🔍 Informations détaillées sur les exceptions :")

    def analyser_exception(code_test, description):
        """Analyser une exception en détail"""
        print(f"\n   📋 Test : {description}")
        print(f"   Code : {code_test}")

        try:
            eval(code_test)
        except Exception as e:
            print(f"   🏷️ Type : {type(e).__name__}")
            print(f"   📝 Message : {e}")
            print(f"   📍 Args : {e.args}")

            # Informations additionnelles pour certains types
            if hasattr(e, 'filename'):
                print(f"   📂 Fichier : {e.filename}")
            if hasattr(e, 'lineno'):
                print(f"   📍 Ligne : {e.lineno}")

    # Tests d'analyse d'exceptions
    tests = [
        ("10 / 0", "Division par zéro"),
        ("int('hello')", "Conversion invalide"),
        ("[1,2,3][5]", "Index invalide"),
        ("{'a': 1}['z']", "Clé invalide"),
        ("'text'.missing_method()", "Méthode inexistante"),
    ]

    for code, desc in tests:
        analyser_exception(code, desc)


demo_infos_exceptions()

print("\n" + "=" * 50)
print("4. BONNES PRATIQUES")
print("=" * 50)

print("\n✅ BONNES PRATIQUES DE GESTION D'ERREURS")
print("-" * 42)


def demo_bonnes_pratiques():
    """Démonstration des bonnes pratiques"""

    print("✅ Bonnes pratiques de gestion d'erreurs :")

    print("\n   1️⃣ Être spécifique dans les exceptions :")

    # ❌ MAUVAIS : trop général
    def mauvais_exemple():
        try:
            return int(input("Entrez un nombre : "))
        except:  # Trop général !
            print("Une erreur s'est produite")
            return None

    # ✅ BON : spécifique
    def bon_exemple():
        try:
            return int(input("Entrez un nombre : "))
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide")
            return None
        except KeyboardInterrupt:
            print("Interruption utilisateur")
            return None

    print("      ❌ Mauvais : except générique sans type")
    print("      ✅ Bon : except spécifique avec type")

    print("\n   2️⃣ Messages d'erreur informatifs :")

    def valider_age(age_str):
        """Validation d'âge avec messages informatifs"""
        try:
            age = int(age_str)
            if age < 0:
                raise ValueError(f"L'âge ne peut pas être négatif : {age}")
            if age > 150:
                raise ValueError(f"L'âge semble irréaliste : {age}")
            return age
        except ValueError as e:
            if "invalid literal" in str(e):
                print(f"   ❌ '{age_str}' n'est pas un nombre valide")
            else:
                print(f"   ❌ {e}")
            return None

    # Tests de validation
    ages_test = ["25", "-5", "200", "abc", "30.5"]
    for age_str in ages_test:
        print(f"      Test age '{age_str}' :", end=" ")
        resultat = valider_age(age_str)
        if resultat is not None:
            print(f"✅ {resultat} ans")
        else:
            print("Invalide")

    print("\n   3️⃣ Gestion en cascade :")

    def traitement_en_cascade(donnees):
        """Exemple de gestion d'erreurs en cascade"""
        try:
            # Étape 1 : Validation
            if not isinstance(donnees, list):
                raise TypeError("Les données doivent être une liste")

            # Étape 2 : Traitement
            resultats = []
            for item in donnees:
                try:
                    resultat = int(item) * 2
                    resultats.append(resultat)
                except ValueError:
                    print(
                        f"      ⚠️ Élément ignoré : '{item}' (non numérique)")
                    continue

            # Étape 3 : Vérification du résultat
            if not resultats:
                raise ValueError("Aucun élément valide trouvé")

            return resultats

        except TypeError as e:
            print(f"   ❌ Erreur de type : {e}")
            return []
        except ValueError as e:
            print(f"   ❌ Erreur de valeur : {e}")
            return []

    # Tests en cascade
    tests_cascade = [
        [1, 2, 3, 4],           # Valide
        ["1", "2", "3"],        # Chaînes valides
        ["1", "abc", "3"],      # Mélange valide/invalide
        ["abc", "def"],         # Tout invalide
        "pas une liste",        # Type incorrect
    ]

    for donnees in tests_cascade:
        print(f"      Test : {donnees}")
        resultat = traitement_en_cascade(donnees)
        print(f"      Résultat : {resultat}")


demo_bonnes_pratiques()


print("\n" + "=" * 50)
print("5. RÉSUMÉ FINAL")
print("=" * 50)

print("""
🎯 POINTS CLÉS À RETENIR :

1. 🚨 STRUCTURE DE BASE :
   • try : bloc de code à risque
   • except : gestion des erreurs spécifiques
   • else : exécuté si aucune exception
   • finally : toujours exécuté

2. 🔧 EXCEPTIONS MULTIPLES :
   • Plusieurs blocs except pour différents types
   • Ordre du plus spécifique au plus général
   • Exception comme dernière capture

3. 🏗️ STRUCTURE COMPLÈTE :
   • try/except/else/finally
   • else : pour le code de succès
   • finally : pour le nettoyage

4. 📚 TYPES COURANTS :
   • ValueError : valeur inappropriée
   • TypeError : type incorrect
   • IndexError : index hors limites
   • KeyError : clé inexistante
   • FileNotFoundError : fichier manquant

5. ✅ BONNES PRATIQUES :
   • Exceptions spécifiques, pas générales
   • Messages d'erreur informatifs
   • Gestion en cascade appropriée
   • Nettoyage dans finally

💡 RÈGLES D'OR :
✅ Capturer des exceptions spécifiques
✅ Fournir des messages d'erreur clairs
✅ Nettoyer les ressources dans finally
✅ Ne pas masquer les erreurs importantes
✅ Utiliser else pour la logique de succès

🚨 À ÉVITER :
❌ except: sans type spécifique
❌ Messages d'erreur vagues
❌ Ignorer les exceptions importantes
❌ Oublier le nettoyage des ressources
❌ Lever des exceptions dans finally

🎉 Félicitations ! Gestion d'erreurs de base maîtrisée !
💡 Prochaine étape : Lever des exceptions personnalisées !
📚 Erreurs gérées, continuez vers les exceptions avancées !
""")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE - EXCEPTIONS DE BASE MAÎTRISÉES !")
print("=" * 70)
