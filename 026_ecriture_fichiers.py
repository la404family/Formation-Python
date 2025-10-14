#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
======================================================================
ÉCRITURE DE FICHIERS EN PYTHON - GUIDE COMPLET
======================================================================

🎯 Ce fichier couvre l'écriture de fichiers en détail :
   • Modes d'écriture et création
   • Méthodes write() et writelines()
   • Gestion du buffering et flush
   • Écriture sécurisée avec context managers
   • Formats texte et binaire
   • Génération de fichiers structurés

📚 Concepts abordés :
   • Création et écrasement de fichiers
   • Ajout et modification
   • Encodage et caractères spéciaux
   • Performance et optimisation
   • Validation et intégrité
   • Patterns d'écriture avancés

💡 Objectif : Maîtriser l'écriture efficace et sécurisée
"""

import os
print("=" * 70)
print("ÉCRITURE DE FICHIERS EN PYTHON - GUIDE COMPLET")
print("=" * 70)

print("\n" + "=" * 50)
print("1. FONDAMENTAUX DE L'ÉCRITURE")
print("=" * 50)

print("\n📝 QU'EST-CE QUE L'ÉCRITURE DE FICHIERS ?")
print("-" * 43)

print("""
🎯 DÉFINITION :
L'écriture de fichiers consiste à créer ou modifier des fichiers
en y stockant des données sous forme d'octets ou de caractères.

🔄 OPÉRATIONS D'ÉCRITURE :
• Création : créer un nouveau fichier
• Écrasement : remplacer complètement un fichier existant
• Ajout : ajouter du contenu à la fin d'un fichier
• Insertion : modifier une partie spécifique (complexe)
• Atomique : écriture sécurisée sans corruption

⚡ CONSIDÉRATIONS IMPORTANTES :
• Permissions du système de fichiers
• Espace disque disponible
• Encodage des caractères
• Performance et buffering
• Intégrité et sécurité des données
• Concurrent access et verrouillage
""")

print("\n🎭 MODES D'ÉCRITURE")
print("-" * 19)

modes_ecriture = [
    ("'w'", "Écriture seule", "Crée/écrase le fichier", "Pointeur au début"),
    ("'w+'", "Lecture/écriture", "Crée/écrase le fichier", "Pointeur au début"),
    ("'a'", "Ajout seul", "Crée si nécessaire", "Pointeur à la fin"),
    ("'a+'", "Lecture/ajout", "Crée si nécessaire", "Pointeur à la fin"),
    ("'x'", "Création exclusive", "Échoue si existe déjà", "Pointeur au début"),
    ("'x+'", "Création + lecture", "Échoue si existe déjà", "Pointeur au début"),
]

print("🎭 Modes d'écriture disponibles :")
for mode, nom, comportement, pointeur in modes_ecriture:
    print(f"   {mode:<6} : {nom:<18} | {comportement:<20} | {pointeur}")

print("\n🔤 MODIFICATEURS")
print("-" * 15)

print("""
🔤 MODIFICATEURS DE MODE :
• 'b' : Mode binaire (octets bruts)
• 't' : Mode texte (défaut, avec encodage)

📝 EXEMPLES COMPLETS :
• 'w'  = 'wt' : écriture texte avec écrasement
• 'wb'        : écriture binaire avec écrasement
• 'a'  = 'at' : ajout texte
• 'ab'        : ajout binaire
• 'x'  = 'xt' : création exclusive texte
• 'xb'        : création exclusive binaire

