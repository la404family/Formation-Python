#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
======================================================================
CONTEXT MANAGERS EN PYTHON - GUIDE COMPLET
======================================================================

🎯 Ce fichier couvre les context managers en détail :
   • Protocole __enter__ et __exit__
   • Statement with et gestion automatique
   • Context managers built-in
   • Création de context managers personnalisés
   • Décorateur @contextmanager
   • Patterns avancés et cas d'usage

📚 Concepts abordés :
   • RAII (Resource Acquisition Is Initialization)
   • Gestion automatique des ressources
   • Exception handling dans les contexts
   • Context managers imbriqués
   • Async context managers
   • Best practices et optimisations

💡 Objectif : Maîtriser la gestion propre des ressources
"""

from contextlib import ExitStack
from contextlib import contextmanager
import os

print("=" * 70)
print("CONTEXT MANAGERS EN PYTHON - GUIDE COMPLET")
print("=" * 70)

print("\n" + "=" * 50)
print("1. CONCEPTS FONDAMENTAUX")
print("=" * 50)

print("\n🎯 QU'EST-CE QU'UN CONTEXT MANAGER ?")
print("-" * 37)

print("""
🎯 DÉFINITION :
Un context manager est un objet qui définit le contexte d'exécution
à utiliser avec le statement 'with'. Il garantit l'exécution de code
de nettoyage même en cas d'exception.

🔄 PROTOCOLE CONTEXT MANAGER :
Un objet context manager doit implémenter deux méthodes :
• __enter__() : setup, appelée en entrant dans le 'with'
• __exit__()  : cleanup, appelée en sortant du 'with'

⚡ PRINCIPE RAII :
Resource Acquisition Is Initialization
• Acquérir la ressource à l'entrée
• Libérer la ressource à la sortie
• Même en cas d'exception !

💡 AVANTAGES :
• Code plus sûr et lisible
• Gestion automatique des ressources
• Évite les fuites de mémoire/fichiers
• Exception safety garantie
• Pattern standardisé et pythonique
""")

print("\n🎭 SYNTAXE WITH")
print("-" * 15)

print("""
🎭 SYNTAXE DE BASE :

with context_manager as variable:
    # Code utilisant la ressource
    pass
# Nettoyage automatique ici

🔄 ÉQUIVALENT SANS WITH :
try:
    resource = context_manager.__enter__()
    variable = resource
    # Code utilisant la ressource
finally:
    context_manager.__exit__(exc_type, exc_value, traceback)

