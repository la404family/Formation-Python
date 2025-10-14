#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
======================================================================
LECTURE DE FICHIERS EN PYTHON - GUIDE COMPLET
======================================================================

🎯 Ce fichier couvre la lecture de fichiers en détail :
   • open, read, readline, readlines
   • Modes d'ouverture et encodage
   • Gestion des erreurs de fichiers
   • Lecture de différents formats
   • Bonnes pratiques de gestion de fichiers

📚 Concepts abordés :
   • Fonction open() et ses paramètres
   • Méthodes de lecture (read, readline, readlines)
   • Context managers avec 'with'
   • Encodage des caractères
   • Position dans le fichier (seek, tell)

💡 Objectif : Maîtriser la lecture de tous types de fichiers
"""

import os
import json
import csv
from pathlib import Path

print("=" * 70)
print("LECTURE DE FICHIERS EN PYTHON - GUIDE COMPLET")
print("=" * 70)

print("\n" + "=" * 50)
print("1. MÉTHODES DE LECTURE DE BASE")
print("=" * 50)

print("\n📖 FONCTION OPEN ET MÉTHODES READ")
print("-" * 33)


def demo_lecture_base():
    """Démonstration des méthodes de lecture de base"""

    print("📖 Méthodes de lecture de base :")

    # Créer un fichier de test
    contenu_test = """Première ligne du fichier
