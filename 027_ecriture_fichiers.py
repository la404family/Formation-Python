#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
======================================================================
ÉCRITURE DE FICHIERS EN PYTHON - GUIDE COMPLET
======================================================================

🎯 Ce fichier couvre l'écriture de fichiers en détail :
   • write, writelines, print vers fichiers
   • Modes d'ouverture (write, append)
   • Gestion des permissions et erreurs
   • Écriture de différents formats
   • Bonnes pratiques de sauvegarde

📚 Concepts abordés :
   • Modes 'w', 'a', 'x' et leurs variantes
   • Méthodes write(), writelines()
   • Fonction print() avec paramètre file
   • Flush et buffering
   • Atomic writes et backups

💡 Objectif : Maîtriser l'écriture sécurisée de fichiers
"""

import os
import json
import csv
import tempfile
import shutil
from pathlib import Path
from datetime import datetime

print("=" * 70)
print("ÉCRITURE DE FICHIERS EN PYTHON - GUIDE COMPLET")
print("=" * 70)

print("\n" + "=" * 50)
print("1. MÉTHODES D'ÉCRITURE DE BASE")
print("=" * 50)

print("\n✍️ MODES D'OUVERTURE ET MÉTHODES WRITE")
print("-" * 39)


def demo_ecriture_base():
    """Démonstration des méthodes d'écriture de base"""

    print("✍️ Méthodes d'écriture de base :")

    print("\n   1️⃣ Mode 'w' - Écriture avec écrasement :")

    # Mode 'w' : écrase le fichier s'il existe
    with open("test_write.txt", "w", encoding="utf-8") as fichier:
        fichier.write("Première ligne\n")
        fichier.write("Deuxième ligne\n")
        fichier.write("Troisième ligne sans \\n")

    # Vérifier le contenu
    with open("test_write.txt", "r", encoding="utf-8") as fichier:
        contenu = fichier.read()
        print(f"      Contenu écrit : {repr(contenu)}")

    print("\n   2️⃣ Mode 'a' - Écriture en ajout :")

    # Mode 'a' : ajoute à la fin du fichier
    with open("test_write.txt", "a", encoding="utf-8") as fichier:
        fichier.write("\nQuatrième ligne ajoutée")
        fichier.write("\nCinquième ligne ajoutée")

    # Vérifier le contenu mis à jour
    with open("test_write.txt", "r", encoding="utf-8") as fichier:
        contenu = fichier.read()
        print(f"      Contenu après ajout : {repr(contenu)}")

    print("\n   3️⃣ Mode 'x' - Écriture exclusive :")

    # Mode 'x' : échoue si le fichier existe déjà
    try:
        with open("test_write.txt", "x", encoding="utf-8") as fichier:
            fichier.write("Ceci ne devrait pas s'écrire")
        print("      ❌ Erreur : le fichier aurait dû exister")
    except FileExistsError:
        print("      ✅ Erreur attendue : fichier existe déjà")

    # Créer un nouveau fichier avec 'x'
    try:
        with open("nouveau_fichier.txt", "x", encoding="utf-8") as fichier:
            fichier.write("Nouveau fichier créé avec mode 'x'")
        print("      ✅ Nouveau fichier créé avec succès")
    except FileExistsError:
        print("      ❌ Le fichier existe déjà")

    print("\n   4️⃣ Méthode writelines() :")

    lignes = [
        "Liste de lignes à écrire\n",
        "Deuxième ligne de la liste\n",
        "Troisième ligne de la liste\n",
        "Dernière ligne sans retour chariot"
    ]

    with open("test_writelines.txt", "w", encoding="utf-8") as fichier:
        fichier.writelines(lignes)

    # Vérifier le résultat
    with open("test_writelines.txt", "r", encoding="utf-8") as fichier:
        contenu = fichier.read()
        print(f"      Résultat writelines : {repr(contenu)}")

    print("\n   5️⃣ Fonction print() vers fichier :")

    with open("test_print.txt", "w", encoding="utf-8") as fichier:
        print("Ligne écrite avec print()", file=fichier)
        print("Avec formatage :", 42, "et", [1, 2, 3], file=fichier)
        print("Sans retour à la ligne", end="", file=fichier)
        print(" - suite de la ligne", file=fichier)

        # Avec séparateur personnalisé
        print("Un", "Deux", "Trois", sep=" | ", file=fichier)

    # Vérifier le résultat
    with open("test_print.txt", "r", encoding="utf-8") as fichier:
        contenu = fichier.read()
        print(f"      Résultat print : {repr(contenu)}")

    # Nettoyage
    for fichier in ["test_write.txt", "nouveau_fichier.txt", "test_writelines.txt", "test_print.txt"]:
        if os.path.exists(fichier):
            os.remove(fichier)