⚠️ ATTENTION :
Mode 'w' écrase complètement le fichier !
Mode 'x' échoue si le fichier existe déjà.
""")


# Créer le répertoire output s'il n'existe pas
os.makedirs("output_files", exist_ok=True)

print("\n📁 Répertoire 'output_files/' créé pour les tests")

print("\n" + "=" * 50)
print("2. MÉTHODES D'ÉCRITURE DE BASE")
print("=" * 50)

print("\n✍️ WRITE() - ÉCRITURE DE CHAÎNES")
print("-" * 32)


def demo_write_basique():
    """Démonstration de la méthode write()"""

    print("✍️ Écriture basique avec write() :")

    try:
        # Écriture simple
        with open("output_files/demo_write.txt", "w", encoding="utf-8") as f:
            # write() retourne le nombre de caractères écrits
            nb_chars = f.write("Bonjour le monde !\n")
            print(f"   Écrit : {nb_chars} caractères")

            # Écriture multiple
            lignes = [
                "Première ligne de texte\n",
                "Deuxième ligne avec des accents : éàùç\n",
                "Troisième ligne avec des chiffres : 12345\n",
                "Dernière ligne sans retour à la ligne"
            ]

            total_chars = 0
            for i, ligne in enumerate(lignes, 1):
                nb = f.write(ligne)
                total_chars += nb
                print(f"   Ligne {i} : {nb} caractères")

            print(f"   Total écrit : {total_chars} caractères")

        # Vérification
        with open("output_files/demo_write.txt", "r", encoding="utf-8") as f:
            contenu = f.read()
            print(f"\n   Vérification - Contenu écrit :")
            for i, ligne in enumerate(contenu.split('\n'), 1):
                print(f"      [{i}] : '{ligne}'")

    except Exception as e:
        print(f"   ❌ Erreur : {e}")


demo_write_basique()

print("\n📝 WRITELINES() - ÉCRITURE DE LISTES")
print("-" * 36)


def demo_writelines():
    """Démonstration de la méthode writelines()"""

    print("📝 Écriture de listes avec writelines() :")

    try:
        # Préparer des données
        donnees = [
            "# Configuration de l'application\n",
            "version = 1.0\n",
            "debug = True\n",
            "\n",  # Ligne vide
            "# Base de données\n",
            "db_host = localhost\n",
            "db_port = 5432\n",
            "db_name = myapp\n"
        ]

        # Écriture avec writelines()
        with open("output_files/config.txt", "w", encoding="utf-8") as f:
            f.writelines(donnees)
            print(f"   Écrit {len(donnees)} lignes avec writelines()")

        # Comparaison avec write() en boucle
        with open("output_files/config_alt.txt", "w", encoding="utf-8") as f:
            for ligne in donnees:
                f.write(ligne)
            print(f"   Écrit {len(donnees)} lignes avec write() en boucle")

        # Vérification de l'identité
        with open("output_files/config.txt", "r", encoding="utf-8") as f1:
            contenu1 = f1.read()
        with open("output_files/config_alt.txt", "r", encoding="utf-8") as f2:
            contenu2 = f2.read()

        print(f"   Contenus identiques : {contenu1 == contenu2}")
        print(f"   Taille : {len(contenu1)} caractères")

        # Attention : writelines() n'ajoute PAS de retours à la ligne !
        print("\n   ⚠️ Démonstration du piège writelines() :")
        donnees_sans_newline = ["ligne1", "ligne2", "ligne3"]

        with open("output_files/piege.txt", "w", encoding="utf-8") as f:
            f.writelines(donnees_sans_newline)

        with open("output_files/piege.txt", "r", encoding="utf-8") as f:
            contenu_piege = f.read()
            print(f"   Résultat : '{contenu_piege}'")  # Tout sur une ligne !

        # Correction
        with open("output_files/corrige.txt", "w", encoding="utf-8") as f:
            f.writelines(ligne + "\n" for ligne in donnees_sans_newline)

        with open("output_files/corrige.txt", "r", encoding="utf-8") as f:
            contenu_corrige = f.read()
            print(f"   Corrigé : '{contenu_corrige.replace(chr(10), '\\n')}'")

    except Exception as e:
        print(f"   ❌ Erreur : {e}")


demo_writelines()

print("\n🖨️ PRINT() VERS FICHIERS")
print("-" * 24)


def demo_print_vers_fichier():
    """Utilisation de print() pour écrire dans des fichiers"""

    print("🖨️ Écriture avec print() :")

    try:
        with open("output_files/demo_print.txt", "w", encoding="utf-8") as f:
            # print() vers fichier avec file=
            print("Utilisation de print() pour écrire", file=f)
            print("Deuxième ligne", file=f)
            print(file=f)  # Ligne vide

            # Avec des paramètres
            print("Valeurs :", 1, 2, 3, sep=", ", file=f)
            print("Sans retour à la ligne", end="", file=f)
            print(" (suite sur la même ligne)", file=f)

            # Formatage
            nom = "Alice"
            age = 25
            print(f"Utilisateur : {nom}, âge : {age}", file=f)

            # Avec des objets complexes
            donnees = {"nom": "Bob", "scores": [85, 92, 78]}
            print("Données :", donnees, file=f)

        # Vérification
        with open("output_files/demo_print.txt", "r", encoding="utf-8") as f:
            print("\n   📖 Contenu généré par print() :")
            for i, ligne in enumerate(f, 1):
                print(f"      [{i}] : {ligne.rstrip()}")

    except Exception as e:
        print(f"   ❌ Erreur : {e}")


demo_print_vers_fichier()

print("\n" + "=" * 50)
print("3. MODES D'ÉCRITURE AVANCÉS")
print("=" * 50)

print("\n🎯 MODE 'W' - ÉCRASEMENT")
print("-" * 24)


def demo_mode_w():
    """Démonstration du mode 'w' (écrasement)"""

    print("🎯 Mode 'w' - Écrasement complet :")

    try:
        # Créer un fichier initial
        with open("output_files/test_ecrasement.txt", "w", encoding="utf-8") as f:
            f.write("Contenu initial\nLigne 2\nLigne 3\n")

        print("   📝 Fichier initial créé")

        # Lire le contenu initial
        with open("output_files/test_ecrasement.txt", "r", encoding="utf-8") as f:
            contenu_initial = f.read()
            print(f"   📖 Contenu initial : {len(contenu_initial)} caractères")
            print(f"      '{contenu_initial.replace(chr(10), '\\n')}'")

        # Écraser avec du nouveau contenu (plus court)
        with open("output_files/test_ecrasement.txt", "w", encoding="utf-8") as f:
            f.write("Nouveau contenu")

        print("   🔄 Fichier écrasé")

        # Vérifier l'écrasement
        with open("output_files/test_ecrasement.txt", "r", encoding="utf-8") as f:
            contenu_final = f.read()
            print(f"   📖 Contenu final : {len(contenu_final)} caractères")
            print(f"      '{contenu_final}'")

        print("   ⚠️ L'ancien contenu a été complètement perdu !")

    except Exception as e:
        print(f"   ❌ Erreur : {e}")


demo_mode_w()

print("\n➕ MODE 'A' - AJOUT")
print("-" * 19)


def demo_mode_a():
    """Démonstration du mode 'a' (ajout)"""

    print("➕ Mode 'a' - Ajout en fin de fichier :")

    try:
        # Créer un fichier initial
        with open("output_files/test_ajout.txt", "w", encoding="utf-8") as f:
            f.write("Ligne initiale 1\nLigne initiale 2\n")

        print("   📝 Fichier initial créé")

        # Ajouter du contenu plusieurs fois
        for i in range(3):
            with open("output_files/test_ajout.txt", "a", encoding="utf-8") as f:
                f.write(f"Ligne ajoutée {i+1}\n")
            print(f"   ➕ Ajout {i+1} effectué")

        # Vérifier le résultat
        with open("output_files/test_ajout.txt", "r", encoding="utf-8") as f:
            lignes = f.readlines()
            print(f"   📖 Fichier final : {len(lignes)} lignes")
            for i, ligne in enumerate(lignes, 1):
                print(f"      [{i:2d}] : {ligne.rstrip()}")

        # Démontrer que le pointeur est toujours en fin
        print("\n   📍 Position du pointeur en mode 'a' :")
        with open("output_files/test_ajout.txt", "a", encoding="utf-8") as f:
            print(f"      Position à l'ouverture : {f.tell()}")
            f.write("Test position")
            print(f"      Position après écriture : {f.tell()}")

            # Même si on essaie de se déplacer...
            f.seek(0)
            print(f"      Position après seek(0) : {f.tell()}")
            f.write(" - Ceci sera ajouté à la fin !")
            print(f"      Position finale : {f.tell()}")

        # Vérifier que l'écriture s'est bien faite à la fin
        with open("output_files/test_ajout.txt", "r", encoding="utf-8") as f:
            contenu = f.read()
            print(f"   📖 Dernière ligne : '{contenu.splitlines()[-1]}'")

    except Exception as e:
        print(f"   ❌ Erreur : {e}")


demo_mode_a()

print("\n🚫 MODE 'X' - CRÉATION EXCLUSIVE")
print("-" * 32)


def demo_mode_x():
    """Démonstration du mode 'x' (création exclusive)"""

    print("🚫 Mode 'x' - Création exclusive :")

    # Nettoyer d'abord
    fichier_test = "output_files/test_exclusif.txt"
    if os.path.exists(fichier_test):
        os.remove(fichier_test)

    try:
        # Première création - doit réussir
        print("   1️⃣ Première tentative de création :")
        with open(fichier_test, "x", encoding="utf-8") as f:
            f.write("Fichier créé en mode exclusif\n")
            f.write("Création réussie !\n")
        print("      ✅ Création réussie")

        # Deuxième tentative - doit échouer
        print("   2️⃣ Deuxième tentative (fichier existe) :")
        try:
            with open(fichier_test, "x", encoding="utf-8") as f:
                f.write("Ceci ne devrait pas s'écrire")
            print("      ❌ Erreur : création réussie alors qu'elle devrait échouer")
        except FileExistsError as e:
            print(f"      ✅ Échec attendu : {e}")

        # Vérifier le contenu original
        with open(fichier_test, "r", encoding="utf-8") as f:
            contenu = f.read()
            print(f"   📖 Contenu préservé : '{contenu.replace(chr(10), '\\n')}'")

        # Cas d'usage typique : éviter l'écrasement accidentel
        print("\n   💡 Cas d'usage - Fichier de sauvegarde unique :")
        import datetime

        for i in range(3):
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            nom_sauvegarde = f"output_files/sauvegarde_{timestamp}_{i}.txt"

            try:
                with open(nom_sauvegarde, "x", encoding="utf-8") as f:
                    f.write(f"Sauvegarde créée le {timestamp}\n")
                    f.write(f"Tentative numéro {i+1}\n")
                print(f"      ✅ Sauvegarde créée : {nom_sauvegarde}")
            except FileExistsError:
                print(f"      ⚠️ Sauvegarde existe déjà : {nom_sauvegarde}")

    except Exception as e:
        print(f"   ❌ Erreur inattendue : {e}")


demo_mode_x()

print("\n🔄 MODES COMBINÉS (+ LECTURE)")
print("-" * 30)


def demo_modes_combines():
    """Démonstration des modes combinés lecture/écriture"""

    print("🔄 Modes combinés lecture/écriture :")

    try:
        # Mode 'w+' : écriture + lecture avec écrasement
        print("   Mode 'w+' :")
        with open("output_files/test_w_plus.txt", "w+", encoding="utf-8") as f:
            # Écrire
            f.write("Ligne 1\nLigne 2\nLigne 3\n")
            print(f"      Position après écriture : {f.tell()}")

            # Lire depuis le début
            f.seek(0)
            contenu = f.read()
            print(f"      Contenu lu : {len(contenu.splitlines())} lignes")

            # Ajouter à la fin
            f.write("Ligne 4 ajoutée\n")

            # Relire tout
            f.seek(0)
            contenu_final = f.read()
            print(
                f"      Contenu final : {len(contenu_final.splitlines())} lignes")

        # Mode 'a+' : ajout + lecture
        print("\n   Mode 'a+' :")
        # D'abord créer un fichier
        with open("output_files/test_a_plus.txt", "w", encoding="utf-8") as f:
            f.write("Contenu initial\n")

        with open("output_files/test_a_plus.txt", "a+", encoding="utf-8") as f:
            print(f"      Position initiale : {f.tell()}")

            # Lire le contenu existant
            f.seek(0)
            contenu_existant = f.read()
            print(f"      Contenu existant : '{contenu_existant.rstrip()}'")

            # Ajouter du nouveau contenu
            f.write("Contenu ajouté\n")

            # Relire tout
            f.seek(0)
            contenu_complet = f.read()
            print(
                f"      Contenu complet : {len(contenu_complet.splitlines())} lignes")

        # Mode 'r+' : lecture/écriture sans écrasement
        print("\n   Mode 'r+' :")
        with open("output_files/test_a_plus.txt", "r+", encoding="utf-8") as f:
            # Lire
            lignes = f.readlines()
            print(f"      Lignes lues : {len(lignes)}")

            # Modifier une ligne (écraser en place)
            f.seek(0)
            f.write("MODIFIÉ: " + lignes[0])

            # Voir le résultat
            f.seek(0)
            nouveau_contenu = f.read()
            print(f"      Après modification : '{nouveau_contenu.replace(chr(10), '\\n')}'")

    except Exception as e:
        print(f"   ❌ Erreur : {e}")


demo_modes_combines()

print("\n" + "=" * 50)
print("4. BUFFERING ET PERFORMANCE")
print("=" * 50)

print("\n⚡ BUFFERING - CONCEPT")
print("-" * 21)

print("""
⚡ QU'EST-CE QUE LE BUFFERING ?
Le buffering consiste à stocker temporairement les données
en mémoire avant de les écrire physiquement sur le disque.

