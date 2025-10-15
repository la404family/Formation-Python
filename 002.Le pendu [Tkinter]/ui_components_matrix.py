"""
Module contenant les composants de l'interface utilisateur pour le jeu du pendu.
Ce module utilise tkinter pour créer une interface graphique complète avec style Matrix.

Fonctionnalités :
- Interface graphique style Matrix (vert sur noir)
- Affichage d'animations au lieu d'ASCII art
- Gestion événementielle robuste
- Validation complète des saisies
- Focus automatique et UX optimisée
"""

import tkinter as tk
from tkinter import messagebox, font
from PIL import Image, ImageTk
import os
import threading
import time
from game_logic import GameManager
from data_manager import DataManager


# =============================================================================
# STYLE HYBRIDE - MATRIX + WINDOWS 95
# =============================================================================
class CouleursHybride:
    """
    Classe contenant toutes les constantes de couleurs et styles.
    Theme hybride : Matrix pour certains éléments, Windows 95 pour l'interface.
    """

    # Couleurs Matrix (pour mot, stats, animation)
    FOND_NOIR = "#000000"           # Noir pur (Matrix)
    VERT_MATRIX = "#00FF00"         # Vert Matrix principal
    VERT_FONCE = "#008000"          # Vert foncé pour les variations
    VERT_CLAIR = "#00FF41"          # Vert Matrix brillant
    VERT_SOMBRE = "#003300"         # Vert très sombre pour les panneaux

    # Couleurs Windows 95
    GRIS_WIN95 = "#C0C0C0"          # Gris Windows 95 classique
    GRIS_FONCE_WIN95 = "#808080"    # Gris foncé Windows 95
    GRIS_CLAIR_WIN95 = "#E0E0E0"    # Gris clair Windows 95
    BLEU_WIN95 = "#000080"          # Bleu Windows 95
    ROUGE_WIN95 = "#800000"         # Rouge Windows 95
    NOIR_WIN95 = "#000000"          # Noir Windows 95
    BLANC_WIN95 = "#FFFFFF"         # Blanc Windows 95

    # Couleurs contextuelles Matrix
    TEXTE_MATRIX_NORMAL = "#00FF00"    # Vert Matrix normal
    TEXTE_MATRIX_SUCCES = "#00FF41"    # Vert brillant (succès)
    TEXTE_MATRIX_ERREUR = "#FF0000"    # Rouge (erreurs)
    TEXTE_MATRIX_AVERTISSEMENT = "#FFFF00"  # Jaune (avertissements)
    TEXTE_MATRIX_INFO = "#00FFFF"      # Cyan (informations)

    # Couleurs contextuelles Windows 95
    TEXTE_WIN95_NORMAL = "#000000"     # Noir standard
    TEXTE_WIN95_ERREUR = "#800000"     # Rouge Windows 95
    TEXTE_WIN95_SUCCES = "#008000"     # Vert Windows 95

    # Animation et effets
    # Taille fixe des images
    ANIMATION_SIZE = (252, 252)

    # Polices
    POLICE_WIN95 = None             # Sera chargée dynamiquement
    POLICE_MATRIX = ("Courier New", 12, "bold")
    POLICE_TITRE_MATRIX = ("Courier New", 24, "bold")
    POLICE_STATS_MATRIX = ("Courier New", 10, "normal")
    POLICE_WIN95_NORMALE = ("MS Sans Serif", 8)
    POLICE_WIN95_BOUTON = ("MS Sans Serif", 8, "bold")