📊 INFORMATIONS D'EXCEPTION :
__exit__ reçoit trois paramètres :
• exc_type : type d'exception (None si pas d'exception)
• exc_value : instance d'exception 
• exc_traceback : objet traceback
""")

print("\n" + "=" * 50)
print("2. CONTEXT MANAGERS BUILT-IN")
print("=" * 50)

print("\n📂 FICHIERS - LE CAS CLASSIQUE")
print("-" * 31)


def demo_context_manager_fichier():
    """Démonstration avec les fichiers (context manager built-in)"""

    print("📂 Context manager avec fichiers :")

    # Créer le répertoire si nécessaire
    import os
    os.makedirs("context_demo", exist_ok=True)

    try:
        # Utilisation normale avec with
        print("   1️⃣ Utilisation normale avec 'with' :")
        with open("context_demo/test.txt", "w", encoding="utf-8") as f:
            print(f"      Fichier ouvert : {f.name}")
            print(f"      Fermé ? {f.closed}")
            f.write("Contenu de test\n")
            f.write("Deuxième ligne\n")
            print(f"      Écriture effectuée")

        print(f"      Après with - Fermé ? {f.closed}")

        # Comparaison sans with (mauvaise pratique)
        print("\n   2️⃣ Sans 'with' (mauvaise pratique) :")
        f = open("context_demo/test2.txt", "w", encoding="utf-8")
        print(f"      Fichier ouvert : {f.name}")
        print(f"      Fermé ? {f.closed}")
        f.write("Contenu sans with\n")
        # Oubli volontaire du close() !
        print(f"      Oubli de close() - Fermé ? {f.closed}")
        f.close()  # Ne pas oublier !

        # With avec exception
        print("\n   3️⃣ 'With' avec exception :")
        try:
            with open("context_demo/test3.txt", "w", encoding="utf-8") as f:
                f.write("Début d'écriture\n")
                print(f"      Avant exception - Fermé ? {f.closed}")
                raise ValueError("Erreur simulée")
                f.write("Cette ligne ne sera jamais écrite\n")
        except ValueError as e:
            print(f"      Exception capturée : {e}")
            print(f"      Après exception - Fermé ? {f.closed}")

    except Exception as e:
        print(f"   ❌ Erreur : {e}")


demo_context_manager_fichier()

print("\n🔒 THREADING.LOCK")
print("-" * 17)


def demo_context_manager_lock():
    """Démonstration avec threading.Lock"""
    import threading
    import time

    print("🔒 Context manager avec threading.Lock :")

    # Ressource partagée
    compteur = {"valeur": 0}
    verrou = threading.Lock()

    def incrementer_avec_with(nom, iterations):
        """Incrémenter avec context manager"""
        for i in range(iterations):
            with verrou:  # Acquisition automatique du verrou
                # Section critique
                valeur_actuelle = compteur["valeur"]
                time.sleep(0.001)  # Simuler du travail
                compteur["valeur"] = valeur_actuelle + 1
                print(f"      {nom} : {compteur['valeur']}")
            # Libération automatique du verrou ici

    def incrementer_sans_with(nom, iterations):
        """Incrémenter sans context manager (dangereux)"""
        for i in range(iterations):
            verrou.acquire()
            try:
                # Section critique
                valeur_actuelle = compteur["valeur"]
                time.sleep(0.001)
                compteur["valeur"] = valeur_actuelle + 1
                print(f"      {nom} : {compteur['valeur']}")
            finally:
                verrou.release()  # Ne pas oublier !

    print("   🎯 Test avec context manager :")

    # Reset du compteur
    compteur["valeur"] = 0

    # Créer des threads
    threads = []
    for i in range(2):
        thread = threading.Thread(
            target=incrementer_avec_with,
            args=(f"Thread-{i+1}", 3)
        )
        threads.append(thread)

    # Lancer et attendre
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    print(f"   ✅ Valeur finale : {compteur['valeur']}")


demo_context_manager_lock()

print("\n⏱️ AUTRES CONTEXT MANAGERS BUILT-IN")
print("-" * 35)


def demo_autres_context_managers():
    """Démonstration d'autres context managers built-in"""
    import tempfile
    import decimal
    import warnings

    print("⏱️ Autres context managers intégrés :")

    # 1. tempfile.TemporaryDirectory
    print("\n   1️⃣ tempfile.TemporaryDirectory :")
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"      Répertoire temporaire : {temp_dir}")

        # Créer un fichier dans le répertoire temporaire
        temp_file = os.path.join(temp_dir, "test.txt")
        with open(temp_file, "w") as f:
            f.write("Fichier temporaire")

        print(f"      Fichier créé : {os.path.exists(temp_file)}")

    print(f"      Après with - Répertoire existe ? {os.path.exists(temp_dir)}")

    # 2. decimal.localcontext
    print("\n   2️⃣ decimal.localcontext :")
    print(f"      Précision par défaut : {decimal.getcontext().prec}")

    with decimal.localcontext() as ctx:
        ctx.prec = 50  # Très haute précision
        print(f"      Précision dans le contexte : {ctx.prec}")

        # Calcul haute précision
        x = decimal.Decimal(1) / decimal.Decimal(3)
        print(f"      1/3 = {x}")

    print(f"      Précision après contexte : {decimal.getcontext().prec}")

    # 3. warnings.catch_warnings
    print("\n   3️⃣ warnings.catch_warnings :")

    def fonction_avec_warning():
        warnings.warn("Ceci est un avertissement", DeprecationWarning)
        return "Résultat"

    print("      Sans capture :")
    try:
        resultat = fonction_avec_warning()
        print(f"      Résultat : {resultat}")
    except:
        pass

    print("      Avec capture des warnings :")
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        resultat = fonction_avec_warning()
        print(f"      Résultat : {resultat}")
        print(f"      Warnings capturés : {len(w)}")
        if w:
            print(f"      Message : {w[0].message}")


demo_autres_context_managers()

print("\n" + "=" * 50)
print("3. CRÉER DES CONTEXT MANAGERS")
print("=" * 50)

print("\n🏗️ MÉTHODE CLASSE - PROTOCOLE COMPLET")
print("-" * 37)


