#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
======================================================================
HÉRITAGE - GUIDE COMPLET
======================================================================

🎯 Ce fichier couvre l'héritage en POO :
   • Concept d'héritage et hiérarchie de classes
   • Classes parent et enfant
   • Méthode super() et redéfinition
   • Héritage multiple

📚 Concepts abordés :
   • Héritage simple
   • Redéfinition de méthodes (override)
   • Appel aux méthodes parent avec super()
   • Héritage multiple et MRO

💡 Objectif : Maîtriser la réutilisation et l'extension de code
"""

print("=" * 70)
print("HÉRITAGE - GUIDE COMPLET")
print("=" * 70)

print("\n" + "=" * 50)
print("1. CONCEPT D'HÉRITAGE")
print("=" * 50)

print("\n🎯 QU'EST-CE QUE L'HÉRITAGE ?")
print("-" * 29)

print("""
L'héritage permet à une classe (enfant) d'hériter des attributs
et méthodes d'une autre classe (parent). C'est un mécanisme
fondamental de la POO qui favorise la réutilisation de code.

🌳 TERMINOLOGIE :
   👑 CLASSE PARENT (base, super-classe) : Classe dont on hérite
   👶 CLASSE ENFANT (dérivée, sous-classe) : Classe qui hérite
   🔄 REDÉFINITION : Modifier une méthode héritée
   📞 super() : Appeler la méthode de la classe parent

💡 ANALOGIE :
   Parent = Animal (manger, dormir, respirer)
   Enfant = Chien (manger, dormir, respirer + aboyer)
""")

print("\n" + "=" * 50)
print("2. HÉRITAGE SIMPLE")
print("=" * 50)

print("\n🐾 EXEMPLE AVEC ANIMAUX")
print("-" * 22)


class Animal:
    """Classe parent représentant un animal générique"""

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        print(f"   🐾 Animal '{nom}' créé")

    def manger(self):
        return f"{self.nom} mange"

    def dormir(self):
        return f"{self.nom} dort"

    def faire_bruit(self):
        return f"{self.nom} fait un bruit"

    def se_presenter(self):
        return f"Je suis {self.nom}, j'ai {self.age} ans"

    def __str__(self):
        return f"Animal({self.nom}, {self.age} ans)"


class Chien(Animal):
    """Classe enfant héritant d'Animal"""

    def __init__(self, nom, age, race):
        # Appel du constructeur parent
        super().__init__(nom, age)
        self.race = race
        print(f"   🐕 Chien de race {race} créé")

    def faire_bruit(self):
        """Redéfinition de la méthode faire_bruit"""
        return f"{self.nom} aboie : Woof!"

    def chercher_balle(self):
        """Nouvelle méthode spécifique aux chiens"""
        return f"{self.nom} court chercher la balle"

    def se_presenter(self):
        """Redéfinition avec appel au parent"""
        presentation_base = super().se_presenter()
        return f"{presentation_base} et je suis un {self.race}"


print("💡 Exemple 1 : Héritage simple")

# Création d'objets
animal_generique = Animal("Créature", 5)
rex = Chien("Rex", 3, "Labrador")

print("\n🔍 MÉTHODES HÉRITÉES :")
print("🍽️", animal_generique.manger())
print("🍽️", rex.manger())  # Méthode héritée
print("😴", rex.dormir())   # Méthode héritée

print("\n🔍 MÉTHODES REDÉFINIES :")
print("🔊", animal_generique.faire_bruit())
print("🔊", rex.faire_bruit())  # Méthode redéfinie

print("\n🔍 MÉTHODES NOUVELLES :")
print("🎾", rex.chercher_balle())  # Méthode spécifique

print("\n🔍 PRÉSENTATION :")
print("👋", animal_generique.se_presenter())
print("👋", rex.se_presenter())

print("\n" + "=" * 50)
print("3. SUPER() ET REDÉFINITION")
print("=" * 50)

print("\n🔄 UTILISATION DE SUPER()")
print("-" * 23)