🎯 AVANTAGES :
• Performance : moins d'accès disque
• Efficacité : écritures groupées
• Système : optimisation OS

📊 TYPES DE BUFFERING :
• Ligne par ligne (line buffering)
• Bloc fixe (block buffering)
• Pas de buffering (unbuffered)

⚠️ RISQUES :
• Perte de données si crash avant flush
• Latence pour voir les changements
• Consommation mémoire
""")


def demo_buffering():
    """Démonstration de l'impact du buffering"""
    import time

    print("⚡ Démonstration du buffering :")

    # Créer un fichier avec buffering par défaut
    print("   1️⃣ Écriture avec buffering par défaut :")
    with open("output_files/test_buffer_default.txt", "w", encoding="utf-8") as f:
        for i in range(5):
            f.write(f"Ligne {i+1} écrite\n")
            print(f"      Écrit ligne {i+1}")

            # Vérifier si visible immédiatement (autre processus)
            # En pratique, on ne verrait pas les changements immédiatement
            time.sleep(0.1)

    print("      ✅ Fichier fermé - tout est maintenant sur disque")

    # Écriture sans buffering
    print("\n   2️⃣ Écriture sans buffering :")
    with open("output_files/test_buffer_none.txt", "w", encoding="utf-8", buffering=0) as f:
        # Note: buffering=0 n'est possible qu'en mode binaire
        pass

    # En mode texte, utiliser buffering=1 (ligne par ligne)
    print("   3️⃣ Écriture ligne par ligne (buffering=1) :")
    with open("output_files/test_buffer_line.txt", "w", encoding="utf-8", buffering=1) as f:
        for i in range(3):
            f.write(f"Ligne {i+1}")  # Pas de \n
            print(f"      Écrit 'Ligne {i+1}' (pas encore sur disque)")

            f.write("\n")  # Maintenant ça flush !
            print(f"      Ajouté \\n (maintenant sur disque)")
            time.sleep(0.1)

    # Buffering manuel avec flush
    print("\n   4️⃣ Contrôle manuel avec flush() :")
    with open("output_files/test_buffer_manuel.txt", "w", encoding="utf-8") as f:
        f.write("Données importantes")
        print("      Écrit en buffer, pas encore sur disque")

        f.flush()  # Forcer l'écriture sur disque
        print("      flush() appelé - maintenant sur disque")

        f.write(" - suite des données")
        print("      Suite écrite en buffer")

        # Le close() automatique à la fin du with fera le flush final