class GestionnaireFichierAvecLog:
    """Context manager personnalisé pour fichiers avec logging"""

    def __init__(self, nom_fichier, mode="r", encoding="utf-8", debug=True):
        self.nom_fichier = nom_fichier
        self.mode = mode
        self.encoding = encoding
        self.debug = debug
        self.fichier = None
        self.temps_debut = None

    def __enter__(self):
        """Entrée dans le context manager"""
        if self.debug:
            import time
            self.temps_debut = time.time()
            print(
                f"   📂 Ouverture de '{self.nom_fichier}' en mode '{self.mode}'")

        try:
            self.fichier = open(self.nom_fichier, self.mode,
                                encoding=self.encoding)
            if self.debug:
                print(f"   ✅ Fichier ouvert avec succès")
            return self.fichier

        except Exception as e:
            if self.debug:
                print(f"   ❌ Erreur d'ouverture : {e}")
            raise

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """Sortie du context manager"""
        if self.fichier:
            self.fichier.close()

            if self.debug:
                import time
                duree = time.time() - self.temps_debut if self.temps_debut else 0
                print(f"   🔒 Fichier fermé (ouvert {duree:.3f}s)")

                if exc_type:
                    print(
                        f"   ⚠️ Fermeture après exception : {exc_type.__name__}: {exc_value}")
                else:
                    print(f"   ✅ Fermeture normale")

        # Retourner False pour propager les exceptions
        # Retourner True pour supprimer les exceptions
        return False


def demo_context_manager_classe():
    """Test du context manager personnalisé"""

    print("🏗️ Context manager personnalisé (classe) :")

    # Créer le répertoire si nécessaire
    os.makedirs("context_demo", exist_ok=True)

    # Test normal
    print("\n   Test normal :")
    with GestionnaireFichierAvecLog("context_demo/test_custom.txt", "w") as f:
        f.write("Test du context manager personnalisé\n")
        f.write("Deuxième ligne\n")

    # Test avec exception
    print("\n   Test avec exception :")
    try:
        with GestionnaireFichierAvecLog("context_demo/test_custom2.txt", "w") as f:
            f.write("Début d'écriture\n")
            raise RuntimeError("Erreur simulée dans le context")
    except RuntimeError as e:
        print(f"   🚨 Exception capturée à l'extérieur : {e}")


demo_context_manager_classe()

print("\n🎲 CONTEXT MANAGER AVANCÉ - GESTION D'ÉTAT")
print("-" * 42)


class GestionnaireEtat:
    """Context manager pour gestion d'état temporaire"""

    def __init__(self, objet, **changements_temporaires):
        self.objet = objet
        self.changements = changements_temporaires
        self.valeurs_originales = {}

    def __enter__(self):
        """Sauvegarder l'état actuel et appliquer les changements"""
        print(f"   💾 Sauvegarde de l'état actuel")

        # Sauvegarder les valeurs actuelles
        for attribut, nouvelle_valeur in self.changements.items():
            if hasattr(self.objet, attribut):
                self.valeurs_originales[attribut] = getattr(
                    self.objet, attribut)
                print(
                    f"      {attribut}: {self.valeurs_originales[attribut]} -> {nouvelle_valeur}")
            else:
                self.valeurs_originales[attribut] = None
                print(f"      {attribut}: (nouveau) -> {nouvelle_valeur}")

            # Appliquer le changement temporaire
            setattr(self.objet, attribut, nouvelle_valeur)

        return self.objet

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """Restaurer l'état original"""
        print(f"   🔄 Restauration de l'état original")

        for attribut, valeur_originale in self.valeurs_originales.items():
            if valeur_originale is not None:
                setattr(self.objet, attribut, valeur_originale)
                print(f"      {attribut}: restauré à {valeur_originale}")
            else:
                if hasattr(self.objet, attribut):
                    delattr(self.objet, attribut)
                    print(f"      {attribut}: supprimé")

        return False


class Configuration:
    """Classe de configuration pour la démo"""

    def __init__(self):
        self.debug = False
        self.timeout = 30
        self.host = "localhost"


def demo_gestionnaire_etat():
    """Test du gestionnaire d'état"""

    print("🎲 Context manager pour gestion d'état :")

    config = Configuration()
    print(f"\n   État initial :")
    print(f"      debug: {config.debug}")
    print(f"      timeout: {config.timeout}")
    print(f"      host: {config.host}")

    # Modifier temporairement la configuration
    print(f"\n   Modification temporaire :")
    with GestionnaireEtat(config, debug=True, timeout=60, env="production") as cfg:
        print(f"      Dans le contexte :")
        print(f"         debug: {cfg.debug}")
        print(f"         timeout: {cfg.timeout}")
        print(f"         host: {cfg.host}")
        print(f"         env: {getattr(cfg, 'env', 'non défini')}")

    print(f"\n   État après contexte :")
    print(f"      debug: {config.debug}")
    print(f"      timeout: {config.timeout}")
    print(f"      host: {config.host}")
    print(f"      env: {getattr(config, 'env', 'non défini')}")


demo_gestionnaire_etat()

print("\n" + "=" * 50)
print("4. DÉCORATEUR @CONTEXTMANAGER")
print("=" * 50)

print("\n🎨 CONTEXTLIB.CONTEXTMANAGER")
print("-" * 29)


