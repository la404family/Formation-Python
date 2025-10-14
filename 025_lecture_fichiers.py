#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
======================================================================
LECTURE DE FICHIERS EN PYTHON - GUIDE COMPLET
======================================================================

🎯 Ce fichier couvre la lecture de fichiers en détail :
   • Ouverture et fermeture de fichiers
   • Modes d'ouverture et encodage
   • Méthodes de lecture (read, readline, readlines)
   • Context managers (with)
   • Gestion d'erreurs pour fichiers
   • Fichiers binaires vs texte

📚 Concepts abordés :
   • File objects et méthodes
   • Buffering et performance
   • Encodage de caractères
   • Chemins et pathlib
   • Parsing de formats courants
   • Sécurité et validation

💡 Objectif : Maîtriser la lecture efficace de fichiers
"""

import os
print("=" * 70)
print("LECTURE DE FICHIERS EN PYTHON - GUIDE COMPLET")
print("=" * 70)

print("\n" + "=" * 50)
print("1. FONDAMENTAUX DE LA LECTURE")
print("=" * 50)

print("\n📂 QU'EST-CE QU'UN FICHIER ?")
print("-" * 28)

print("""
🎯 DÉFINITION :
Un fichier est une séquence d'octets stockée sur un système de stockage,
identifiée par un nom et organisée par le système de fichiers.

🔄 TYPES DE FICHIERS :
• Fichiers texte : contenu interprété comme caractères
• Fichiers binaires : séquence brute d'octets
• Fichiers spéciaux : périphériques, pipes, etc.

📊 MÉTADONNÉES :
• Nom et extension
• Taille en octets
• Dates (création, modification, accès)
• Permissions (lecture, écriture, exécution)
• Propriétaire et groupe

⚡ OPÉRATIONS DE BASE :
• Ouverture (open) : créer un objet fichier
• Lecture (read) : récupérer le contenu
• Position (seek/tell) : naviguer dans le fichier
• Fermeture (close) : libérer les ressources
""")

print("\n🔧 FONCTION OPEN() - SYNTAXE")
print("-" * 29)

print("""
🎯 SYNTAXE COMPLÈTE :
open(file, mode='r', buffering=-1, encoding=None, 
     errors=None, newline=None, closefd=True, opener=None)

📋 PARAMÈTRES PRINCIPAUX :
• file : chemin du fichier (str ou Path)
• mode : mode d'ouverture ('r', 'w', 'a', 'x', etc.)
• encoding : encodage des caractères ('utf-8', 'cp1252', etc.)
• buffering : taille du buffer (-1=système, 0=non bufferisé)
• errors : gestion des erreurs d'encodage
• newline : gestion des fins de ligne

🚨 IMPORTANT :
Toujours fermer les fichiers après usage !
Utiliser des context managers (with) pour la sécurité.
""")

# Créons d'abord quelques fichiers de test

# Créer le répertoire test_files s'il n'existe pas
os.makedirs("test_files", exist_ok=True)

# Créer un fichier texte simple
with open("test_files/exemple_simple.txt", "w", encoding="utf-8") as f:
    f.write("""Bonjour le monde !
Ceci est un fichier de test.
Il contient plusieurs lignes.
Chaque ligne se termine par un retour à la ligne.
Ligne 5 avec des caractères spéciaux : éàùç
""")

# Créer un fichier CSV
with open("test_files/donnees.csv", "w", encoding="utf-8") as f:
    f.write("""nom,age,ville
Alice,25,Paris
Bob,30,Lyon
Charlie,35,Marseille
Diane,28,Toulouse
Eve,22,Nice
""")

# Créer un fichier JSON
with open("test_files/configuration.json", "w", encoding="utf-8") as f:
    f.write("""{
    "version": "1.0",
    "debug": true,
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "app_db"
    },
    "features": ["auth", "logging", "cache"],
    "limits": {
        "max_users": 1000,
        "timeout": 30.5
    }
}""")

# Créer un fichier de log
with open("test_files/application.log", "w", encoding="utf-8") as f:
    f.write("""2024-01-15 10:00:00 INFO Application démarrée
2024-01-15 10:00:01 DEBUG Configuration chargée
2024-01-15 10:00:02 INFO Connexion base de données OK
2024-01-15 10:05:30 WARNING Cache presque plein (85%)
2024-01-15 10:10:15 ERROR Timeout connexion utilisateur 123
2024-01-15 10:10:16 INFO Reconnexion automatique réussie
2024-01-15 10:15:00 INFO 50 utilisateurs actifs
""")

print("📁 Fichiers de test créés dans le répertoire 'test_files/'")

print("\n" + "=" * 50)
print("2. MODES D'OUVERTURE")
print("=" * 50)

print("\n🎭 MODES DE BASE")
print("-" * 16)

modes_base = [
    ("'r'", "Lecture seule (défaut)", "Fichier doit exister"),
    ("'w'", "Écriture seule", "Crée/écrase le fichier"),
    ("'a'", "Ajout en fin", "Crée le fichier si nécessaire"),
    ("'x'", "Création exclusive", "Échoue si fichier existe"),
    ("'r+'", "Lecture/écriture", "Fichier doit exister"),
    ("'w+'", "Lecture/écriture", "Crée/écrase le fichier"),
    ("'a+'", "Lecture/ajout", "Crée le fichier si nécessaire"),
]

print("🎭 Modes d'ouverture principaux :")
for mode, description, comportement in modes_base:
    print(f"   {mode:<6} : {description:<20} | {comportement}")

print("\n🔤 MODIFICATEURS DE MODE")
print("-" * 24)

print("""
🔤 MODIFICATEURS :
• 'b' : Mode binaire (ex: 'rb', 'wb')
• 't' : Mode texte (défaut, ex: 'rt', 'wt')