class Chat(Animal):
    """Autre classe enfant d'Animal"""

    def __init__(self, nom, age, couleur):
        super().__init__(nom, age)  # Appel constructeur parent
        self.couleur = couleur
        self.vies = 9
        print(f"   🐱 Chat {couleur} créé")

    def faire_bruit(self):
        """Redéfinition complète"""
        return f"{self.nom} miaule : Miaou!"

    def manger(self):
        """Redéfinition avec extension"""
        action_base = super().manger()
        return f"{action_base} des croquettes"

    def ronronner(self):
        """Méthode spécifique aux chats"""
        return f"{self.nom} ronronne : Purrr..."

    def perdre_vie(self):
        """Méthode spécifique utilisant un attribut propre"""
        if self.vies > 0:
            self.vies -= 1
            return f"{self.nom} perd une vie, il en reste {self.vies}"
        return f"{self.nom} n'a plus de vies !"


print("💡 Exemple 2 : Super() et redéfinition")

felix = Chat("Félix", 2, "orange")

print("\n🔍 REDÉFINITION COMPLÈTE :")
print("🔊", felix.faire_bruit())

print("\n🔍 REDÉFINITION AVEC EXTENSION :")
print("🍽️", felix.manger())

print("\n🔍 MÉTHODES SPÉCIFIQUES :")
print("😸", felix.ronronner())
print("💀", felix.perdre_vie())
print("💀", felix.perdre_vie())

print("\n" + "=" * 50)
print("4. HIÉRARCHIE PLUS COMPLEXE")
print("=" * 50)

print("\n🌳 PLUSIEURS NIVEAUX D'HÉRITAGE")
print("-" * 32)


class Mammifere(Animal):
    """Classe intermédiaire entre Animal et classes spécifiques"""

    def __init__(self, nom, age, temperature_corps=37):
        super().__init__(nom, age)
        self.temperature_corps = temperature_corps
        self.poils = True
        print(f"   🌡️ Mammifère à {temperature_corps}°C créé")

    def allaiter(self):
        return f"{self.nom} peut allaiter ses petits"

    def reguler_temperature(self):
        return f"{self.nom} maintient sa température à {self.temperature_corps}°C"


class ChienDeTravail(Chien, Mammifere):
    """Classe héritant de Chien (qui hérite d'Animal)"""

    def __init__(self, nom, age, race, specialite):
        # Héritage multiple - on doit gérer l'ordre
        super().__init__(nom, age, race)
        self.specialite = specialite
        print(f"   👮 Chien de travail spécialisé en {specialite}")

    def travailler(self):
        return f"{self.nom} travaille comme {self.specialite}"

    def se_presenter(self):
        """Triple redéfinition avec super()"""
        presentation = super().se_presenter()
        return f"{presentation} et je travaille comme {self.specialite}"


print("💡 Exemple 3 : Hiérarchie complexe")

# Création avec hiérarchie
commissaire = ChienDeTravail(
    "Commissaire Rex", 4, "Berger Allemand", "chien policier")

print("\n🔍 MÉTHODES DE TOUS LES NIVEAUX :")
print("🍽️", commissaire.manger())        # Animal
print("🎾", commissaire.chercher_balle())  # Chien
print("👮", commissaire.travailler())     # ChienDeTravail
print("🌡️", commissaire.reguler_temperature())  # Mammifere

print("\n🔍 PRÉSENTATION COMPLÈTE :")
print("👋", commissaire.se_presenter())

print("\n" + "=" * 50)
print("5. HÉRITAGE MULTIPLE")
print("=" * 50)

print("\n🔄 HÉRITER DE PLUSIEURS CLASSES")
print("-" * 31)