@contextmanager
def gestionnaire_simple(nom):
    """Context manager simple avec décorateur"""
    print(f"   🚀 Entrée dans le contexte '{nom}'")
    try:
        yield f"Ressource: {nom}"
    finally:
        print(f"   🧹 Sortie du contexte '{nom}'")


@contextmanager
def gestionnaire_fichier_temp(nom_fichier):
    """Context manager pour fichier temporaire"""
    print(f"   📝 Création du fichier temporaire '{nom_fichier}'")

    # Setup
    with open(nom_fichier, "w", encoding="utf-8") as f:
        f.write(f"Fichier temporaire créé\n")

    try:
        # Yield la ressource
        yield nom_fichier
    finally:
        # Cleanup
        if os.path.exists(nom_fichier):
            os.remove(nom_fichier)
            print(f"   🗑️ Fichier temporaire '{nom_fichier}' supprimé")


@contextmanager
def chronometre(nom_operation):
    """Context manager pour mesurer le temps d'exécution"""
    import time

    print(f"   ⏱️ Début de '{nom_operation}'")
    debut = time.time()

    try:
        yield
    finally:
        fin = time.time()
        duree = fin - debut
        print(f"   ✅ '{nom_operation}' terminé en {duree:.3f}s")


def demo_contextmanager_decorateur():
    """Test des context managers avec décorateur"""

    print("🎨 Context managers avec @contextmanager :")

    # Test du gestionnaire simple
    print("\n   1️⃣ Gestionnaire simple :")
    with gestionnaire_simple("test") as ressource:
        print(f"      Utilisation de : {ressource}")

    # Test du gestionnaire de fichier temporaire
    print("\n   2️⃣ Fichier temporaire :")
    with gestionnaire_fichier_temp("context_demo/temp.txt") as nom_fichier:
        print(f"      Fichier disponible : {nom_fichier}")
        print(f"      Existe ? {os.path.exists(nom_fichier)}")

        # Utiliser le fichier
        with open(nom_fichier, "a") as f:
            f.write("Contenu ajouté\n")

    print(
        f"      Après contexte - Existe ? {os.path.exists('context_demo/temp.txt')}")

    # Test du chronomètre
    print("\n   3️⃣ Chronomètre :")
    with chronometre("Opération de test"):
        import time
        time.sleep(0.1)  # Simuler du travail
        print(f"      Travail en cours...")


demo_contextmanager_decorateur()

print("\n🔧 CONTEXT MANAGER AVEC EXCEPTION HANDLING")
print("-" * 44)


@contextmanager
def gestionnaire_avec_exceptions(nom, supprimer_exceptions=False):
    """Context manager avec gestion d'exceptions"""
    print(f"   🎯 Entrée '{nom}'")

    try:
        yield f"Contexte: {nom}"
    except Exception as e:
        print(
            f"   🚨 Exception capturée dans le contexte : {type(e).__name__}: {e}")

        if supprimer_exceptions:
            print(f"   🔇 Exception supprimée (pas de propagation)")
            # Ne pas re-raise = supprimer l'exception
        else:
            print(f"   📤 Exception propagée vers l'extérieur")
            raise  # Re-raise l'exception
    finally:
        print(f"   🧹 Nettoyage '{nom}'")


def demo_exceptions_context_manager():
    """Test de la gestion d'exceptions"""

    print("🔧 Gestion d'exceptions dans context managers :")

    # Test avec propagation d'exception
    print("\n   1️⃣ Avec propagation d'exception :")
    try:
        with gestionnaire_avec_exceptions("test1", supprimer_exceptions=False):
            print("      Code avant exception")
            raise ValueError("Erreur de test")
            print("      Cette ligne ne sera jamais exécutée")
    except ValueError as e:
        print(f"   ✅ Exception reçue à l'extérieur : {e}")

    # Test avec suppression d'exception
    print("\n   2️⃣ Avec suppression d'exception :")
    try:
        with gestionnaire_avec_exceptions("test2", supprimer_exceptions=True):
            print("      Code avant exception")
            raise RuntimeError("Erreur qui sera supprimée")
            print("      Cette ligne ne sera jamais exécutée")

        print("   ✅ Code après le contexte (exception supprimée)")
    except Exception as e:
        print(f"   ❌ Exception non attendue : {e}")


demo_exceptions_context_manager()

print("\n" + "=" * 50)
print("5. CONTEXT MANAGERS IMBRIQUÉS")
print("=" * 50)

print("\n🪆 IMBRICATION MANUELLE")
print("-" * 21)