print()
demo_buffering()

print("\n🚀 FLUSH() - CONTRÔLE MANUEL")
print("-" * 27)


def demo_flush():
    """Démonstration de flush() pour contrôle précis"""
    import time

    print("🚀 Contrôle précis avec flush() :")

    try:
        with open("output_files/demo_flush.txt", "w", encoding="utf-8") as f:
            # Écriture critique qui doit être sauvée immédiatement
            f.write("=== DÉBUT DE SESSION ===\n")
            f.write(f"Timestamp: {time.time()}\n")
            f.flush()  # Sauvegarder immédiatement
            print("   ✅ En-tête de session sauvegardé")

            # Simulation d'opérations avec sauvegarde périodique
            for i in range(10):
                f.write(f"Opération {i+1} en cours...\n")

                # Sauvegarder toutes les 3 opérations
                if (i+1) % 3 == 0:
                    f.flush()
                    print(f"   💾 Sauvegarde après opération {i+1}")

                time.sleep(0.05)  # Simulation de travail

            # Fin de session
            f.write("=== FIN DE SESSION ===\n")
            f.flush()
            print("   ✅ Fin de session sauvegardée")

        # Vérifier le contenu
        with open("output_files/demo_flush.txt", "r", encoding="utf-8") as f:
            lignes = f.readlines()
            print(f"   📊 Fichier final : {len(lignes)} lignes")

    except Exception as e:
        print(f"   ❌ Erreur : {e}")


demo_flush()

print("\n📈 PERFORMANCE COMPARISONS")
print("-" * 27)