📝 EXEMPLES :
• 'r'   = 'rt'  : lecture texte
• 'rb'          : lecture binaire
• 'w'   = 'wt'  : écriture texte
• 'wb'          : écriture binaire
• 'a+'  = 'a+t' : ajout + lecture texte
• 'r+b'         : lecture/écriture binaire
""")

print("\n🧪 TESTS DES MODES D'OUVERTURE")
print("-" * 30)


def tester_mode_ouverture(fichier, mode, description):
    """Test d'ouverture avec un mode spécifique"""
    try:
        with open(fichier, mode, encoding="utf-8" if 'b' not in mode else None) as f:
            print(f"   ✅ {mode:<4} ({description}) : Ouverture réussie")

            # Informations sur le fichier
            print(f"      Mode : {f.mode}")
            print(f"      Nom : {f.name}")
            print(f"      Lisible : {f.readable()}")
            print(f"      Écrivable : {f.writable()}")

            # Essayer de lire quelques caractères si possible
            if f.readable():
                position_initiale = f.tell()
                try:
                    if 'b' in mode:
                        preview = f.read(20)
                        print(f"      Aperçu : {preview}")
                    else:
                        preview = f.read(30)
                        print(f"      Aperçu : '{preview.replace(chr(10), '\\n')}'")
                except:
                    print(f"      Aperçu : Non disponible")

                # Remettre au début si on a lu
                f.seek(position_initiale)

    except Exception as e:
        print(f"   ❌ {mode:<4} ({description}) : {e}")


print("🧪 Tests des modes sur fichier existant :")
fichier_test = "test_files/exemple_simple.txt"

modes_test = [
    ('r', 'Lecture seule'),
    ('r+', 'Lecture/écriture'),
    ('rb', 'Lecture binaire'),
    ('rt', 'Lecture texte explicite'),
]

for mode, desc in modes_test:
    tester_mode_ouverture(fichier_test, mode, desc)
    print()

print("\n" + "=" * 50)
print("3. MÉTHODES DE LECTURE")
print("=" * 50)

print("\n📖 READ() - LECTURE COMPLÈTE")
print("-" * 28)


def demo_read_complete():
    """Démonstration de read() pour lecture complète"""

    print("📖 Lecture complète du fichier :")
    try:
        with open("test_files/exemple_simple.txt", "r", encoding="utf-8") as f:
            contenu_complet = f.read()
            print(f"   Type : {type(contenu_complet)}")
            print(f"   Longueur : {len(contenu_complet)} caractères")
            print(
                f"   Nombre de lignes : {contenu_complet.count(chr(10)) + 1}")
            print("   Contenu :")
            for i, ligne in enumerate(contenu_complet.split('\n'), 1):
                print(f"      {i:2d}: {ligne}")

    except Exception as e:
        print(f"   ❌ Erreur : {e}")


demo_read_complete()

print("\n📄 READ(SIZE) - LECTURE PARTIELLE")
print("-" * 32)


def demo_read_partielle():
    """Démonstration de read(size) pour lecture par blocs"""

    print("📄 Lecture par blocs de 20 caractères :")
    try:
        with open("test_files/exemple_simple.txt", "r", encoding="utf-8") as f:
            bloc_num = 1
            while True:
                bloc = f.read(20)  # Lire 20 caractères
                if not bloc:  # Fin de fichier
                    break

                print(f"   Bloc {bloc_num} ({len(bloc)} chars) : '{bloc.replace(chr(10), '\\n')}'")
                bloc_num += 1

                if bloc_num > 10:  # Limiter pour la démo
                    print("   ... (lecture limitée pour la démo)")
                    break

    except Exception as e:
        print(f"   ❌ Erreur : {e}")


demo_read_partielle()

print("\n📝 READLINE() - LECTURE LIGNE PAR LIGNE")
print("-" * 37)


def demo_readline():
    """Démonstration de readline() pour lecture séquentielle"""

    print("📝 Lecture ligne par ligne avec readline() :")
    try:
        with open("test_files/exemple_simple.txt", "r", encoding="utf-8") as f:
            ligne_num = 1
            while True:
                ligne = f.readline()
                if not ligne:  # Fin de fichier
                    break

                # Afficher avec informations
                # Enlever les retours à la ligne
                ligne_propre = ligne.rstrip('\n\r')
                print(
                    f"   Ligne {ligne_num} ({len(ligne)} chars) : '{ligne_propre}'")
                ligne_num += 1

    except Exception as e:
        print(f"   ❌ Erreur : {e}")


demo_readline()

print("\n📋 READLINES() - TOUTES LES LIGNES")
print("-" * 33)


def demo_readlines():
    """Démonstration de readlines() pour charger toutes les lignes"""

    print("📋 Lecture de toutes les lignes avec readlines() :")
    try:
        with open("test_files/exemple_simple.txt", "r", encoding="utf-8") as f:
            toutes_lignes = f.readlines()

            print(f"   Type : {type(toutes_lignes)}")
            print(f"   Nombre de lignes : {len(toutes_lignes)}")

            for i, ligne in enumerate(toutes_lignes, 1):
                ligne_propre = ligne.rstrip('\n\r')
                print(f"   [{i}] : '{ligne_propre}'")

    except Exception as e:
        print(f"   ❌ Erreur : {e}")


demo_readlines()

print("\n🔄 ITÉRATION SUR FICHIER")
print("-" * 24)


def demo_iteration_fichier():
    """Démonstration de l'itération directe sur un fichier"""

    print("🔄 Itération directe sur le fichier (méthode recommandée) :")
    try:
        with open("test_files/exemple_simple.txt", "r", encoding="utf-8") as f:
            for numero_ligne, ligne in enumerate(f, 1):
                ligne_propre = ligne.rstrip('\n\r')
                print(f"   Ligne {numero_ligne} : '{ligne_propre}'")

    except Exception as e:
        print(f"   ❌ Erreur : {e}")


demo_iteration_fichier()

print("\n⚡ COMPARAISON DES PERFORMANCES")
print("-" * 32)