def demo_imbrication_manuelle():
    """Démonstration d'imbrication manuelle"""

    print("🪆 Imbrication manuelle de context managers :")

    os.makedirs("context_demo", exist_ok=True)

    with chronometre("Opération complète"):
        with gestionnaire_simple("Niveau 1") as ctx1:
            print(f"      Dans {ctx1}")

            with gestionnaire_fichier_temp("context_demo/nested.txt") as fichier:
                print(f"      Fichier temporaire : {fichier}")

                with open(fichier, "a") as f:
                    print(f"      Écriture dans le fichier")
                    f.write("Contenu imbriqué\n")

                    # Simulation de travail
                    import time
                    time.sleep(0.05)


demo_imbrication_manuelle()

print("\n🔗 CONTEXTLIB.EXITSTACK")
print("-" * 24)


def demo_exitstack():
    """Démonstration d'ExitStack pour gestion dynamique"""

    print("🔗 ExitStack pour context managers dynamiques :")

    os.makedirs("context_demo", exist_ok=True)

    fichiers = ["file1.txt", "file2.txt", "file3.txt"]

    print("\n   1️⃣ Ouverture de multiples fichiers :")
    with ExitStack() as stack:
        # Ouvrir plusieurs fichiers dynamiquement
        file_objects = []
        for nom in fichiers:
            chemin = f"context_demo/{nom}"
            f = stack.enter_context(open(chemin, "w", encoding="utf-8"))
            file_objects.append(f)
            print(f"      Ouvert : {nom}")

        # Utiliser tous les fichiers
        for i, f in enumerate(file_objects):
            f.write(f"Contenu du fichier {i+1}\n")
            f.write(f"Géré par ExitStack\n")

        print(f"      Écriture dans {len(file_objects)} fichiers")

        # Tous les fichiers seront fermés automatiquement

    print(f"   ✅ Tous les fichiers fermés automatiquement")

    # Exemple avec gestion conditionnelle
    print("\n   2️⃣ Gestion conditionnelle :")
    conditions = [True, False, True]

    with ExitStack() as stack:
        contexts = []

        for i, condition in enumerate(conditions):
            if condition:
                ctx = stack.enter_context(
                    gestionnaire_simple(f"Conditionnel-{i+1}"))
                contexts.append(ctx)
                print(f"      Context {i+1} : {ctx}")
            else:
                print(f"      Context {i+1} : ignoré")

        print(f"   📊 {len(contexts)} contexts actifs")


demo_exitstack()

print("\n⚡ CONTEXT MANAGERS EN PARALLÈLE")
print("-" * 33)


def demo_context_managers_parallele():
    """Context managers avec threading"""
    import threading
    import time

    print("⚡ Context managers avec threading :")

    @contextmanager
    def worker_context(worker_id, duree):
        """Context manager pour worker thread"""
        print(f"   🚀 Worker {worker_id} : démarrage")
        debut = time.time()

        try:
            yield worker_id
        finally:
            fin = time.time()
            print(f"   ✅ Worker {worker_id} : terminé ({fin-debut:.2f}s)")

    def worker_function(worker_id, duree):
        """Fonction worker utilisant le context manager"""
        with worker_context(worker_id, duree):
            print(f"      Worker {worker_id} : travail en cours")
            time.sleep(duree)

    # Lancer plusieurs workers
    threads = []
    durees = [0.1, 0.15, 0.08]

    for i, duree in enumerate(durees):
        thread = threading.Thread(
            target=worker_function,
            args=(i+1, duree)
        )
        threads.append(thread)
        thread.start()

    # Attendre tous les threads
    for thread in threads:
        thread.join()

    print("   🎉 Tous les workers terminés")


demo_context_managers_parallele()

print("\n" + "=" * 50)
print("6. PATTERNS AVANCÉS")
print("=" * 50)

print("\n🔄 CONTEXT MANAGER RÉENTRANT")
print("-" * 30)


class ContextManagerReentrant:
    """Context manager réentrant (peut être imbriqué avec lui-même)"""

    def __init__(self, nom):
        self.nom = nom
        self.niveau = 0

    def __enter__(self):
        self.niveau += 1
        print(
            f"   {'  ' * (self.niveau-1)}🔽 Entrée '{self.nom}' niveau {self.niveau}")
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print(
            f"   {'  ' * (self.niveau-1)}🔼 Sortie '{self.nom}' niveau {self.niveau}")
        self.niveau -= 1
        return False


def demo_context_manager_reentrant():
    """Test du context manager réentrant"""

    print("🔄 Context manager réentrant :")

    cm = ContextManagerReentrant("Réentrant")

    with cm:
        print("      Dans le niveau 1")

        with cm:
            print("      Dans le niveau 2")

            with cm:
                print("      Dans le niveau 3")

            print("      Retour au niveau 2")

        print("      Retour au niveau 1")


demo_context_manager_reentrant()