demo_ecriture_base()

print("\n🔧 GESTION DU BUFFERING ET FLUSH")
print("-" * 33)


def demo_buffering_flush():
    """Démonstration du buffering et flush"""

    print("🔧 Buffering et flush :")

    print("\n   1️⃣ Écriture avec flush manuel :")

    with open("test_flush.txt", "w", encoding="utf-8") as fichier:
        fichier.write("Première ligne (bufferisée)\n")
        print("      ✍️ Ligne écrite en mémoire (buffer)")

        # Vérifier si visible dans un autre processus (simulation)
        try:
            with open("test_flush.txt", "r", encoding="utf-8") as lecture:
                contenu_avant_flush = lecture.read()
            print(f"      📖 Contenu avant flush : '{contenu_avant_flush}'")
        except:
            print("      📖 Fichier non accessible avant flush")

        # Forcer l'écriture sur disque
        fichier.flush()
        print("      💾 flush() appelé - données écrites sur disque")

        # Vérifier après flush
        with open("test_flush.txt", "r", encoding="utf-8") as lecture:
            contenu_apres_flush = lecture.read()
        print(f"      📖 Contenu après flush : '{contenu_apres_flush}'")

        fichier.write("Deuxième ligne après flush\n")

    print("\n   2️⃣ Buffering désactivé :")

    # Avec buffering=0 (seulement en mode binaire)
    with open("test_unbuffered.txt", "wb", buffering=0) as fichier:
        fichier.write(b"Ecriture sans buffer (binaire)\n")
        print("      ✅ Écriture directe sur disque (mode binaire)")

    # Avec buffering=1 (line buffering en mode texte)
    with open("test_line_buffered.txt", "w", encoding="utf-8", buffering=1) as fichier:
        fichier.write("Ligne 1 (sera flushée après \\n)\n")
        print("      ✅ Line buffering : flush automatique après \\n")
        fichier.write("Ligne 2 sans \\n")
        print("      ⏳ Pas de flush automatique sans \\n")

    print("\n   3️⃣ Context manager avec flush automatique :")

    class AutoFlushFile:
        """Context manager qui flush après chaque écriture"""

        def __init__(self, nom_fichier, mode="w", encoding="utf-8"):
            self.nom_fichier = nom_fichier
            self.mode = mode
            self.encoding = encoding
            self.fichier = None

        def __enter__(self):
            self.fichier = open(self.nom_fichier, self.mode,
                                encoding=self.encoding)
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            if self.fichier:
                self.fichier.close()

        def write(self, texte):
            """Écrire avec flush automatique"""
            self.fichier.write(texte)
            self.fichier.flush()  # Flush après chaque écriture
            return len(texte)

    with AutoFlushFile("test_auto_flush.txt") as fichier:
        fichier.write("Ligne 1 avec auto-flush\n")
        print("      ✅ Ligne 1 écrite et flushée")
        fichier.write("Ligne 2 avec auto-flush\n")
        print("      ✅ Ligne 2 écrite et flushée")

    # Vérification des résultats
    for nom_fichier in ["test_flush.txt", "test_unbuffered.txt", "test_line_buffered.txt", "test_auto_flush.txt"]:
        if os.path.exists(nom_fichier):
            with open(nom_fichier, "r", encoding="utf-8", errors="ignore") as f:
                contenu = f.read()
                print(f"      📄 {nom_fichier} : {repr(contenu)}")

    # Nettoyage
    for fichier in ["test_flush.txt", "test_unbuffered.txt", "test_line_buffered.txt", "test_auto_flush.txt"]:
        if os.path.exists(fichier):
            os.remove(fichier)


