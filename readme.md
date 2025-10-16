# 🐍 Formation Python Complète

![Logo Python](logoPython.png)

## Apprendre Python de zéro jusqu'aux projets avancés

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Niveau](https://img.shields.io/badge/Niveau-Débutant%20à%20Avancé-purple?style=for-the-badge)

![GitHub stars](https://img.shields.io/github/stars/la404family/Formation-Python?style=social)
![GitHub forks](https://img.shields.io/github/forks/la404family/Formation-Python?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/la404family/Formation-Python?style=social)

---

## 📖 À propos de cette formation

**Formation Python** est un cours complet et progressif pour maîtriser le langage de programmation Python. De l'installation aux projets avancés, cette formation couvre tous les aspects essentiels avec des explications détaillées, des exemples pratiques et des exercices interactifs.

### 🎯 Objectifs pédagogiques

- ✅ **Bases solides** : Variables, types de données, opérateurs
- ✅ **Fonctions intégrées** : Manipulation de chaînes, nombres, calculs
- ✅ **Modules avancés** : Math, datetime, os, et plus encore
- ✅ **Projets pratiques** : Jeux interactifs avec Pygame et Tkinter
- ✅ **Bonnes pratiques** : Code propre, documentation, optimisation

---

## 🎮 Projets pratiques

### 🏰 [The Legend of Turgut](001.The%20Legend%20Of%20Turgut%20%5BPygame%5D/README.md)

![Pygame](https://img.shields.io/badge/Pygame-Jeu%202D-red?style=flat-square&logo=python)

Jeu d'aventure 2D développé avec Pygame - RPG rétro avec héros nomade turc

**Technologies :** Pygame, OOP, Architecture modulaire, Gestion manette/clavier, Caméra avec zoom

#### 🏗️ Architecture du Projet

**Structure modulaire** organisée en classes spécialisées :

```text
001.The Legend Of Turgut [Pygame]/
├── main.py                    # Point d'entrée et boucle principale
├── classes/                   # Architecture orientée objet
│   ├── level.py              # Gestionnaire de niveau et monde
│   ├── player.py             # Héros Turgut (déplacement, combat, animation)
│   ├── entity.py             # Classe mère (déplacement, collisions)
│   ├── enemy.py              # Intelligence artificielle des ennemis
│   ├── camera.py             # Caméra avec zoom x4 et tri Y-sort
│   ├── weapon.py             # Système d'armes (4 types d'attaques)
│   ├── joystick.py           # Gestionnaire de manette de jeu
│   ├── keyboard.py           # Gestionnaire de clavier
│   ├── tile.py               # Tuiles et obstacles de la carte
│   └── ui.py                 # Interface utilisateur (barres de vie/énergie)
├── settings/                  # Configuration centralisée
│   └── settings.py           # Constantes, données armes, positions
├── functions/                 # Utilitaires système
│   ├── get_os_adapted_path.py # Chemins multi-plateforme
│   ├── get_screen_dimensions.py # Adaptation écran automatique
│   ├── debug.py              # Système de débogage visuel
│   └── apply_font.py         # Gestion des polices rétro
├── assets/ imagesOfMaps/     # Ressources graphiques
├── sounds/                   # Effets sonores
└── font/                     # Police pixel-art rétro
```

#### 🎮 Système de Contrôles Hybride (Clavier + Manette)

**Gestion simultanée** clavier et manette Xbox/PlayStation :

- **Détection automatique** : La manette est détectée au démarrage
- **Priorité intelligente** : Le clavier a priorité sur la manette pour éviter les conflits
- **Déplacement anti-diagonal** : Un seul axe à la fois (haut/bas OU gauche/droite)
- **4 armes mappées** : Touches U/I/J/K (clavier) ou boutons 0/1/2/3 (manette)
- **Course** : Touches O/P/L/M (clavier) ou gâchettes L2/R2 (manette)

**Code technique manette** :

```python
# Détection axes analogiques avec zone morte
if joystick and self.direction.length() == 0:
    joystick_x = joystick.get_axis(0)  # Stick gauche X
    joystick_y = joystick.get_axis(1)  # Stick gauche Y

    # Priorité à l'axe dominant (pas de diagonale)
    if abs(joystick_x) > abs(joystick_y):
        if joystick_x < -0.5: self.direction.x = -1  # Gauche
        elif joystick_x > 0.5: self.direction.x = 1  # Droite
```

#### ⚔️ Système de Combat Avancé

**4 types d'attaques** avec animations mathématiques :

- **Hache1** : Attaque circulaire (rotation 360°)
- **Hache2** : Attaque droite (projection linéaire)
- **Hache3** : Attaque en dent de scie (pattern sinusoïdal)
- **Hache4** : Attaque en S (courbe paramétrique complexe)

#### 🎯 Fonctionnalités Techniques

- **Caméra intelligente** : Zoom x4, tri Y-sort pour profondeur
- **Détection de collisions** : Hitbox séparée du sprite pour précision
- **Animation fluide** : 60 FPS avec gestion frame-rate indépendante
- **Chargement de carte** : Analyse pixel par pixel des images PNG
- **Système de debug** : Affichage temps réel des informations
- **Adaptation écran** : Redimensionnement automatique selon résolution

### 🎯 [Le Pendu](002.Le%20pendu%20%5BTkinter%5D/README.md)

![Tkinter](https://img.shields.io/badge/Tkinter-Interface%20GUI-blue?style=flat-square&logo=python)

Jeu de devinettes avec interface graphique

**Technologies :** Tkinter, JSON, Statistiques, UI/UX

---

## 📚 Contenu du cours

- **[`000` 🔧 Installation](000_installation.py)**  
  Configuration de l'environnement Python

- **[`001` 🏷️ Types de variables](001_les_types_de_variables.py)**  
  int, float, str, bool, complexes

- **[`002` 📦 Variables](002_les_variables.py)**  
  Déclaration, affectation, portée

- **[`003` 🔄 Conversions](003_les_conversions.py)**  
  Casting entre types de données

- **[`004` 🔤 Fonctions str](004_les_fonctions_str.py)**  
  Manipulation avancée des chaînes

- **[`005` 🔢 Fonctions int](005_les_fonctions_int.py)**  
  Opérations sur les entiers

- **[`006` 🌊 Fonctions float](006_les_fonctions_float.py)**  
  Calculs avec les nombres décimaux

- **[`007` 📐 Module math](007_le_module_math.py)**  
  Fonctions mathématiques avancées

- **[`008` ⚖️ Opérateurs de comparaison](008_operateurs_comparaison.py)**  
  ==, !=, <, >, <=, >=

- **[`009` 🔀 Conditions (if/elif/else)](009_conditions.py)**  
  Structures conditionnelles et branchements

- **[`010` 🔁 Boucle while](010_boucle_while.py)**  
  Répétitions conditionnelles

- **[`011` 🔂 Boucle for](011_boucle_for.py)**  
  Itérations sur séquences

- **[`012` 🎯 Break, continue, pass](012_controle_flux.py)**  
  Contrôle de flux dans les boucles

- **[`013` 📋 Listes (list)](013_listes.py)**  
  Création, manipulation, méthodes

- **[`014` 🔧 Méthodes de listes](014_methodes_listes.py)**  
  append, insert, remove, sort, etc.

- **[`015` 📑 Tuples (tuple)](015_tuples.py)**  
  Séquences immuables

- **[`016` 📖 Dictionnaires (dict)](016_dictionnaires.py)**  
  Paires clé-valeur, accès, modification

- **[`017` 🎲 Ensembles (set)](017_ensembles.py)**  
  Collections non ordonnées, opérations mathématiques

- **[`018` 🔄 Compréhensions](018_comprehensions.py)**  
  List, dict, set comprehensions

- **[`019` 🎪 Définir des fonctions](019_definir_fonctions.py)**  
  def, paramètres, return

- **[`020` 📦 Arguments et paramètres](020_arguments_parametres.py)**  
  Positionnels, nommés, \*args, \*\*kwargs

- **[`021` 🌐 Portée des variables](021_portee_variables.py)**  
  local, global, nonlocal

- **[`022` 🎭 Fonctions lambda](022_fonctions_lambda.py)**  
  Fonctions anonymes

- **[`023` 🎁 Fonctions intégrées](023_fonctions_integrees.py)**  
  map, filter, zip, enumerate, range

- **[`024` ⚠️ Exceptions](024_exceptions.py)**  
  try, except, else, finally

- **[`025` 🎯 Lever des exceptions](025_lever_exceptions.py)**  
  raise, exceptions personnalisées

- **[`026` 📁 Lecture de fichiers](026_lecture_fichiers.py)**  
  open, read, readline, readlines

- **[`027` ✍️ Écriture de fichiers](027_ecriture_fichiers.py)**  
  write, append, modes d'ouverture

- **[`028` 🗂️ Context managers](028_context_managers.py)**  
  with statement, gestion automatique

- **[`029` 🏗️ Classes et objets](029_classes_objets.py)**  
  Définition, instanciation

- **[`030` 🎯 Attributs et méthodes](030_attributs_methodes.py)**  
  self, `__init__`, méthodes d'instance

- **[`031` 🔒 Encapsulation](031_encapsulation.py)**  
  Public, privé (\_), très privé (\_\_)

- **[`032` 👨‍👦 Héritage](032_heritage.py)**  
  Sous-classes, super()

- **[`033` 🎭 Polymorphisme](033_polymorphisme.py)**  
  Surcharge de méthodes

- **[`034` 🔮 Méthodes spéciales](034_methodes_speciales.py)**  
  `__str__`, `__repr__`, `__len__`, etc.

- **[`035` 📊 Properties](035_properties.py)**  
  @property, getters, setters

- **[`036` 📦 Importer des modules](036_importer_modules.py)**  
  import, from...import, as

- **[`037` 🔨 Créer des modules](037_creer_modules.py)**  
  Organisation du code

- **[`038` 📚 Packages](038_packages.py)**  
  `__init__.py`, structure de projet

- **[`039` 🌍 Modules standards](039_modules_standards.py)**  
  os, sys, datetime, random, json

- **[`040` 🎨 Décorateurs](040_decorateurs.py)**  
  @decorator, fonctions d'ordre supérieur

- **[`041` 🔄 Générateurs](041_generateurs.py)**  
  yield, expressions génératrices

- **[`042` 🔗 Itérateurs](042_iterateurs.py)**  
  `__iter__`, `__next__`, protocole d'itération

- **[`043` 📝 Type hints](043_type_hints.py)**  
  Annotations de types

- **[`044` 🧵 Context managers personnalisés](044_context_managers_personnalises.py)**  
  enter, exit

- **[`045` 🗂️ Collections](045_collections.py)**  
  defaultdict, Counter, deque, namedtuple

- **[`046` 🔤 Expressions régulières (re)](046_expressions_regulieres.py)**  
  Patterns, recherche, substitution

- **[`047` 📅 Module datetime](047_module_datetime.py)**  
  Dates, heures, timedelta

- **[`048` 🎲 Module random avancé](048_module_random.py)**  
  Distributions, échantillonnage

- **[`049` 🗄️ Module json](049_module_json.py)**  
  Sérialisation, parsing

- **[`050` 🧰 Programmation modulaire](050_programmation_modulaire.py)**  
  Organisation en packages, séparation logique du code, imports relatifs, bonnes pratiques PEP8

- **[`051` 🧪 Tests unitaires](051_tests_unitaires.py)**  
  unittest, pytest, mock, tests paramétrés, couverture de code

- **[`052` 🧾 Logging et débogage](052_logging_debogage.py)**  
  logging, niveaux (DEBUG, INFO…), gestion des logs dans des fichiers, inspection avec pdb

- **[`053` ⚙️ Automatisation système](053_automatisation_systeme.py)**  
  Scripts utilitaires : renommage de fichiers, sauvegardes, interaction avec os, pathlib, subprocess

- **[`054` 📬 Scripts CLI](054_scripts_cli.py)**  
  argparse, click, création d'outils exécutables en ligne de commande

- **[`060` 🌍 Requêtes HTTP et APIs](060_requetes_http_apis.py)**  
  requests, récupération de données, authentification, JSON, APIs publiques (GitHub, OpenWeather...)

- **[`061` 💾 Bases de données](061_bases_donnees.py)**  
  sqlite3, ORM (SQLAlchemy), introduction à MongoDB

- **[`062` 🌐 Développement web backend](062_developpement_web.py)**  
  Introduction à Flask ou FastAPI, routage, templates, endpoints, JSON response

- **[`063` 🔁 API REST complète](063_api_rest.py)**  
  CRUD, validation, gestion d'erreurs, documentation automatique (Swagger/OpenAPI)

- **[`064` 🧰 Interfaces graphiques](064_interfaces_graphiques.py)**  
  Tkinter, PyQt, ou customtkinter — création d'interfaces simples

- **[`070` 📈 Analyse de données avec pandas](070_pandas.py)**  
  Séries, DataFrames, filtrage, groupby, import/export (CSV, Excel, JSON)

- **[`071` 📊 Visualisation](071_visualisation.py)**  
  matplotlib, seaborn, graphiques et tableaux de bord de base

- **[`072` 🧮 NumPy et calcul scientifique](072_numpy.py)**  
  Tableaux multidimensionnels, vecteurs, matrices, algèbre linéaire

- **[`073` 🧠 Introduction aux algorithmes](073_algorithmes.py)**  
  Recherche, tri, complexité, structures de données, notions d'optimisation

- **[`074` 🧩 Initiation à l'IA et ML](074_ia_machine_learning.py)**  
  scikit-learn, régression linéaire, classification, preprocessing

- **[`080` 🔀 Multithreading et multiprocessing](080_multithreading.py)**  
  Threads, Process, asynchronisme avec asyncio

- **[`081` 🧩 Design patterns](081_design_patterns.py)**  
  Singleton, Factory, Observer, Strategy, MVC simplifié

- **[`082` 🧰 Métaprogrammation](082_metaprogrammation.py)**  
  introspection, décorateurs avancés, type(), `__new__`, métaclasses

- **[`083` 🧱 Architecture logicielle avancée](083_architecture_logicielle.py)**  
  SOLID, séparation en modules/services, bonnes pratiques de structuration de projet

- **[`090` 🕹️ Développement de jeux](090_developpement_jeux.py)**  
  Boucle de jeu, collisions, gestion d'événements, sons, animations

- **[`091` 🧰 Génération procédurale](091_generation_procedurale.py)**  
  Bruit de Perlin, génération de cartes, fractales

- **[`092` 🪄 Automatisation bureautique](092_automatisation_bureautique.py)**  
  Manipuler Excel (openpyxl), PDF (reportlab), mails (smtplib)

- **[`093` 🤖 Scripts d'analyse Web](093_web_scraping.py)**  
  BeautifulSoup, requests-html, respect du robots.txt

- **[`094` 📦 Distribution d'applications](094_distribution_applications.py)**  
  setuptools, pip, venv, pyinstaller (créer des .exe)

---

**Made with ❤️ by [la404family](https://github.com/la404family)**

⭐ N'oubliez pas de donner une étoile si ce projet vous aide !