Deuxième ligne avec des accents : café, naïve, château
Troisième ligne avec des chiffres : 123, 456.789
Quatrième ligne finale."""

    with open("test_lecture.txt", "w", encoding="utf-8") as f:
        f.write(contenu_test)

    print("\n   1️⃣ Lecture complète avec read() :")

    # Méthode 1 : read() - tout le fichier
    with open("test_lecture.txt", "r", encoding="utf-8") as fichier:
        contenu_complet = fichier.read()
        print(f"      Contenu complet ({len(contenu_complet)} caractères) :")
        print(f"      {repr(contenu_complet)}")

    print("\n   2️⃣ Lecture par blocs avec read(n) :")

    # Méthode 2 : read(n) - n caractères
    with open("test_lecture.txt", "r", encoding="utf-8") as fichier:
        bloc1 = fichier.read(20)  # 20 premiers caractères
        bloc2 = fichier.read(20)  # 20 suivants
        reste = fichier.read()    # Le reste

        print(f"      Bloc 1 (20 car.) : {repr(bloc1)}")
        print(f"      Bloc 2 (20 car.) : {repr(bloc2)}")
        print(f"      Reste ({len(reste)} car.) : {repr(reste)}")

    print("\n   3️⃣ Lecture ligne par ligne avec readline() :")

    # Méthode 3 : readline() - une ligne à la fois
    with open("test_lecture.txt", "r", encoding="utf-8") as fichier:
        ligne_num = 1
        while True:
            ligne = fichier.readline()
            if not ligne:  # Fin de fichier
                break
            print(f"      Ligne {ligne_num} : {repr(ligne)}")
            ligne_num += 1

    print("\n   4️⃣ Lecture toutes lignes avec readlines() :")

    # Méthode 4 : readlines() - toutes les lignes en liste
    with open("test_lecture.txt", "r", encoding="utf-8") as fichier:
        toutes_lignes = fichier.readlines()
        print(f"      Nombre de lignes : {len(toutes_lignes)}")
        for i, ligne in enumerate(toutes_lignes, 1):
            print(f"      Ligne {i} : {repr(ligne)}")

    print("\n   5️⃣ Itération directe sur le fichier :")

    # Méthode 5 : Itération directe (recommandée)
    with open("test_lecture.txt", "r", encoding="utf-8") as fichier:
        for i, ligne in enumerate(fichier, 1):
            ligne_propre = ligne.strip()  # Enlever \n
            print(f"      Ligne {i} : '{ligne_propre}'")

    # Nettoyage
    os.remove("test_lecture.txt")


demo_lecture_base()

print("\n🔧 GESTION DE POSITION ET ENCODAGE")
print("-" * 35)


def demo_position_encodage():
    """Démonstration de la gestion de position et encodage"""

    print("🔧 Position dans le fichier et encodage :")

    # Créer un fichier avec différents encodages
    texte_unicode = "Héllo Wørld! 🐍 Pythön avec émojis: 😊🚀💻"

    with open("test_unicode.txt", "w", encoding="utf-8") as f:
        f.write(texte_unicode)

    print("\n   1️⃣ Gestion de la position avec tell() et seek() :")

    with open("test_unicode.txt", "r", encoding="utf-8") as fichier:
        # Position initiale
        pos_debut = fichier.tell()
        print(f"      Position initiale : {pos_debut}")

        # Lire quelques caractères
        premiers_chars = fichier.read(10)
        pos_apres_lecture = fichier.tell()
        print(
            f"      Après lecture de 10 chars : position {pos_apres_lecture}")
        print(f"      Caractères lus : '{premiers_chars}'")

        # Revenir au début
        fichier.seek(0)
        pos_retour = fichier.tell()
        print(f"      Après seek(0) : position {pos_retour}")

        # Aller à une position spécifique
        fichier.seek(15)
        chars_depuis_pos15 = fichier.read(10)
        print(f"      Depuis position 15 : '{chars_depuis_pos15}'")

        # Aller à la fin
        fichier.seek(0, 2)  # 2 = fin de fichier
        pos_fin = fichier.tell()
        print(f"      Position en fin de fichier : {pos_fin}")

    print("\n   2️⃣ Test de différents encodages :")

    # Créer fichiers avec différents encodages
    encodages_test = [
        ("utf-8", "UTF-8 : café, naïve, 🐍"),
        ("latin-1", "Latin-1 : café, naïve"),
        ("ascii", "ASCII : hello world"),
    ]

    # Créer les fichiers
    for encoding, texte in encodages_test:
        try:
            with open(f"test_{encoding}.txt", "w", encoding=encoding) as f:
                f.write(texte)
            print(f"      ✅ Fichier {encoding} créé : '{texte}'")
        except UnicodeEncodeError as e:
            print(f"      ❌ Erreur encodage {encoding} : {e}")

    # Lire avec bon encodage
    print("\n   3️⃣ Lecture avec bon encodage :")
    for encoding, _ in encodages_test:
        filename = f"test_{encoding}.txt"
        if os.path.exists(filename):
            try:
                with open(filename, "r", encoding=encoding) as f:
                    contenu = f.read()
                print(f"      ✅ {encoding} : '{contenu}'")
            except Exception as e:
                print(f"      ❌ Erreur lecture {encoding} : {e}")

    # Lire avec mauvais encodage
    print("\n   4️⃣ Erreurs de mauvais encodage :")
    if os.path.exists("test_utf-8.txt"):
        try:
            with open("test_utf-8.txt", "r", encoding="ascii") as f:
                contenu = f.read()
            print(f"      Lecture ASCII d'un fichier UTF-8 : '{contenu}'")
        except UnicodeDecodeError as e:
            print(f"      ❌ Erreur attendue : {e}")

    # Nettoyage
    for encoding, _ in encodages_test:
        filename = f"test_{encoding}.txt"
        if os.path.exists(filename):
            os.remove(filename)


demo_position_encodage()

print("\n" + "=" * 50)
print("2. GESTION D'ERREURS DE FICHIERS")
print("=" * 50)

print("\n🚨 ERREURS COURANTES DE FICHIERS")
print("-" * 31)


def demo_erreurs_fichiers():
    """Démonstration de la gestion d'erreurs de fichiers"""

    print("🚨 Gestion des erreurs de fichiers :")

    def lire_fichier_robuste(nom_fichier, encoding="utf-8"):
        """Lecture robuste avec gestion d'erreurs"""
        print(f"\n      🔍 Tentative de lecture : '{nom_fichier}'")

        try:
            with open(nom_fichier, "r", encoding=encoding) as fichier:
                contenu = fichier.read()
                print(f"      ✅ Lecture réussie ({len(contenu)} caractères)")
                return contenu

        except FileNotFoundError:
            print(f"      ❌ Fichier non trouvé : '{nom_fichier}'")
            return None
        except PermissionError:
            print(f"      ❌ Permissions insuffisantes pour : '{nom_fichier}'")
            return None
        except UnicodeDecodeError as e:
            print(f"      ❌ Erreur d'encodage : {e}")
            print(f"         Essayez un autre encodage que '{encoding}'")
            return None
        except IsADirectoryError:
            print(f"      ❌ '{nom_fichier}' est un répertoire, pas un fichier")
            return None
        except OSError as e:
            print(f"      ❌ Erreur système : {e}")
            return None
        except Exception as e:
            print(f"      ❌ Erreur inattendue : {type(e).__name__}: {e}")
            return None

    # Tests d'erreurs de fichiers
    print("\n   Tests de gestion d'erreurs :")

    # Créer un fichier de test valide
    with open("fichier_valide.txt", "w", encoding="utf-8") as f:
        f.write("Contenu du fichier valide")

    # Créer un répertoire pour test
    os.makedirs("repertoire_test", exist_ok=True)

    fichiers_test = [
        ("fichier_valide.txt", "utf-8", "Fichier existant"),
        ("fichier_inexistant.txt", "utf-8", "Fichier inexistant"),
        ("repertoire_test", "utf-8", "Répertoire au lieu de fichier"),
    ]

    # Test fichier avec mauvais encodage
    with open("fichier_latin1.txt", "w", encoding="latin-1") as f:
        f.write("Texte avec caractères spéciaux : café")
    fichiers_test.append(("fichier_latin1.txt", "ascii", "Mauvais encodage"))

    for nom_fichier, encoding, description in fichiers_test:
        print(f"\n   📋 Test : {description}")
        contenu = lire_fichier_robuste(nom_fichier, encoding)
        if contenu:
            print(f"      📄 Aperçu : '{contenu[:50]}...' " if len(
                contenu) > 50 else f"      📄 Contenu : '{contenu}'")

    # Nettoyage
    for fichier in ["fichier_valide.txt", "fichier_latin1.txt"]:
        if os.path.exists(fichier):
            os.remove(fichier)

    if os.path.exists("repertoire_test"):
        os.rmdir("repertoire_test")