demo_buffering_flush()

print("\n" + "=" * 50)
print("2. GESTION D'ERREURS ET SÉCURITÉ")
print("=" * 50)

print("\n🚨 ERREURS D'ÉCRITURE ET PERMISSIONS")
print("-" * 36)


def demo_erreurs_ecriture():
    """Démonstration de la gestion d'erreurs d'écriture"""

    print("🚨 Gestion des erreurs d'écriture :")

    def ecrire_fichier_robuste(nom_fichier, contenu, mode="w", encoding="utf-8"):
        """Écriture robuste avec gestion d'erreurs"""
        print(
            f"\n      🔍 Tentative d'écriture : '{nom_fichier}' (mode: {mode})")

        try:
            with open(nom_fichier, mode, encoding=encoding) as fichier:
                if isinstance(contenu, list):
                    fichier.writelines(contenu)
                else:
                    fichier.write(contenu)

                print(
                    f"      ✅ Écriture réussie ({len(str(contenu))} caractères)")
                return True

        except FileNotFoundError:
            print(
                f"      ❌ Répertoire parent inexistant pour : '{nom_fichier}'")
            return False
        except PermissionError:
            print(f"      ❌ Permissions insuffisantes pour : '{nom_fichier}'")
            return False
        except FileExistsError:
            print(f"      ❌ Fichier existe déjà (mode 'x') : '{nom_fichier}'")
            return False
        except IsADirectoryError:
            print(f"      ❌ '{nom_fichier}' est un répertoire, pas un fichier")
            return False
        except OSError as e:
            print(f"      ❌ Erreur système : {e}")
            return False
        except UnicodeEncodeError as e:
            print(f"      ❌ Erreur d'encodage : {e}")
            return False
        except Exception as e:
            print(f"      ❌ Erreur inattendue : {type(e).__name__}: {e}")
            return False

    # Tests d'erreurs d'écriture
    print("\n   Tests de gestion d'erreurs :")

    # Créer un répertoire de test
    os.makedirs("test_ecriture", exist_ok=True)

    tests_ecriture = [
        ("test_ecriture/fichier_valide.txt",
         "Contenu valide", "w", "Écriture normale"),
        ("repertoire_inexistant/fichier.txt",
         "Contenu", "w", "Répertoire inexistant"),
        ("test_ecriture", "Contenu", "w", "Écrire sur un répertoire"),
        ("test_ecriture/fichier_exist.txt",
         "Premier contenu", "x", "Création exclusive 1"),
        ("test_ecriture/fichier_exist.txt", "Deuxième contenu",
         "x", "Création exclusive 2 (échec)"),
    ]

    for nom_fichier, contenu, mode, description in tests_ecriture:
        print(f"\n   📋 Test : {description}")
        succes = ecrire_fichier_robuste(nom_fichier, contenu, mode)

        # Vérifier le résultat si succès
        if succes and os.path.exists(nom_fichier):
            with open(nom_fichier, "r", encoding="utf-8") as f:
                contenu_lu = f.read()
                print(f"      📄 Contenu vérifié : '{contenu_lu}'")

    # Test d'encodage
    print("\n   📋 Test : Problème d'encodage")
    texte_unicode = "Texte avec émojis : 🐍🚀💻 et accents : café, naïve"
    ecrire_fichier_robuste("test_ecriture/unicode.txt",
                           texte_unicode, "w", "utf-8")

    # Tentative d'écriture avec mauvais encodage
    ecrire_fichier_robuste("test_ecriture/ascii_fail.txt",
                           texte_unicode, "w", "ascii")

    # Nettoyage
    if os.path.exists("test_ecriture"):
        shutil.rmtree("test_ecriture")