def comparer_methodes_lecture():
    """Comparaison des performances des différentes méthodes"""
    import time

    # Créer un fichier plus grand pour le test
    with open("test_files/gros_fichier.txt", "w", encoding="utf-8") as f:
        for i in range(1000):
            f.write(
                f"Ligne {i:04d} avec du contenu pour tester les performances de lecture\n")

    methodes = [
        ("read()", lambda f: f.read()),
        ("readlines()", lambda f: f.readlines()),
        ("iteration", lambda f: list(f)),
        ("readline loop", lambda f: [f.readline()
         for _ in range(1000) if f.readline()]),
    ]

    print("⚡ Test de performance sur 1000 lignes :")

    # Éviter la méthode readline loop qui est bugée
    for nom, methode in methodes[:3]:
        try:
            start_time = time.time()

            with open("test_files/gros_fichier.txt", "r", encoding="utf-8") as f:
                resultat = methode(f)

            end_time = time.time()
            duree = (end_time - start_time) * 1000  # en ms

            if isinstance(resultat, str):
                nb_lignes = resultat.count('\n')
            else:
                nb_lignes = len(resultat)

            print(f"   {nom:<15} : {duree:6.2f} ms ({nb_lignes} lignes)")

        except Exception as e:
            print(f"   {nom:<15} : ❌ Erreur - {e}")


comparer_methodes_lecture()

print("\n" + "=" * 50)
print("4. GESTION DE LA POSITION")
print("=" * 50)

print("\n📍 TELL() ET SEEK() - NAVIGATION")
print("-" * 32)


def demo_position_fichier():
    """Démonstration de la gestion de position dans un fichier"""

    print("📍 Navigation dans un fichier avec tell() et seek() :")

    try:
        with open("test_files/exemple_simple.txt", "r", encoding="utf-8") as f:
            # Position initiale
            print(f"   Position initiale : {f.tell()}")

            # Lire quelques caractères
            debut = f.read(10)
            print(f"   Après lecture de 10 chars : position {f.tell()}")
            print(f"   Texte lu : '{debut}'")

            # Revenir au début
            f.seek(0)
            print(f"   Après seek(0) : position {f.tell()}")

            # Aller à la position 20
            f.seek(20)
            print(f"   Après seek(20) : position {f.tell()}")
            suite = f.read(15)
            print(f"   Texte à partir de la position 20 : '{suite}'")

            # Aller à la fin
            f.seek(0, 2)  # 2 = SEEK_END
            taille_fichier = f.tell()
            print(f"   Taille du fichier : {taille_fichier} octets")

            # Position relative
            f.seek(0)  # Retour au début
            f.read(5)  # Lire 5 caractères
            print(f"   Position avant seek relatif : {f.tell()}")
            f.seek(10, 1)  # 1 = SEEK_CUR (position courante + 10)
            print(f"   Position après seek(+10) relatif : {f.tell()}")

    except Exception as e:
        print(f"   ❌ Erreur : {e}")


demo_position_fichier()

print("\n🎯 MODES DE SEEK")
print("-" * 16)

print("""
🎯 CONSTANTES DE SEEK :
• 0 ou os.SEEK_SET : depuis le début du fichier
• 1 ou os.SEEK_CUR : depuis la position courante
• 2 ou os.SEEK_END : depuis la fin du fichier

📐 EXEMPLES :
• seek(0)     : aller au début
• seek(0, 2)  : aller à la fin
• seek(-10, 2): 10 octets avant la fin
• seek(5, 1)  : avancer de 5 octets
• seek(-3, 1) : reculer de 3 octets

⚠️ ATTENTION :
En mode texte, seek() avec offset relatif peut poser problème
avec l'encodage multi-octets. Préférer les positions absolues.
""")


def demo_seek_avance():
    """Démonstration avancée de seek()"""

    print("🎯 Techniques avancées de navigation :")

    try:
        with open("test_files/donnees.csv", "r", encoding="utf-8") as f:
            # Mémoriser des positions importantes
            positions = {}

            # Lire l'en-tête
            positions['debut'] = f.tell()
            header = f.readline()
            positions['apres_header'] = f.tell()
            print(f"   En-tête : '{header.strip()}'")

            # Lire quelques lignes en mémorisant les positions
            for i in range(3):
                pos_avant = f.tell()
                ligne = f.readline()
                if ligne:
                    positions[f'ligne_{i+1}'] = pos_avant
                    print(
                        f"   Ligne {i+1} (pos {pos_avant}) : '{ligne.strip()}'")

            print(f"\n   Positions mémorisées : {positions}")

            # Revenir à une position spécifique
            print(f"\n   Retour à la ligne 2 :")
            f.seek(positions['ligne_2'])
            ligne_2_bis = f.readline()
            print(f"   Relecture : '{ligne_2_bis.strip()}'")

            # Lire les derniers caractères
            f.seek(-20, 2)  # 20 caractères avant la fin
            fin = f.read()
            print(f"   Fin du fichier : '{fin.replace(chr(10), '\\n')}'")

    except Exception as e:
        print(f"   ❌ Erreur : {e}")


demo_seek_avance()

print("\n" + "=" * 50)
print("5. ENCODAGE ET CARACTÈRES")
print("=" * 50)

print("\n🌍 ENCODAGES DE CARACTÈRES")
print("-" * 26)

print("""
🌍 ENCODAGES COURANTS :
• UTF-8 : Standard universel, compatible ASCII
• UTF-16 : Unicode 16 bits, BOM optionnel
• UTF-32 : Unicode 32 bits, fixe
• CP1252 : Windows Western Europe (Latin-1 étendu)
• ISO-8859-1 : Latin-1, Europe occidentale
• ASCII : 7 bits, caractères de base seulement

🎯 RECOMMANDATION :
Toujours spécifier encoding='utf-8' pour la compatibilité !
""")