print("\n🏭 FACTORY DE CONTEXT MANAGERS")
print("-" * 32)


class ContextManagerFactory:
    """Factory pour créer différents types de context managers"""

    @staticmethod
    @contextmanager
    def connexion_db(host, base):
        """Simuler une connexion DB"""
        print(f"   🔗 Connexion à {base} sur {host}")
        connexion = f"connexion_{base}_{host}"
        try:
            yield connexion
        finally:
            print(f"   🔌 Déconnexion de {base}")

    @staticmethod
    @contextmanager
    def cache_redis(host, port=6379):
        """Simuler une connexion Redis"""
        print(f"   📦 Connexion Redis {host}:{port}")
        cache = f"redis_{host}_{port}"
        try:
            yield cache
        finally:
            print(f"   📦 Fermeture Redis")

    @staticmethod
    @contextmanager
    def transaction():
        """Simuler une transaction"""
        print(f"   💳 Début de transaction")
        transaction_id = "tx_12345"
        try:
            yield transaction_id
            print(f"   ✅ Commit transaction {transaction_id}")
        except Exception as e:
            print(f"   ❌ Rollback transaction {transaction_id} : {e}")
            raise

    @classmethod
    def creer_contexte(cls, type_contexte, **kwargs):
        """Factory method pour créer des contextes"""
        if type_contexte == "db":
            return cls.connexion_db(kwargs.get("host", "localhost"),
                                    kwargs.get("base", "mydb"))
        elif type_contexte == "cache":
            return cls.cache_redis(kwargs.get("host", "localhost"),
                                   kwargs.get("port", 6379))
        elif type_contexte == "transaction":
            return cls.transaction()
        else:
            raise ValueError(f"Type de contexte inconnu : {type_contexte}")


def demo_factory_context_managers():
    """Test de la factory de context managers"""

    print("🏭 Factory de context managers :")

    factory = ContextManagerFactory()

    # Test des différents types
    types_test = [
        ("db", {"host": "prod-server", "base": "users"}),
        ("cache", {"host": "redis-server", "port": 6380}),
        ("transaction", {})
    ]

    for type_ctx, params in types_test:
        print(f"\n   Test {type_ctx} :")
        try:
            with factory.creer_contexte(type_ctx, **params) as ctx:
                print(f"      Utilisation de : {ctx}")
        except Exception as e:
            print(f"      Erreur : {e}")


demo_factory_context_managers()

print("\n🎛️ CONTEXT MANAGER CONFIGURABLE")
print("-" * 33)


class ContextManagerConfigurable:
    """Context manager avec configuration flexible"""

    def __init__(self, **config):
        self.config = {
            'debug': False,
            'timeout': 30,
            'retry_count': 3,
            'log_level': 'INFO',
            'cleanup_on_error': True
        }
        self.config.update(config)
        self.resources = []

    def __enter__(self):
        if self.config['debug']:
            print(f"   🔧 Configuration : {self.config}")

        # Simuler l'acquisition de ressources
        for i in range(3):
            resource = f"resource_{i}"
            self.resources.append(resource)
            if self.config['debug']:
                print(f"      Ressource acquise : {resource}")

        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        # Nettoyage des ressources
        if exc_type and self.config['cleanup_on_error']:
            print(f"   🧹 Nettoyage d'urgence après {exc_type.__name__}")

        for resource in reversed(self.resources):
            if self.config['debug']:
                print(f"      Libération : {resource}")

        self.resources.clear()

        if self.config['debug']:
            print(f"   ✅ Toutes les ressources libérées")

        return False


def demo_context_manager_configurable():
    """Test du context manager configurable"""

    print("🎛️ Context manager configurable :")

    # Configuration normale
    print("\n   1️⃣ Configuration normale :")
    with ContextManagerConfigurable(debug=True, timeout=60) as cm:
        print(f"      Utilisation des ressources : {len(cm.resources)}")

    # Configuration avec erreur
    print("\n   2️⃣ Configuration avec gestion d'erreur :")
    try:
        with ContextManagerConfigurable(debug=True, cleanup_on_error=True) as cm:
            print(f"      Avant erreur : {len(cm.resources)} ressources")
            raise RuntimeError("Erreur de test")
    except RuntimeError as e:
        print(f"   🚨 Exception gérée : {e}")


demo_context_manager_configurable()

print("\n" + "=" * 50)
print("7. ASYNC CONTEXT MANAGERS")
print("=" * 50)

print("\n🚀 ASYNC/AWAIT CONTEXT MANAGERS")
print("-" * 33)

