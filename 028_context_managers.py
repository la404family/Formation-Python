#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
======================================================================
CONTEXT MANAGERS - GUIDE COMPLET
======================================================================

🎯 Ce fichier couvre les context managers en détail :
   • Le statement 'with' et son fonctionnement
   • Gestion automatique des ressources
   • Context managers intégrés et personnalisés
   • Protocole __enter__ et __exit__

📚 Concepts abordés :
   • with statement
   • Gestion des fichiers
   • Gestion des exceptions dans les context managers
   • Context managers personnalisés

💡 Objectif : Maîtriser la gestion automatique des ressources
"""

import os
from contextlib import ExitStack
from contextlib import contextmanager
import time
import threading
print("=" * 70)
print("CONTEXT MANAGERS - GUIDE COMPLET")
print("=" * 70)

print("\n" + "=" * 50)
print("1. INTRODUCTION AUX CONTEXT MANAGERS")
print("=" * 50)

print("\n🎯 QU'EST-CE QU'UN CONTEXT MANAGER ?")
print("-" * 40)

print("""
Un context manager est un objet qui définit le contexte d'exécution
à utiliser avec le statement 'with'. Il garantit qu'une action de 
nettoyage est exécutée après le bloc de code, même en cas d'exception.

🔧 AVANTAGES :
   ✅ Gestion automatique des ressources
   ✅ Code plus propre et sûr
   ✅ Prévention des fuites de ressources
   ✅ Gestion d'erreurs intégrée
""")

print("\n" + "=" * 50)
print("2. UTILISATION BASIQUE AVEC LES FICHIERS")
print("=" * 50)

print("\n📁 GESTION DE FICHIERS AVEC 'WITH'")
print("-" * 35)

# Exemple de base avec fichiers
print("💡 Exemple 1 : Lecture de fichier")

# Créer un fichier de test
contenu_test = """Ligne 1 du fichier
Ligne 2 du fichier
Ligne 3 du fichier"""

with open("test_context.txt", "w", encoding="utf-8") as fichier:
    fichier.write(contenu_test)
    print("   ✅ Fichier créé et écrit automatiquement fermé")

# Lecture avec context manager
with open("test_context.txt", "r", encoding="utf-8") as fichier:
    contenu = fichier.read()
    print(f"   📖 Contenu lu : {repr(contenu[:30])}...")
    print("   ✅ Fichier automatiquement fermé après lecture")

print("\n💡 Comparaison sans/avec context manager :")
print("""
❌ SANS context manager (dangereux) :
fichier = open("test.txt", "r")
contenu = fichier.read()
# Oubli possible de fermer le fichier !
# fichier.close()  # Si oublié = fuite de ressource

✅ AVEC context manager (sûr) :
with open("test.txt", "r") as fichier:
    contenu = fichier.read()