class AnimationPlayer:
    """
    Classe pour gérer la lecture des animations du pendu.
    SYSTÈME SIMPLE : Une seule animation à la fois, pas de file d'attente.
    """

    def __init__(self, label_widget):
        self.label = label_widget
        self.images = []
        self.current_frame = 0
        self.is_playing = False
        self.animation_thread = None
        self.current_animation_level = 0  # Niveau d'animation actuel (0-6)
        self.all_animations = {}  # Stocke toutes les animations chargées
        # Bloque les nouvelles animations d'erreur
        self.is_error_animation_playing = False

    def get_optimal_size(self, force_recalculate=False):
        """
        Retourne la taille fixe des animations (252x252).

        Args:
            force_recalculate (bool): Ignoré, la taille est maintenant fixe

        Returns:
            tuple: (largeur, hauteur) fixes pour les images
        """
        # Taille fixe - plus de calcul dynamique
        return CouleursHybride.ANIMATION_SIZE

    def load_all_animations(self, game_manager):
        """Charge toutes les animations au démarrage."""
        self.all_animations = {}

        # Calcule la taille optimale
        optimal_size = self.get_optimal_size()

        # Charge les animations d'erreurs (0 à 6)
        for level in range(7):  # 0 à 6 erreurs
            images = []
            # Récupère les images pour ce niveau d'erreur
            image_paths = game_manager.animation_manager.lister_images_animation(
                level)

            for path in image_paths:
                try:
                    img = Image.open(path)
                    img = img.resize(optimal_size, Image.Resampling.LANCZOS)
                    photo = ImageTk.PhotoImage(img)
                    images.append(photo)
                except Exception as e:
                    print(f"Erreur lors du chargement de {path}: {e}")

            self.all_animations[level] = images

        # Charge l'animation de victoire (niveau spécial "victoire")
        victory_images = []
        victory_paths = game_manager.animation_manager.lister_images_animation_victoire()

        for path in victory_paths:
            try:
                img = Image.open(path)
                img = img.resize(optimal_size, Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                victory_images.append(photo)
            except Exception as e:
                print(
                    f"Erreur lors du chargement de l'animation de victoire {path}: {e}")

        self.all_animations["victoire"] = victory_images
        print(f"Animation de victoire chargée : {len(victory_images)} images")

        # Lance l'animation initiale (niveau 0) en boucle
        self.start_initial_animation()

    def load_animation(self, image_paths):
        """Charge une animation à partir d'une liste de chemins d'images (méthode de compatibilité)."""
        self.images = []
        optimal_size = self.get_optimal_size()

        for path in image_paths:
            try:
                img = Image.open(path)
                img = img.resize(optimal_size, Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                self.images.append(photo)
            except Exception as e:
                print(f"Erreur lors du chargement de {path}: {e}")

        if self.images:
            self.label.config(image=self.images[0])
            self.label.image = self.images[0]

    def start_initial_animation(self):
        """Lance l'animation initiale (niveau 0) en boucle continue."""
        # Remet à zéro et vide la file
        self.is_error_animation_playing = False
        if hasattr(self, 'animation_queue'):
            self.animation_queue.clear()

        if 0 in self.all_animations and self.all_animations[0]:
            self.current_animation_level = 0
            self.images = self.all_animations[0]
            self.stop_animation()
            self.is_playing = True
            self.animation_thread = threading.Thread(
                target=self._animate_loop_continuous,
                daemon=True
            )
            self.animation_thread.start()

    def continue_current_animation(self):
        """Continue l'animation actuelle si ce n'est pas une animation d'erreur figée."""
        if self.current_animation_level == 0 and not self.is_playing:
            # Relance l'animation initiale si elle s'est arrêtée
            self.start_initial_animation()
        # Pour les autres niveaux, l'animation reste figée sur la dernière image

    def play_victory_animation(self):
        """Lance l'animation de victoire une seule fois."""
        if "victoire" not in self.all_animations or not self.all_animations["victoire"]:
            print("Animation de victoire non disponible")
            return

        # Vérifie si l'animation de victoire est déjà en cours
        if hasattr(self, 'victory_animation_played') and self.victory_animation_played:
            print("Animation de victoire déjà jouée - ignorée")
            return

        print("Lancement de l'animation de victoire")

        # Marque que l'animation de victoire va être jouée
        self.victory_animation_played = True

        # Arrête toute animation en cours
        self.stop_animation()
        self.is_error_animation_playing = False

        # Vide la file d'attente des animations d'erreur
        if hasattr(self, 'animation_queue'):
            self.animation_queue.clear()

        # Configure l'animation de victoire
        self.current_animation_level = "victoire"
        self.images = self.all_animations["victoire"]
        self.is_playing = True

        # Lance l'animation de victoire en une seule fois (pas en boucle)
        self.animation_thread = threading.Thread(
            target=self._animate_victory_once,
            daemon=True
        )
        self.animation_thread.start()

    def _animate_victory_once(self):
        """Animation de victoire qui se joue une seule fois."""
        if not self.images:
            print("Pas d'images pour l'animation de victoire")
            return

        print(f"Début animation de victoire : {len(self.images)} images")

        for i, img in enumerate(self.images):
            if not self.is_playing:
                print("Animation de victoire interrompue")
                break

            print(f"Frame victoire {i+1}/{len(self.images)}")
            # Met à jour l'image dans le thread principal
            self.label.after(0, self._update_image, img)

            # Délai entre les frames (plus lent pour la victoire)
            time.sleep(0.5)  # 500ms entre chaque frame pour plus de visibilité

        print("Animation de victoire terminée - ARRÊT")

        # Arrête explicitement l'animation
        self.is_playing = False

        # Reste sur la dernière image de victoire
        if self.images:
            self.label.after(0, self._update_image, self.images[-1])
            print("Affichage de la dernière image de victoire")

    def play_error_animation(self, error_level, delay_before_start=2.0):
        """Ajoute l'animation à la file d'attente - N'exécute JAMAIS directement."""
        if error_level not in self.all_animations:
            return

        print(f"Ajout animation niveau {error_level} à la file")

        # Ajoute TOUJOURS à la file, même si une animation est en cours
        if not hasattr(self, 'animation_queue'):
            self.animation_queue = []

        self.animation_queue.append((error_level, delay_before_start))

        # Démarre le traitement de la file si elle n'est pas en cours
        if not self.is_error_animation_playing:
            self._process_next_animation()

    def _process_next_animation(self):
        """Traite la prochaine animation dans la file."""
        if not self.animation_queue or self.is_error_animation_playing:
            return

        # Récupère la prochaine animation
        error_level, delay_before_start = self.animation_queue.pop(0)
        print(
            f"Traitement animation niveau {error_level} (reste {len(self.animation_queue)} en file)")

        # Marque qu'une animation est en cours
        self.is_error_animation_playing = True

        # Programme l'animation avec délai
        self.label.after(int(delay_before_start * 1000),
                         lambda: self._start_error_animation(error_level))

    def _start_error_animation(self, error_level):
        """Démarre une animation d'erreur spécifique."""
        print(f"Début animation niveau {error_level}")

        if error_level in self.all_animations:
            self.current_animation_level = error_level
            self.images = self.all_animations[error_level]

            if self.images:
                # Arrête l'animation en cours
                self.stop_animation()

                # Démarre l'animation frame par frame
                self._animate_error_frames(0)

    def _animate_error_frames(self, frame_index):
        """Anime les frames d'erreur une par une."""
        if frame_index >= len(self.images):
            # Animation terminée
            print(f"Animation niveau {self.current_animation_level} terminée")
            self.is_error_animation_playing = False

            # Traite la prochaine animation dans la file
            self.label.after(100, self._process_next_animation)
            return

        # Affiche la frame actuelle
        img = self.images[frame_index]
        self.label.config(image=img)
        self.label.image = img

        # Programme la prochaine frame
        self.label.after(
            400, lambda: self._animate_error_frames(frame_index + 1))

    def _play_single_error_animation(self, error_level, delay_before_start):
        """Joue UNE SEULE animation d'erreur de manière complète."""
        try:
            # Arrête l'animation initiale
            self.stop_animation()

            # Attend le délai
            print(f"Attente {delay_before_start} secondes...")
            time.sleep(delay_before_start)

            # Change le niveau et les images
            self.current_animation_level = error_level
            self.images = self.all_animations[error_level]

            if self.images:
                print(
                    f"Début animation {error_level} ({len(self.images)} frames)")

                # Joue chaque frame
                for i, img in enumerate(self.images):
                    if not self.is_error_animation_playing:
                        break

                    # Met à jour l'image de manière thread-safe
                    self.label.after(
                        0, lambda image=img: self._update_image_safe(image))
                    time.sleep(0.6)  # Délai entre frames

                # Reste sur la dernière image
                if self.images and self.is_error_animation_playing:
                    final_img = self.images[-1]
                    self.label.after(
                        0, lambda: self._update_image_safe(final_img))

                print(f"Animation {error_level} terminée")

        except Exception as e:
            print(f"Erreur animation {error_level}: {e}")

        finally:
            # Libère le verrou
            self.is_error_animation_playing = False

    def _update_image_safe(self, image):
        """Met à jour l'image de manière thread-safe."""
        try:
            if self.label.winfo_exists():
                self.label.config(image=image)
                self.label.image = image
        except Exception as e:
            print(f"Erreur mise à jour image: {e}")

    def _delayed_error_animation(self, error_level, delay_before_start):
        """DEPRECATED - Attend le délai puis lance l'animation d'erreur."""
        time.sleep(delay_before_start)

        if error_level in self.all_animations:
            self.current_animation_level = error_level
            self.images = self.all_animations[error_level]

            if self.images:
                self.is_playing = True
                # Joue l'animation une fois puis reste sur la dernière image
                self._animate_once_and_stop(0.6)  # Animation plus lente

    def _animate_loop_continuous(self):
        """Boucle d'animation continue (pour l'animation initiale)."""
        while self.is_playing and self.images:
            for img in self.images:
                if not self.is_playing:
                    break
                self.label.after(0, self._update_image, img)
                time.sleep(0.3)  # Vitesse normale pour l'animation continue

    def _animate_once_and_stop(self, delay):
        """Joue l'animation une fois et reste sur la dernière image."""
        if not self.images:
            return

        for i, img in enumerate(self.images):
            if not self.is_playing:
                break
            self.label.after(0, self._update_image, img)
            time.sleep(delay)

        # Reste sur la dernière image
        if self.images:
            self.label.after(0, self._update_image, self.images[-1])

        self.is_playing = False

    def _animate_once_and_stop_sync(self, delay):
        """Joue l'animation une fois et reste sur la dernière image (version synchrone)."""
        if not self.images:
            return

        for i, img in enumerate(self.images):
            if not self.is_playing:
                break
            # Utilise after_idle pour s'assurer que l'image est mise à jour
            self.label.after_idle(lambda img=img: self._update_image(img))
            # Force la mise à jour de l'affichage
            self.label.update_idletasks()
            time.sleep(delay)

        # Reste sur la dernière image
        if self.images:
            self.label.after_idle(lambda: self._update_image(self.images[-1]))
            self.label.update_idletasks()

        self.is_playing = False

    def play_animation(self, loop=False, delay=0.5):
        """Lance la lecture de l'animation (version simplifiée, une seule fois par défaut)."""
        if not self.images or self.is_playing:
            return

        self.is_playing = True
        self.animation_thread = threading.Thread(
            target=self._animate_loop,
            args=(loop, delay),
            daemon=True
        )
        self.animation_thread.start()

    def _animate_once(self, delay):
        """Joue l'animation une seule fois."""
        if not self.images:
            return

        for i, img in enumerate(self.images):
            if not self.is_playing:
                break

            # Met à jour l'image dans le thread principal
            self.label.after(0, self._update_image, img)
            time.sleep(delay)

        self.is_playing = False

    def stop_animation(self):
        """Arrête la lecture de l'animation."""
        self.is_playing = False

    def _animate_loop(self, loop, delay):
        """Boucle d'animation (exécutée dans un thread séparé)."""
        if not loop:
            # Si pas de boucle, joue une seule fois
            self._animate_once(delay)
            return

        while self.is_playing and self.images:
            for i, img in enumerate(self.images):
                if not self.is_playing:
                    break

                # Met à jour l'image dans le thread principal
                self.label.after(0, self._update_image, img)
                time.sleep(delay)

            if not loop:
                break

        self.is_playing = False

    def _update_image(self, image):
        """Met à jour l'image (appelé dans le thread principal)."""
        if self.label.winfo_exists():
            self.label.config(image=image)
            self.label.image = image


class PenduHybrideUI(tk.Tk):
    """
    Interface utilisateur du jeu du pendu avec style hybride Matrix/Windows 95.
    """

    def __init__(self):
        super().__init__()

        # Initialisation des gestionnaires
        self.data_manager = DataManager()
        self.game_manager = GameManager()
        self.saisie_active = True

        # Variables pour l'animation
        self.animation_player = None

        # Chargement de la police Windows 95
        self.charger_police_win95()

        # Configuration de la fenêtre
        self.configurer_fenetre()

        # Création de l'interface
        self.creer_interface()

        # Chargement des données
        self.charger_donnees()

        # Charge toutes les animations avec taille fixe
        self.after(100, self._load_animations_delayed)

        # Nouvelle partie
        self.nouvelle_partie()

    def charger_police_win95(self):
        """Charge la police Windows 95 depuis le dossier font."""
        try:
            import tkinter.font as tkfont
            # Chemin vers la police
            font_path = os.path.join(
                os.path.dirname(__file__), "font", "W95FA.otf")
            if os.path.exists(font_path):
                # Charge la police personnalisée
                self.police_win95 = tkfont.Font(family="W95FA", size=8)
                self.police_win95_bouton = tkfont.Font(
                    family="W95FA", size=8, weight="bold")
                CouleursHybride.POLICE_WIN95 = ("W95FA", 8)
            else:
                # Utilise une police par défaut si la police n'est pas trouvée
                self.police_win95 = tkfont.Font(family="MS Sans Serif", size=8)
                self.police_win95_bouton = tkfont.Font(
                    family="MS Sans Serif", size=8, weight="bold")
                CouleursHybride.POLICE_WIN95 = ("MS Sans Serif", 8)
        except Exception as e:
            print(f"Erreur lors du chargement de la police : {e}")
            # Police de fallback
            import tkinter.font as tkfont
            self.police_win95 = tkfont.Font(family="MS Sans Serif", size=8)
            self.police_win95_bouton = tkfont.Font(
                family="MS Sans Serif", size=8, weight="bold")
            CouleursHybride.POLICE_WIN95 = ("MS Sans Serif", 8)

    def configurer_fenetre(self):
        """Configure la fenêtre principale avec le style Windows 95."""
        self.title("Pendu - HX - 4000")
        self.geometry("800x700")
        self.configure(bg=CouleursHybride.GRIS_WIN95)

        # Empêche le redimensionnement
        self.resizable(False, False)

        # Configuration du grid - Nouvelle disposition
        # Mot à trouver (en haut, pleine largeur)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)  # Animation (1/3 largeur)
        self.grid_rowconfigure(2, weight=0)  # Statistiques
        self.grid_rowconfigure(3, weight=0)  # Saisie et boutons
        self.grid_columnconfigure(0, weight=1)

    def creer_interface(self):
        """Crée l'interface utilisateur style hybride Windows 95 / Matrix."""

        # =============================================================================
        # 1. MOT À TROUVER (EN HAUT, PLEINE LARGEUR) - STYLE MATRIX
        # =============================================================================
        mot_frame = tk.Frame(
            self,
            bg=CouleursHybride.FOND_NOIR,
            relief=tk.SUNKEN,
            borderwidth=2
        )
        mot_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        mot_frame.grid_columnconfigure(0, weight=1)

        # Titre et compteur d'erreurs
        info_frame = tk.Frame(mot_frame, bg=CouleursHybride.FOND_NOIR)
        info_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=5)
        info_frame.grid_columnconfigure(1, weight=1)

        title_label = tk.Label(
            info_frame,
            text="◉ PENDU - HX - 4000 ◉",
            font=CouleursHybride.POLICE_TITRE_MATRIX,
            bg=CouleursHybride.FOND_NOIR,
            fg=CouleursHybride.VERT_CLAIR
        )
        title_label.grid(row=0, column=0, sticky="w")

        self.label_erreurs = tk.Label(
            info_frame,
            text="ERREURS: 0/7",
            font=CouleursHybride.POLICE_MATRIX,
            bg=CouleursHybride.FOND_NOIR,
            fg=CouleursHybride.VERT_MATRIX
        )
        self.label_erreurs.grid(row=0, column=2, sticky="e")

        # Mot à deviner (grande taille)
        self.label_mot = tk.Label(
            mot_frame,
            text="_ _ _ _ _",
            font=("Courier New", 32, "bold"),
            bg=CouleursHybride.FOND_NOIR,
            fg=CouleursHybride.VERT_CLAIR,
            pady=20
        )
        self.label_mot.grid(row=1, column=0, pady=10)

        # Lettres essayées
        self.label_lettres = tk.Label(
            mot_frame,
            text="LETTRES ESSAYÉES: AUCUNE",
            font=CouleursHybride.POLICE_MATRIX,
            bg=CouleursHybride.FOND_NOIR,
            fg=CouleursHybride.VERT_MATRIX,
            wraplength=700
        )
        self.label_lettres.grid(row=2, column=0, pady=5)

        # =============================================================================
        # 2. ZONE INFORMATIONS WINDOWS 95 (100% LARGEUR)
        # =============================================================================
        info_frame = tk.Frame(
            self,
            bg=CouleursHybride.GRIS_WIN95,
            relief=tk.RAISED,
            borderwidth=2
        )
        info_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
        info_frame.grid_rowconfigure(1, weight=1)
        info_frame.grid_columnconfigure(0, weight=1)

        # Titre Windows 95
        win95_title = tk.Label(
            info_frame,
            text="Informations de jeu",
            font=CouleursHybride.POLICE_WIN95_BOUTON,
            bg=CouleursHybride.GRIS_WIN95,
            fg=CouleursHybride.NOIR_WIN95
        )
        win95_title.grid(row=0, column=0, pady=10)

        # Messages
        self.label_message = tk.Label(
            info_frame,
            text="Bienvenue dans le jeu du pendu !",
            font=("MS Sans Serif", 12, "bold"),
            bg=CouleursHybride.GRIS_WIN95,
            fg=CouleursHybride.NOIR_WIN95,
            wraplength=700,
            height=2,
            justify=tk.CENTER
        )
        self.label_message.grid(row=1, column=0, sticky="ew", padx=20, pady=5)

        # =============================================================================
        # 3. STATISTIQUES (1/3) + ANIMATION (1/3) - STYLE MATRIX
        # =============================================================================
        stats_main_frame = tk.Frame(self, bg=CouleursHybride.GRIS_WIN95)
        stats_main_frame.grid(row=2, column=0, sticky="ew", padx=10, pady=10)
        stats_main_frame.grid_columnconfigure(
            0, weight=2)  # Statistiques (2/3)
        stats_main_frame.grid_columnconfigure(1, weight=1)  # Animation (1/3)

        # STATISTIQUES (Style Matrix) - 2/3 de l'espace
        stats_frame = tk.Frame(
            stats_main_frame,
            bg=CouleursHybride.VERT_SOMBRE,
            relief=tk.SUNKEN,
            borderwidth=2
        )
        stats_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 5), pady=0)
        stats_frame.grid_rowconfigure(1, weight=1)
        stats_frame.grid_columnconfigure(0, weight=1)

        stats_title = tk.Label(
            stats_frame,
            text=">>> STATISTIQUES <<<",
            font=CouleursHybride.POLICE_MATRIX,
            bg=CouleursHybride.VERT_SOMBRE,
            fg=CouleursHybride.VERT_CLAIR
        )
        stats_title.grid(row=0, column=0, pady=5)

        self.label_stats = tk.Label(
            stats_frame,
            text="CHARGEMENT DES STATISTIQUES...",
            font=CouleursHybride.POLICE_STATS_MATRIX,
            bg=CouleursHybride.VERT_SOMBRE,
            fg=CouleursHybride.VERT_MATRIX,
            justify=tk.LEFT
        )
        self.label_stats.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        # ANIMATION (Style Matrix) - 1/3 de l'espace
        animation_frame = tk.Frame(
            stats_main_frame,
            bg=CouleursHybride.FOND_NOIR,
            relief=tk.SUNKEN,
            borderwidth=2
        )
        animation_frame.grid(
            row=0, column=1, sticky="nsew", padx=(5, 0), pady=0)

        self.animation_label = tk.Label(
            animation_frame,
            bg=CouleursHybride.FOND_NOIR
        )
        self.animation_label.pack(expand=True, fill="both", padx=2, pady=2)

        # Initialise le lecteur d'animation
        self.animation_player = AnimationPlayer(self.animation_label)

        # =============================================================================
        # 4. SAISIE ET BOUTONS (STYLE WINDOWS 95)
        # =============================================================================
        saisie_frame = tk.Frame(
            self,
            bg=CouleursHybride.GRIS_WIN95,
            relief=tk.RAISED,
            borderwidth=2
        )
        saisie_frame.grid(row=3, column=0, sticky="ew", padx=10, pady=10)
        saisie_frame.grid_columnconfigure(1, weight=1)

        # Étiquette
        instruction_label = tk.Label(
            saisie_frame,
            text="Entrez une lettre :",
            font=CouleursHybride.POLICE_WIN95_NORMALE,
            bg=CouleursHybride.GRIS_WIN95,
            fg=CouleursHybride.NOIR_WIN95
        )
        instruction_label.grid(row=0, column=0, padx=10, pady=10)

        # Zone de saisie
        self.entry_lettre = tk.Entry(
            saisie_frame,
            font=("Arial", 12, "bold"),
            width=5,
            justify=tk.CENTER,
            bg=CouleursHybride.BLANC_WIN95,
            fg=CouleursHybride.NOIR_WIN95,
            relief=tk.SUNKEN,
            borderwidth=2
        )
        self.entry_lettre.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        self.entry_lettre.bind("<KeyPress>", self.on_key_press)
        self.entry_lettre.focus_set()

        # Boutons Windows 95
        btn_nouvelle = tk.Button(
            saisie_frame,
            text="Nouvelle Partie",
            font=CouleursHybride.POLICE_WIN95_BOUTON,
            bg=CouleursHybride.GRIS_WIN95,
            fg=CouleursHybride.NOIR_WIN95,
            activebackground=CouleursHybride.GRIS_CLAIR_WIN95,
            command=self.nouvelle_partie,
            relief=tk.RAISED,
            borderwidth=2,
            width=12
        )
        btn_nouvelle.grid(row=0, column=2, padx=5, pady=10)

        btn_quitter = tk.Button(
            saisie_frame,
            text="Quitter",
            font=CouleursHybride.POLICE_WIN95_BOUTON,
            bg=CouleursHybride.GRIS_WIN95,
            fg=CouleursHybride.ROUGE_WIN95,
            activebackground=CouleursHybride.GRIS_CLAIR_WIN95,
            command=self.quitter_jeu,
            relief=tk.RAISED,
            borderwidth=2,
            width=12
        )
        btn_quitter.grid(row=0, column=3, padx=5, pady=10)

    def charger_donnees(self):
        """Charge les données et statistiques."""
        try:
            self.data_manager.charger_stats()
            self.mettre_a_jour_statistiques()
        except Exception as e:
            print(f"Erreur lors du chargement des données : {e}")

    def _load_animations_delayed(self):
        """Charge les animations avec la taille fixe."""
        if self.animation_player:
            self.animation_player.load_all_animations(self.game_manager)

    def nouvelle_partie(self):
        """Démarre une nouvelle partie."""
        if self.game_manager.nouvelle_partie():
            self.saisie_active = True
            self.mettre_a_jour_affichage()
            self.effacer_message()
            self.entry_lettre.focus_set()
            # Relance l'animation initiale en boucle
            if self.animation_player:
                # Réinitialise le flag d'animation de victoire
                self.animation_player.victory_animation_played = False
                self.animation_player.start_initial_animation()

    def on_key_press(self, event):
        """Gestionnaire d'événement pour les touches pressées."""
        if not self.saisie_active:
            return "break"

        char = event.char

        if char.isalpha() and len(char) == 1:
            self.entry_lettre.delete(0, tk.END)
            self.traiter_proposition(char)
            return "break"

        # Touches spéciales autorisées
        if event.keysym in ["BackSpace", "Delete", "Left", "Right", "Home", "End"]:
            return

        # Bloque les autres caractères
        return "break"

    def traiter_proposition(self, lettre):
        """Traite une proposition de lettre."""
        resultat = self.game_manager.proposer_lettre(lettre)

        if not resultat["valide"]:
            self.afficher_message(resultat["message"], "avertissement")
            return

        # Affiche le résultat
        if resultat["correcte"]:
            self.afficher_message(resultat["message"], "succes")
            # Met à jour l'affichage pour les bonnes réponses
            self.mettre_a_jour_affichage()
            # Continue l'animation actuelle (seulement si c'est l'animation initiale)
            if self.animation_player:
                self.animation_player.continue_current_animation()
        else:
            self.afficher_message(resultat["message"], "erreur")
            # Met à jour l'affichage
            self.mettre_a_jour_affichage()
            # Lance l'animation d'erreur avec délai de 2 secondes
            self.lancer_animation_erreur()

        # Vérifie fin de partie
        if self.game_manager.est_gagne():
            self.fin_partie_victoire()
        elif self.game_manager.est_perdu():
            self.fin_partie_defaite()

    def lancer_animation_erreur(self):
        """Lance l'animation d'erreur avec délai de 2 secondes."""
        if self.animation_player:
            nb_erreurs = self.game_manager.erreurs
            # Lance l'animation correspondant au niveau d'erreur
            self.animation_player.play_error_animation(
                error_level=nb_erreurs,
                delay_before_start=2.0
            )

    def mettre_a_jour_affichage(self):
        """Met à jour tous les éléments d'affichage."""
        info = self.game_manager.obtenir_info_jeu()

        # Met à jour le compteur d'erreurs
        self.label_erreurs.config(
            text=f"ERREURS: {info['erreurs']}/{info['max_erreurs']}"
        )

        # Met à jour le mot
        self.label_mot.config(text=info["mot_affiche"])

        # Met à jour les lettres essayées
        lettres = info["lettres_essayees"]
        if lettres["toutes"] != "Aucune":
            self.label_lettres.config(
                text=f"LETTRES ESSAYÉES: {lettres['toutes']}"
            )
        else:
            self.label_lettres.config(text="LETTRES ESSAYÉES: AUCUNE")

        # Met à jour l'animation
        self.mettre_a_jour_animation(info['erreurs'])

        # Met à jour les statistiques
        self.mettre_a_jour_statistiques()

    def mettre_a_jour_animation(self, nb_erreurs):
        """Met à jour l'animation selon le nombre d'erreurs."""
        # Ne fait rien ici car les animations sont gérées séparément
        # L'animation initiale continue en boucle sauf si une erreur survient
        pass

    def mettre_a_jour_statistiques(self):
        """Met à jour l'affichage des statistiques."""
        try:
            stats_text = self.data_manager.obtenir_statistiques_formatees()
            # Adapte le formatage pour le style Matrix
            stats_text = stats_text.replace("📊", ">>").replace(
                "🎯", ">>").replace("⚡", ">>")
            self.label_stats.config(text=stats_text)
        except Exception as e:
            self.label_stats.config(text=f"ERREUR STATS: {e}")

    def afficher_message(self, message, type_message="normal"):
        """Affiche un message avec la couleur appropriée."""
        couleurs = {
            "normal": CouleursHybride.TEXTE_WIN95_NORMAL,
            "succes": CouleursHybride.TEXTE_WIN95_SUCCES,
            "erreur": CouleursHybride.TEXTE_WIN95_ERREUR,
            "avertissement": CouleursHybride.TEXTE_WIN95_ERREUR,
            "info": CouleursHybride.TEXTE_WIN95_NORMAL
        }

        couleur = couleurs.get(
            type_message, CouleursHybride.TEXTE_WIN95_NORMAL)
        self.label_message.config(text=message, fg=couleur)

    def effacer_message(self):
        """Efface le message affiché."""
        self.label_message.config(text="")

    def fin_partie_victoire(self):
        """Gère la fin de partie en cas de victoire."""
        self.saisie_active = False
        self.game_manager.terminer_partie()

        info = self.game_manager.obtenir_info_jeu()
        message = f"VICTOIRE ! LE MOT ÉTAIT : {info['mot_original']}"
        self.afficher_message(message, "succes")

        # Lance l'animation de victoire
        if self.animation_player:
            self.animation_player.play_victory_animation()

        # Met à jour les statistiques
        self.mettre_a_jour_statistiques()

    def fin_partie_defaite(self):
        """Gère la fin de partie en cas de défaite."""
        self.saisie_active = False
        self.game_manager.terminer_partie()

        info = self.game_manager.obtenir_info_jeu()
        message = f"DÉFAITE ! LE MOT ÉTAIT : {info['mot_original']}"
        self.afficher_message(message, "erreur")

        # Met à jour les statistiques
        self.mettre_a_jour_statistiques()

    def quitter_jeu(self):
        """Quitte le jeu."""
        if messagebox.askyesno("QUITTER", "VOULEZ-VOUS VRAIMENT QUITTER ?"):
            self.destroy()


def lancer_jeu():
    """Lance le jeu du pendu avec l'interface hybride."""
    try:
        app = PenduHybrideUI()
        app.mainloop()
    except Exception as e:
        print(f"Erreur lors du lancement : {e}")
        messagebox.showerror("Erreur", f"Erreur lors du lancement :\n{e}")


if __name__ == "__main__":
    lancer_jeu()
