"""
Module contenant la logique du jeu du pendu.
Ce module gère l'état du jeu, les propositions de lettres et les dessins ASCII.
"""

import random
import os
from data_manager import DataManager, normaliser_texte


class AnimationManager:
    """
    Classe qui gère les animations du pendu.
    Contient les chemins vers les 8 animations (de 0 à 7 erreurs).
    """

    def __init__(self):
        """
        Initialise les chemins vers les animations du pendu.
        Animation 1 = état initial (0 erreur)
        Animation 7 = fin lors de l'échec (6 erreurs max)
        """
        # Chemin de base vers le dossier images
        self.chemin_images = os.path.join(os.path.dirname(__file__), "images")

        # Liste des dossiers d'animations (animation01 a animation08)
        # animation01-07 : erreurs (0 à 6)
        # animation08 : victoire
        self.animations = []
        for i in range(1, 9):  # 1 à 8 inclus
            dossier_animation = f"animation{i:02d}"
            chemin_animation = os.path.join(
                self.chemin_images, dossier_animation)
            self.animations.append(chemin_animation)

    def obtenir_chemin_animation(self, nb_erreurs):
        """
        Retourne le chemin vers le dossier d'animation correspondant au nombre d'erreurs.

        Args:
            nb_erreurs (int): Nombre d'erreurs (0 à 6)

        Returns:
            str: Chemin vers le dossier d'animation
        """
        # S'assure que le nombre d'erreurs est dans la plage valide
        if nb_erreurs < 0:
            nb_erreurs = 0
        elif nb_erreurs > 6:  # Maintenant 6 erreurs max (7 animations)
            nb_erreurs = 6

        return self.animations[nb_erreurs]

    def lister_images_animation(self, nb_erreurs):
        """
        Retourne la liste des fichiers images dans le dossier d'animation.

        Args:
            nb_erreurs (int): Nombre d'erreurs (0 à 6)

        Returns:
            list: Liste des chemins vers les images de l'animation
        """
        dossier_animation = self.obtenir_chemin_animation(nb_erreurs)

        if not os.path.exists(dossier_animation):
            return []

        # Extensions d'images supportées
        extensions_images = {'.png', '.jpg', '.jpeg', '.gif', '.bmp'}

        images = []
        try:
            fichiers = os.listdir(dossier_animation)
            for fichier in sorted(fichiers):  # Tri pour ordre cohérent
                if any(fichier.lower().endswith(ext) for ext in extensions_images):
                    chemin_complet = os.path.join(dossier_animation, fichier)
                    images.append(chemin_complet)
        except OSError:
            pass  # Dossier inaccessible

        return images

    def obtenir_animation_victoire(self):
        """
        Retourne le chemin vers le dossier d'animation de victoire (animation8).

        Returns:
            str: Chemin vers le dossier d'animation de victoire
        """
        # Le dossier de victoire s'appelle "animation8" (sans le 0)
        return os.path.join(self.chemin_images, "animation8")

    def lister_images_animation_victoire(self):
        """
        Retourne la liste des fichiers images dans le dossier d'animation de victoire.

        Returns:
            list: Liste des chemins vers les images de l'animation de victoire
        """
        dossier_animation = self.obtenir_animation_victoire()

        if not os.path.exists(dossier_animation):
            return []

        # Extensions d'images supportées
        extensions_images = {'.png', '.jpg', '.jpeg', '.gif', '.bmp'}

        images = []
        try:
            fichiers = os.listdir(dossier_animation)
            for fichier in sorted(fichiers):  # Tri pour ordre cohérent
                if any(fichier.lower().endswith(ext) for ext in extensions_images):
                    chemin_complet = os.path.join(dossier_animation, fichier)
                    images.append(chemin_complet)
        except OSError:
            pass  # Dossier inaccessible

        return images

    def obtenir_dessin(self, nb_erreurs):
        """
        Retourne le chemin vers le dossier d'animation correspondant au nombre d'erreurs.

        Args:
            nb_erreurs (int): Nombre d'erreurs (0 à 6)

        Returns:
            str: Chemin vers le dossier d'animation du pendu
        """
        return self.obtenir_chemin_animation(nb_erreurs)