# Fichier automatiquement fermé, même en cas d'exception !
""")

print("\n" + "=" * 50)
print("3. CONTEXT MANAGERS INTÉGRÉS")
print("=" * 50)

print("\n🔧 AUTRES CONTEXT MANAGERS INTÉGRÉS")
print("-" * 37)

# Exemple avec threading.Lock

verrou = threading.Lock()


def fonction_avec_verrou():
    """Fonction utilisant un verrou avec context manager"""
    with verrou:
        print("   🔒 Verrou acquis automatiquement")
        time.sleep(0.1)  # Simulation de travail
        print("   🔓 Verrou sera libéré automatiquement")


print("💡 Exemple 2 : Threading Lock")
fonction_avec_verrou()

# Exemple avec gestion d'exceptions
print("\n💡 Exemple 3 : Gestion d'exceptions avec context manager")

try:
    with open("fichier_inexistant.txt", "r") as f:
        contenu = f.read()
except FileNotFoundError:
    print("   ❌ Fichier non trouvé, mais pas de fuite de ressource !")
    print("   ✅ Context manager a géré la fermeture proprement")

print("\n" + "=" * 50)
print("4. CRÉER DES CONTEXT MANAGERS PERSONNALISÉS")
print("=" * 50)

print("\n🏗️ CONTEXT MANAGERS AVEC CLASSES")
print("-" * 33)


class MonContextManager:
    """Exemple de context manager personnalisé"""

    def __init__(self, nom):
        self.nom = nom
        print(f"   🏗️ Initialisation du context manager '{nom}'")

    def __enter__(self):
        print(f"   🚪 Entrée dans le contexte '{self.nom}'")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"   ❌ Sortie avec exception : {exc_type.__name__}")
        else:
            print(f"   ✅ Sortie normale du contexte '{self.nom}'")
        return False  # Ne supprime pas l'exception


print("💡 Exemple 4 : Context manager personnalisé")

with MonContextManager("Test") as cm:
    print("   🔧 Code exécuté dans le contexte")
    print(f"   📝 Context manager reçu : {cm.nom}")

print("\n🔧 CONTEXT MANAGER AVEC DÉCORATEUR")
print("-" * 37)


@contextmanager
def mon_context_simple(nom):
    """Context manager créé avec un décorateur"""
    print(f"   🚪 Entrée dans '{nom}'")
    try:
        yield nom.upper()  # Valeur retournée par __enter__
    finally:
        print(f"   🚪 Sortie de '{nom}'")


print("💡 Exemple 5 : Context manager avec @contextmanager")

with mon_context_simple("demo") as valeur:
    print(f"   🔧 Valeur reçue : {valeur}")
    print("   💼 Travail effectué dans le contexte")

print("\n" + "=" * 50)
print("5. GESTION DES EXCEPTIONS")
print("=" * 50)

print("\n⚠️ GESTION D'ERREURS DANS LES CONTEXT MANAGERS")
print("-" * 45)


class ContextAvecGestionErreur:
    """Context manager qui gère les exceptions"""

    def __enter__(self):
        print("   🚪 Entrée - ressources allouées")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("   🧹 Nettoyage des ressources")

        if exc_type is None:
            print("   ✅ Aucune exception")
            return False

        if exc_type == ValueError:
            print("   🔧 ValueError capturée et gérée")
            return True  # Supprime l'exception

        print(f"   ❌ Exception non gérée : {exc_type.__name__}")
        return False  # Propage l'exception


print("💡 Exemple 6 : Gestion d'exceptions personnalisée")

# Cas sans exception
with ContextAvecGestionErreur():
    print("   ✅ Code normal")

# Cas avec ValueError (gérée)
with ContextAvecGestionErreur():
    print("   ⚠️ Avant l'erreur")
    raise ValueError("Erreur de test")
    print("   ❌ Cette ligne ne s'exécutera pas")

print("   🔧 Code après le context manager - ValueError gérée")

print("\n" + "=" * 50)
print("6. CONTEXT MANAGERS MULTIPLES")
print("=" * 50)

print("\n🔄 UTILISATION DE PLUSIEURS CONTEXT MANAGERS")
print("-" * 43)

# Context managers multiples
print("💡 Exemple 7 : Context managers multiples")

with open("test_context.txt", "r", encoding="utf-8") as fichier1, \
        MonContextManager("Second") as cm2:
    print("   📖 Lecture du fichier 1")
    print("   🔧 Utilisation du context manager 2")
    print("   ✅ Les deux seront fermés automatiquement")

# Avec contextlib.ExitStack

print("\n💡 Exemple 8 : ExitStack pour gérer plusieurs contexts")

with ExitStack() as pile:
    cm1 = pile.enter_context(MonContextManager("Premier"))
    cm2 = pile.enter_context(MonContextManager("Second"))
    fichier = pile.enter_context(
        open("test_context.txt", "r", encoding="utf-8"))

    print("   🏗️ Tous les contexts sont actifs")
    print("   📖 Lecture :", fichier.readline().strip())

print("   ✅ Tous les contexts fermés automatiquement")

print("\n" + "=" * 50)
print("7. CAS D'USAGE PRATIQUES")
print("=" * 50)

print("\n💼 EXEMPLES CONCRETS D'UTILISATION")
print("-" * 33)

# Context manager pour chronométrage


@contextmanager
def chronometre(nom="Opération"):
    """Context manager pour mesurer le temps d'exécution"""
    import time
    debut = time.time()
    print(f"   ⏱️ Début de '{nom}'")
    try:
        yield
    finally:
        duree = time.time() - debut
        print(f"   ⏱️ '{nom}' terminée en {duree:.3f}s")


print("💡 Exemple 9 : Chronométrage automatique")

with chronometre("Calcul complexe"):
    # Simulation d'un calcul
    resultat = sum(i**2 for i in range(1000))
    print(f"   🔢 Résultat du calcul : {resultat}")

# Context manager pour changement de répertoire


@contextmanager
def changer_repertoire(nouveau_rep):
    """Context manager pour changer temporairement de répertoire"""
    import os
    ancien_rep = os.getcwd()
    try:
        os.chdir(nouveau_rep)
        print(f"   📁 Changement vers : {nouveau_rep}")
        yield nouveau_rep
    finally:
        os.chdir(ancien_rep)
        print(f"   📁 Retour vers : {ancien_rep}")


print("\n💡 Exemple 10 : Changement temporaire de répertoire")

try:
    with changer_repertoire(".."):
        print(f"   📍 Répertoire actuel : {os.getcwd()}")
except:
    print("   ⚠️ Impossible de changer de répertoire")

print(f"   📍 Répertoire final : {os.getcwd()}")

print("\n" + "=" * 50)
print("8. RÉSUMÉ FINAL")
print("=" * 50)

print("""
🎯 POINTS CLÉS À RETENIR :

1. 🏗️ CONTEXT MANAGERS :
   • Gestion automatique des ressources
   • Protocole __enter__ et __exit__
   • Nettoyage garanti même en cas d'exception

2. 🔧 STATEMENT 'WITH' :
   • Syntaxe propre et lisible
   • Gestion d'erreurs intégrée
   • Support de multiples context managers

3. 🎨 CRÉATION PERSONNALISÉE :
   • Classes avec __enter__ et __exit__
   • Décorateur @contextmanager
   • Gestion fine des exceptions

4. 💼 CAS D'USAGE :
   • Fichiers et ressources système
   • Verrous et synchronisation
   • Chronométrage et monitoring
   • Changements d'état temporaires

💡 FORMULE MAGIQUE :
   Acquisition → Utilisation → Libération (automatique)

🎉 Félicitations ! Vous maîtrisez maintenant les context managers !
💡 Prochaine étape : Classes et objets !
📚 Ressources gérées, passez à la POO !
""")

# Nettoyage
if os.path.exists("test_context.txt"):
    os.remove("test_context.txt")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE - CONTEXT MANAGERS MAÎTRISÉS !")
print("=" * 70)