def comparer_performances_ecriture():
    """Comparaison des performances d'écriture"""
    import time

    print("📈 Comparaison des performances :")

    nb_lignes = 10000
    donnees = [
        f"Ligne de test numéro {i:05d} avec du contenu\n" for i in range(nb_lignes)]

    # Test 1 : Écriture une par une avec flush
    start_time = time.time()
    with open("output_files/perf_flush_chaque.txt", "w", encoding="utf-8") as f:
        for ligne in donnees:
            f.write(ligne)
            f.flush()  # Flush après chaque ligne (lent !)
    duree_flush_chaque = time.time() - start_time

    # Test 2 : Écriture une par une sans flush
    start_time = time.time()
    with open("output_files/perf_sans_flush.txt", "w", encoding="utf-8") as f:
        for ligne in donnees:
            f.write(ligne)
    duree_sans_flush = time.time() - start_time

    # Test 3 : Écriture en une fois avec writelines
    start_time = time.time()
    with open("output_files/perf_writelines.txt", "w", encoding="utf-8") as f:
        f.writelines(donnees)
    duree_writelines = time.time() - start_time

    # Test 4 : Écriture par blocs
    start_time = time.time()
    with open("output_files/perf_par_blocs.txt", "w", encoding="utf-8") as f:
        taille_bloc = 1000
        for i in range(0, len(donnees), taille_bloc):
            bloc = donnees[i:i+taille_bloc]
            f.writelines(bloc)
            f.flush()
    duree_par_blocs = time.time() - start_time

    # Affichage des résultats
    print(f"   📊 Résultats pour {nb_lignes:,} lignes :")
    print(f"      Flush chaque ligne : {duree_flush_chaque:.3f}s (très lent)")
    print(f"      Sans flush manuel  : {duree_sans_flush:.3f}s")
    print(f"      Writelines()       : {duree_writelines:.3f}s (rapide)")
    print(f"      Par blocs (1000)   : {duree_par_blocs:.3f}s")

    # Calculer les ratios
    if duree_writelines > 0:
        ratio_flush = duree_flush_chaque / duree_writelines
        ratio_sans = duree_sans_flush / duree_writelines
        ratio_blocs = duree_par_blocs / duree_writelines

        print(f"\n   📈 Ratios par rapport à writelines() :")
        print(f"      Flush chaque : {ratio_flush:.1f}x plus lent")
        print(f"      Sans flush   : {ratio_sans:.1f}x")
        print(f"      Par blocs    : {ratio_blocs:.1f}x")


comparer_performances_ecriture()

print("\n" + "=" * 50)
print("5. ÉCRITURE SÉCURISÉE")
print("=" * 50)

print("\n🛡️ ÉCRITURE ATOMIQUE")
print("-" * 21)


def ecriture_atomique(nom_fichier, donnees):
    """Écriture atomique pour éviter la corruption"""
    import tempfile
    import shutil

    print(f"🛡️ Écriture atomique de '{nom_fichier}' :")

    try:
        # Créer un fichier temporaire dans le même répertoire
        repertoire = os.path.dirname(nom_fichier) or "."

        with tempfile.NamedTemporaryFile(
            mode='w',
            encoding='utf-8',
            dir=repertoire,
            delete=False,
            suffix='.tmp'
        ) as temp_file:

            temp_nom = temp_file.name
            print(f"   📝 Écriture dans fichier temporaire : {temp_nom}")

            # Écrire toutes les données
            if isinstance(donnees, str):
                temp_file.write(donnees)
            elif isinstance(donnees, list):
                temp_file.writelines(donnees)
            else:
                temp_file.write(str(donnees))

            # S'assurer que tout est écrit
            temp_file.flush()
            os.fsync(temp_file.fileno())  # Force sync to disk

        # Maintenant déplacer atomiquement
        shutil.move(temp_nom, nom_fichier)
        print(f"   ✅ Fichier déplacé atomiquement vers {nom_fichier}")

        return True

    except Exception as e:
        print(f"   ❌ Erreur lors de l'écriture atomique : {e}")

        # Nettoyer le fichier temporaire si nécessaire
        try:
            if os.path.exists(temp_nom):
                os.remove(temp_nom)
        except:
            pass

        return False


# Test de l'écriture atomique
donnees_test = [
    "Données critiques ligne 1\n",
    "Données critiques ligne 2\n",
    "Configuration importante\n",
    "Ne doit jamais être corrompue\n"
]

ecriture_atomique("output_files/donnees_critiques.txt", donnees_test)

print("\n🔐 GESTION DES PERMISSIONS")
print("-" * 26)


def demo_permissions():
    """Démonstration de la gestion des permissions"""
    import stat

    print("🔐 Gestion des permissions de fichiers :")

    try:
        # Créer un fichier avec permissions par défaut
        nom_fichier = "output_files/test_permissions.txt"
        with open(nom_fichier, "w", encoding="utf-8") as f:
            f.write("Fichier de test pour permissions\n")

        # Vérifier les permissions actuelles
        permissions_actuelles = oct(os.stat(nom_fichier).st_mode)[-3:]
        print(f"   📊 Permissions actuelles : {permissions_actuelles}")

        # Modifier les permissions (lecture seule pour le propriétaire)
        os.chmod(nom_fichier, stat.S_IRUSR)
        nouvelles_permissions = oct(os.stat(nom_fichier).st_mode)[-3:]
        print(
            f"   🔒 Nouvelles permissions : {nouvelles_permissions} (lecture seule)")

        # Tenter d'écrire (devrait échouer)
        try:
            with open(nom_fichier, "a", encoding="utf-8") as f:
                f.write("Tentative d'ajout\n")
            print("   ❌ Erreur : écriture réussie alors qu'elle devrait échouer")
        except PermissionError as e:
            print(f"   ✅ Erreur de permission attendue : {e}")

        # Restaurer les permissions d'écriture
        os.chmod(nom_fichier, stat.S_IRUSR | stat.S_IWUSR)
        permissions_finales = oct(os.stat(nom_fichier).st_mode)[-3:]
        print(f"   🔓 Permissions restaurées : {permissions_finales}")

        # Maintenant l'écriture devrait marcher
        with open(nom_fichier, "a", encoding="utf-8") as f:
            f.write("Ajout après restauration des permissions\n")
        print("   ✅ Écriture réussie après restauration")

    except Exception as e:
        print(f"   ❌ Erreur : {e}")


demo_permissions()

