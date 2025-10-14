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