print("""
🚀 ASYNC CONTEXT MANAGERS :

Pour les opérations asynchrones, Python fournit :
• __aenter__() : version async de __enter__()
• __aexit__()  : version async de __exit__()
• async with   : version async du statement with

📝 EXEMPLE DE STRUCTURE :

class AsyncContextManager:
    async def __aenter__(self):
        # Setup asynchrone
        return self
    
    async def __aexit__(self, exc_type, exc_value, traceback):
        # Cleanup asynchrone
        return False

# Utilisation :
async def main():
    async with AsyncContextManager() as ctx:
        # Code asynchrone
        pass

💡 CAS D'USAGE :
• Connexions réseau (HTTP, WebSocket, DB)
• Fichiers asynchrones
• Verrous asynchrones
• Pools de ressources async
""")

# Exemple simple d'async context manager (structure seulement)


class ExempleAsyncContextManager:
    """Exemple conceptuel d'async context manager"""

    def __init__(self, nom):
        self.nom = nom

    # Version synchrone pour la démo
    def __enter__(self):
        print(f"   🚀 [Sync] Entrée async contexte '{self.nom}'")
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print(f"   🧹 [Sync] Sortie async contexte '{self.nom}'")
        return False


def demo_concept_async():
    """Démonstration conceptuelle (version sync)"""

    print("🚀 Concept d'async context manager (version sync) :")

    with ExempleAsyncContextManager("Demo") as ctx:
        print(f"      Dans le contexte async : {ctx.nom}")


demo_concept_async()

print("\n" + "=" * 50)
print("8. DEBUGGING ET BEST PRACTICES")
print("=" * 50)

print("\n🔍 DEBUGGING CONTEXT MANAGERS")
print("-" * 30)


class ContextManagerDebug:
    """Context manager avec debugging intégré"""

    def __init__(self, nom, debug=True):
        self.nom = nom
        self.debug = debug
        self.entree_reussie = False

    def __enter__(self):
        if self.debug:
            import traceback
            print(f"   🔍 [DEBUG] Entrée '{self.nom}'")
            print(f"      Stack trace :")
            for ligne in traceback.format_stack()[-3:-1]:  # 2 derniers appels
                print(f"        {ligne.strip()}")

        try:
            # Simuler acquisition de ressource
            ressource = f"ressource_{self.nom}"
            self.entree_reussie = True

            if self.debug:
                print(f"      Ressource acquise : {ressource}")

            return ressource

        except Exception as e:
            if self.debug:
                print(f"   ❌ [DEBUG] Erreur dans __enter__ : {e}")
            raise

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.debug:
            print(f"   🔍 [DEBUG] Sortie '{self.nom}'")
            print(f"      Entrée réussie : {self.entree_reussie}")

            if exc_type:
                print(f"      Exception : {exc_type.__name__}: {exc_value}")
                print(
                    f"      Traceback disponible : {exc_traceback is not None}")
            else:
                print(f"      Sortie normale")

        # Cleanup même en cas d'erreur d'entrée
        if self.entree_reussie and self.debug:
            print(f"      Nettoyage des ressources")

        return False


def demo_debugging():
    """Test du debugging de context managers"""

    print("🔍 Debugging de context managers :")

    # Test normal
    print("\n   1️⃣ Utilisation normale :")
    with ContextManagerDebug("test-normal") as ressource:
        print(f"      Utilisation de : {ressource}")

    # Test avec exception
    print("\n   2️⃣ Avec exception :")
    try:
        with ContextManagerDebug("test-exception") as ressource:
            print(f"      Avant exception : {ressource}")
            raise ValueError("Erreur de test")
    except ValueError as e:
        print(f"   🚨 Exception capturée : {e}")


demo_debugging()

print("\n✅ BEST PRACTICES")
print("-" * 17)

print("""
✅ MEILLEURES PRATIQUES :

1. 🎯 RESPONSABILITÉ UNIQUE :
   • Un context manager = une responsabilité
   • Séparer acquisition et logique métier
   • Noms explicites et descriptifs

2. 🛡️ ROBUSTESSE :
   • Toujours implémenter __exit__ correctement
   • Gérer les exceptions dans __enter__ et __exit__
   • Nettoyage même si __enter__ échoue

3. 📝 DOCUMENTATION :
   • Documenter le comportement en cas d'exception
   • Expliquer les ressources gérées
   • Exemples d'utilisation

4. 🧪 TESTS :
   • Tester les cas normaux ET les exceptions
   • Vérifier la libération des ressources
   • Tests de réentrance si applicable

5. ⚡ PERFORMANCE :
   • Éviter le travail lourd dans __enter__/__exit__
   • Utiliser des pools pour ressources coûteuses
   • Async pour opérations I/O

❌ ANTI-PATTERNS À ÉVITER :
• Ne pas nettoyer en cas d'exception
• Logique métier dans __enter__/__exit__
• Suppression silencieuse d'exceptions importantes
• Context managers non thread-safe sans documentation
• Acquisition de ressources sans garantie de libération
""")