class Volant:
    """Mixin pour objets volants"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.altitude = 0
        print("   ✈️ Capacité de vol ajoutée")

    def voler(self):
        self.altitude = 100
        return f"S'envole à {self.altitude}m d'altitude"

    def atterrir(self):
        self.altitude = 0
        return f"Atterrit au sol"


class Nageur:
    """Mixin pour objets nageurs"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.profondeur = 0
        print("   🏊 Capacité de nage ajoutée")

    def nager(self):
        self.profondeur = 10
        return f"Nage à {self.profondeur}m de profondeur"

    def remonter(self):
        self.profondeur = 0
        return f"Remonte à la surface"


class Canard(Animal, Volant, Nageur):
    """Classe héritant de plusieurs classes (héritage multiple)"""

    def __init__(self, nom, age):
        super().__init__(nom, age)
        print("   🦆 Canard polyvalent créé")

    def faire_bruit(self):
        return f"{self.nom} fait : Coin-coin!"

    def faire_demonstration(self):
        """Démonstration des capacités multiples"""
        actions = [
            self.manger(),      # Animal
            self.faire_bruit(),  # Redéfini
            self.voler(),       # Volant
            self.nager(),       # Nageur
            self.atterrir(),    # Volant
            self.remonter()     # Nageur
        ]
        return actions


print("💡 Exemple 4 : Héritage multiple")

donald = Canard("Donald", 5)

print("\n🔍 DÉMONSTRATION COMPLÈTE :")
actions = donald.faire_demonstration()
for i, action in enumerate(actions, 1):
    print(f"   {i}. {action}")

print("\n🔍 MRO (Method Resolution Order) :")
print("📋", Canard.__mro__)

print("\n" + "=" * 50)
print("6. VÉRIFICATION DE TYPE")
print("=" * 50)

print("\n🔍 ISINSTANCE() ET ISSUBCLASS()")
print("-" * 31)

print("💡 Exemple 5 : Vérification de types")

# Création d'instances pour tests
animaux = [
    Animal("Créature", 1),
    Chien("Buddy", 2, "Golden"),
    Chat("Whiskers", 3, "gris"),
    Canard("Daffy", 4)
]

print("\n🔍 TESTS ISINSTANCE :")
for animal in animaux:
    print(f"\n👤 {animal.nom} :")
    print(f"   Animal ? {isinstance(animal, Animal)}")
    print(f"   Chien ? {isinstance(animal, Chien)}")
    print(f"   Chat ? {isinstance(animal, Chat)}")
    print(f"   Volant ? {isinstance(animal, Volant)}")
    print(f"   Nageur ? {isinstance(animal, Nageur)}")

print("\n🔍 TESTS ISSUBCLASS :")
classes = [Animal, Chien, Chat, Canard, Volant, Nageur]
for classe in classes:
    print(f"\n📊 {classe.__name__} :")
    print(f"   Sous-classe d'Animal ? {issubclass(classe, Animal)}")
    if classe != Animal:
        print(f"   Parents directs : {classe.__bases__}")

print("\n" + "=" * 50)
print("7. EXEMPLE PRATIQUE COMPLET")
print("=" * 50)

print("\n💼 SYSTÈME DE GESTION D'EMPLOYÉS")
print("-" * 32)


class Personne:
    """Classe de base pour toutes les personnes"""

    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def se_presenter(self):
        return f"{self.prenom} {self.nom}, {self.age} ans"

    def __str__(self):
        return self.se_presenter()


class Employe(Personne):
    """Classe pour les employés de base"""

    def __init__(self, nom, prenom, age, salaire, poste):
        super().__init__(nom, prenom, age)
        self.salaire = salaire
        self.poste = poste
        self.heures_travaillees = 0

    def travailler(self, heures):
        self.heures_travaillees += heures
        return f"{self.prenom} a travaillé {heures}h (total: {self.heures_travaillees}h)"

    def calculer_salaire_mensuel(self):
        return self.salaire

    def se_presenter(self):
        base = super().se_presenter()
        return f"{base}, {self.poste} (salaire: {self.salaire}€)"