print("\n🔒 VERROUILLAGE DE FICHIERS")
print("-" * 28)


def demo_verrouillage():
    """Démonstration du verrouillage de fichiers"""
    import fcntl
    import time
    import threading

    print("🔒 Verrouillage de fichiers :")

    def ecrire_avec_verrou(nom_fichier, contenu, delai=1):
        """Écrire dans un fichier avec verrouillage"""
        try:
            with open(nom_fichier, "a", encoding="utf-8") as f:
                print(
                    f"   🔐 Tentative de verrouillage par thread {threading.current_thread().name}")

                # Verrouiller le fichier (Unix/Linux uniquement)
                if hasattr(fcntl, 'flock'):
                    fcntl.flock(f.fileno(), fcntl.LOCK_EX)
                    print(
                        f"   ✅ Verrou acquis par {threading.current_thread().name}")

                # Simuler du travail
                f.write(f"=== DÉBUT {threading.current_thread().name} ===\n")
                time.sleep(delai)
                f.write(contenu)
                f.write(f"=== FIN {threading.current_thread().name} ===\n\n")

                print(
                    f"   📝 Écriture terminée par {threading.current_thread().name}")

                # Le verrou sera libéré automatiquement à la fermeture

        except Exception as e:
            print(f"   ❌ Erreur dans {threading.current_thread().name} : {e}")

    # Test sur systèmes supportant fcntl
    try:
        import fcntl

        # Nettoyer le fichier de test
        nom_fichier = "output_files/test_verrou.txt"
        if os.path.exists(nom_fichier):
            os.remove(nom_fichier)

        # Créer plusieurs threads qui écrivent simultanément
        threads = []
        for i in range(3):
            contenu = f"Contenu du thread {i+1}\nLigne 2 du thread {i+1}\n"
            thread = threading.Thread(
                target=ecrire_avec_verrou,
                args=(nom_fichier, contenu, 0.5),
                name=f"Thread-{i+1}"
            )
            threads.append(thread)

        # Lancer tous les threads
        for thread in threads:
            thread.start()

        # Attendre que tous finissent
        for thread in threads:
            thread.join()

        # Vérifier le résultat
        if os.path.exists(nom_fichier):
            with open(nom_fichier, "r", encoding="utf-8") as f:
                contenu = f.read()
                print(
                    f"   📖 Contenu final ({len(contenu.splitlines())} lignes) :")
                # Premiers 10 lignes
                for i, ligne in enumerate(contenu.splitlines()[:10], 1):
                    print(f"      [{i:2d}] : {ligne}")

    except ImportError:
        print("   ⚠️ fcntl non disponible sur ce système (Windows)")
        print("   💡 Utiliser des solutions alternatives comme filelock")


demo_verrouillage()

print("\n" + "=" * 50)
print("6. FORMATS SPÉCIALISÉS")
print("=" * 50)

print("\n📊 GÉNÉRATION DE CSV")
print("-" * 20)


def generer_csv():
    """Génération de fichiers CSV"""
    import csv

    print("📊 Génération de fichiers CSV :")

    # Données de test
    employes = [
        {"nom": "Dupont", "prenom": "Jean", "age": 30,
            "salaire": 35000, "departement": "IT"},
        {"nom": "Martin", "prenom": "Marie", "age": 25,
            "salaire": 32000, "departement": "RH"},
        {"nom": "Durand", "prenom": "Pierre", "age": 35,
            "salaire": 42000, "departement": "Finance"},
        {"nom": "Dubois", "prenom": "Sophie", "age": 28,
            "salaire": 38000, "departement": "Marketing"},
        {"nom": "Leroy", "prenom": "Paul", "age": 45,
            "salaire": 55000, "departement": "Direction"},
    ]

    # Méthode 1 : CSV manuel
    print("   1️⃣ Génération CSV manuelle :")
    with open("output_files/employes_manuel.csv", "w", encoding="utf-8") as f:
        # En-tête
        f.write("nom,prenom,age,salaire,departement\n")

        # Données
        for emp in employes:
            ligne = f"{emp['nom']},{emp['prenom']},{emp['age']},{emp['salaire']},{emp['departement']}\n"
            f.write(ligne)

    print("      ✅ CSV manuel généré")

    # Méthode 2 : Module CSV (recommandé)
    print("   2️⃣ Génération avec module CSV :")
    with open("output_files/employes_module.csv", "w", encoding="utf-8", newline='') as f:
        writer = csv.DictWriter(
            f, fieldnames=["nom", "prenom", "age", "salaire", "departement"])

        # En-tête
        writer.writeheader()

        # Données
        writer.writerows(employes)

    print("      ✅ CSV avec module généré")

    # Méthode 3 : CSV avec caractères spéciaux (échappement)
    print("   3️⃣ CSV avec caractères spéciaux :")
    donnees_speciales = [
        {"nom": "O'Connor", "commentaire": "Très bien, \"excellent\" travail", "note": "A+"},
        {"nom": "Müller", "commentaire": "Contient des , virgules", "note": "B"},
        {"nom": "José", "commentaire": "Multiline\ncomment", "note": "A"},
    ]

    with open("output_files/donnees_speciales.csv", "w", encoding="utf-8", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["nom", "commentaire", "note"])
        writer.writeheader()
        writer.writerows(donnees_speciales)

    print("      ✅ CSV avec échappement généré")

    # Vérification
    print("\n   📖 Vérification du CSV avec échappement :")
    with open("output_files/donnees_speciales.csv", "r", encoding="utf-8") as f:
        contenu = f.read()
        for i, ligne in enumerate(contenu.splitlines(), 1):
            print(f"      [{i}] : {ligne}")