def demo_encodages():
    """Démonstration des différents encodages"""

    # Créer des fichiers avec différents encodages
    texte_multilingue = "Bonjour ! Héllo! 你好! Здравствуй! مرحبا"

    encodages_test = [
        ('utf-8', 'UTF-8 standard'),
        ('utf-16', 'UTF-16 avec BOM'),
        ('cp1252', 'Windows-1252'),
        ('iso-8859-1', 'Latin-1'),
    ]

    print("🌍 Test des encodages :")

    for encodage, description in encodages_test:
        try:
            # Écrire avec l'encodage
            nom_fichier = f"test_files/test_{encodage.replace('-', '_')}.txt"
            with open(nom_fichier, "w", encoding=encodage) as f:
                f.write(texte_multilingue)

            # Lire avec le même encodage
            with open(nom_fichier, "r", encoding=encodage) as f:
                contenu = f.read()

            print(f"   ✅ {encodage:<12} ({description}) : '{contenu}'")

            # Taille du fichier
            taille = os.path.getsize(nom_fichier)
            print(f"      Taille : {taille} octets")

        except Exception as e:
            print(f"   ❌ {encodage:<12} : {e}")

    print()


demo_encodages()

print("\n⚠️ ERREURS D'ENCODAGE")
print("-" * 22)


def demo_erreurs_encodage():
    """Démonstration des erreurs d'encodage"""

    print("⚠️ Gestion des erreurs d'encodage :")

    # Créer un fichier avec caractères spéciaux
    texte_special = "Café français : 15€ — Très bon !"

    with open("test_files/test_utf8.txt", "w", encoding="utf-8") as f:
        f.write(texte_special)

    # Essayer de lire avec différents encodages
    stratégies_erreur = [
        ('strict', 'Lever une exception (défaut)'),
        ('ignore', 'Ignorer les caractères problématiques'),
        ('replace', 'Remplacer par des marqueurs'),
        ('xmlcharrefreplace', 'Remplacer par des références XML'),
        ('backslashreplace', 'Remplacer par des séquences \\u'),
    ]

    for strategie, description in stratégies_erreur:
        try:
            with open("test_files/test_utf8.txt", "r", encoding="ascii", errors=strategie) as f:
                contenu = f.read()
            print(f"   {strategie:<18} : '{contenu}'")
            print(f"      {description}")

        except Exception as e:
            print(f"   {strategie:<18} : ❌ {e}")

        print()


demo_erreurs_encodage()

print("\n🔍 DÉTECTION D'ENCODAGE")
print("-" * 23)


def analyser_encodage_fichier(nom_fichier):
    """Analyse l'encodage probable d'un fichier"""

    print(f"🔍 Analyse de l'encodage de '{nom_fichier}' :")

    try:
        # Lire en mode binaire pour analyser
        with open(nom_fichier, "rb") as f:
            debut = f.read(100)  # Premiers 100 octets

        print(f"   Premiers octets : {debut[:20]}")

        # Tester différents encodages
        encodages_test = ['utf-8', 'utf-16', 'cp1252', 'iso-8859-1']

        for encodage in encodages_test:
            try:
                with open(nom_fichier, "r", encoding=encodage) as f:
                    contenu = f.read(50)  # Lire quelques caractères
                print(f"   ✅ {encodage:<12} : '{contenu.replace(chr(10), '\\n')[:30]}...'")

            except UnicodeDecodeError as e:
                print(f"   ❌ {encodage:<12} : Erreur de décodage")
            except Exception as e:
                print(f"   ❌ {encodage:<12} : {e}")

    except Exception as e:
        print(f"   ❌ Erreur d'analyse : {e}")

    print()


# Analyser nos fichiers de test
analyser_encodage_fichier("test_files/test_utf_8.txt")
analyser_encodage_fichier("test_files/test_utf_16.txt")

print("\n" + "=" * 50)
print("6. CONTEXT MANAGERS (WITH)")
print("=" * 50)

print("\n🔒 POURQUOI UTILISER WITH ?")
print("-" * 27)

print("""
🔒 PROBLÈMES SANS CONTEXT MANAGER :
• Oubli de fermer les fichiers (fuite de ressources)
• Fichiers restent ouverts en cas d'exception
• Gestion manuelle des erreurs complexe
• Code verbeux et répétitif

✅ AVANTAGES AVEC WITH :
• Fermeture automatique garantie
• Même en cas d'exception
• Code plus lisible et sûr
• Gestion des ressources simplifiée
• Pattern recommandé par Python
""")

print("\n❌ MAUVAISE PRATIQUE")
print("-" * 20)


def demo_sans_with():
    """Démonstration des problèmes sans context manager"""

    print("❌ Ouverture sans context manager (MAUVAIS) :")

    try:
        # Mauvaise pratique
        f = open("test_files/exemple_simple.txt", "r", encoding="utf-8")
        contenu = f.read()
        print(f"   Contenu lu : {len(contenu)} caractères")

        # Si une exception se produit ici, le fichier reste ouvert !
        # Par exemple : division par zéro
        # resultat = 10 / 0  # Décommentez pour voir le problème

        f.close()  # Cette ligne pourrait ne jamais être exécutée !
        print("   Fichier fermé manuellement")

    except Exception as e:
        print(f"   ❌ Erreur : {e}")
        # Le fichier reste ouvert !
        try:
            f.close()
            print("   Fichier fermé dans except")
        except:
            print("   Impossible de fermer le fichier")


demo_sans_with()

print("\n✅ BONNE PRATIQUE")
print("-" * 18)


def demo_avec_with():
    """Démonstration avec context manager"""

    print("✅ Ouverture avec context manager (BON) :")

    try:
        with open("test_files/exemple_simple.txt", "r", encoding="utf-8") as f:
            contenu = f.read()
            print(f"   Contenu lu : {len(contenu)} caractères")
            print(f"   Fichier ouvert : {not f.closed}")

            # Même si une exception se produit ici...
            # resultat = 10 / 0  # Le fichier sera fermé automatiquement !

        print(f"   Fichier fermé automatiquement : {f.closed}")

    except Exception as e:
        print(f"   ❌ Erreur : {e}")
        print(f"   Fichier fermé malgré l'erreur : {f.closed}")


demo_avec_with()

print("\n🔄 MULTIPLES FICHIERS")
print("-" * 21)


