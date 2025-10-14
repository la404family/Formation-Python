"""
Module contenant les composants de l'interface utilisateur pour le jeu du pendu.
Ce module utilise tkinter pour créer une interface graphique complète.

Fonctionnalités :
- Interface graphique intuitive avec feedback visuel
- Gestion événementielle robuste
- Couleurs contextuelles selon l'état du jeu
- Validation complète des saisies
- Focus automatique et UX optimisée
"""

import tkinter as tk
from tkinter import messagebox, font
from game_logic import GameManager
from data_manager import DataManager


# =============================================================================
# 4.2 GESTION DES COULEURS CONTEXTUELLES
# =============================================================================
class CouleursPendu:
    """
    Classe contenant toutes les constantes de couleurs pour le jeu du pendu.
    Cela permet de centraliser et de modifier facilement les couleurs.
    """

    # Couleurs principales de l'interface
    FOND_PRINCIPAL = "#2E8B57"      # Vert mer (fond de la fenêtre)
    FOND_PANNEAUX = "#4682B4"       # Bleu acier (panneaux)
    FOND_PENDU = "#F0F8FF"          # Bleu Alice (zone ASCII art)
    TEXTE_PENDU = "#000080"         # Bleu marine (dessin du pendu)

    # Couleurs contextuelles selon l'état du jeu
    TEXTE_NORMAL = "white"          # Blanc (texte normal)
    TEXTE_SUCCES = "#32CD32"        # Vert lime (succès, victoire)
    TEXTE_ERREUR = "#FF6B6B"        # Rouge clair (erreurs)
    TEXTE_AVERTISSEMENT = "#FFD93D"  # Jaune (avertissements)
    TEXTE_INFO = "#87CEEB"          # Bleu ciel (informations)
    TEXTE_DEFAITE = "#DC143C"       # Rouge cramoisi (défaite)

    # Couleurs des boutons
    BOUTON_NOUVEAU = "#32CD32"      # Vert lime (nouvelle partie)
    BOUTON_QUITTER = "#DC143C"      # Rouge cramoisi (quitter)

    # Couleurs des lettres essayées
    LETTRES_CORRECTES = "#90EE90"   # Vert clair
    LETTRES_INCORRECTES = "#FFA07A"  # Saumon clair