generer_csv()

print("\n🔧 GÉNÉRATION DE JSON")
print("-" * 21)


def generer_json():
    """Génération de fichiers JSON"""
    import json
    from datetime import datetime, date

    print("🔧 Génération de fichiers JSON :")

    # Données complexes
    donnees = {
        "application": {
            "nom": "MonApp",
            "version": "2.1.0",
            "date_release": "2024-01-15"
        },
        "utilisateurs": [
            {
                "id": 1,
                "nom": "Alice",
                "email": "alice@example.com",
                "actif": True,
                "derniere_connexion": "2024-01-14T10:30:00Z",
                "preferences": {
                    "theme": "sombre",
                    "notifications": True,
                    "langue": "fr"
                }
            },
            {
                "id": 2,
                "nom": "Bob",
                "email": "bob@example.com",
                "actif": False,
                "derniere_connexion": None,
                "preferences": {
                    "theme": "clair",
                    "notifications": False,
                    "langue": "en"
                }
            }
        ],
        "statistiques": {
            "total_utilisateurs": 2,
            "utilisateurs_actifs": 1,
            "taux_activation": 0.5
        }
    }

    # Écriture JSON standard
    print("   1️⃣ JSON standard (compact) :")
    with open("output_files/donnees_compact.json", "w", encoding="utf-8") as f:
        json.dump(donnees, f, ensure_ascii=False)
    print("      ✅ JSON compact généré")

    # Écriture JSON formaté
    print("   2️⃣ JSON formaté (lisible) :")
    with open("output_files/donnees_lisible.json", "w", encoding="utf-8") as f:
        json.dump(donnees, f, ensure_ascii=False, indent=2, sort_keys=True)
    print("      ✅ JSON formaté généré")

    # JSON avec types personnalisés
    print("   3️⃣ JSON avec sérialiseur personnalisé :")

    class EncodeurPersonnalise(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            elif isinstance(obj, date):
                return obj.isoformat()
            return super().default(obj)

    donnees_avec_dates = {
        "timestamp": datetime.now(),
        "date_creation": date.today(),
        "donnees": donnees
    }

    with open("output_files/donnees_avec_dates.json", "w", encoding="utf-8") as f:
        json.dump(donnees_avec_dates, f, cls=EncodeurPersonnalise,
                  ensure_ascii=False, indent=2)
    print("      ✅ JSON avec dates généré")

    # Vérification des tailles
    tailles = {}
    for nom in ["compact", "lisible", "avec_dates"]:
        fichier = f"output_files/donnees_{nom}.json"
        taille = os.path.getsize(fichier)
        tailles[nom] = taille
        print(f"      {nom:<12} : {taille:,} octets")


generer_json()

print("\n📋 GÉNÉRATION DE MARKDOWN")
print("-" * 26)


def generer_markdown():
    """Génération de fichiers Markdown"""

    print("📋 Génération de fichiers Markdown :")

    # Données pour le rapport
    donnees_rapport = {
        "titre": "Rapport d'Activité Mensuel",
        "date": "Janvier 2024",
        "auteur": "Jean Dupont",
        "sections": [
            {
                "titre": "Résumé Exécutif",
                "contenu": "Ce mois a été marqué par une croissance significative de nos activités."
            },
            {
                "titre": "Métriques Clés",
                "contenu": "Voici les principales métriques du mois :"
            }
        ],
        "metriques": [
            {"nom": "Utilisateurs actifs", "valeur": 15420, "evolution": "+12%"},
            {"nom": "Revenus", "valeur": 85300, "evolution": "+8%"},
            {"nom": "Taux de satisfaction", "valeur": 94.5, "evolution": "+2%"}
        ],
        "taches": [
            {"nom": "Améliorer la performance", "statut": "✅ Terminé"},
            {"nom": "Nouvelle fonctionnalité", "statut": "🚧 En cours"},
            {"nom": "Documentation", "statut": "📋 Planifié"}
        ]
    }

    with open("output_files/rapport.md", "w", encoding="utf-8") as f:
        # En-tête
        f.write(f"# {donnees_rapport['titre']}\n\n")
        f.write(f"**Date :** {donnees_rapport['date']}  \n")
        f.write(f"**Auteur :** {donnees_rapport['auteur']}  \n\n")
        f.write("---\n\n")

        # Table des matières
        f.write("## Table des Matières\n\n")
        for i, section in enumerate(donnees_rapport['sections'], 1):
            f.write(
                f"{i}. [{section['titre']}](#{section['titre'].lower().replace(' ', '-')})\n")
        f.write("3. [Métriques](#métriques)\n")
        f.write("4. [Tâches](#tâches)\n\n")

        # Sections
        for section in donnees_rapport['sections']:
            f.write(f"## {section['titre']}\n\n")
            f.write(f"{section['contenu']}\n\n")

        # Métriques sous forme de tableau
        f.write("## Métriques\n\n")
        f.write("| Métrique | Valeur | Évolution |\n")
        f.write("|----------|--------|----------|\n")
        for metrique in donnees_rapport['metriques']:
            valeur = f"{metrique['valeur']:,}" if isinstance(
                metrique['valeur'], int) else metrique['valeur']
            f.write(
                f"| {metrique['nom']} | {valeur} | {metrique['evolution']} |\n")
        f.write("\n")

        # Tâches sous forme de liste
        f.write("## Tâches\n\n")
        for tache in donnees_rapport['taches']:
            f.write(f"- **{tache['nom']}** : {tache['statut']}\n")
        f.write("\n")

        # Code exemple
        f.write("## Exemple de Code\n\n")
        f.write("```python\n")
        f.write("def calculer_croissance(ancien, nouveau):\n")
        f.write("    return ((nouveau - ancien) / ancien) * 100\n")
        f.write("\n")
        f.write("croissance = calculer_croissance(1000, 1120)\n")
        f.write("print(f'Croissance: {croissance:.1f}%')\n")
        f.write("```\n\n")

        # Conclusion
        f.write("## Conclusion\n\n")
        f.write("> Les résultats de ce mois montrent une **progression constante** ")
        f.write("de nos indicateurs clés. Nous restons confiants pour la suite.\n\n")
        f.write("---\n\n")
        f.write("*Rapport généré automatiquement*\n")

    print("   ✅ Rapport Markdown généré")

    # Vérification
    with open("output_files/rapport.md", "r", encoding="utf-8") as f:
        lignes = f.readlines()
        print(f"   📊 Fichier généré : {len(lignes)} lignes")


generer_markdown()

print("\n" + "=" * 50)
print("7. EXERCICES PRATIQUES")
print("=" * 50)

print("""
💪 EXERCICES À IMPLÉMENTER :

🎯 Exercice 1 : Générateur de rapports
Créez un système de génération de rapports :
• Support multiple formats (HTML, PDF, CSV, JSON)
• Templates configurables
• Graphiques intégrés (matplotlib)
• Export automatique par email
• Planification et archivage

📊 Exercice 2 : Logger personnalisé
Créez votre propre système de logging :
• Rotation automatique des fichiers
• Niveaux de log configurables
• Format personnalisable avec couleurs
• Compression des anciens logs
• Dashboard de monitoring

🔄 Exercice 3 : Système de sauvegarde
Créez un système de sauvegarde incrémentale :
• Détection des changements
• Compression et déduplication
• Sauvegarde vers cloud (S3, etc.)
• Restauration sélective
• Vérification d'intégrité

📝 Exercice 4 : Éditeur de configuration
Créez un éditeur pour fichiers de config :
• Support YAML, JSON, INI, TOML
• Validation en temps réel
• Interface web ou GUI
• Historique des changements
• Déploiement automatique

🎮 Exercice 5 : Générateur de code
Créez un générateur de code source :
• Templates Jinja2 ou similaire
• Métadonnées depuis JSON/YAML
• Support multi-langages
• Tests automatiques générés
• Documentation intégrée
""")

print("\n" + "=" * 50)
print("8. RÉSUMÉ FINAL")
print("=" * 50)

print("""
🎯 POINTS CLÉS À RETENIR :

1. 📝 MÉTHODES D'ÉCRITURE :
   • write(string) : écrire une chaîne
   • writelines(list) : écrire une liste (sans \\n automatique !)
   • print(file=f) : utiliser print() vers fichier
   • Toujours utiliser encoding='utf-8'

2. 🎭 MODES D'ÉCRITURE :
   • 'w' : écrasement complet du fichier
   • 'a' : ajout en fin de fichier
   • 'x' : création exclusive (échoue si existe)
   • '+' : combinaison lecture/écriture
   • 'b' : mode binaire vs 't' mode texte

3. ⚡ PERFORMANCE ET BUFFERING :
   • Buffering automatique pour performance
   • flush() pour forcer l'écriture sur disque
   • writelines() plus rapide que write() en boucle
   • Éviter flush() après chaque write() (très lent)

4. 🛡️ SÉCURITÉ :
   • Context managers (with) obligatoires
   • Écriture atomique pour données critiques
   • Gestion des permissions de fichiers
   • Verrouillage pour accès concurrent
   • Validation avant écriture

5. 📊 FORMATS SPÉCIALISÉS :
   • CSV : module csv pour échappement correct
   • JSON : json.dump() avec encodage proper
   • Markdown : génération programmatique
   • Binaires : struct pour données structurées

💡 BONNES PRATIQUES :
✅ Toujours utiliser with pour ouvrir des fichiers
✅ Spécifier encoding='utf-8' explicitement
✅ flush() seulement quand nécessaire (données critiques)
✅ Écriture atomique pour éviter corruption
✅ Valider les données avant écriture
✅ Gérer les erreurs d'espace disque et permissions

🚨 ERREURS COURANTES :
❌ Oublier le \\n dans writelines()
❌ Mode 'w' efface tout le contenu existant
❌ Pas de gestion d'erreurs (disque plein, permissions)
❌ flush() après chaque write() (performance)
❌ Oublier de fermer les fichiers
❌ Encodage incorrect pour caractères spéciaux

⚡ OPTIMISATIONS :
• Utiliser writelines() pour écriture en lot
• Buffer les données avant écriture massive
• Écriture par blocs pour gros volumes
• Compression pour économiser l'espace
• Threads pour E/S parallèles

🔧 PATTERNS AVANCÉS :
• Context managers personnalisés
• Factories de writers par format
• Pipelines de transformation de données
• Système de templates
• Génération de code automatique

🎯 CAS D'USAGE COURANTS :
• Logs d'application avec rotation
• Export de données en CSV/JSON
• Génération de rapports
• Sauvegarde de configuration
• Cache de données sur disque

🔍 DEBUGGING :
• Vérifier les permissions de fichier
• Contrôler l'espace disque disponible
• Tester avec des caractères spéciaux
• Simuler les erreurs d'E/O
• Surveiller les performances

🎉 Félicitations ! Écriture de fichiers maîtrisée !
💡 Prochaine étape : Context managers !
📚 Écriture maîtrisée, explorez les context managers !
""")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE - ÉCRITURE DE FICHIERS MAÎTRISÉE !")
print("=" * 70)