def demo_multiples_fichiers():
    """Ouverture de multiples fichiers avec with"""

    print("🔄 Ouverture de multiples fichiers :")

    try:
        # Méthode 1 : with imbriqués
        print("   Méthode 1 - with imbriqués :")
        with open("test_files/donnees.csv", "r", encoding="utf-8") as f1:
            with open("test_files/application.log", "r", encoding="utf-8") as f2:
                lignes_csv = len(f1.readlines())
                lignes_log = len(f2.readlines())
                print(f"      CSV : {lignes_csv} lignes")
                print(f"      LOG : {lignes_log} lignes")

        # Méthode 2 : with multiple (Python 2.7+)
        print("   Méthode 2 - with multiple :")
        with open("test_files/donnees.csv", "r", encoding="utf-8") as f1, \
                open("test_files/application.log", "r", encoding="utf-8") as f2:

            premiere_ligne_csv = f1.readline().strip()
            premiere_ligne_log = f2.readline().strip()
            print(f"      Première ligne CSV : '{premiere_ligne_csv}'")
            print(f"      Première ligne LOG : '{premiere_ligne_log}'")

    except Exception as e:
        print(f"   ❌ Erreur : {e}")


demo_multiples_fichiers()

print("\n🛠️ CONTEXT MANAGER PERSONNALISÉ")
print("-" * 32)


class GestionnaireFichierAvecLog:
    """Context manager personnalisé avec logging"""

    def __init__(self, nom_fichier, mode="r", encoding="utf-8", log=True):
        self.nom_fichier = nom_fichier
        self.mode = mode
        self.encoding = encoding
        self.log = log
        self.fichier = None
        self.temps_ouverture = None

    def __enter__(self):
        """Entrée dans le context manager"""
        if self.log:
            import time
            self.temps_ouverture = time.time()
            print(
                f"   📂 Ouverture de '{self.nom_fichier}' en mode '{self.mode}'")

        try:
            self.fichier = open(self.nom_fichier, self.mode,
                                encoding=self.encoding)
            if self.log:
                print(f"   ✅ Fichier ouvert avec succès")
            return self.fichier

        except Exception as e:
            if self.log:
                print(f"   ❌ Erreur d'ouverture : {e}")
            raise

    def __exit__(self, exc_type, exc_value, traceback):
        """Sortie du context manager"""
        if self.fichier:
            self.fichier.close()

            if self.log:
                import time
                duree = time.time() - self.temps_ouverture
                print(f"   🔒 Fichier fermé (ouvert pendant {duree:.3f}s)")

                if exc_type:
                    print(
                        f"   ⚠️ Fermeture après exception : {exc_type.__name__}")
                else:
                    print(f"   ✅ Fermeture normale")

        # Retourner False pour propager les exceptions
        return False


def demo_context_manager_personnalise():
    """Test du context manager personnalisé"""

    print("🛠️ Test du context manager personnalisé :")

    # Test normal
    print("\n   Test normal :")
    with GestionnaireFichierAvecLog("test_files/exemple_simple.txt") as f:
        contenu = f.read(50)
        print(f"   📖 Lu : '{contenu[:30]}...'")

    # Test avec exception
    print("\n   Test avec exception :")
    try:
        with GestionnaireFichierAvecLog("test_files/exemple_simple.txt") as f:
            contenu = f.read(10)
            # Simuler une erreur
            raise ValueError("Erreur simulée")
    except ValueError as e:
        print(f"   🚨 Exception capturée : {e}")


demo_context_manager_personnalise()

print("\n" + "=" * 50)
print("7. PARSING DE FORMATS COURANTS")
print("=" * 50)

print("\n📊 FICHIERS CSV")
print("-" * 15)


def lire_csv_manuel():
    """Lecture manuelle d'un fichier CSV"""

    print("📊 Lecture manuelle de CSV :")

    try:
        with open("test_files/donnees.csv", "r", encoding="utf-8") as f:
            # Lire l'en-tête
            header = f.readline().strip().split(',')
            print(f"   En-tête : {header}")

            # Lire les données
            donnees = []
            # Commencer à 2 (après header)
            for numero_ligne, ligne in enumerate(f, 2):
                if ligne.strip():  # Ignorer les lignes vides
                    valeurs = ligne.strip().split(',')
                    if len(valeurs) == len(header):
                        enregistrement = dict(zip(header, valeurs))
                        donnees.append(enregistrement)
                        print(f"   Ligne {numero_ligne} : {enregistrement}")
                    else:
                        print(
                            f"   ⚠️ Ligne {numero_ligne} mal formée : {valeurs}")

            print(f"   Total : {len(donnees)} enregistrements")
            return donnees

    except Exception as e:
        print(f"   ❌ Erreur : {e}")
        return []


donnees_csv = lire_csv_manuel()

print("\n📊 AVEC MODULE CSV")
print("-" * 19)


def lire_csv_module():
    """Lecture avec le module csv (recommandé)"""
    import csv

    print("📊 Lecture avec module csv :")

    try:
        with open("test_files/donnees.csv", "r", encoding="utf-8", newline='') as f:
            lecteur = csv.DictReader(f)

            print(f"   Colonnes : {lecteur.fieldnames}")

            donnees = []
            for numero_ligne, enregistrement in enumerate(lecteur, 2):
                donnees.append(enregistrement)
                print(f"   Ligne {numero_ligne} : {enregistrement}")

            print(f"   Total : {len(donnees)} enregistrements")
            return donnees

    except Exception as e:
        print(f"   ❌ Erreur : {e}")
        return []


donnees_csv_module = lire_csv_module()

print("\n🔧 JSON")
print("--------")


