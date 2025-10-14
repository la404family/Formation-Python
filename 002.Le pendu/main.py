"""
Jeu du Pendu - Application principale
=====================================

Ce programme implémente un jeu du pendu complet avec interface graphique tkinter.

Fonctionnalités :
- Interface graphique intuitive avec art ASCII
- Gestion automatique des accents (é→e, è→e, ç→c, etc.)
- Statistiques détaillées sauvegardées automatiquement
- Conservation des tirets et apostrophes dans les mots
- Gestion des erreurs robuste
- Plus de 100,000 mots français

Architecture :
- data_manager.py : Gestion des données (mots, statistiques)
- game_logic.py : Logique du jeu et art ASCII
- ui_components.py : Interface utilisateur tkinter
- main.py : Point d'entrée de l'application

Auteur : Formation Python
Version : 1.0
"""

# Importation des modules nécessaires
import tkinter as tk
from tkinter import messagebox
import sys
import os

# Importation des modules du jeu
from ui_components import lancer_jeu


def main():
    """
    Fonction principale qui lance le jeu du pendu.

    Cette fonction :
    1. Vérifie que tous les fichiers nécessaires sont présents
    2. Initialise l'environnement de jeu
    3. Lance l'interface graphique
    """
    print("🎯 Démarrage du Jeu du Pendu 🎯")
    print("=" * 40)

    try:
        # Vérification des fichiers essentiels
        fichiers_requis = ["mots.json"]
        fichiers_manquants = []

        for fichier in fichiers_requis:
            if not os.path.exists(fichier):
                fichiers_manquants.append(fichier)

        # Si des fichiers sont manquants, affiche un message d'erreur
        if fichiers_manquants:
            message_erreur = f"Fichiers manquants : {', '.join(fichiers_manquants)}"
            print(f"❌ Erreur : {message_erreur}")

            # Essaie d'afficher une boîte de dialogue d'erreur
            try:
                root = tk.Tk()
                root.withdraw()  # Cache la fenêtre principale
                messagebox.showerror("Fichiers manquants", message_erreur)
                root.destroy()
            except:
                pass

            return False

        print("✓ Tous les fichiers nécessaires sont présents")
        print("✓ Lancement de l'interface graphique...")
        print()

        # Lance le jeu
        lancer_jeu()

        print("🎯 Merci d'avoir joué au Jeu du Pendu ! À bientôt ! 👋")
        return True

    except ImportError as e:
        print(f"❌ Erreur d'importation : {e}")
        print("Vérifiez que tous les modules sont présents dans le dossier.")
        return False

    except Exception as e:
        print(f"❌ Erreur inattendue : {e}")
        print("Contactez le développeur si le problème persiste.")

        # Essaie d'afficher une boîte de dialogue d'erreur
        try:
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror(
                "Erreur", f"Une erreur inattendue est survenue :\n{e}")
            root.destroy()
        except:
            pass

        return False


def afficher_aide():
    """
    Affiche les instructions et l'aide pour jouer au jeu du pendu.
    """
    aide = """
🎯 JEU DU PENDU - AIDE 🎯
========================

OBJECTIF :
Devinez le mot secret en proposant des lettres une par une.
Vous avez droit à 6 erreurs maximum !

COMMENT JOUER :
1. Un mot secret est choisi aléatoirement
2. Tapez une lettre sur votre clavier
3. Si la lettre est dans le mot, elle s'affiche
4. Sinon, une partie du pendu se dessine
5. Trouvez le mot avant que le pendu soit complet !

FONCTIONNALITÉS :
✓ Plus de 100,000 mots français
✓ Gestion automatique des accents (é→e, ç→c, etc.)
✓ Statistiques détaillées sauvegardées
✓ Interface graphique intuitive
✓ Art ASCII du pendu

CONSEILS :
• Commencez par les voyelles (A, E, I, O, U)
• Puis essayez les consonnes fréquentes (S, T, R, N, L)
• Les tirets et apostrophes sont toujours visibles
• Utilisez les statistiques pour suivre vos progrès

RACCOURCIS :
• Tapez directement une lettre (pas besoin d'Entrée)
• F5 ou "Nouvelle Partie" pour recommencer
• Échap ou "Quitter" pour sortir

Amusez-vous bien ! 🎉
    """
    print(aide)


if __name__ == "__main__":
    """
    Point d'entrée du programme.
    Analyse les arguments de ligne de commande et lance l'application appropriée.
    """
    # Vérifie les arguments de ligne de commande
    if len(sys.argv) > 1:
        if sys.argv[1] in ["-h", "--help", "aide"]:
            afficher_aide()
        elif sys.argv[1] in ["-v", "--version"]:
            print("Jeu du Pendu - Version 1.0")
            print("Développé pour la Formation Python")
        else:
            print(f"Argument non reconnu : {sys.argv[1]}")
            print("Utilisez -h ou --help pour l'aide")
    else:
        # Lance le jeu normalement
        success = main()
        sys.exit(0 if success else 1)
