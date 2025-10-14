# 🎯 Jeu du Pendu - Version Complète avec Interface Tkinter

## 📋 Description

Ce projet implémente un jeu du pendu complet avec interface graphique tkinter, développé selon les spécifications avancées pour débutants en Python. Le jeu comprend une architecture modulaire, une gestion d'événements robuste, et de nombreuses fonctionnalités avancées.

## ✨ Fonctionnalités Principales

### 🎮 Gameplay

- **Plus de 109,000 mots français** chargés depuis `mots.json`
- **Gestion automatique des accents** : "été" → "ETE", "français" → "FRANCAIS"
- **Conservation des caractères spéciaux** : tirets et apostrophes toujours visibles
- **6 niveaux de pendu** avec art ASCII détaillé
- **Saisie immédiate** : pas besoin d'appuyer sur Entrée

### 🖥️ Interface Graphique

- **Interface tkinter complète** avec 3 zones principales
- **Couleurs contextuelles** selon l'état du jeu
- **Feedback visuel immédiat** avec messages colorés
- **Redimensionnement adaptatif** de la fenêtre
- **Focus automatique** sur le champ de saisie

### 📊 Statistiques Avancées

- **Suivi complet des performances** sauvegardé automatiquement
- **Pourcentage de réussite** calculé en temps réel
- **Mot le plus long trouvé** et **meilleur score**
- **Historique des mots trouvés**
- **Moyenne d'erreurs par partie**

### 🛡️ Robustesse et Sécurité

- **Gestion complète des erreurs** avec try/catch
- **Validation stricte des saisies** (une lettre uniquement)
- **Gestion des touches spéciales** (Ctrl, Alt, Échap, etc.)
- **Messages d'erreur clairs** pour l'utilisateur
- **Sauvegarde automatique** des statistiques

## 🏗️ Architecture du Code

### 📁 Structure des Fichiers

```
002.Le pendu/
├── main.py                    # Point d'entrée de l'application
├── data_manager.py           # Gestion des données (mots, statistiques)
├── game_logic.py            # Logique du jeu et art ASCII
├── ui_components.py         # Interface utilisateur tkinter
├── mots.json               # Base de données des mots français
├── statistiques_pendu.json.json  # Fichier des statistiques
├── icon.ico                # Icône de l'application
└── README.md              # Ce fichier
```

### 🧩 Modules Principaux

#### 1. **DataManager** (`data_manager.py`)

```python
# Responsabilités :
- Chargement des mots depuis mots.json
- Gestion des statistiques (chargement/sauvegarde)
- Normalisation des textes (suppression accents)
- Gestion robuste des erreurs de fichiers
```

#### 2. **GameManager** (`game_logic.py`)

```python
# Responsabilités :
- Logique du jeu (état, validation, victoire/défaite)
- Gestion des propositions de lettres
- Art ASCII du pendu (7 états)
- Interface avec DataManager pour les stats
```

#### 3. **PenduUI** (`ui_components.py`)

```python
# Responsabilités :
- Interface graphique tkinter complète
- Gestion des événements clavier
- Couleurs contextuelles et feedback visuel
- Connexion UI ↔ Logique métier
```

## 🎯 Spécifications Techniques Implémentées

### 4.1 Intégration et Logique Événementielle ✅

#### **Connexion UI ↔ Logique**

- ✅ Instanciation `DataManager` et `GameManager` dans `PenduUI.__init__()`
- ✅ Chargement et affichage automatique des statistiques
- ✅ Architecture MVC respectée

#### **Méthode `nouvelle_partie()`**

- ✅ Réinitialisation complète du GameManager
- ✅ Réinitialisation de l'affichage avec gestion d'état
- ✅ Focus automatique sur le champ de saisie
- ✅ Gestion robuste des erreurs

#### **Méthode `on_key_press(event)`**

- ✅ Capture immédiate des touches pressées
- ✅ Validation complète (lettre unique, pas déjà essayée)
- ✅ Appel automatique à `game_manager.proposer_lettre()`
- ✅ Mise à jour automatique de l'affichage
- ✅ Vérification automatique victoire/défaite
- ✅ Effacement automatique du champ

#### **Méthode `mettre_a_jour_affichage()`**

- ✅ Rafraîchissement ASCII art selon erreurs
- ✅ Rafraîchissement mot affiché avec couleurs
- ✅ Rafraîchissement lettres essayées
- ✅ Rafraîchissement messages contextuels

#### **Méthode `fin_de_partie(victoire)`**

- ✅ Messages personnalisés victoire/défaite
- ✅ Mise à jour et sauvegarde automatique des stats
- ✅ Désactivation de la saisie
- ✅ Proposition de nouvelle partie

### 4.2 Gestion des Couleurs Contextuelles ✅

```python
class CouleursPendu:
    FOND_PRINCIPAL = "#2E8B57"      # Vert mer
    TEXTE_SUCCES = "#32CD32"        # Vert lime (victoire)
    TEXTE_ERREUR = "#FF6B6B"        # Rouge clair (erreurs)
    TEXTE_AVERTISSEMENT = "#FFD93D" # Jaune (avertissements)
    TEXTE_INFO = "#87CEEB"          # Bleu ciel (informations)
    # ... et bien d'autres
```

### 5.1 Gestion Robuste des Erreurs ✅