def lire_json():
    """Lecture d'un fichier JSON"""
    import json

    print("🔧 Lecture de fichier JSON :")

    try:
        with open("test_files/configuration.json", "r", encoding="utf-8") as f:
            # Lecture complète
            config = json.load(f)

            print(f"   Type : {type(config)}")
            print(f"   Clés principales : {list(config.keys())}")

            # Affichage structuré
            for cle, valeur in config.items():
                if isinstance(valeur, dict):
                    print(f"   {cle} : {dict} avec {len(valeur)} éléments")
                    for sous_cle, sous_valeur in valeur.items():
                        print(f"      {sous_cle} : {sous_valeur}")
                elif isinstance(valeur, list):
                    print(
                        f"   {cle} : {list} avec {len(valeur)} éléments : {valeur}")
                else:
                    print(f"   {cle} : {valeur}")

            return config

    except json.JSONDecodeError as e:
        print(f"   ❌ Erreur JSON : {e}")
        return None
    except Exception as e:
        print(f"   ❌ Erreur : {e}")
        return None


config_json = lire_json()

print("\n📝 FICHIERS DE LOG")
print("-" * 18)


def analyser_logs():
    """Analyse d'un fichier de log"""
    import re
    from datetime import datetime

    print("📝 Analyse de fichier de log :")

    try:
        # Pattern pour parser les logs
        pattern_log = re.compile(
            r'(?P<date>\d{4}-\d{2}-\d{2})\s+'
            r'(?P<heure>\d{2}:\d{2}:\d{2})\s+'
            r'(?P<niveau>\w+)\s+'
            r'(?P<message>.*)'
        )

        statistiques = {'INFO': 0, 'DEBUG': 0, 'WARNING': 0, 'ERROR': 0}
        entrees_log = []

        with open("test_files/application.log", "r", encoding="utf-8") as f:
            for numero_ligne, ligne in enumerate(f, 1):
                ligne = ligne.strip()
                if ligne:
                    match = pattern_log.match(ligne)
                    if match:
                        donnees = match.groupdict()

                        # Parser la date/heure
                        timestamp_str = f"{donnees['date']} {donnees['heure']}"
                        timestamp = datetime.strptime(
                            timestamp_str, "%Y-%m-%d %H:%M:%S")

                        entree = {
                            'ligne': numero_ligne,
                            'timestamp': timestamp,
                            'niveau': donnees['niveau'],
                            'message': donnees['message']
                        }

                        entrees_log.append(entree)
                        statistiques[donnees['niveau']] += 1

                        print(
                            f"   [{numero_ligne:2d}] {donnees['niveau']:<7} : {donnees['message']}")
                    else:
                        print(
                            f"   [{numero_ligne:2d}] ❌ Format non reconnu : {ligne}")

        print(f"\n   Statistiques :")
        for niveau, count in statistiques.items():
            if count > 0:
                print(f"      {niveau:<7} : {count}")

        return entrees_log

    except Exception as e:
        print(f"   ❌ Erreur : {e}")
        return []


logs_analyses = analyser_logs()

print("\n" + "=" * 50)
print("8. GESTION D'ERREURS AVANCÉE")
print("=" * 50)

print("\n🚨 ERREURS COURANTES")
print("-" * 20)


def demo_erreurs_fichiers():
    """Démonstration des erreurs courantes avec les fichiers"""

    erreurs_courantes = [
        ("FileNotFoundError", "test_files/inexistant.txt", "r"),
        # x échoue si existe
        ("PermissionError", "test_files/exemple_simple.txt", "x"),
        ("IsADirectoryError", "test_files", "r"),  # Essayer d'ouvrir un dossier
        ("UnicodeDecodeError", "test_files/test_utf_16.txt", "r", "ascii"),
    ]

    print("🚨 Tests d'erreurs courantes :")

    for erreur_attendue, fichier, mode, *args in erreurs_courantes:
        encoding = args[0] if args else "utf-8"

        try:
            print(f"\n   Test {erreur_attendue} :")
            print(f"      Fichier : {fichier}")
            print(f"      Mode : {mode}, Encoding : {encoding}")

            with open(fichier, mode, encoding=encoding) as f:
                contenu = f.read(10)
                print(f"      ✅ Succès inattendu : '{contenu}'")

        except FileNotFoundError as e:
            print(f"      ❌ FileNotFoundError : {e}")
        except PermissionError as e:
            print(f"      ❌ PermissionError : {e}")
        except IsADirectoryError as e:
            print(f"      ❌ IsADirectoryError : {e}")
        except UnicodeDecodeError as e:
            print(f"      ❌ UnicodeDecodeError : {e}")
        except Exception as e:
            print(f"      ❌ Autre erreur ({type(e).__name__}) : {e}")


demo_erreurs_fichiers()

print("\n🛡️ GESTION ROBUSTE")
print("-" * 19)


def lecteur_fichier_robuste(nom_fichier, encodages_test=None, max_taille=10*1024*1024):
    """Lecteur de fichier robuste avec fallbacks"""

    if encodages_test is None:
        encodages_test = ['utf-8', 'cp1252', 'iso-8859-1']

    print(f"🛡️ Lecture robuste de '{nom_fichier}' :")

    # Vérifications préliminaires
    try:
        if not os.path.exists(nom_fichier):
            raise FileNotFoundError(f"Fichier non trouvé : {nom_fichier}")

        if os.path.isdir(nom_fichier):
            raise IsADirectoryError(f"'{nom_fichier}' est un répertoire")

        taille = os.path.getsize(nom_fichier)
        print(f"   📊 Taille : {taille:,} octets")

        if taille > max_taille:
            raise ValueError(
                f"Fichier too volumineux : {taille:,} > {max_taille:,} octets")

        if taille == 0:
            print("   ⚠️ Fichier vide")
            return ""

    except Exception as e:
        print(f"   ❌ Vérification échouée : {e}")
        return None

    # Tentatives de lecture avec différents encodages
    for encodage in encodages_test:
        try:
            print(f"   🔍 Tentative avec encodage '{encodage}'...")

            with open(nom_fichier, "r", encoding=encodage) as f:
                contenu = f.read()

            print(f"   ✅ Succès avec '{encodage}' : {len(contenu)} caractères")
            return contenu

        except UnicodeDecodeError as e:
            print(f"   ❌ Échec '{encodage}' : {e}")
            continue
        except Exception as e:
            print(f"   ❌ Erreur '{encodage}' : {e}")
            break

    # Fallback : lecture binaire
    try:
        print("   🔄 Fallback : lecture binaire...")
        with open(nom_fichier, "rb") as f:
            contenu_binaire = f.read()

        print(f"   ✅ Lecture binaire réussie : {len(contenu_binaire)} octets")
        return contenu_binaire

    except Exception as e:
        print(f"   ❌ Échec lecture binaire : {e}")
        return None