class PenduUI(tk.Tk):
    """
    Classe principale de l'interface utilisateur du jeu du pendu.
    Hérite de tk.Tk pour créer la fenêtre principale.
    """

    def __init__(self):
        """
        Initialise l'interface utilisateur du jeu du pendu.
        Configure la fenêtre et tous les composants graphiques.

        4.1 CONNEXION UI ↔ LOGIQUE
        Cette méthode établit la connexion entre l'interface et la logique du jeu.
        """
        # Appelle le constructeur de la classe parent (tk.Tk)
        super().__init__()

        # =============================================================================
        # 4.1 INSTANCIATION DES GESTIONNAIRES
        # =============================================================================

        # 1. Instancier le gestionnaire de données
        # Le DataManager s'occupe du chargement des mots et des statistiques
        print("🔧 Initialisation du gestionnaire de données...")
        self.data_manager = DataManager()

        # 2. Instancier le gestionnaire de jeu en lui passant le data_manager
        # Le GameManager utilise le DataManager pour accéder aux mots et stats
        print("🎮 Initialisation du gestionnaire de jeu...")
        self.game_manager = GameManager()

        # 3. Variable pour contrôler l'état de la saisie
        # Permet de désactiver la saisie pendant les fins de partie
        self.saisie_active = True

        # 4. Configuration initiale de la fenêtre
        print("🖼️ Configuration de la fenêtre...")
        self.configurer_fenetre()

        # 5. Création des composants d'interface
        print("🎨 Création de l'interface...")
        self.creer_interface()

        # 6. Charger et afficher les statistiques initiales
        print("📊 Chargement des statistiques...")
        self.charger_et_afficher_statistiques()

        # 7. Démarre une nouvelle partie
        print("🚀 Démarrage d'une nouvelle partie...")
        self.nouvelle_partie()

        print("✅ Interface initialisée avec succès !")

    def charger_et_afficher_statistiques(self):
        """
        Charge les statistiques depuis le fichier et les affiche.
        Cette méthode est appelée lors de l'initialisation.
        """
        try:
            # Charge les statistiques via le data_manager
            self.data_manager.charger_stats()

            # Met à jour l'affichage des statistiques
            self.mettre_a_jour_statistiques()

            print("✅ Statistiques chargées et affichées")

        except Exception as e:
            print(f"⚠️ Erreur lors du chargement des statistiques : {e}")
            # En cas d'erreur, on continue avec des stats par défaut

    def configurer_fenetre(self):
        """
        Configure les propriétés de la fenêtre principale.
        Utilise les constantes de couleurs pour une gestion centralisée.
        """
        # Titre de la fenêtre avec émojis pour un aspect ludique
        self.title("🎯 Jeu du Pendu 🎯")

        # Taille optimale de la fenêtre (largeur x hauteur)
        self.geometry("800x700")

        # Couleur de fond utilisant les constantes de couleurs
        self.configure(bg=CouleursPendu.FOND_PRINCIPAL)

        # Configuration pour le redimensionnement
        # Configure les lignes et colonnes pour qu'elles s'étendent
        self.grid_rowconfigure(0, weight=1)    # Frame du pendu
        self.grid_rowconfigure(1, weight=1)    # Frame centrale
        self.grid_rowconfigure(2, weight=0)    # Frame de saisie (taille fixe)
        self.grid_columnconfigure(0, weight=1)  # Colonne principale

        # Empêche le redimensionnement manuel (optionnel)
        self.resizable(True, True)

        # Icône de la fenêtre (si le fichier existe)
        try:
            self.iconbitmap("icon.ico")
        except:
            pass  # Ignore si l'icône n'existe pas

    def creer_interface(self):
        """
        Crée tous les composants de l'interface utilisateur.
        Organise l'interface en trois zones principales.
        """
        # =============================================================================
        # FRAME 1 : ZONE ASCII ART DU PENDU (en haut)
        # =============================================================================
        self.frame_pendu = tk.Frame(
            self, bg=CouleursPendu.FOND_PRINCIPAL, relief=tk.RAISED, bd=2)
        self.frame_pendu.grid(row=0, column=0, sticky="nsew", padx=10, pady=5)

        # Configure le frame pour le redimensionnement
        self.frame_pendu.grid_rowconfigure(0, weight=1)
        self.frame_pendu.grid_columnconfigure(0, weight=1)

        # Zone d'affichage du pendu (Text widget en lecture seule)
        self.text_pendu = tk.Text(
            self.frame_pendu,
            width=25,
            height=10,
            # Police monospace pour l'ASCII art
            font=("Courier New", 12, "bold"),
            bg=CouleursPendu.FOND_PENDU,    # Utilise les constantes de couleurs
            fg=CouleursPendu.TEXTE_PENDU,   # Utilise les constantes de couleurs
            state=tk.DISABLED,  # Lecture seule
            wrap=tk.NONE,       # Pas de retour à la ligne automatique
            relief=tk.SUNKEN,
            bd=3
        )
        self.text_pendu.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        # =============================================================================
        # FRAME 2 : ZONE CENTRALE (mot à deviner + informations)
        # =============================================================================
        self.frame_central = tk.Frame(
            self, bg=CouleursPendu.FOND_PRINCIPAL, relief=tk.RAISED, bd=2)
        self.frame_central.grid(
            row=1, column=0, sticky="nsew", padx=10, pady=5)

        # Configure le frame central
        self.frame_central.grid_rowconfigure(0, weight=1)  # Mot à deviner
        self.frame_central.grid_rowconfigure(1, weight=1)  # Lettres essayées
        self.frame_central.grid_rowconfigure(2, weight=1)  # Messages
        self.frame_central.grid_rowconfigure(3, weight=2)  # Statistiques
        self.frame_central.grid_columnconfigure(0, weight=1)

        # --- Mot à deviner ---
        self.label_mot = tk.Label(
            self.frame_central,
            text="_ _ _ _ _",
            font=("Arial", 24, "bold"),
            bg=CouleursPendu.FOND_PRINCIPAL,
            fg=CouleursPendu.TEXTE_NORMAL,
            pady=10
        )
        self.label_mot.grid(row=0, column=0, sticky="ew", padx=10, pady=5)

        # --- Lettres essayées ---
        self.label_lettres = tk.Label(
            self.frame_central,
            text="Lettres essayées : Aucune",
            font=("Arial", 12),
            bg=CouleursPendu.FOND_PRINCIPAL,
            fg=CouleursPendu.TEXTE_INFO,  # Utilise les constantes
            wraplength=600  # Retour à la ligne automatique
        )
        self.label_lettres.grid(row=1, column=0, sticky="ew", padx=10, pady=5)

        # --- Messages d'erreur/avertissement ---
        self.label_message = tk.Label(
            self.frame_central,
            text="",
            font=("Arial", 11, "italic"),
            bg=CouleursPendu.FOND_PRINCIPAL,
            fg=CouleursPendu.TEXTE_NORMAL,
            wraplength=600,
            height=2
        )
        self.label_message.grid(row=2, column=0, sticky="ew", padx=10, pady=5)

        # --- Panneau des statistiques ---
        self.frame_stats = tk.Frame(
            self.frame_central, bg=CouleursPendu.FOND_PANNEAUX, relief=tk.SUNKEN, bd=2)
        self.frame_stats.grid(row=3, column=0, sticky="nsew", padx=10, pady=5)

        # Configure le frame des statistiques
        self.frame_stats.grid_rowconfigure(0, weight=1)
        self.frame_stats.grid_columnconfigure(0, weight=1)

        self.label_stats = tk.Label(
            self.frame_stats,
            text="Chargement des statistiques...",
            font=("Arial", 10),
            bg=CouleursPendu.FOND_PANNEAUX,
            fg=CouleursPendu.TEXTE_NORMAL,
            justify=tk.LEFT,
            anchor="nw"
        )
        self.label_stats.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # =============================================================================
        # FRAME 3 : ZONE DE SAISIE ET BOUTONS (en bas)
        # =============================================================================
        self.frame_saisie = tk.Frame(
            self, bg=CouleursPendu.FOND_PRINCIPAL, relief=tk.RAISED, bd=2)
        self.frame_saisie.grid(row=2, column=0, sticky="ew", padx=10, pady=5)

        # Configure le frame de saisie
        self.frame_saisie.grid_columnconfigure(0, weight=1)  # Zone de saisie
        self.frame_saisie.grid_columnconfigure(
            1, weight=0)  # Bouton nouvelle partie
        self.frame_saisie.grid_columnconfigure(2, weight=0)  # Bouton quitter

        # --- Zone de saisie de lettres ---
        self.frame_input = tk.Frame(
            self.frame_saisie, bg=CouleursPendu.FOND_PRINCIPAL)
        self.frame_input.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

        # Label d'instruction
        self.label_instruction = tk.Label(
            self.frame_input,
            text="Tapez une lettre :",
            font=("Arial", 12, "bold"),
            bg=CouleursPendu.FOND_PRINCIPAL,
            fg=CouleursPendu.TEXTE_NORMAL
        )
        self.label_instruction.pack(side=tk.LEFT, padx=(0, 10))

        # Champ de saisie avec amélioration UX
        self.entry_lettre = tk.Entry(
            self.frame_input,
            font=("Arial", 14, "bold"),
            width=5,
            justify=tk.CENTER,
            relief=tk.SUNKEN,
            bd=3,
            # 5.3 AMÉLIORATION UX - Couleurs personnalisées pour le champ
            bg="white",
            fg="black",
            insertbackground="black"  # Couleur du curseur
        )
        self.entry_lettre.pack(side=tk.LEFT, padx=(0, 10))

        # Binding pour détecter la saisie immédiatement
        self.entry_lettre.bind("<KeyPress>", self.on_key_press)

        # 5.3 FOCUS AUTOMATIQUE SUR ENTRY
        self.entry_lettre.focus_set()  # Met automatiquement le focus

        # --- Boutons avec couleurs contextuelles ---
        # Bouton Nouvelle Partie
        self.btn_nouvelle_partie = tk.Button(
            self.frame_saisie,
            text="🔄 Nouvelle Partie",
            font=("Arial", 12, "bold"),
            bg=CouleursPendu.BOUTON_NOUVEAU,  # Utilise les constantes
            fg=CouleursPendu.TEXTE_NORMAL,
            command=self.nouvelle_partie,
            relief=tk.RAISED,
            bd=3,
            padx=10,
            pady=5,
            # 5.3 AMÉLIORATION UX - Effet au survol
            activebackground="#28A428",  # Vert plus foncé au survol
            activeforeground="white"
        )
        self.btn_nouvelle_partie.grid(row=0, column=1, padx=5, pady=10)

        # Bouton Quitter
        self.btn_quitter = tk.Button(
            self.frame_saisie,
            text="❌ Quitter",
            font=("Arial", 12, "bold"),
            bg=CouleursPendu.BOUTON_QUITTER,  # Utilise les constantes
            fg=CouleursPendu.TEXTE_NORMAL,
            command=self.quitter_jeu,
            relief=tk.RAISED,
            bd=3,
            padx=10,
            pady=5,
            # 5.3 AMÉLIORATION UX - Effet au survol
            activebackground="#B22222",  # Rouge plus foncé au survol
            activeforeground="white"
        )
        self.btn_quitter.grid(row=0, column=2, padx=5, pady=10)

    def on_key_press(self, event):
        """
        MÉTHODE ON_KEY_PRESS(EVENT) - Gestionnaire d'événements selon spécifications 4.1

        Cette méthode est le cœur de l'interaction utilisateur. Elle est appelée
        à chaque fois qu'une touche est pressée dans le champ de saisie.

        Fonctions :
        - Capturer la touche pressée
        - Valider (lettre unique, pas déjà essayée)
        - Appeler game_manager.proposer_lettre()
        - Mettre à jour l'affichage
        - Vérifier victoire/défaite
        - Effacer l'Entry

        Args:
            event: Événement tkinter contenant les informations sur la touche pressée
        """

        # =============================================================================
        # 5.3 AMÉLIORATION UX - Vérification de l'état de la saisie
        # =============================================================================

        # Si la saisie est désactivée (par exemple en fin de partie), on ignore
        if not self.saisie_active:
            return "break"

        # =============================================================================
        # 1. CAPTURER LA TOUCHE PRESSÉE
        # =============================================================================

        # Récupère le caractère tapé (event.char)
        char = event.char
        # Récupère aussi le nom de la touche pour les touches spéciales (event.keysym)
        key_name = event.keysym

        # Debug : affiche la touche pressée (utile pour le développement)
        print(f"🔤 Touche pressée : '{char}' (keysym: {key_name})")

        # Efface immédiatement le message précédent pour un feedback visuel rapide
        self.effacer_message()

        # =============================================================================
        # 5.2 VALIDATION ET SÉCURITÉ - Vérification du type de touche
        # =============================================================================

        # 5.2.1 Vérifier que la saisie est bien une lettre
        if char.isalpha() and len(char) == 1:
            print(f"✅ Lettre valide détectée : {char.upper()}")

            # 5.3 FEEDBACK VISUEL IMMÉDIAT - Efface le contenu du champ
            self.entry_lettre.delete(0, tk.END)

            # 2. VALIDER (lettre unique, pas déjà essayée) et
            # 3. APPELER game_manager.proposer_lettre()
            self.traiter_proposition(char)

            # 5. EFFACER L'ENTRY - Empêche l'affichage du caractère
            # (car on vient de l'effacer)
            return "break"

        # 5.2.2 Ignorer les touches spéciales autorisées (Shift, Ctrl, Alt, etc.)
        elif key_name in ['Shift_L', 'Shift_R', 'Control_L', 'Control_R',
                          'Alt_L', 'Alt_R', 'Meta_L', 'Meta_R', 'Super_L', 'Super_R',
                          'Caps_Lock', 'Num_Lock', 'Scroll_Lock']:
            # Ces touches ne font rien mais ne déclenchent pas d'avertissement
            print(f"🔧 Touche spéciale ignorée : {key_name}")
            return "break"

        # 5.2.3 Permettre certaines touches d'édition
        elif key_name in ['BackSpace', 'Delete', 'Left', 'Right', 'Home', 'End']:
            print(f"⌨️ Touche d'édition autorisée : {key_name}")
            return  # Laisse la touche faire son effet normal

        # 5.2.4 Gestion des touches Enter et Escape
        elif key_name == 'Return':
            print("↩️ Touche Entrée pressée - Ignorée (saisie immédiate)")
            self.afficher_message(
                "Tapez directement une lettre, pas besoin d'appuyer sur Entrée ! ⌨️", "info")
            return "break"

        elif key_name == 'Escape':
            print("⎋ Touche Échap pressée - Nouvelle partie")
            self.nouvelle_partie()
            return "break"

        # 5.2.5 Gestion des caractères non-alphabétiques
        elif char and char.isprintable():
            # C'est un caractère visible mais pas une lettre
            print(f"⚠️ Caractère non-alphabétique : {char}")
            self.afficher_message(
                f"'{char}' n'est pas une lettre. Tapez uniquement des lettres ! 🔤",
                "avertissement"
            )
            return "break"

        # 5.2.6 Toutes les autres touches (caractères de contrôle, etc.)
        else:
            # Touches de contrôle invisibles - ignorées silencieusement
            print(f"🔇 Touche de contrôle ignorée : {key_name}")
            return "break"

    def traiter_proposition(self, lettre):
        """
        Traite une proposition de lettre du joueur.
        Cette méthode centralise le traitement d'une lettre proposée.

        Args:
            lettre (str): La lettre proposée par le joueur
        """
        print(f"🎯 Traitement de la proposition : {lettre.upper()}")

        try:
            # =============================================================================
            # 2. VALIDER ET 3. APPELER game_manager.proposer_lettre()
            # =============================================================================

            # Envoie la lettre au gestionnaire de jeu pour validation et traitement
            # Le GameManager va vérifier si la lettre est valide, pas déjà essayée, etc.
            resultat = self.game_manager.proposer_lettre(lettre)

            # Affiche le résultat de la validation dans la console (debug)
            print(f"📝 Résultat : {resultat}")

            # =============================================================================
            # GESTION DES PROPOSITIONS NON VALIDES
            # =============================================================================

            # Si la proposition n'est pas valide (déjà essayée, caractère invalide, etc.)
            if not resultat["valide"]:
                # Affiche le message d'erreur/avertissement à l'utilisateur
                self.afficher_message(resultat["message"], resultat["type"])
                print(f"❌ Proposition invalide : {resultat['message']}")
                return  # Sort de la méthode sans rien faire d'autre

            # =============================================================================
            # 4. METTRE À JOUR L'AFFICHAGE
            # =============================================================================

            # Si la proposition est valide, met à jour tous les éléments visuels
            self.mettre_a_jour_affichage()

            # =============================================================================
            # 5.3 FEEDBACK VISUEL IMMÉDIAT
            # =============================================================================

            # Affiche le message de résultat (lettre correcte/incorrecte)
            self.afficher_message(resultat["message"], resultat["type"])

            # Feedback visuel selon le résultat
            if resultat["correcte"]:
                print(f"✅ Lettre correcte : {lettre.upper()}")
                # On pourrait ajouter ici un effet visuel (clignotement vert, son, etc.)
            else:
                print(f"❌ Lettre incorrecte : {lettre.upper()}")
                # On pourrait ajouter ici un effet visuel (clignotement rouge, son, etc.)

            # =============================================================================
            # 5. VÉRIFIER VICTOIRE/DÉFAITE
            # =============================================================================

            # Vérifie si la partie est terminée après cette proposition
            if self.game_manager.est_gagne():
                print(
                    f"🎉 VICTOIRE ! Mot trouvé : {self.game_manager.mot_original}")
                # Termine la partie côté logique (sauvegarde des stats)
                self.game_manager.terminer_partie()
                # Gère l'interface de fin de partie
                self.fin_de_partie(victoire=True)

            elif self.game_manager.est_perdu():
                print(
                    f"💀 DÉFAITE ! Mot était : {self.game_manager.mot_original}")
                # Termine la partie côté logique (sauvegarde des stats)
                self.game_manager.terminer_partie()
                # Gère l'interface de fin de partie
                self.fin_de_partie(victoire=False)

            else:
                # La partie continue
                erreurs_restantes = self.game_manager.max_erreurs - self.game_manager.erreurs
                print(
                    f"🎮 Partie en cours - Erreurs restantes : {erreurs_restantes}")

        except Exception as e:
            # 5.1 GESTION ROBUSTE DES ERREURS
            print(f"❌ Erreur lors du traitement de la proposition : {e}")
            self.afficher_message(
                f"Erreur inattendue : {str(e)}",
                "erreur"
            )

    def mettre_a_jour_affichage(self):
        """
        MÉTHODE METTRE_A_JOUR_AFFICHAGE() - selon spécifications 4.1

        Met à jour tous les éléments de l'affichage avec les données actuelles du jeu.
        Cette méthode est le centre de rafraîchissement de l'interface utilisateur.

        Fonctions :
        - Rafraîchir ASCII art selon le nombre d'erreurs
        - Rafraîchir mot affiché
        - Rafraîchir lettres essayées  
        - Rafraîchir messages
        """
        print("🔄 Mise à jour de l'affichage...")

        try:
            # =============================================================================
            # RÉCUPÉRATION DES DONNÉES DU JEU
            # =============================================================================

            # Récupère toutes les informations actuelles du jeu
            info = self.game_manager.obtenir_info_jeu()
            print(
                f"📊 Info jeu : Erreurs={info['erreurs']}, Gagné={info['est_gagne']}, Perdu={info['est_perdu']}")

            # =============================================================================
            # 1. RAFRAÎCHIR LE MOT AFFICHÉ
            # =============================================================================

            # Met à jour le texte du mot avec les lettres trouvées
            self.label_mot.config(text=info["mot_affiche"])

            # 4.2 COULEURS CONTEXTUELLES - Change la couleur selon l'état du jeu
            if info["est_gagne"]:
                # Victoire : couleur verte
                self.label_mot.config(fg=CouleursPendu.TEXTE_SUCCES)
                print("🎉 Mot affiché en vert (victoire)")
            elif info["est_perdu"]:
                # Défaite : couleur rouge
                self.label_mot.config(fg=CouleursPendu.TEXTE_DEFAITE)
                print("💀 Mot affiché en rouge (défaite)")
            else:
                # Jeu en cours : couleur normale
                self.label_mot.config(fg=CouleursPendu.TEXTE_NORMAL)
                print("🎮 Mot affiché en blanc (jeu en cours)")

            # =============================================================================
            # 2. RAFRAÎCHIR LES LETTRES ESSAYÉES
            # =============================================================================

            # Récupère les lettres formatées
            lettres = info["lettres_essayees"]

            # Crée un texte coloré et informatif
            texte_lettres = (
                f"✅ Lettres correctes : {lettres['correctes']} | "
                f"❌ Lettres incorrectes : {lettres['incorrectes']}"
            )

            # Met à jour l'affichage des lettres
            self.label_lettres.config(text=texte_lettres)

            # Couleur selon le contexte
            if info["erreurs"] == 0:
                # Aucune erreur : couleur positive
                self.label_lettres.config(fg=CouleursPendu.TEXTE_SUCCES)
            elif info["erreurs"] >= info["max_erreurs"] - 1:
                # Danger (dernière chance) : couleur d'avertissement
                self.label_lettres.config(fg=CouleursPendu.TEXTE_AVERTISSEMENT)
            else:
                # Normal : couleur d'info
                self.label_lettres.config(fg=CouleursPendu.TEXTE_INFO)

            # =============================================================================
            # 3. RAFRAÎCHIR ASCII ART SELON LE NOMBRE D'ERREURS
            # =============================================================================

            # Met à jour le dessin du pendu en fonction du nombre d'erreurs
            self.mettre_a_jour_pendu(info["dessin_pendu"])
            print(f"🎨 Dessin du pendu mis à jour ({info['erreurs']} erreurs)")

            # =============================================================================
            # 4. RAFRAÎCHIR LES STATISTIQUES
            # =============================================================================

            # Met à jour le panneau des statistiques en temps réel
            self.mettre_a_jour_statistiques()
            print("📈 Statistiques mises à jour")

            # =============================================================================
            # 5. INFORMATIONS DE PROGRESSION
            # =============================================================================

            # Affiche des informations utiles dans la console
            erreurs_restantes = info["max_erreurs"] - info["erreurs"]
            lettres_trouvees = len(info["lettres_essayees"]["correctes"].split(
                ", ")) if info["lettres_essayees"]["correctes"] != "Aucune" else 0

            print(
                f"📝 Progression : {lettres_trouvees} lettres trouvées, {erreurs_restantes} chances restantes")

            print("✅ Affichage mis à jour avec succès")

        except Exception as e:
            # 5.1 GESTION ROBUSTE DES ERREURS
            print(f"❌ Erreur lors de la mise à jour de l'affichage : {e}")
            # En cas d'erreur, on affiche un message mais on continue
            self.afficher_message(
                "Erreur d'affichage - Le jeu continue",
                "erreur"
            )

    def mettre_a_jour_pendu(self, dessin):
        """
        Met à jour l'affichage du dessin ASCII du pendu.

        Args:
            dessin (str): Le dessin ASCII à afficher
        """
        # Active temporairement le widget Text pour pouvoir le modifier
        self.text_pendu.config(state=tk.NORMAL)

        # Efface le contenu actuel
        self.text_pendu.delete(1.0, tk.END)

        # Insère le nouveau dessin
        self.text_pendu.insert(1.0, dessin)

        # Centre le texte (approximativement)
        self.text_pendu.tag_add("center", 1.0, tk.END)
        self.text_pendu.tag_config("center", justify=tk.CENTER)

        # Remet en lecture seule
        self.text_pendu.config(state=tk.DISABLED)

    def mettre_a_jour_statistiques(self):
        """
        Met à jour l'affichage des statistiques.
        """
        stats_formatees = self.game_manager.obtenir_statistiques()
        self.label_stats.config(text=stats_formatees)

    def afficher_message(self, message, type_message):
        """
        Affiche un message dans la zone de messages avec couleurs contextuelles.

        5.3 AMÉLIORATION UX - Feedback visuel immédiat avec couleurs
        Cette méthode fournit un retour visuel immédiat à l'utilisateur.

        Args:
            message (str): Le message à afficher
            type_message (str): Le type de message ("erreur", "avertissement", "succes", "info")
        """

        # 4.2 COULEURS CONTEXTUELLES - Utilise les constantes de couleurs
        couleurs = {
            "erreur": CouleursPendu.TEXTE_ERREUR,           # Rouge pour les erreurs
            "avertissement": CouleursPendu.TEXTE_AVERTISSEMENT,  # Jaune pour les avertissements
            "succes": CouleursPendu.TEXTE_SUCCES,           # Vert pour les succès
            "info": CouleursPendu.TEXTE_INFO                # Bleu ciel pour les infos
        }

        # Récupère la couleur appropriée ou utilise la couleur par défaut
        couleur = couleurs.get(type_message, CouleursPendu.TEXTE_NORMAL)

        # Log du message dans la console pour le debug
        print(f"💬 Message [{type_message}] : {message}")

        # Affiche le message avec la couleur appropriée
        self.label_message.config(text=message, fg=couleur)

        # 5.3 AMÉLIORATION UX - Programme l'effacement automatique après 4 secondes
        # (augmenté de 3 à 4 secondes pour laisser plus de temps de lecture)
        self.after(4000, self.effacer_message)

    def effacer_message(self):
        """
        Efface le message affiché.
        """
        self.label_message.config(text="")

    def nouvelle_partie(self):
        """
        Démarre une nouvelle partie avec gestion complète de l'état.

        MÉTHODE NOUVELLE_PARTIE() - selon spécifications 4.1
        - Réinitialise le GameManager avec un nouveau mot
        - Réinitialise complètement l'affichage
        - Remet le focus sur le champ de saisie (Entry)
        """
        print("🔄 Démarrage d'une nouvelle partie...")

        try:
            # =============================================================================
            # 1. RÉINITIALISER LE GAMEMANAGER AVEC UN NOUVEAU MOT
            # =============================================================================

            # Demande au gestionnaire de jeu de démarrer une nouvelle partie
            # Cela va sélectionner un nouveau mot aléatoirement
            if not self.game_manager.nouvelle_partie():
                # Si la nouvelle partie n'a pas pu démarrer (pas de mots disponibles)
                messagebox.showerror(
                    "Erreur",
                    "Impossible de démarrer une nouvelle partie.\n" +
                    "Vérifiez que le fichier mots.json est présent et contient des mots."
                )
                return False

            # =============================================================================
            # 2. RÉINITIALISER L'AFFICHAGE COMPLET
            # =============================================================================

            # Réactive la saisie (au cas où elle aurait été désactivée en fin de partie)
            self.saisie_active = True

            # Efface tous les messages d'erreur/avertissement précédents
            self.effacer_message()

            # Remet les couleurs par défaut
            self.label_mot.config(fg=CouleursPendu.TEXTE_NORMAL)

            # Efface le contenu du champ de saisie
            self.entry_lettre.delete(0, tk.END)

            # Met à jour tous les éléments graphiques avec les nouvelles données
            self.mettre_a_jour_affichage()

            # =============================================================================
            # 3. FOCUS SUR LE CHAMP DE SAISIE (ENTRY)
            # =============================================================================

            # Remet automatiquement le focus sur le champ de saisie
            # Cela permet au joueur de taper directement sans cliquer
            self.entry_lettre.focus_set()

            # Force la fenêtre à passer au premier plan (si elle était en arrière-plan)
            self.focus_force()

            # =============================================================================
            # 4. FEEDBACK VISUEL ET SONORE
            # =============================================================================

            # Message de confirmation avec émoji pour rendre l'expérience plus ludique
            self.afficher_message(
                "✨ Nouvelle partie commencée ! Bonne chance ! 🍀",
                "info"
            )

            print("✅ Nouvelle partie démarrée avec succès !")
            return True

        except Exception as e:
            # 5.1 GESTION ROBUSTE DES ERREURS
            print(f"❌ Erreur lors du démarrage de la nouvelle partie : {e}")

            # Message d'erreur clair pour l'utilisateur
            messagebox.showerror(
                "Erreur de nouvelle partie",
                f"Une erreur est survenue lors du démarrage :\n{str(e)}\n\n" +
                "Vérifiez que tous les fichiers sont présents."
            )
            return False

    def fin_de_partie(self, victoire):
        """
        MÉTHODE FIN_DE_PARTIE(VICTOIRE) - selon spécifications 4.1

        Gère complètement la fin de partie (victoire ou défaite).
        Cette méthode centralise toutes les actions à effectuer en fin de partie.

        Fonctions :
        - Afficher message victoire/défaite
        - Mettre à jour statistiques
        - Sauvegarder statistiques
        - Désactiver saisie
        - Proposer nouvelle partie

        Args:
            victoire (bool): True si le joueur a gagné, False sinon
        """
        print(f"🏁 Fin de partie - Victoire : {victoire}")

        try:
            # =============================================================================
            # 1. DÉSACTIVER LA SAISIE
            # =============================================================================

            # Désactive la saisie pour éviter que le joueur continue à taper
            self.saisie_active = False
            print("🔒 Saisie désactivée")

            # Efface le contenu du champ de saisie
            self.entry_lettre.delete(0, tk.END)

            # =============================================================================
            # RÉCUPÉRATION DES INFORMATIONS DE LA PARTIE
            # =============================================================================

            # Récupère toutes les informations de la partie qui vient de se terminer
            info = self.game_manager.obtenir_info_jeu()

            # =============================================================================
            # 2. METTRE À JOUR ET 3. SAUVEGARDER LES STATISTIQUES
            # =============================================================================

            # Les statistiques sont automatiquement mises à jour par GameManager.terminer_partie()
            # qui a été appelé avant cette méthode, mais on rafraîchit l'affichage
            self.mettre_a_jour_statistiques()
            print("📊 Statistiques mises à jour et sauvegardées")

            # =============================================================================
            # 1. AFFICHER MESSAGE VICTOIRE/DÉFAITE
            # =============================================================================

            # Prépare le message de fin selon le résultat
            if victoire:
                # Messages de victoire avec émojis et informations détaillées
                titre = "🎉 VICTOIRE ! 🎉"

                # Crée un message personnalisé selon la performance
                if info['erreurs'] == 0:
                    performance = "PARFAIT ! Aucune erreur ! 🏆"
                elif info['erreurs'] <= 2:
                    performance = "EXCELLENT ! Très peu d'erreurs ! ⭐"
                elif info['erreurs'] <= 4:
                    performance = "BIEN JOUÉ ! 👍"
                else:
                    performance = "Gagné de justesse ! 😅"

                message = (
                    f"Félicitations ! Vous avez trouvé le mot :\\n"
                    f"'{info['mot_original']}'\\n\\n"
                    f"📊 Votre performance :\\n"
                    f"• Erreurs : {info['erreurs']}/{info['max_erreurs']}\\n"
                    f"• {performance}\\n\\n"
                    f"🎯 Continuez sur cette lancée !"
                )

                # Couleur de victoire
                self.afficher_message("🎉 VICTOIRE ! 🎉", "succes")

            else:
                # Messages de défaite encourageants
                titre = "💀 Défaite 💀"

                message = (
                    f"Dommage ! Le mot était :\\n"
                    f"'{info['mot_original']}'\\n\\n"
                    f"📊 Vos tentatives :\\n"
                    f"• Lettres correctes trouvées : {info['lettres_essayees']['correctes']}\\n"
                    f"• Erreurs commises : {info['erreurs']}/{info['max_erreurs']}\\n\\n"
                    f"💪 Ne vous découragez pas, vous ferez mieux la prochaine fois !"
                )

                # Couleur de défaite
                self.afficher_message("💀 Essayez encore ! 💀", "erreur")

            # =============================================================================
            # 4. PROPOSER NOUVELLE PARTIE
            # =============================================================================

            # Affiche une boîte de dialogue avec le choix de rejouer
            reponse = messagebox.askyesno(
                titre,
                message + "\\n\\nVoulez-vous jouer une nouvelle partie ?"
            )

            # Traite la réponse du joueur
            if reponse:
                print("🔄 Le joueur veut rejouer")
                # Le joueur veut rejouer - démarre une nouvelle partie
                self.nouvelle_partie()
            else:
                print("⏸️ Le joueur ne veut pas rejouer")
                # Le joueur ne veut pas rejouer - garde la partie affichée mais inactive
                self.afficher_message(
                    "🎮 Partie terminée. Cliquez sur 'Nouvelle Partie' pour rejouer ou 'Quitter' pour fermer.",
                    "info"
                )

                # Affiche un résumé des statistiques
                stats = self.data_manager.obtenir_statistiques_formatees()
                print("📈 Statistiques finales :")
                print(stats)

            print("✅ Fin de partie gérée avec succès")

        except Exception as e:
            # 5.1 GESTION ROBUSTE DES ERREURS
            print(f"❌ Erreur lors de la gestion de fin de partie : {e}")

            # Message d'erreur pour l'utilisateur
            messagebox.showerror(
                "Erreur",
                f"Une erreur est survenue en fin de partie :\\n{str(e)}\\n\\n" +
                "Vous pouvez continuer à jouer normalement."
            )

            # Réactive la saisie en cas d'erreur pour que le jeu reste utilisable
            self.saisie_active = True

    def quitter_jeu(self):
        """
        Ferme l'application après confirmation.
        """
        reponse = messagebox.askyesno(
            "Quitter",
            "Êtes-vous sûr de vouloir quitter le jeu ?"
        )

        if reponse:
            self.destroy()  # Ferme la fenêtre et termine le programme


# Fonction pour créer et lancer l'interface
def lancer_jeu():
    """
    Lance le jeu du pendu avec l'interface graphique.
    """
    try:
        # Crée et lance l'application
        app = PenduUI()
        app.mainloop()
    except Exception as e:
        print(f"Erreur lors du lancement du jeu : {e}")
        messagebox.showerror("Erreur", f"Une erreur est survenue :\\n{e}")


# Test de l'interface (si ce module est exécuté directement)
if __name__ == "__main__":
    lancer_jeu()