- ✅ **Try/except** autour de toutes les opérations fichier
- ✅ **Messages d'erreur clairs** et informatifs pour l'utilisateur
- ✅ **Fallback** sur valeurs par défaut en cas de problème
- ✅ **Continuation du jeu** même en cas d'erreur non-critique

### 5.2 Validation et Sécurité ✅

- ✅ **Vérification stricte** : saisie = une lettre alphabétique uniquement
- ✅ **Gestion des touches spéciales** : Shift, Ctrl, Alt ignorées proprement
- ✅ **Limitation à un caractère** avec feedback immédiat
- ✅ **Gestion des raccourcis** : Échap = nouvelle partie, Entrée = info

### 5.3 Amélioration UX ✅

- ✅ **Focus automatique** sur le champ de saisie
- ✅ **Feedback visuel immédiat** avec couleurs contextuelles
- ✅ **Messages auto-effaçables** après 4 secondes
- ✅ **Effets de survol** sur les boutons
- ✅ **Curseur personnalisé** dans le champ de saisie

## 🚀 Comment Jouer

### Installation et Lancement

```bash
# 1. Naviguer vers le dossier du jeu
cd "002.Le pendu"

# 2. Lancer le jeu
python main.py

# 3. Afficher l'aide (optionnel)
python main.py --help
```

### Règles du Jeu

1. **Objectif** : Devinez le mot secret en proposant des lettres
2. **Limite** : 6 erreurs maximum (sinon le pendu est complet)
3. **Saisie** : Tapez directement une lettre (pas besoin d'Entrée)
4. **Indices** : Les tirets et apostrophes sont toujours visibles
5. **Victoire** : Trouvez toutes les lettres avant 6 erreurs

### Conseils de Stratégie

- 🔤 **Commencez par les voyelles** : A, E, I, O, U
- 📝 **Puis les consonnes fréquentes** : S, T, R, N, L, M
- 🎯 **Observez la longueur** du mot pour deviner le type
- 📊 **Consultez vos statistiques** pour améliorer votre stratégie

### Raccourcis Clavier

| Touche   | Action                       |
| -------- | ---------------------------- |
| `Lettre` | Proposer une lettre          |
| `Échap`  | Nouvelle partie              |
| `Entrée` | Affiche un conseil           |
| `F5`     | Nouvelle partie (via bouton) |

## 🎨 Captures d'Écran

### Interface Principale

```
🎯 Jeu du Pendu 🎯
┌─────────────────────────────┐
│     +---+                   │
│     |   |                   │
│     O   |    (ASCII Art)    │
│    /|\  |                   │
│    / \  |                   │
│         |                   │
│   =========                 │
└─────────────────────────────┘

        _ O _ J _ U R

✅ Lettres correctes : O, R, U, J
❌ Lettres incorrectes : A, E, I

┌─── 📊 STATISTIQUES ────┐
│ Parties jouées : 15    │
│ Victoires : 12         │
│ Taux de réussite : 80% │
│ Meilleur score : 1     │
└────────────────────────┘

Tapez une lettre : [_] 🔄 Nouvelle Partie ❌ Quitter
```

## 🔧 Personnalisation

### Modifier les Couleurs

```python
# Dans ui_components.py, classe CouleursPendu
class CouleursPendu:
    FOND_PRINCIPAL = "#VotreCouleur"     # Changez ici
    TEXTE_SUCCES = "#VotreCouleur"       # Et ici
    # ...
```

### Ajouter des Mots

```json
// Dans mots.json
[
  "mot1",
  "mot2",
  "votre-nouveau-mot"
  // ...
]
```

### Modifier le Nombre d'Erreurs

```python
# Dans game_logic.py, classe GameManager
self.max_erreurs = 8  # Au lieu de 6
```

## 🐛 Dépannage

### Problèmes Courants

**Q: Le jeu ne démarre pas**

```
R : Vérifiez que mots.json existe et contient des mots valides
```

**Q: Les statistiques ne se sauvegardent pas**

```
R : Vérifiez les permissions d'écriture dans le dossier
```

**Q: L'interface est déformée**

```
R : Redimensionnez la fenêtre ou relancez le jeu
```

### Logs de Debug

Le jeu affiche des logs détaillés dans la console :

```
🔧 Initialisation du gestionnaire de données...
🎮 Initialisation du gestionnaire de jeu...
✓ 109280 mots chargés avec succès.
🔤 Touche pressée : 'a' (keysym: a)
✅ Lettre valide détectée : A
📝 Progression : 1 lettres trouvées, 6 chances restantes
```

## 👨‍💻 Pour les Développeurs

### Tests

```bash
# Test du module data_manager
python -c "from data_manager import DataManager; dm = DataManager(); dm.charger_mots()"

# Test du module game_logic
python -c "from game_logic import GameManager; gm = GameManager(); gm.nouvelle_partie()"

# Test de l'interface
python ui_components.py
```

### Extension

Le code est conçu pour être facilement extensible :

- **Sons** : Ajoutez `pygame.mixer` pour les effets sonores
- **Animations** : Utilisez `tkinter.ttk` pour des transitions
- **Multijoueur** : Étendez `GameManager` pour plusieurs joueurs
- **Thèmes** : Créez plusieurs classes `CouleursPendu`

## 📝 Licence

Ce projet est développé dans le cadre de la Formation Python pour des fins éducatives.

## 🙏 Remerciements

- **Formation Python** pour les spécifications détaillées
- **Communauté tkinter** pour la documentation
- **Base de mots français** (109,280 mots inclus)

---