# Tests de lecture robuste
print("🛡️ Tests de lecture robuste :")
lecteur_fichier_robuste("test_files/exemple_simple.txt")
print()
lecteur_fichier_robuste("test_files/inexistant.txt")
print()
lecteur_fichier_robuste("test_files")  # Répertoire

print("\n🔄 RETRY ET TIMEOUT")
print("-" * 20)


def lire_fichier_avec_retry(nom_fichier, max_tentatives=3, delai=0.1):
    """Lecture avec système de retry"""
    import time

    print(f"🔄 Lecture avec retry de '{nom_fichier}' :")

    for tentative in range(1, max_tentatives + 1):
        try:
            print(f"   Tentative {tentative}/{max_tentatives}")

            # Simuler des conditions instables
            if tentative < 2:  # Première tentative échoue (simulation)
                # Ici on pourrait avoir des erreurs réseau, verrous, etc.
                pass

            with open(nom_fichier, "r", encoding="utf-8") as f:
                contenu = f.read()

            print(f"   ✅ Succès à la tentative {tentative}")
            return contenu

        except Exception as e:
            print(f"   ❌ Tentative {tentative} échouée : {e}")

            if tentative == max_tentatives:
                print(
                    f"   💥 Échec définitif après {max_tentatives} tentatives")
                raise

            print(f"   ⏳ Attente de {delai}s...")
            time.sleep(delai)
            delai *= 2  # Backoff exponentiel


# Test du retry (succès)
try:
    contenu = lire_fichier_avec_retry("test_files/exemple_simple.txt")
    print(f"   📝 Contenu récupéré : {len(contenu)} caractères\n")
except Exception as e:
    print(f"   ❌ Échec final : {e}\n")

print("\n" + "=" * 50)
print("9. OPTIMISATION ET PERFORMANCE")
print("=" * 50)

print("\n⚡ BUFFERING")
print("-" * 11)


def demo_buffering():
    """Démonstration de l'impact du buffering"""
    import time

    print("⚡ Impact du buffering sur les performances :")

    # Créer un fichier de test plus volumineux
    nom_fichier = "test_files/gros_fichier_perf.txt"
    taille_cible = 50000  # 50k lignes

    print(f"   Création d'un fichier de {taille_cible} lignes...")
    with open(nom_fichier, "w", encoding="utf-8") as f:
        for i in range(taille_cible):
            f.write(
                f"Ligne {i:05d} : Contenu de test pour mesurer les performances de lecture\n")

    # Test avec différentes tailles de buffer
    buffers_test = [
        (-1, "Par défaut"),
        (0, "Non bufferisé"),
        (1024, "1 KB"),
        (8192, "8 KB"),
        (65536, "64 KB"),
    ]

    for taille_buffer, description in buffers_test:
        try:
            start_time = time.time()
            lignes_lues = 0

            with open(nom_fichier, "r", encoding="utf-8", buffering=taille_buffer) as f:
                for ligne in f:
                    lignes_lues += 1

            duree = time.time() - start_time
            print(
                f"   Buffer{taille_buffer:>6} ({description:<12}) : {duree:.3f}s ({lignes_lues} lignes)")

        except Exception as e:
            print(f"   Buffer{taille_buffer:>6} : ❌ {e}")


demo_buffering()

print("\n🔍 LECTURE SÉLECTIVE")
print("-" * 21)