demo_erreurs_ecriture()

print("\n🛡️ ÉCRITURE ATOMIQUE ET SÉCURISÉE")
print("-" * 34)


def demo_ecriture_atomique():
    """Démonstration d'écriture atomique"""

    print("🛡️ Écriture atomique et sécurisée :")

    def ecrire_atomique(nom_fichier, contenu, encoding="utf-8"):
        """Écriture atomique : tout ou rien"""

        print(f"      🔒 Écriture atomique vers '{nom_fichier}'")

        # Créer un fichier temporaire dans le même répertoire
        repertoire = os.path.dirname(nom_fichier) or "."
        nom_base = os.path.basename(nom_fichier)

        try:
            # Créer fichier temporaire
            with tempfile.NamedTemporaryFile(
                mode="w",
                encoding=encoding,
                dir=repertoire,
                prefix=f".{nom_base}.tmp.",
                delete=False
            ) as fichier_temp:

                fichier_temp.write(contenu)
                fichier_temp.flush()
                os.fsync(fichier_temp.fileno())  # Force sync sur disque
                nom_temp = fichier_temp.name

            # Renommage atomique
            if os.name == 'nt':  # Windows
                if os.path.exists(nom_fichier):
                    os.remove(nom_fichier)

            os.rename(nom_temp, nom_fichier)
            print(f"      ✅ Écriture atomique réussie")
            return True

        except Exception as e:
            # Nettoyage en cas d'erreur
            if 'nom_temp' in locals() and os.path.exists(nom_temp):
                os.remove(nom_temp)
            print(f"      ❌ Erreur écriture atomique : {e}")
            return False

    def ecrire_avec_backup(nom_fichier, contenu, encoding="utf-8"):
        """Écriture avec sauvegarde de l'ancien fichier"""

        print(f"      💾 Écriture avec backup vers '{nom_fichier}'")

        nom_backup = f"{nom_fichier}.backup"

        try:
            # Créer backup de l'ancien fichier s'il existe
            if os.path.exists(nom_fichier):
                shutil.copy2(nom_fichier, nom_backup)
                print(f"      📄 Backup créé : '{nom_backup}'")

            # Écrire le nouveau contenu
            with open(nom_fichier, "w", encoding=encoding) as fichier:
                fichier.write(contenu)

            print(f"      ✅ Écriture avec backup réussie")
            return True

        except Exception as e:
            # Restaurer depuis backup en cas d'erreur
            if os.path.exists(nom_backup):
                shutil.move(nom_backup, nom_fichier)
                print(f"      🔄 Fichier restauré depuis backup")

            print(f"      ❌ Erreur : {e}")
            return False

    def ecrire_avec_verifications(nom_fichier, contenu, encoding="utf-8"):
        """Écriture avec vérifications multiples"""

        print(f"      🔍 Écriture avec vérifications vers '{nom_fichier}'")

        try:
            # Vérifications préalables
            repertoire = os.path.dirname(nom_fichier) or "."

            if not os.path.exists(repertoire):
                print(f"      📁 Création du répertoire : '{repertoire}'")
                os.makedirs(repertoire, exist_ok=True)

            if not os.access(repertoire, os.W_OK):
                raise PermissionError(
                    f"Pas de droits d'écriture sur '{repertoire}'")

            # Vérifier l'espace disque (simulation)
            espace_requis = len(contenu.encode(encoding))
            espace_libre = shutil.disk_usage(repertoire).free

            if espace_requis > espace_libre:
                raise OSError(
                    f"Espace disque insuffisant : {espace_requis} > {espace_libre}")

            # Écriture sécurisée
            with open(nom_fichier, "w", encoding=encoding) as fichier:
                fichier.write(contenu)
                fichier.flush()
                os.fsync(fichier.fileno())

            # Vérification post-écriture
            with open(nom_fichier, "r", encoding=encoding) as fichier:
                contenu_lu = fichier.read()

                if contenu_lu != contenu:
                    raise ValueError(
                        "Contenu écrit différent du contenu attendu")

            taille_fichier = os.path.getsize(nom_fichier)
            print(f"      ✅ Écriture vérifiée : {taille_fichier} octets")
            return True

        except Exception as e:
            print(f"      ❌ Erreur : {e}")
            return False

    # Tests d'écriture sécurisée
    print("\n   Tests d'écriture sécurisée :")

    contenu_test = """Contenu de test pour écriture sécurisée
Avec plusieurs lignes
Et des caractères spéciaux : àéèùç
Émojis : 🔒💾✅"""

    print("\n   1️⃣ Écriture atomique :")
    ecrire_atomique("fichier_atomique.txt", contenu_test)

    print("\n   2️⃣ Écriture avec backup :")
    # Créer d'abord un fichier existant
    with open("fichier_backup.txt", "w", encoding="utf-8") as f:
        f.write("Ancien contenu à sauvegarder")

    ecrire_avec_backup("fichier_backup.txt", contenu_test)

    print("\n   3️⃣ Écriture avec vérifications :")
    ecrire_avec_verifications("securise/fichier_verifie.txt", contenu_test)

    # Vérifier les résultats
    fichiers_crees = ["fichier_atomique.txt",
                      "fichier_backup.txt", "securise/fichier_verifie.txt"]

    for fichier in fichiers_crees:
        if os.path.exists(fichier):
            with open(fichier, "r", encoding="utf-8") as f:
                contenu = f.read()
                print(f"      📄 {fichier} : {len(contenu)} caractères")

    # Nettoyage
    for fichier in ["fichier_atomique.txt", "fichier_backup.txt", "fichier_backup.txt.backup"]:
        if os.path.exists(fichier):
            os.remove(fichier)

    if os.path.exists("securise"):
        shutil.rmtree("securise")


