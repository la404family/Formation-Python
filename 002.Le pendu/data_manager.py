"""
Module de gestion des données pour le jeu du pendu.
Ce module s'occupe du chargement des mots et de la gestion des statistiques.
"""

import json
import unicodedata
import os


def normaliser_texte(texte):
    """
    Normalise un texte en retirant les accents et en convertissant en majuscules.

    Exemples :
    - "été" devient "ETE"
    - "français" devient "FRANCAIS"
    - "saint-pierre" devient "SAINT-PIERRE" (conserve les tirets)
    - "aujourd'hui" devient "AUJOURD'HUI" (conserve les apostrophes)

    Args:
        texte (str): Le texte à normaliser

    Returns:
        str: Le texte normalisé (majuscules, sans accents)
    """
    # Supprime les accents en décomposant les caractères Unicode
    # puis en retirant les marques diacritiques (accents)
    texte_sans_accents = ''.join(
        char for char in unicodedata.normalize('NFD', texte)
        # 'Mn' = marques non-espacées (accents)
        if unicodedata.category(char) != 'Mn'
    )

    # Convertit en majuscules
    return texte_sans_accents.upper()


class DataManager:
    """
    Classe responsable de la gestion des données du jeu du pendu.
    Elle s'occupe du chargement des mots et de la gestion des statistiques.
    """

    def __init__(self):
        """
        Initialise le gestionnaire de données.
        Définit les chemins des fichiers de données.
        """
        # Chemin du fichier contenant la liste des mots
        self.fichier_mots = "mots.json"

        # Chemin du fichier des statistiques
        self.fichier_stats = "statistiques_pendu.json.json"

        # Variables pour stocker les données en mémoire
        self.mots = []  # Liste des mots chargés
        self.statistiques = {}  # Dictionnaire des statistiques

    def charger_mots(self):
        """
        Charge la liste des mots depuis le fichier mots.json.

        Returns:
            list: Liste des mots chargés, ou liste vide en cas d'erreur
        """
        try:
            # Vérifie si le fichier existe
            if not os.path.exists(self.fichier_mots):
                print(f"Erreur : Le fichier {self.fichier_mots} n'existe pas.")
                return []

            # Ouvre et lit le fichier JSON
            with open(self.fichier_mots, 'r', encoding='utf-8') as fichier:
                data = json.load(fichier)

                # Le fichier peut contenir soit directement une liste,
                # soit un dictionnaire avec une clé 'mots'
                if isinstance(data, list):
                    self.mots = data
                elif isinstance(data, dict) and 'mots' in data:
                    self.mots = data['mots']
                else:
                    print("Format de fichier non reconnu.")
                    return []

                print(f"✓ {len(self.mots)} mots chargés avec succès.")
                return self.mots

        except json.JSONDecodeError as e:
            print(f"Erreur lors de la lecture du fichier JSON : {e}")
            return []
        except Exception as e:
            print(f"Erreur inattendue lors du chargement des mots : {e}")
            return []

    def charger_stats(self):
        """
        Charge les statistiques depuis le fichier.
        Si le fichier n'existe pas, initialise des statistiques par défaut.

        Returns:
            dict: Dictionnaire contenant les statistiques
        """
        try:
            # Vérifie si le fichier de statistiques existe
            if os.path.exists(self.fichier_stats):
                with open(self.fichier_stats, 'r', encoding='utf-8') as fichier:
                    self.statistiques = json.load(fichier)
                    print("✓ Statistiques chargées.")
            else:
                # Initialise des statistiques par défaut
                self.statistiques = {
                    "parties_jouees": 0,      # Nombre total de parties
                    "parties_gagnees": 0,     # Nombre de parties gagnées
                    "parties_perdues": 0,     # Nombre de parties perdues
                    "pourcentage_victoire": 0,  # Pourcentage de victoires
                    "mot_le_plus_long": "",   # Le mot le plus long trouvé
                    # Score le plus bas (moins d'erreurs)
                    "meilleur_score": 0,
                    "total_erreurs": 0,       # Total des erreurs commises
                    "mots_trouves": []        # Liste des mots trouvés
                }
                print("✓ Statistiques initialisées avec les valeurs par défaut.")

            return self.statistiques

        except json.JSONDecodeError as e:
            print(f"Erreur lors de la lecture des statistiques : {e}")
            # Retourne des stats par défaut en cas d'erreur
            return self.charger_stats_par_defaut()
        except Exception as e:
            print(
                f"Erreur inattendue lors du chargement des statistiques : {e}")
            return self.charger_stats_par_defaut()

    def charger_stats_par_defaut(self):
        """
        Retourne des statistiques par défaut.

        Returns:
            dict: Statistiques par défaut
        """
        self.statistiques = {
            "parties_jouees": 0,
            "parties_gagnees": 0,
            "parties_perdues": 0,
            "pourcentage_victoire": 0,
            "mot_le_plus_long": "",
            "meilleur_score": 0,
            "total_erreurs": 0,
            "mots_trouves": []
        }
        return self.statistiques

    def sauvegarder_stats(self):
        """
        Sauvegarde les statistiques dans le fichier.
        Cette méthode est appelée après chaque partie terminée.

        Returns:
            bool: True si la sauvegarde a réussi, False sinon
        """
        try:
            # Calcule le pourcentage de victoire
            if self.statistiques["parties_jouees"] > 0:
                self.statistiques["pourcentage_victoire"] = round(
                    (self.statistiques["parties_gagnees"] /
                     self.statistiques["parties_jouees"]) * 100, 1
                )

            # Sauvegarde dans le fichier
            with open(self.fichier_stats, 'w', encoding='utf-8') as fichier:
                json.dump(self.statistiques, fichier,
                          indent=2, ensure_ascii=False)

            print("✓ Statistiques sauvegardées.")
            return True

        except Exception as e:
            print(f"Erreur lors de la sauvegarde des statistiques : {e}")
            return False

    def mettre_a_jour_stats(self, victoire, mot_trouve, nb_erreurs):
        """
        Met à jour les statistiques après une partie.

        Args:
            victoire (bool): True si le joueur a gagné
            mot_trouve (str): Le mot qui était à deviner
            nb_erreurs (int): Nombre d'erreurs commises
        """
        # Incrémente le nombre de parties jouées
        self.statistiques["parties_jouees"] += 1

        # Met à jour selon le résultat
        if victoire:
            self.statistiques["parties_gagnees"] += 1

            # Ajoute le mot à la liste des mots trouvés (s'il n'y est pas déjà)
            if mot_trouve not in self.statistiques["mots_trouves"]:
                self.statistiques["mots_trouves"].append(mot_trouve)

            # Met à jour le mot le plus long trouvé
            if len(mot_trouve) > len(self.statistiques["mot_le_plus_long"]):
                self.statistiques["mot_le_plus_long"] = mot_trouve

            # Met à jour le meilleur score (moins d'erreurs = meilleur score)
            if self.statistiques["meilleur_score"] == 0 or nb_erreurs < self.statistiques["meilleur_score"]:
                self.statistiques["meilleur_score"] = nb_erreurs
        else:
            self.statistiques["parties_perdues"] += 1

        # Ajoute les erreurs au total
        self.statistiques["total_erreurs"] += nb_erreurs

        # Sauvegarde automatiquement
        self.sauvegarder_stats()

    def obtenir_statistiques_formatees(self):
        """
        Retourne les statistiques sous forme de texte formaté pour l'affichage.

        Returns:
            str: Statistiques formatées
        """
        stats = self.statistiques

        # Calcule la moyenne d'erreurs par partie
        if stats["parties_jouees"] > 0:
            moyenne_erreurs = round(
                stats["total_erreurs"] / stats["parties_jouees"], 1)
        else:
            moyenne_erreurs = 0

        # Formate le texte des statistiques
        texte_stats = f"""📊 STATISTIQUES 📊
        
Parties jouées : {stats['parties_jouees']}
Victoires : {stats['parties_gagnees']}
Défaites : {stats['parties_perdues']}
Taux de réussite : {stats['pourcentage_victoire']}%

Mot le plus long trouvé : {stats['mot_le_plus_long'] or 'Aucun'}
Meilleur score : {stats['meilleur_score']} erreur(s)
Moyenne d'erreurs : {moyenne_erreurs}

Mots trouvés : {len(stats['mots_trouves'])}"""

        return texte_stats