def demo_lecture_selective():
    """Techniques de lecture sélective pour gros fichiers"""

    print("🔍 Techniques de lecture sélective :")

    nom_fichier = "test_files/gros_fichier_perf.txt"

    # 1. Lire seulement les N premières lignes
    print("   1. Premières lignes seulement :")
    with open(nom_fichier, "r", encoding="utf-8") as f:
        for i, ligne in enumerate(f):
            if i >= 5:  # Arrêter après 5 lignes
                break
            print(f"      [{i+1}] {ligne.strip()}")

    # 2. Lire une ligne sur N
    print("\n   2. Une ligne sur 10000 :")
    with open(nom_fichier, "r", encoding="utf-8") as f:
        for i, ligne in enumerate(f):
            if i % 10000 == 0:  # Une ligne sur 10000
                print(f"      [{i+1}] {ligne.strip()}")
                if i > 40000:  # Limiter pour la démo
                    break

    # 3. Chercher des lignes spécifiques
    print("\n   3. Lignes contenant '00000' :")
    with open(nom_fichier, "r", encoding="utf-8") as f:
        for i, ligne in enumerate(f):
            if '00000' in ligne:
                print(f"      [{i+1}] {ligne.strip()}")

    # 4. Lire à partir d'une position
    print("\n   4. Lecture à partir du milieu du fichier :")
    with open(nom_fichier, "r", encoding="utf-8") as f:
        # Aller au milieu approximatif
        f.seek(0, 2)  # Fin du fichier
        taille = f.tell()
        f.seek(taille // 2)  # Milieu

        # Aller au début de la ligne suivante
        f.readline()  # Ignorer la ligne potentiellement coupée

        # Lire quelques lignes
        for i in range(3):
            ligne = f.readline()
            if ligne:
                print(f"      [milieu+{i+1}] {ligne.strip()}")


demo_lecture_selective()

print("\n💾 MEMORY MAPPING")
print("-" * 17)


def demo_memory_mapping():
    """Démonstration du memory mapping pour gros fichiers"""
    import mmap

    print("💾 Memory mapping pour gros fichiers :")

    nom_fichier = "test_files/gros_fichier_perf.txt"

    try:
        with open(nom_fichier, "r", encoding="utf-8") as f:
            # Memory mapping en mode lecture
            with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
                print(f"   📊 Taille mappée : {len(mm):,} octets")

                # Lire les premiers caractères
                debut = mm[:100].decode('utf-8')
                print(f"   📖 Début : '{debut.replace(chr(10), '\\n')}'")

                # Chercher dans le fichier mappé
                position = mm.find(b'30000')
                if position != -1:
                    print(f"   🔍 '30000' trouvé à la position {position}")

                    # Lire autour de cette position
                    debut_ligne = mm.rfind(b'\n', 0, position) + 1
                    fin_ligne = mm.find(b'\n', position)
                    ligne = mm[debut_ligne:fin_ligne].decode('utf-8')
                    print(f"   📝 Ligne trouvée : '{ligne}'")

                # Statistiques
                nb_lignes = mm.count(b'\n')
                print(f"   📊 Nombre de lignes : {nb_lignes:,}")

    except Exception as e:
        print(f"   ❌ Erreur memory mapping : {e}")


demo_memory_mapping()

print("\n" + "=" * 50)
print("10. EXERCICES PRATIQUES")
print("=" * 50)

print("""
💪 EXERCICES À IMPLÉMENTER :

🎯 Exercice 1 : Analyseur de logs web
Créez un analyseur pour des logs Apache/Nginx :
• Parsing des lignes avec regex
• Extraction IP, timestamp, code de réponse, taille
• Statistiques par heure/jour
• Top des pages visitées
• Détection d'attaques (404 répétés, etc.)

📊 Exercice 2 : Convertisseur de formats
Créez un convertisseur CSV/JSON/XML :
• Détection automatique du format source
• Validation de structure
• Conversion avec préservation des types
• Gestion des erreurs par ligne
• Progress bar pour gros fichiers

🔍 Exercice 3 : Moniteur de fichiers
Créez un moniteur de fichiers en temps réel :
• Watch de répertoires avec watchdog
• Lecture incrémentale (tail -f like)
• Filtrage par patterns
• Alertes sur conditions
• Rotation de logs automatique

📋 Exercice 4 : Gestionnaire de configuration
Créez un système de configuration multi-format :
• Support JSON, YAML, INI, TOML
• Validation avec schémas
• Merge de configurations
• Variables d'environnement
• Hot-reload des changements

🎮 Exercice 5 : Parser de données scientifiques
Créez un parser pour données expérimentales :
• Formats binaires et texte
• Métadonnées et payload
• Validation d'intégrité
• Export vers différents formats
• Visualisation des données
""")

print("\n" + "=" * 50)
print("11. RÉSUMÉ FINAL")
print("=" * 50)

print("""
🎯 POINTS CLÉS À RETENIR :

1. 📂 OUVERTURE DE FICHIERS :
   • open(file, mode, encoding) : fonction de base
   • Modes : 'r' (lecture), 'w' (écriture), 'a' (ajout)
   • Toujours spécifier encoding='utf-8'
   • Context managers (with) obligatoires

2. 📖 MÉTHODES DE LECTURE :
   • read() : contenu complet
   • read(size) : lecture par blocs
   • readline() : ligne par ligne
   • readlines() : toutes les lignes en liste
   • Itération directe : for ligne in f (recommandé)

3. 🎯 GESTION DE POSITION :
   • tell() : position courante
   • seek(pos) : aller à une position
   • seek(offset, whence) : relatif (0=début, 1=courant, 2=fin)
   • Position en octets, pas en caractères !

4. 🌍 ENCODAGE :
   • UTF-8 : recommandé pour tous les nouveaux fichiers
   • Erreurs d'encodage : strict, ignore, replace
   • Détection : tester plusieurs encodages
   • Binaire vs texte : modes 'b' vs 't'

5. 🔒 SÉCURITÉ ET ROBUSTESSE :
   • With statements pour cleanup automatique
   • Gestion d'erreurs spécifiques
   • Validation de taille et existence
   • Retry avec backoff pour instabilités

💡 BONNES PRATIQUES :
✅ Toujours utiliser with pour ouvrir des fichiers
✅ Spécifier l'encodage explicitement
✅ Gérer les erreurs spécifiques (FileNotFound, etc.)
✅ Valider la taille pour éviter les OOM
✅ Fermer les fichiers même en cas d'erreur
✅ Préférer l'itération à readlines() pour gros fichiers

🚨 ERREURS COURANTES :
❌ Oublier de fermer les fichiers
❌ Ignorer l'encodage (problèmes avec caractères spéciaux)
❌ Charger de gros fichiers entièrement en mémoire
❌ Ne pas gérer les erreurs d'ouverture
❌ Utiliser seek() incorrectement en mode texte
❌ Mélanger modes binaire et texte

⚡ OPTIMISATIONS :
• Buffering approprié pour les performances
• Lecture sélective pour gros fichiers
• Memory mapping pour accès aléatoire
• Streaming pour traitement en pipeline
• Parallélisation pour traitement multiple

🔧 FORMATS SPÉCIALISÉS :
• CSV : module csv pour parsing robuste
• JSON : module json pour sérialisation
• XML : lxml ou xml.etree pour parsing
• Binaires : struct pour décomposition
• Logs : regex pour extraction de données

🎯 PATTERNS AVANCÉS :
• Context managers personnalisés
• Retry automatique avec backoff
• Progress tracking pour gros fichiers
• Validation en streaming
• Conversion de formats à la volée

🔍 DEBUGGING :
• Vérifier l'encodage avec hexdump
• Tester avec petits échantillons
• Logging des erreurs de lecture
• Validation des assumptions sur le format
• Tests avec fichiers corrompus

🎉 Félicitations ! Lecture de fichiers maîtrisée !
💡 Prochaine étape : Écriture de fichiers !
📚 Lecture maîtrisée, écrivez maintenant !
""")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE - LECTURE DE FICHIERS MAÎTRISÉE !")
print("=" * 70)