demo_ecriture_atomique()

print("\n" + "=" * 50)
print("3. ÉCRITURE DE FORMATS SPÉCIFIQUES")
print("=" * 50)

print("\n📄 GÉNÉRATION DE FICHIERS STRUCTURÉS")
print("-" * 37)


def demo_ecriture_formats():
    """Démonstration d'écriture de différents formats"""

    print("📄 Écriture de formats spécifiques :")

    # Données de test
    donnees_utilisateurs = [
        {"nom": "Alice Martin", "age": 25, "ville": "Paris", "salaire": 45000},
        {"nom": "Bob Durand", "age": 30, "ville": "Lyon", "salaire": 50000},
        {"nom": "Charlie Petit", "age": 35, "ville": "Marseille", "salaire": 48000},
        {"nom": "Diane Rouge", "age": 28, "ville": "Toulouse", "salaire": 52000},
    ]

    print("\n   1️⃣ Écriture de fichier CSV :")

    # CSV manuel
    def ecrire_csv_manuel(nom_fichier, donnees):
        """Écriture CSV manuelle"""
        with open(nom_fichier, "w", encoding="utf-8", newline="") as fichier:
            # En-têtes
            entetes = list(donnees[0].keys())
            fichier.write(",".join(entetes) + "\n")

            # Données
            for ligne in donnees:
                valeurs = [str(ligne[cle]) for cle in entetes]
                fichier.write(",".join(valeurs) + "\n")

        print(f"      ✅ CSV manuel écrit : '{nom_fichier}'")

    ecrire_csv_manuel("utilisateurs_manuel.csv", donnees_utilisateurs)

    # CSV avec module csv
    with open("utilisateurs_module.csv", "w", encoding="utf-8", newline="") as fichier:
        writer = csv.DictWriter(
            fichier, fieldnames=donnees_utilisateurs[0].keys())
        writer.writeheader()
        writer.writerows(donnees_utilisateurs)

    print(f"      ✅ CSV avec module écrit : 'utilisateurs_module.csv'")

    print("\n   2️⃣ Écriture de fichier JSON :")

    # Structure JSON complexe
    donnees_json = {
        "metadata": {
            "version": "1.0",
            "created": datetime.now().isoformat(),
            "total_users": len(donnees_utilisateurs)
        },
        "users": donnees_utilisateurs,
        "statistics": {
            "average_age": sum(u["age"] for u in donnees_utilisateurs) / len(donnees_utilisateurs),
            "cities": list(set(u["ville"] for u in donnees_utilisateurs)),
            "salary_range": {
                "min": min(u["salaire"] for u in donnees_utilisateurs),
                "max": max(u["salaire"] for u in donnees_utilisateurs)
            }
        }
    }

    # JSON formaté
    with open("donnees_formatees.json", "w", encoding="utf-8") as fichier:
        json.dump(donnees_json, fichier, indent=2, ensure_ascii=False)

    print(f"      ✅ JSON formaté écrit : 'donnees_formatees.json'")

    # JSON compact
    with open("donnees_compactes.json", "w", encoding="utf-8") as fichier:
        json.dump(donnees_json, fichier, separators=(
            ',', ':'), ensure_ascii=False)

    print(f"      ✅ JSON compact écrit : 'donnees_compactes.json'")

    print("\n   3️⃣ Écriture de fichier de configuration :")

    # Configuration INI
    config_ini = """[DATABASE]
host = localhost
port = 5432
username = admin
password = secret123
ssl_enabled = true

[APPLICATION]
debug = false
max_connections = 100
timeout = 30
log_level = INFO

[FEATURES]
enable_caching = true
enable_monitoring = true
enable_backup = false"""

    with open("config.ini", "w", encoding="utf-8") as fichier:
        fichier.write(config_ini)

    print(f"      ✅ Configuration INI écrite : 'config.ini'")

    print("\n   4️⃣ Génération de rapport HTML :")

    def generer_rapport_html(donnees, nom_fichier):
        """Générer un rapport HTML simple"""
        html = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rapport Utilisateurs</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        .stats { background-color: #e8f4fd; padding: 10px; margin: 20px 0; }
    </style>
</head>
<body>
    <h1>Rapport des Utilisateurs</h1>
    <div class="stats">
        <h2>Statistiques</h2>
        <p><strong>Nombre total:</strong> {total}</p>
        <p><strong>Âge moyen:</strong> {age_moyen:.1f} ans</p>
        <p><strong>Salaire moyen:</strong> {salaire_moyen:.0f} €</p>
    </div>
    
    <h2>Détails des Utilisateurs</h2>
    <table>
        <tr>
            <th>Nom</th>
            <th>Âge</th>
            <th>Ville</th>
            <th>Salaire</th>
        </tr>
        {lignes_tableau}
    </table>
    
    <p><em>Rapport généré le {date}</em></p>
</body>
</html>"""

        # Calculer statistiques
        total = len(donnees)
        age_moyen = sum(u["age"] for u in donnees) / total
        salaire_moyen = sum(u["salaire"] for u in donnees) / total

        # Générer lignes du tableau
        lignes = []
        for user in donnees:
            ligne = f"""        <tr>
            <td>{user['nom']}</td>
            <td>{user['age']}</td>
            <td>{user['ville']}</td>
            <td>{user['salaire']:,} €</td>
        </tr>"""
            lignes.append(ligne)

        lignes_tableau = "\n".join(lignes)

        # Remplacer les placeholders
        html_final = html.format(
            total=total,
            age_moyen=age_moyen,
            salaire_moyen=salaire_moyen,
            lignes_tableau=lignes_tableau,
            date=datetime.now().strftime("%d/%m/%Y à %H:%M")
        )

        with open(nom_fichier, "w", encoding="utf-8") as fichier:
            fichier.write(html_final)

    generer_rapport_html(donnees_utilisateurs, "rapport.html")
    print(f"      ✅ Rapport HTML généré : 'rapport.html'")

    print("\n   5️⃣ Écriture de log structuré :")

    def ecrire_log_structure(nom_fichier, evenements):
        """Écrire un log structuré"""
        with open(nom_fichier, "w", encoding="utf-8") as fichier:
            for evenement in evenements:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ligne_log = f"[{timestamp}] {evenement['niveau'].upper():<7} {evenement['module']:<15} {evenement['message']}\n"
                fichier.write(ligne_log)

    evenements_log = [
        {"niveau": "info", "module": "auth",
            "message": "Utilisateur connecté: alice@test.com"},
        {"niveau": "warning", "module": "database",
            "message": "Connexion lente: 2.5s"},
        {"niveau": "error", "module": "payment",
            "message": "Échec paiement: carte expirée"},
        {"niveau": "info", "module": "auth",
            "message": "Utilisateur déconnecté: alice@test.com"},
        {"niveau": "debug", "module": "cache",
            "message": "Cache vidé: 1250 entrées supprimées"},
    ]

    ecrire_log_structure("application.log", evenements_log)
    print(f"      ✅ Log structuré écrit : 'application.log'")

    # Affichage des tailles de fichiers créés
    print("\n   📊 Tailles des fichiers créés :")
    fichiers_crees = [
        "utilisateurs_manuel.csv", "utilisateurs_module.csv",
        "donnees_formatees.json", "donnees_compactes.json",
        "config.ini", "rapport.html", "application.log"
    ]

    for fichier in fichiers_crees:
        if os.path.exists(fichier):
            taille = os.path.getsize(fichier)
            print(f"      📄 {fichier}: {taille} octets")

    # Nettoyage
    for fichier in fichiers_crees:
        if os.path.exists(fichier):
            os.remove(fichier)


demo_ecriture_formats()

print("\n🗂️ ÉCRITURE AVEC PATHLIB")
print("-" * 25)


def demo_pathlib_ecriture():
    """Démonstration d'écriture avec pathlib"""

    print("🗂️ Écriture moderne avec pathlib :")

    # Créer structure de répertoires
    base_dir = Path("demo_pathlib_write")
    base_dir.mkdir(exist_ok=True)

    print("\n   1️⃣ Écriture simple avec pathlib :")

    # Écriture directe
    (base_dir / "simple.txt").write_text("Contenu simple avec pathlib", encoding="utf-8")
    print(f"      ✅ Fichier écrit: simple.txt")

    # Écriture binaire
    (base_dir / "binaire.bin").write_bytes(b"Contenu binaire")
    print(f"      ✅ Fichier binaire écrit: binaire.bin")

    print("\n   2️⃣ Création de structure complexe :")

    # Créer sous-répertoires et fichiers
    structure = {
        "docs": ["readme.txt", "changelog.txt", "license.txt"],
        "src": ["main.py", "utils.py", "config.py"],
        "tests": ["test_main.py", "test_utils.py"],
        "data": ["sample.json", "config.ini"]
    }

    for repertoire, fichiers in structure.items():
        sous_dir = base_dir / repertoire
        sous_dir.mkdir(exist_ok=True)

        for fichier in fichiers:
            chemin_fichier = sous_dir / fichier
            contenu = f"Contenu généré pour {repertoire}/{fichier}\nCréé le {datetime.now()}\n"
            chemin_fichier.write_text(contenu, encoding="utf-8")

        print(f"      📁 {repertoire}/: {len(fichiers)} fichiers créés")

    print("\n   3️⃣ Écriture conditionnelle :")

    def ecrire_si_nexiste_pas(chemin, contenu):
        """Écrire seulement si le fichier n'existe pas"""
        if not chemin.exists():
            chemin.write_text(contenu, encoding="utf-8")
            print(f"      ✅ Créé: {chemin.name}")
            return True
        else:
            print(f"      ⚠️ Existe déjà: {chemin.name}")
            return False

    # Tests d'écriture conditionnelle
    ecrire_si_nexiste_pas(base_dir / "nouveau.txt", "Nouveau fichier")
    ecrire_si_nexiste_pas(base_dir / "nouveau.txt", "Tentative réécriture")
    ecrire_si_nexiste_pas(base_dir / "autre.txt", "Autre nouveau fichier")

    print("\n   4️⃣ Statistiques des fichiers créés :")

    total_fichiers = 0
    total_taille = 0

    for fichier in base_dir.rglob("*"):
        if fichier.is_file():
            taille = fichier.stat().st_size
            total_fichiers += 1
            total_taille += taille
            print(f"      📄 {fichier.relative_to(base_dir)}: {taille} octets")

    print(f"\n      📊 Total: {total_fichiers} fichiers, {total_taille} octets")

    # Nettoyage
    shutil.rmtree(base_dir)


demo_pathlib_ecriture()

print("\n" + "=" * 50)
print("4. RÉSUMÉ FINAL")
print("=" * 50)

print("""
🎯 POINTS CLÉS À RETENIR :

1. ✍️ MODES D'ÉCRITURE :
   • 'w' : écriture avec écrasement
   • 'a' : écriture en ajout
   • 'x' : écriture exclusive (échec si existe)
   • '+' : lecture/écriture combinées

2. 🔧 MÉTHODES D'ÉCRITURE :
   • write() : écrire une chaîne
   • writelines() : écrire une liste de lignes
   • print(..., file=f) : print vers fichier
   • flush() : forcer écriture sur disque

3. 🚨 GESTION D'ERREURS :
   • PermissionError : droits insuffisants
   • FileExistsError : fichier existe (mode 'x')
   • IsADirectoryError : chemin vers répertoire
   • UnicodeEncodeError : problème d'encodage

4. 🛡️ ÉCRITURE SÉCURISÉE :
   • Écriture atomique avec fichiers temporaires
   • Backup avant modification
   • Vérifications post-écriture
   • Gestion d'espace disque

5. 📄 FORMATS SPÉCIALISÉS :
   • CSV avec module csv
   • JSON avec module json
   • HTML avec templates
   • Logs structurés

💡 BONNES PRATIQUES :
✅ Toujours utiliser with pour ouvrir fichiers
✅ Spécifier l'encodage explicitement
✅ Faire des écritures atomiques pour données critiques
✅ Gérer les erreurs spécifiques
✅ Utiliser flush() pour données importantes

🚨 À ÉVITER :
❌ Oublier de fermer les fichiers
❌ Écraser des fichiers sans backup
❌ Ignorer les erreurs d'écriture
❌ Pas de gestion d'espace disque
❌ Encodage incorrect pour caractères spéciaux

⚡ OPTIMISATIONS :
• Buffering approprié pour performance
• Écriture par chunks pour gros volumes
• Compression pour fichiers volumineux
• Validation avant écriture
• Atomic operations pour cohérence

🔧 PATTERNS AVANCÉS :
• Context managers personnalisés
• Templates pour génération
• Factory patterns pour formats
• Observer pattern pour monitoring
• Strategy pattern pour différents formats

🎉 Félicitations ! Écriture de fichiers maîtrisée !
💡 Prochaine étape : Context managers !
📚 Fichiers écrits, contextes à gérer !
""")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE - ÉCRITURE DE FICHIERS MAÎTRISÉE !")
print("=" * 70)