demo_erreurs_fichiers()

print("\n🛡️ LECTURE SÉCURISÉE")
print("-" * 19)


def demo_lecture_securisee():
    """Démonstration de lecture sécurisée"""

    print("🛡️ Techniques de lecture sécurisée :")

    def lire_avec_limite_taille(nom_fichier, taille_max=1024, encoding="utf-8"):
        """Lire un fichier avec limite de taille"""
        try:
            # Vérifier la taille avant de lire
            taille_fichier = os.path.getsize(nom_fichier)

            if taille_fichier > taille_max:
                print(
                    f"      ⚠️ Fichier trop volumineux : {taille_fichier} > {taille_max} octets")
                return None

            with open(nom_fichier, "r", encoding=encoding) as fichier:
                contenu = fichier.read()
                print(f"      ✅ Fichier lu : {taille_fichier} octets")
                return contenu

        except Exception as e:
            print(f"      ❌ Erreur : {e}")
            return None

    def lire_par_chunks(nom_fichier, taille_chunk=1024, encoding="utf-8"):
        """Lire un fichier par chunks pour économiser la mémoire"""
        try:
            contenu_total = ""
            chunks_lus = 0

            with open(nom_fichier, "r", encoding=encoding) as fichier:
                while True:
                    chunk = fichier.read(taille_chunk)
                    if not chunk:
                        break

                    contenu_total += chunk
                    chunks_lus += 1

                    if chunks_lus > 10:  # Limite de sécurité
                        print(f"      ⚠️ Trop de chunks, arrêt de la lecture")
                        break

            print(
                f"      ✅ Lecture par chunks : {chunks_lus} chunks de {taille_chunk} caractères max")
            return contenu_total

        except Exception as e:
            print(f"      ❌ Erreur : {e}")
            return None

    def lire_avec_timeout_simule(nom_fichier, encoding="utf-8"):
        """Simulation de lecture avec timeout"""
        import time

        try:
            debut = time.time()

            with open(nom_fichier, "r", encoding=encoding) as fichier:
                lignes = []
                for ligne in fichier:
                    lignes.append(ligne.strip())

                    # Simulation de vérification de timeout
                    if time.time() - debut > 0.1:  # 100ms max
                        print(
                            f"      ⏰ Timeout simulé après {len(lignes)} lignes")
                        break

            contenu = "\n".join(lignes)
            print(f"      ✅ Lecture avec timeout : {len(lignes)} lignes")
            return contenu

        except Exception as e:
            print(f"      ❌ Erreur : {e}")
            return None

    # Créer fichiers de test
    print("\n   Création de fichiers de test :")

    # Petit fichier
    with open("petit_fichier.txt", "w", encoding="utf-8") as f:
        f.write("Petit contenu\nsur plusieurs\nlignes")

    # Fichier plus volumineux
    with open("gros_fichier.txt", "w", encoding="utf-8") as f:
        for i in range(100):
            f.write(
                f"Ligne {i+1} avec du contenu répétitif pour tester la lecture\n")

    # Tests de lecture sécurisée
    print("\n   Tests de lecture sécurisée :")

    print("\n   1️⃣ Lecture avec limite de taille :")
    lire_avec_limite_taille("petit_fichier.txt", 1000)
    lire_avec_limite_taille("gros_fichier.txt", 1000)

    print("\n   2️⃣ Lecture par chunks :")
    lire_par_chunks("petit_fichier.txt", 10)
    lire_par_chunks("gros_fichier.txt", 100)

    print("\n   3️⃣ Lecture avec timeout simulé :")
    lire_avec_timeout_simule("petit_fichier.txt")
    lire_avec_timeout_simule("gros_fichier.txt")

    # Nettoyage
    for fichier in ["petit_fichier.txt", "gros_fichier.txt"]:
        if os.path.exists(fichier):
            os.remove(fichier)