class Manager(Employe):
    """Classe pour les managers"""

    def __init__(self, nom, prenom, age, salaire, equipe_size=0):
        super().__init__(nom, prenom, age, salaire, "Manager")
        self.equipe_size = equipe_size
        self.bonus = 0

    def gerer_equipe(self):
        return f"{self.prenom} gère une équipe de {self.equipe_size} personnes"

    def donner_bonus(self, montant):
        self.bonus += montant
        return f"Bonus de {montant}€ accordé à {self.prenom}"

    def calculer_salaire_mensuel(self):
        salaire_base = super().calculer_salaire_mensuel()
        return salaire_base + self.bonus

    def se_presenter(self):
        base = super().se_presenter()
        return f"{base}, équipe de {self.equipe_size}"


class Developpeur(Employe):
    """Classe pour les développeurs"""

    def __init__(self, nom, prenom, age, salaire, langages):
        super().__init__(nom, prenom, age, salaire, "Développeur")
        self.langages = langages if isinstance(langages, list) else [langages]
        self.projets_termines = 0

    def coder(self, langage, heures):
        if langage in self.langages:
            self.travailler(heures)
            return f"{self.prenom} code en {langage} pendant {heures}h"
        return f"{self.prenom} ne connaît pas {langage}"

    def terminer_projet(self):
        self.projets_termines += 1
        return f"{self.prenom} a terminé le projet #{self.projets_termines}"

    def se_presenter(self):
        base = super().se_presenter()
        langages_str = ", ".join(self.langages)
        return f"{base}, langages: {langages_str}"


print("💡 Exemple 6 : Hiérarchie d'employés")

# Création d'employés
employes = [
    Employe("Dupont", "Jean", 30, 2500, "Assistant"),
    Developpeur("Martin", "Alice", 28, 3500, ["Python", "JavaScript", "Java"]),
    Manager("Bernard", "Pierre", 40, 4500, 8)
]

print("\n👥 PRÉSENTATION DE L'ÉQUIPE :")
for emp in employes:
    print(f"   👤 {emp.se_presenter()}")

print("\n💼 ACTIVITÉS DE TRAVAIL :")
# Jean travaille
print("📋", employes[0].travailler(8))

# Alice code
alice = employes[1]
print("💻", alice.coder("Python", 6))
print("💻", alice.coder("C++", 2))  # Langage non maîtrisé
print("✅", alice.terminer_projet())

# Pierre manage
pierre = employes[2]
print("👔", pierre.gerer_equipe())
print("💰", pierre.donner_bonus(500))

print("\n💰 SALAIRES MENSUELS :")
for emp in employes:
    salaire = emp.calculer_salaire_mensuel()
    print(f"   💵 {emp.prenom} : {salaire}€")

print("\n" + "=" * 50)
print("8. RÉSUMÉ FINAL")
print("=" * 50)

print("""
🎯 POINTS CLÉS À RETENIR :

1. 🌳 HÉRITAGE :
   • class Enfant(Parent): pour hériter
   • Réutilisation du code parent
   • Extension avec nouvelles méthodes

2. 🔄 REDÉFINITION :
   • Même nom de méthode dans enfant
   • super() pour appeler la méthode parent
   • Possibilité d'étendre ou remplacer

3. 📞 SUPER() :
   • super().__init__() dans constructeur
   • super().methode() pour appeler parent
   • Respecte l'ordre d'héritage (MRO)

4. 🔄 HÉRITAGE MULTIPLE :
   • class Enfant(Parent1, Parent2):
   • MRO détermine l'ordre de résolution
   • Mixins pour fonctionnalités transversales

5. 🔍 VÉRIFICATION :
   • isinstance(obj, Classe) : obj est instance ?
   • issubclass(Enfant, Parent) : héritage ?
   • obj.__class__.__mro__ : ordre résolution

💡 FORMULE MAGIQUE :
   Héritage = Extension + Réutilisation + Spécialisation

🎉 Félicitations ! Vous maîtrisez l'héritage !
💡 Prochaine étape : Polymorphisme et méthodes abstraites !
📚 Code réutilisé, passez au polymorphisme !
""")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE - HÉRITAGE MAÎTRISÉ !")
print("=" * 70)