class GameManager:
    """
    Classe principale qui gère la logique du jeu du pendu.
    Elle s'occupe de l'état du jeu, des propositions de lettres et des conditions de victoire/défaite.
    """

    def __init__(self):
        """
        Initialise le gestionnaire de jeu.
        """
        # Gestionnaire de données pour charger les mots et stats
        self.data_manager = DataManager()

        # Gestionnaire d'animations
        self.animation_manager = AnimationManager()

        # Variables de jeu - seront initialisées lors d'une nouvelle partie
        self.mot_secret = ""           # Le mot à deviner (normalisé)
        self.mot_original = ""         # Le mot original (avec accents)
        self.mot_affiche = ""          # Le mot affiché avec les lettres trouvées
        self.lettres_essayees = set()  # Ensemble des lettres déjà essayées
        self.lettres_correctes = set()  # Ensemble des lettres correctes trouvées
        self.lettres_incorrectes = set()  # Ensemble des lettres incorrectes
        self.erreurs = 0               # Nombre d'erreurs actuelles
        # Nombre maximum d'erreurs autorisées (7 animations : 0 à 6)
        self.max_erreurs = 6

        # État du jeu
        self.partie_terminee = False   # True si la partie est finie

        # Charge les données au démarrage
        self.data_manager.charger_mots()
        self.data_manager.charger_stats()

    def nouvelle_partie(self):
        """
        Démarre une nouvelle partie en sélectionnant un mot aléatoire
        et en réinitialisant toutes les variables de jeu.

        Returns:
            bool: True si une nouvelle partie a pu commencer, False sinon
        """
        # Vérifie qu'il y a des mots disponibles
        if not self.data_manager.mots:
            print("Erreur : Aucun mot disponible pour jouer.")
            return False

        # Sélectionne un mot aléatoire
        self.mot_original = random.choice(self.data_manager.mots)
        self.mot_secret = normaliser_texte(self.mot_original)

        # Réinitialise les variables de jeu
        self.lettres_essayees = set()
        self.lettres_correctes = set()
        self.lettres_incorrectes = set()
        self.erreurs = 0
        self.partie_terminee = False

        # Met à jour l'affichage du mot
        self.mettre_a_jour_mot_affiche()

        print(
            f"✓ Nouvelle partie commencée ! Mot à deviner : {len(self.mot_secret)} lettres")
        # Pour le développement
        print(f"Debug - Mot secret : {self.mot_secret}")

        return True

    def mettre_a_jour_mot_affiche(self):
        """
        Met à jour la représentation affichée du mot.
        Les lettres trouvées sont affichées, les autres remplacées par des underscores.
        Les tirets et apostrophes sont toujours visibles.

        Exemple : "SAINT-PIERRE" avec les lettres S,A,I,N,T trouvées donne "S A I N T - _ I _ _ _ _"
        """
        mot_affiche = []

        for lettre in self.mot_secret:
            if lettre.isalpha():  # Si c'est une lettre
                if lettre in self.lettres_correctes:
                    mot_affiche.append(lettre)  # Affiche la lettre trouvée
                else:
                    mot_affiche.append("_")     # Affiche un underscore
            else:
                # Affiche les caractères non-alphabétiques (tirets, apostrophes, espaces)
                mot_affiche.append(lettre)

        # Joint avec des espaces pour une meilleure lisibilité
        self.mot_affiche = " ".join(mot_affiche)

    def proposer_lettre(self, lettre):
        """
        Traite une proposition de lettre du joueur.

        Args:
            lettre (str): La lettre proposée par le joueur

        Returns:
            dict: Dictionnaire contenant les informations sur le résultat de la proposition
        """
        # Normalise la lettre (majuscule, sans accent)
        lettre = normaliser_texte(lettre.strip())

        # Vérifie que c'est une seule lettre alphabétique
        if not lettre or len(lettre) != 1 or not lettre.isalpha():
            return {
                "valide": False,
                "message": "Veuillez entrer une seule lettre.",
                "type": "erreur"
            }

        # Vérifie si la lettre a déjà été essayée
        if lettre in self.lettres_essayees:
            return {
                "valide": False,
                "message": f"Vous avez déjà essayé la lettre '{lettre}'.",
                "type": "avertissement"
            }

        # Vérifie si la partie est terminée
        if self.partie_terminee:
            return {
                "valide": False,
                "message": "La partie est terminée. Commencez une nouvelle partie.",
                "type": "erreur"
            }

        # Ajoute la lettre aux lettres essayées
        self.lettres_essayees.add(lettre)

        # Vérifie si la lettre est dans le mot
        if lettre in self.mot_secret:
            # Lettre correcte
            self.lettres_correctes.add(lettre)
            self.mettre_a_jour_mot_affiche()

            # Compte combien de fois la lettre apparaît
            nb_occurrences = self.mot_secret.count(lettre)

            return {
                "valide": True,
                "correcte": True,
                "message": f"Bien joué ! La lettre '{lettre}' apparaît {nb_occurrences} fois.",
                "type": "succes"
            }
        else:
            # Lettre incorrecte
            self.lettres_incorrectes.add(lettre)
            self.erreurs += 1

            return {
                "valide": True,
                "correcte": False,
                "message": f"Dommage ! La lettre '{lettre}' n'est pas dans le mot.",
                "type": "erreur"
            }

    def est_gagne(self):
        """
        Vérifie si le joueur a gagné (toutes les lettres du mot ont été trouvées).

        Returns:
            bool: True si le joueur a gagné, False sinon
        """
        # Récupère toutes les lettres uniques du mot secret
        lettres_du_mot = set(
            lettre for lettre in self.mot_secret if lettre.isalpha())

        # Vérifie qu'il y a bien des lettres dans le mot
        if not lettres_du_mot:
            return False

        # Vérifie si toutes les lettres ont été trouvées
        return lettres_du_mot.issubset(self.lettres_correctes)

    def est_perdu(self):
        """
        Vérifie si le joueur a perdu (nombre maximum d'erreurs atteint).

        Returns:
            bool: True si le joueur a perdu, False sinon
        """
        return self.erreurs >= self.max_erreurs

    def obtenir_mot_affiche(self):
        """
        Retourne la représentation actuelle du mot à deviner.

        Returns:
            str: Le mot avec les lettres trouvées et les underscores
        """
        return self.mot_affiche

    def obtenir_lettres_essayees_formatees(self):
        """
        Retourne une chaîne formatée des lettres essayées.
        Les lettres correctes et incorrectes sont séparées.

        Returns:
            dict: Dictionnaire contenant les lettres formatées
        """
        correctes = sorted(list(self.lettres_correctes))
        incorrectes = sorted(list(self.lettres_incorrectes))

        return {
            "correctes": ", ".join(correctes) if correctes else "Aucune",
            "incorrectes": ", ".join(incorrectes) if incorrectes else "Aucune",
            "toutes": ", ".join(sorted(list(self.lettres_essayees))) if self.lettres_essayees else "Aucune"
        }

    def obtenir_dessin_pendu(self):
        """
        Retourne le chemin vers le dossier d'animation du pendu correspondant au nombre d'erreurs actuel.

        Returns:
            str: Chemin vers le dossier d'animation du pendu
        """
        return self.animation_manager.obtenir_dessin(self.erreurs)

    def obtenir_images_animation(self):
        """
        Retourne la liste des images de l'animation correspondant au nombre d'erreurs actuel.

        Returns:
            list: Liste des chemins vers les images de l'animation
        """
        return self.animation_manager.lister_images_animation(self.erreurs)

    def obtenir_animation_victoire(self):
        """
        Retourne le chemin vers le dossier d'animation de victoire.

        Returns:
            str: Chemin vers le dossier d'animation de victoire
        """
        return self.animation_manager.obtenir_animation_victoire()

    def obtenir_images_animation_victoire(self):
        """
        Retourne la liste des images de l'animation de victoire.

        Returns:
            list: Liste des chemins vers les images de l'animation de victoire
        """
        return self.animation_manager.lister_images_animation_victoire()

    def obtenir_info_jeu(self):
        """
        Retourne un dictionnaire contenant toutes les informations actuelles du jeu.

        Returns:
            dict: Informations complètes sur l'état du jeu
        """
        return {
            "mot_affiche": self.mot_affiche,
            "mot_original": self.mot_original,
            "mot_secret": self.mot_secret,
            "erreurs": self.erreurs,
            "max_erreurs": self.max_erreurs,
            "lettres_essayees": self.obtenir_lettres_essayees_formatees(),
            "dossier_animation": self.obtenir_dessin_pendu(),
            "images_animation": self.obtenir_images_animation(),
            "est_gagne": self.est_gagne(),
            "est_perdu": self.est_perdu(),
            "partie_terminee": self.partie_terminee
        }

    def terminer_partie(self):
        """
        Termine la partie actuelle et met à jour les statistiques.
        """
        if self.partie_terminee:
            return  # La partie est déjà terminée

        self.partie_terminee = True

        # Détermine si c'est une victoire
        victoire = self.est_gagne()

        # Met à jour les statistiques
        self.data_manager.mettre_a_jour_stats(
            victoire=victoire,
            mot_trouve=self.mot_original,
            nb_erreurs=self.erreurs
        )

        # Message de fin de partie
        if victoire:
            print(
                f"🎉 Félicitations ! Vous avez trouvé le mot '{self.mot_original}' avec {self.erreurs} erreur(s).")
        else:
            print(
                f"💀 Dommage ! Le mot était '{self.mot_original}'. Essayez encore !")

    def obtenir_statistiques(self):
        """
        Retourne les statistiques formatées du joueur.

        Returns:
            str: Statistiques formatées
        """
        return self.data_manager.obtenir_statistiques_formatees()