demo_lecture_securisee()

print("\n" + "=" * 50)
print("3. LECTURE DE FORMATS SPÉCIFIQUES")
print("=" * 50)

print("\n📄 LECTURE DE FICHIERS TEXTE AVANCÉE")
print("-" * 36)


def demo_lecture_formats():
    """Démonstration de lecture de différents formats"""

    print("📄 Lecture de formats spécifiques :")

    # 1. Fichier CSV
    print("\n   1️⃣ Lecture de fichier CSV :")

    donnees_csv = """nom,age,ville,salaire
Alice Martin,25,Paris,45000
Bob Durand,30,Lyon,50000
Charlie Petit,35,Marseille,48000
Diane Rouge,28,Toulouse,52000"""

    with open("donnees.csv", "w", encoding="utf-8") as f:
        f.write(donnees_csv)

    # Lecture manuelle du CSV
    def lire_csv_manuel(nom_fichier):
        """Lecture CSV manuelle"""
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            lignes = fichier.readlines()

            # En-têtes
            entetes = lignes[0].strip().split(",")
            print(f"      En-têtes : {entetes}")

            # Données
            donnees = []
            for ligne in lignes[1:]:
                valeurs = ligne.strip().split(",")
                personne = dict(zip(entetes, valeurs))
                donnees.append(personne)

            return donnees

    personnes = lire_csv_manuel("donnees.csv")
    for personne in personnes:
        print(f"      {personne}")

    # Lecture avec module csv
    print("\n      Avec le module csv :")
    with open("donnees.csv", "r", encoding="utf-8") as fichier:
        lecteur_csv = csv.DictReader(fichier)
        for ligne in lecteur_csv:
            print(f"      {dict(ligne)}")

    # 2. Fichier JSON
    print("\n   2️⃣ Lecture de fichier JSON :")

    donnees_json = {
        "utilisateurs": [
            {"nom": "Alice", "age": 25, "actif": True},
            {"nom": "Bob", "age": 30, "actif": False},
            {"nom": "Charlie", "age": 35, "actif": True}
        ],
        "configuration": {
            "debug": False,
            "version": "1.0.0"
        }
    }

    with open("donnees.json", "w", encoding="utf-8") as f:
        json.dump(donnees_json, f, indent=2, ensure_ascii=False)

    # Lecture du JSON
    with open("donnees.json", "r", encoding="utf-8") as fichier:
        donnees = json.load(fichier)
        print(f"      Utilisateurs : {len(donnees['utilisateurs'])}")
        for user in donnees["utilisateurs"]:
            statut = "actif" if user["actif"] else "inactif"
            print(f"      - {user['nom']} ({user['age']} ans) : {statut}")

        print(
            f"      Configuration : version {donnees['configuration']['version']}")

    # 3. Fichier de configuration
    print("\n   3️⃣ Lecture de fichier de configuration :")

    config_ini = """[DATABASE]
host = localhost
port = 5432
username = admin
password = secret123

[APPLICATION]
debug = true
max_connections = 100
timeout = 30

[LOGGING]
level = INFO
file = app.log"""

    with open("config.ini", "w", encoding="utf-8") as f:
        f.write(config_ini)

    def lire_config_ini(nom_fichier):
        """Lecture manuelle d'un fichier INI"""
        config = {}
        section_actuelle = None

        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            for ligne in fichier:
                ligne = ligne.strip()

                if not ligne or ligne.startswith("#"):
                    continue

                if ligne.startswith("[") and ligne.endswith("]"):
                    section_actuelle = ligne[1:-1]
                    config[section_actuelle] = {}
                elif "=" in ligne and section_actuelle:
                    cle, valeur = ligne.split("=", 1)
                    config[section_actuelle][cle.strip()] = valeur.strip()

        return config

    config = lire_config_ini("config.ini")
    for section, parametres in config.items():
        print(f"      [{section}]")
        for cle, valeur in parametres.items():
            print(f"        {cle} = {valeur}")

    # 4. Fichier de log
    print("\n   4️⃣ Lecture et analyse de fichier de log :")

    log_content = """2024-01-15 10:30:15 INFO Application démarrée
2024-01-15 10:30:16 INFO Connexion base de données établie
2024-01-15 10:31:20 WARNING Tentative de connexion échouée pour user 'test'
2024-01-15 10:32:45 ERROR Erreur de validation pour email 'invalid-email'
2024-01-15 10:35:12 INFO Utilisateur 'alice' connecté
2024-01-15 10:36:30 WARNING Mémoire faible : 85% utilisée
2024-01-15 10:40:15 ERROR Exception non gérée dans module payment
2024-01-15 10:45:22 INFO Sauvegarde automatique terminée"""

    with open("app.log", "w", encoding="utf-8") as f:
        f.write(log_content)

    def analyser_logs(nom_fichier):
        """Analyser un fichier de log"""
        compteurs = {"INFO": 0, "WARNING": 0, "ERROR": 0}
        erreurs = []

        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            for ligne in fichier:
                if "ERROR" in ligne:
                    compteurs["ERROR"] += 1
                    erreurs.append(ligne.strip())
                elif "WARNING" in ligne:
                    compteurs["WARNING"] += 1
                elif "INFO" in ligne:
                    compteurs["INFO"] += 1

        return compteurs, erreurs

    compteurs, erreurs = analyser_logs("app.log")
    print(f"      Statistiques des logs :")
    for niveau, count in compteurs.items():
        print(f"        {niveau}: {count}")

    print(f"      Erreurs détectées :")
    for erreur in erreurs:
        print(f"        - {erreur}")

    # Nettoyage
    for fichier in ["donnees.csv", "donnees.json", "config.ini", "app.log"]:
        if os.path.exists(fichier):
            os.remove(fichier)