print("\n" + "=" * 50)
print("9. EXERCICES PRATIQUES")
print("=" * 50)

print("""
💪 EXERCICES À IMPLÉMENTER :

🎯 Exercice 1 : Pool de connexions DB
Créez un context manager pour pool de connexions :
• Acquisition/libération automatique de connexions
• Gestion des timeouts et retry
• Monitoring des connexions actives
• Thread-safety et async support
• Health checks automatiques

🔒 Exercice 2 : Gestionnaire de verrous distribués
Créez un système de verrous distribués :
• Verrous Redis/ZooKeeper
• Timeout et renouvellement automatique
• Détection de deadlocks
• Monitoring et métriques
• Fallback en cas de panne

🎮 Exercice 3 : Context manager de test
Créez un framework de test avec context managers :
• Setup/teardown automatique
• Mocks et fixtures temporaires
• Capture d'output et logs
• Nettoyage de base de données
• Génération de rapports

⚡ Exercice 4 : Gestionnaire de cache intelligent
Créez un système de cache avec context managers :
• Cache multi-niveaux (mémoire, Redis, disque)
• Invalidation intelligente
• Compression et sérialisation
• Métriques de performance
• Warmup automatique

🌐 Exercice 5 : Context manager réseau
Créez un gestionnaire pour opérations réseau :
• Pool de connexions HTTP/WebSocket
• Circuit breaker et retry
• Monitoring latence et erreurs
• Load balancing
• Graceful shutdown
""")

print("\n" + "=" * 50)
print("10. RÉSUMÉ FINAL")
print("=" * 50)

print("""
🎯 POINTS CLÉS À RETENIR :

1. 🏗️ PROTOCOLE CONTEXT MANAGER :
   • __enter__() : setup, retourne la ressource
   • __exit__() : cleanup, reçoit info d'exception
   • Garantit l'exécution du cleanup même si exception
   • Base du pattern RAII en Python

2. 🎭 STATEMENT WITH :
   • with obj as var: syntaxe claire et sûre
   • Équivaut à try/finally mais plus lisible
   • Support de l'imbrication et des multiples ressources
   • Gestion automatique des exceptions

3. 🎨 CRÉATION DE CONTEXT MANAGERS :
   • Classe avec __enter__/__exit__ : contrôle total
   • @contextmanager : plus simple avec yield
   • ExitStack : gestion dynamique de multiples contexts
   • Personnalisation selon les besoins

4. 🔒 GESTION DES RESSOURCES :
   • Fichiers, connexions DB, verrous, sockets
   • Acquisition fiable et libération garantie
   • Thread-safety si nécessaire
   • Gestion des timeouts et erreurs

5. ⚡ PATTERNS AVANCÉS :
   • Context managers réentrants
   • Factories et configuration
   • Imbrication et parallélisme
   • Async context managers (__aenter__/__aexit__)

💡 BONNES PRATIQUES :
✅ Toujours utiliser with pour les ressources
✅ Implémenter __exit__ même si pas d'exception
✅ Documenter le comportement en cas d'erreur
✅ Tester les cas normaux ET exceptionnels
✅ Responsabilité unique par context manager
✅ Noms explicites et descriptifs

🚨 ERREURS COURANTES :
❌ Oublier de libérer les ressources en cas d'exception
❌ Logique métier dans __enter__/__exit__
❌ Suppression d'exceptions sans justification
❌ Context managers non thread-safe
❌ Acquisition sans garantie de libération
❌ Ressources partagées sans synchronisation

⚡ CAS D'USAGE COURANTS :
• Gestion de fichiers et I/O
• Connexions base de données
• Verrous et synchronisation
• Sessions et authentification  
• Transactions et rollback
• Monitoring et profiling

🔧 OUTILS ET EXTENSIONS :
• contextlib : décorateurs et utilitaires
• ExitStack : gestion dynamique
• asyncio : context managers asynchrones
• Bibliothèques tierces avec support contextuel
• Frameworks utilisant le pattern

🎯 ARCHITECTURE ROBUSTE :
• Séparation des responsabilités
• Gestion centralisée des ressources
• Monitoring et observabilité
• Graceful degradation
• Recovery automatique

🎉 Félicitations ! Context managers maîtrisés !
💡 Prochaine étape : Gestion d'erreurs avancée !
📚 Ressources sous contrôle, gérez les erreurs !
""")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE - CONTEXT MANAGERS MAÎTRISÉS !")
print("=" * 70)