demo_lecture_formats()

print("\n🗂️ LECTURE AVEC PATHLIB")
print("-" * 23)


def demo_pathlib():
    """Démonstration de lecture avec pathlib"""

    print("🗂️ Lecture moderne avec pathlib :")

    # Créer structure de répertoires et fichiers
    base_dir = Path("demo_pathlib")
    base_dir.mkdir(exist_ok=True)

    # Créer des fichiers dans différents répertoires
    (base_dir / "fichier1.txt").write_text("Contenu du fichier 1", encoding="utf-8")
    (base_dir / "fichier2.txt").write_text("Contenu du fichier 2", encoding="utf-8")

    sous_dir = base_dir / "sous_repertoire"
    sous_dir.mkdir(exist_ok=True)
    (sous_dir / "fichier3.txt").write_text("Contenu du fichier 3", encoding="utf-8")

    print("\n   1️⃣ Lecture simple avec pathlib :")

    # Lecture directe
    for fichier in base_dir.glob("*.txt"):
        contenu = fichier.read_text(encoding="utf-8")
        print(f"      {fichier.name} : '{contenu}'")

    print("\n   2️⃣ Recherche récursive :")

    # Recherche récursive de tous les .txt
    for fichier in base_dir.rglob("*.txt"):
        contenu = fichier.read_text(encoding="utf-8")
        print(f"      {fichier.relative_to(base_dir)} : '{contenu}'")

    print("\n   3️⃣ Informations sur les fichiers :")

    for fichier in base_dir.rglob("*.txt"):
        stat = fichier.stat()
        print(f"      {fichier.name} :")
        print(f"        Taille : {stat.st_size} octets")
        print(f"        Modifié : {stat.st_mtime}")
        print(f"        Existe : {fichier.exists()}")
        print(f"        Est fichier : {fichier.is_file()}")

    print("\n   4️⃣ Lecture conditionnelle :")

    def lire_si_conditions(chemin, taille_max=100):
        """Lire seulement si les conditions sont remplies"""
        if not chemin.exists():
            print(f"      ❌ {chemin.name} n'existe pas")
            return None

        if not chemin.is_file():
            print(f"      ❌ {chemin.name} n'est pas un fichier")
            return None

        if chemin.stat().st_size > taille_max:
            print(f"      ⚠️ {chemin.name} trop volumineux")
            return None

        try:
            contenu = chemin.read_text(encoding="utf-8")
            print(f"      ✅ {chemin.name} lu avec succès")
            return contenu
        except Exception as e:
            print(f"      ❌ Erreur lecture {chemin.name} : {e}")
            return None

    for fichier in base_dir.rglob("*.txt"):
        contenu = lire_si_conditions(fichier, 50)
        if contenu:
            print(f"        Contenu : '{contenu}'")

    # Nettoyage
    import shutil
    if base_dir.exists():
        shutil.rmtree(base_dir)


demo_pathlib()

print("\n" + "=" * 50)
print("4. RÉSUMÉ FINAL")
print("=" * 50)

print("""
🎯 POINTS CLÉS À RETENIR :

1. 📖 MÉTHODES DE LECTURE :
   • read() : tout le fichier en mémoire
   • readline() : une ligne à la fois
   • readlines() : toutes les lignes en liste
   • Itération directe : for ligne in fichier

2. 🔧 GESTION DE POSITION :
   • tell() : obtenir position actuelle
   • seek(pos) : aller à une position
   • seek(0, 2) : aller à la fin
   • Position en octets, pas en caractères

3. 🚨 GESTION D'ERREURS :
   • FileNotFoundError : fichier inexistant
   • PermissionError : droits insuffisants
   • UnicodeDecodeError : problème d'encodage
   • IsADirectoryError : chemin vers répertoire

4. 🛡️ LECTURE SÉCURISÉE :
   • Vérifier taille avant lecture
   • Lire par chunks pour gros fichiers
   • Timeout pour éviter blocages
   • Validation d'encodage

5. 📄 FORMATS SPÉCIALISÉS :
   • CSV avec module csv
   • JSON avec module json
   • INI avec configparser
   • Pathlib pour chemins modernes

💡 BONNES PRATIQUES :
✅ Toujours utiliser with pour ouvrir fichiers
✅ Spécifier l'encodage explicitement
✅ Gérer les erreurs spécifiques
✅ Lire par chunks pour gros fichiers
✅ Valider existence avant lecture

🚨 À ÉVITER :
❌ Oublier de fermer les fichiers
❌ Charger énormes fichiers en mémoire
❌ Ignorer les erreurs d'encodage
❌ Hardcoder les chemins de fichiers
❌ Pas de gestion d'erreurs

⚡ OPTIMISATIONS :
• Lecture streaming pour gros volumes
• Cache pour fichiers fréquemment lus
• Index pour accès rapide
• Compression pour stockage
• Parallélisation pour multiple fichiers

🔧 OUTILS AVANCÉS :
• pathlib pour manipulation de chemins
• mmap pour fichiers très volumineux
• watchdog pour monitoring
• chardet pour détection d'encodage
• pandas pour fichiers structurés

🎉 Félicitations ! Lecture de fichiers maîtrisée !
💡 Prochaine étape : Écriture de fichiers !
📚 Fichiers lus, maintenant à écrire !
""")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE - LECTURE DE FICHIERS MAÎTRISÉE !")
print("=" * 70)
