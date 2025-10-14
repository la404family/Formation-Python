#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
======================================================================
DÉFINITION DES CLASSES EN PYTHON - GUIDE COMPLET
======================================================================

🎯 Ce fichier couvre la création et définition de classes en Python :
   • Syntaxe de base des classes
   • Constructeurs et méthodes
   • Attributs d'instance et de classe
   • Méthodes spéciales (__init__, __str__, __repr__)
   • Encapsulation et convention de nommage
   • Propriétés et accesseurs

📚 Concepts abordés :
   • Différence objet/classe/instance
   • Méthodes d'instance, de classe et statiques
   • Attributs publics, protégés et privés
   • Décorateurs @property, @classmethod, @staticmethod
   • Introspection et métaclasses de base

💡 Objectif : Maîtriser la création de classes robustes
"""

import math
from datetime import datetime, date
from typing import Optional, List, Dict, Any
from dataclasses import dataclass, field

print("=" * 70)
print("DÉFINITION DES CLASSES EN PYTHON - GUIDE COMPLET")
print("=" * 70)

print("\n" + "=" * 50)
print("1. SYNTAXE DE BASE DES CLASSES")
print("=" * 50)

print("\n🏗️ CRÉATION D'UNE CLASSE SIMPLE")
print("-" * 29)


class PersonneSimple:
    """Classe de base pour représenter une personne"""

    def __init__(self, nom, age):
        """Constructeur de la classe"""
        self.nom = nom
        self.age = age

    def se_presenter(self):
        """Méthode pour se présenter"""
        return f"Bonjour, je suis {self.nom} et j'ai {self.age} ans"

    def avoir_anniversaire(self):
        """Méthode pour vieillir d'un an"""
        self.age += 1
        return f"{self.nom} a maintenant {self.age} ans"


def demo_classe_simple():
    """Démonstration d'une classe simple"""

    print("🏗️ Utilisation d'une classe simple :")

    # Création d'instances
    personne1 = PersonneSimple("Alice", 25)
    personne2 = PersonneSimple("Bob", 30)

    print(f"   Personne 1 : {personne1.se_presenter()}")
    print(f"   Personne 2 : {personne2.se_presenter()}")

    # Modification d'attributs
    print(f"\n   Avant anniversaire : {personne1.nom} a {personne1.age} ans")
    print(f"   {personne1.avoir_anniversaire()}")

    # Accès direct aux attributs
    personne2.nom = "Robert"  # Modification directe
    print(f"   Nom modifié : {personne2.se_presenter()}")

    # Information sur la classe
    print(f"\n   Type de personne1 : {type(personne1)}")
    print(f"   Classe de personne1 : {personne1.__class__.__name__}")
    print(
        f"   personne1 est une instance de PersonneSimple : {isinstance(personne1, PersonneSimple)}")


demo_classe_simple()

print("\n🔧 AMÉLIORATION AVEC VALIDATION")
print("-" * 31)


class PersonneAmelioree:
    """Classe améliorée avec validation"""

    def __init__(self, nom: str, age: int, email: str = None):
        """Constructeur avec validation"""
        # Validation des paramètres
        if not isinstance(nom, str) or not nom.strip():
            raise ValueError("Le nom doit être une chaîne non vide")

        if not isinstance(age, int) or age < 0:
            raise ValueError("L'âge doit être un entier positif")

        if email is not None and "@" not in email:
            raise ValueError("L'email doit contenir un @")

        # Initialisation des attributs
        self.nom = nom.strip().title()  # Formatage
        self.age = age
        self.email = email
        self.date_creation = datetime.now()

    def se_presenter(self) -> str:
        """Présentation formatée"""
        presentation = f"Je suis {self.nom}, {self.age} ans"
        if self.email:
            presentation += f" ({self.email})"
        return presentation

    def est_majeur(self) -> bool:
        """Vérifier si la personne est majeure"""
        return self.age >= 18

    def __str__(self) -> str:
        """Représentation string pour l'utilisateur"""
        return f"{self.nom} ({self.age} ans)"

    def __repr__(self) -> str:
        """Représentation technique pour le développeur"""
        return f"PersonneAmelioree(nom='{self.nom}', age={self.age}, email='{self.email}')"


def demo_classe_amelioree():
    """Démonstration de la classe améliorée"""

    print("🔧 Classe avec validation et améliorations :")

    try:
        # Création avec validation
        personne = PersonneAmelioree("alice dupont", 25, "alice@test.com")
        print(f"   Création réussie : {personne}")
        print(f"   Présentation : {personne.se_presenter()}")
        print(f"   Est majeure : {personne.est_majeur()}")
        print(f"   Repr technique : {repr(personne)}")

        # Test des validations
        print(f"\n   Tests de validation :")

        try:
            PersonneAmelioree("", 25)  # Nom vide
        except ValueError as e:
            print(f"   ❌ Nom vide : {e}")

        try:
            PersonneAmelioree("Bob", -5)  # Âge négatif
        except ValueError as e:
            print(f"   ❌ Âge négatif : {e}")

        try:
            # Email invalide
            PersonneAmelioree("Charlie", 30, "email-invalide")
        except ValueError as e:
            print(f"   ❌ Email invalide : {e}")

    except Exception as e:
        print(f"   💥 Erreur : {e}")


demo_classe_amelioree()

print("\n" + "=" * 50)
print("2. ATTRIBUTS D'INSTANCE ET DE CLASSE")
print("=" * 50)

print("\n🏷️ ATTRIBUTS D'INSTANCE VS CLASSE")
print("-" * 31)


class Employe:
    """Classe démontrant les attributs d'instance et de classe"""

    # Attributs de classe (partagés par toutes les instances)
    entreprise = "Tech Corp"
    nombre_employes = 0
    salaire_minimum = 30000

    def __init__(self, nom: str, poste: str, salaire: float):
        """Constructeur avec attributs d'instance"""
        # Attributs d'instance (spécifiques à chaque instance)
        self.nom = nom
        self.poste = poste
        # Utilise attribut de classe
        self.salaire = max(salaire, Employe.salaire_minimum)
        self.date_embauche = datetime.now()
        self.numero_employe = Employe.nombre_employes + 1

        # Incrémenter le compteur de classe
        Employe.nombre_employes += 1

    def obtenir_info(self) -> str:
        """Informations sur l'employé"""
        return f"#{self.numero_employe} - {self.nom} ({self.poste}) - {self.salaire}€ chez {Employe.entreprise}"

    def augmentation(self, pourcentage: float):
        """Donner une augmentation"""
        ancien_salaire = self.salaire
        self.salaire *= (1 + pourcentage / 100)
        return f"Salaire de {self.nom} : {ancien_salaire}€ → {self.salaire:.2f}€"

    @classmethod
    def modifier_entreprise(cls, nouvelle_entreprise: str):
        """Modifier le nom de l'entreprise (méthode de classe)"""
        ancienne = cls.entreprise
        cls.entreprise = nouvelle_entreprise
        return f"Entreprise changée : {ancienne} → {nouvelle_entreprise}"

    @classmethod
    def augmenter_salaire_minimum(cls, nouveau_minimum: float):
        """Modifier le salaire minimum (méthode de classe)"""
        ancien = cls.salaire_minimum
        cls.salaire_minimum = nouveau_minimum
        return f"Salaire minimum : {ancien}€ → {nouveau_minimum}€"

    @staticmethod
    def valider_salaire(salaire: float) -> bool:
        """Valider un salaire (méthode statique)"""
        return isinstance(salaire, (int, float)) and salaire > 0

    def __del__(self):
        """Destructeur (appelé quand l'objet est supprimé)"""
        Employe.nombre_employes -= 1
        print(f"   👋 {self.nom} a quitté l'entreprise")


def demo_attributs_classe():
    """Démonstration des attributs de classe et d'instance"""

    print("🏷️ Attributs d'instance vs classe :")

    print(f"   État initial :")
    print(f"   📊 Entreprise : {Employe.entreprise}")
    print(f"   📊 Nombre d'employés : {Employe.nombre_employes}")
    print(f"   📊 Salaire minimum : {Employe.salaire_minimum}€")

    # Création d'employés
    print(f"\n   Création d'employés :")
    emp1 = Employe("Alice Martin", "Développeuse", 45000)
    emp2 = Employe("Bob Durand", "Designer", 25000)  # Sous le minimum
    emp3 = Employe("Charlie Petit", "Manager", 55000)

    print(f"   {emp1.obtenir_info()}")
    print(f"   {emp2.obtenir_info()}")  # Salaire ajusté au minimum
    print(f"   {emp3.obtenir_info()}")

    print(
        f"\n   📊 Après création - Nombre d'employés : {Employe.nombre_employes}")

    # Modification d'attributs de classe
    print(f"\n   Modifications de classe :")
    print(f"   {Employe.modifier_entreprise('Nouvelle Tech Corp')}")
    print(f"   {Employe.augmenter_salaire_minimum(35000)}")

    # Impact sur les instances existantes
    print(f"\n   Impact sur les instances existantes :")
    print(f"   {emp1.obtenir_info()}")  # Nouvelle entreprise affichée

    # Nouvel employé avec nouveau minimum
    emp4 = Employe("Diane Rouge", "Analyste", 32000)  # Sous le nouveau minimum
    print(f"   {emp4.obtenir_info()}")

    # Test méthode statique
    print(f"\n   Validation de salaires :")
    print(f"   Salaire 50000 valide : {Employe.valider_salaire(50000)}")
    print(f"   Salaire -1000 valide : {Employe.valider_salaire(-1000)}")
    print(f"   Salaire 'abc' valide : {Employe.valider_salaire('abc')}")


demo_attributs_classe()

print("\n🎯 ATTRIBUTS DYNAMIQUES")
print("-" * 21)


class PersonneDynamique:
    """Classe permettant l'ajout dynamique d'attributs"""

    def __init__(self, nom: str):
        self.nom = nom
        self._attributs_personnalises = {}

    def ajouter_attribut(self, nom_attribut: str, valeur: Any):
        """Ajouter un attribut personnalisé"""
        if hasattr(self, nom_attribut):
            raise ValueError(f"L'attribut '{nom_attribut}' existe déjà")

        self._attributs_personnalises[nom_attribut] = valeur
        setattr(self, nom_attribut, valeur)

        return f"Attribut '{nom_attribut}' ajouté avec la valeur '{valeur}'"

    def lister_attributs(self) -> Dict[str, Any]:
        """Lister tous les attributs"""
        attributs = {}

        # Attributs de base
        for attr, valeur in self.__dict__.items():
            if not attr.startswith('_'):
                attributs[attr] = valeur

        return attributs

    def supprimer_attribut(self, nom_attribut: str):
        """Supprimer un attribut personnalisé"""
        if nom_attribut in self._attributs_personnalises:
            del self._attributs_personnalises[nom_attribut]
            if hasattr(self, nom_attribut):
                delattr(self, nom_attribut)
            return f"Attribut '{nom_attribut}' supprimé"
        else:
            raise ValueError(f"Attribut '{nom_attribut}' non trouvé")


def demo_attributs_dynamiques():
    """Démonstration des attributs dynamiques"""

    print("🎯 Attributs dynamiques :")

    personne = PersonneDynamique("Alice")

    print(f"   Attributs initiaux : {personne.lister_attributs()}")

    # Ajout d'attributs dynamiques
    print(f"\n   Ajout d'attributs :")
    print(f"   {personne.ajouter_attribut('age', 25)}")
    print(f"   {personne.ajouter_attribut('ville', 'Paris')}")
    print(f"   {personne.ajouter_attribut('hobbies', ['lecture', 'sport'])}")

    # Utilisation des nouveaux attributs
    print(f"\n   Utilisation des attributs ajoutés :")
    print(f"   Nom : {personne.nom}")
    print(f"   Âge : {personne.age}")
    print(f"   Ville : {personne.ville}")
    print(f"   Hobbies : {personne.hobbies}")

    print(f"\n   Tous les attributs : {personne.lister_attributs()}")

    # Suppression d'attribut
    print(f"\n   {personne.supprimer_attribut('ville')}")
    print(f"   Attributs après suppression : {personne.lister_attributs()}")

    # Test d'erreur
    try:
        personne.ajouter_attribut('nom', 'Bob')  # Existe déjà
    except ValueError as e:
        print(f"   ❌ Erreur attendue : {e}")


demo_attributs_dynamiques()

print("\n" + "=" * 50)
print("3. ENCAPSULATION ET CONVENTION DE NOMMAGE")
print("=" * 50)

print("\n🔒 ENCAPSULATION ET VISIBILITÉ")
print("-" * 29)


class CompteBancaire:
    """Classe démontrant l'encapsulation en Python"""

    def __init__(self, numero_compte: str, titulaire: str, solde_initial: float = 0):
        # Attribut public
        self.numero_compte = numero_compte
        self.titulaire = titulaire

        # Attribut protégé (convention : un underscore)
        self._solde = solde_initial
        self._historique = [f"Ouverture compte avec {solde_initial}€"]

        # Attribut privé (convention : deux underscores)
        self.__code_secret = self._generer_code_secret()
        self.__tentatives_echec = 0

    def _generer_code_secret(self) -> str:
        """Méthode protégée pour générer un code secret"""
        import random
        return ''.join([str(random.randint(0, 9)) for _ in range(4)])

    def __valider_code(self, code: str) -> bool:
        """Méthode privée pour valider le code"""
        if code == self.__code_secret:
            self.__tentatives_echec = 0
            return True
        else:
            self.__tentatives_echec += 1
            return False

    def deposer(self, montant: float, code_secret: str) -> str:
        """Déposer de l'argent"""
        if not self.__valider_code(code_secret):
            return f"❌ Code incorrect ({self.__tentatives_echec} tentatives)"

        if montant <= 0:
            return "❌ Le montant doit être positif"

        self._solde += montant
        self._historique.append(f"Dépôt de {montant}€")
        return f"✅ Dépôt de {montant}€ effectué. Nouveau solde : {self._solde}€"

    def retirer(self, montant: float, code_secret: str) -> str:
        """Retirer de l'argent"""
        if not self.__valider_code(code_secret):
            return f"❌ Code incorrect ({self.__tentatives_echec} tentatives)"

        if montant <= 0:
            return "❌ Le montant doit être positif"

        if montant > self._solde:
            return f"❌ Solde insuffisant (solde actuel : {self._solde}€)"

        self._solde -= montant
        self._historique.append(f"Retrait de {montant}€")
        return f"✅ Retrait de {montant}€ effectué. Nouveau solde : {self._solde}€"

    def consulter_solde(self, code_secret: str) -> str:
        """Consulter le solde"""
        if not self.__valider_code(code_secret):
            return f"❌ Code incorrect ({self.__tentatives_echec} tentatives)"

        return f"💰 Solde actuel : {self._solde}€"

    def obtenir_historique(self, code_secret: str) -> List[str]:
        """Obtenir l'historique des opérations"""
        if not self.__valider_code(code_secret):
            return [f"❌ Code incorrect ({self.__tentatives_echec} tentatives)"]

        return self._historique.copy()  # Copie pour éviter modification externe

    def changer_code(self, ancien_code: str, nouveau_code: str) -> str:
        """Changer le code secret"""
        if not self.__valider_code(ancien_code):
            return f"❌ Ancien code incorrect"

        if len(nouveau_code) != 4 or not nouveau_code.isdigit():
            return "❌ Le nouveau code doit être composé de 4 chiffres"

        self.__code_secret = nouveau_code
        self._historique.append("Code secret modifié")
        return "✅ Code secret modifié avec succès"

    def __str__(self) -> str:
        """Représentation publique du compte"""
        return f"Compte {self.numero_compte} - {self.titulaire}"

    def __repr__(self) -> str:
        """Représentation technique"""
        return f"CompteBancaire(numero='{self.numero_compte}', titulaire='{self.titulaire}')"


def demo_encapsulation():
    """Démonstration de l'encapsulation"""

    print("🔒 Encapsulation et sécurité :")

    # Création d'un compte
    compte = CompteBancaire("12345", "Alice Martin", 1000)
    print(f"   Compte créé : {compte}")

    # Le code secret est généré automatiquement, mais on peut le récupérer pour les tests
    # Note : En réalité, on ne devrait JAMAIS pouvoir accéder au code ainsi !
    code_secret = compte._CompteBancaire__code_secret  # Name mangling
    print(f"   Code secret (pour test) : {code_secret}")

    # Opérations normales
    print(f"\n   Opérations avec bon code :")
    print(f"   {compte.consulter_solde(code_secret)}")
    print(f"   {compte.deposer(500, code_secret)}")
    print(f"   {compte.retirer(200, code_secret)}")

    # Tentatives avec mauvais code
    print(f"\n   Tentatives avec mauvais code :")
    print(f"   {compte.consulter_solde('0000')}")
    print(f"   {compte.deposer(100, '1111')}")
    print(f"   {compte.retirer(50, '2222')}")

    # Accès aux attributs
    print(f"\n   Accès aux attributs :")
    print(f"   Numéro compte (public) : {compte.numero_compte}")
    print(f"   Titulaire (public) : {compte.titulaire}")

    # Attribut protégé (possible mais déconseillé)
    print(f"   Solde (protégé) : {compte._solde}€")

    # Historique avec bon code
    print(f"\n   Historique des opérations :")
    historique = compte.obtenir_historique(code_secret)
    for operation in historique:
        print(f"      • {operation}")

    # Changement de code
    print(f"\n   Changement de code :")
    print(f"   {compte.changer_code(code_secret, '9876')}")
    print(f"   {compte.consulter_solde('9876')}")


demo_encapsulation()

print("\n🎨 CONVENTIONS DE NOMMAGE PYTHON")
print("-" * 33)


class ConventionsNommage:
    """Classe illustrant les conventions de nommage Python"""

    # Constante de classe (tout en majuscules)
    VERSION = "1.0.0"
    MAX_TENTATIVES = 3

    def __init__(self, nom: str):
        # Attribut public
        self.nom = nom

        # Attribut protégé (usage interne)
        self._id_interne = id(self)

        # Attribut privé (name mangling)
        self.__token_prive = f"token_{id(self)}"

    def methode_publique(self) -> str:
        """Méthode publique accessible de partout"""
        return f"Méthode publique appelée pour {self.nom}"

    def _methode_protegee(self) -> str:
        """Méthode protégée (usage interne recommandé)"""
        return f"ID interne : {self._id_interne}"

    def __methode_privee(self) -> str:
        """Méthode privée (name mangling)"""
        return f"Token privé : {self.__token_prive}"

    @property
    def info_publique(self) -> str:
        """Propriété publique"""
        return f"{self.nom} (v{self.VERSION})"

    @property
    def _info_protegee(self) -> str:
        """Propriété protégée"""
        return self._methode_protegee()

    def obtenir_infos_completes(self) -> Dict[str, str]:
        """Méthode utilisant tous les niveaux d'accès"""
        return {
            "public": self.methode_publique(),
            "protegé": self._methode_protegee(),
            "privé": self.__methode_privee()
        }


def demo_conventions_nommage():
    """Démonstration des conventions de nommage"""

    print("🎨 Conventions de nommage Python :")

    obj = ConventionsNommage("Test")

    # Accès public normal
    print(f"   Méthode publique : {obj.methode_publique()}")
    print(f"   Propriété publique : {obj.info_publique}")
    print(f"   Constante de classe : {ConventionsNommage.VERSION}")

    # Accès protégé (possible mais déconseillé hors héritage)
    print(f"\n   Accès protégé (déconseillé) :")
    print(f"   Méthode protégée : {obj._methode_protegee()}")
    print(f"   Propriété protégée : {obj._info_protegee}")
    print(f"   Attribut protégé : {obj._id_interne}")

    # Accès privé (name mangling)
    print(f"\n   Accès privé via name mangling :")
    try:
        # Ceci ne fonctionne pas
        print(obj.__token_prive)
    except AttributeError as e:
        print(f"   ❌ Accès direct impossible : {e}")

    # Accès via name mangling (déconseillé)
    token_via_mangling = obj._ConventionsNommage__token_prive
    print(f"   Token via name mangling : {token_via_mangling}")

    # Utilisation recommandée via méthode publique
    print(f"\n   Utilisation recommandée :")
    infos = obj.obtenir_infos_completes()
    for niveau, info in infos.items():
        print(f"   {niveau.capitalize()} : {info}")

    # Inspection des attributs
    print(f"\n   Inspection des attributs :")
    print(f"   dir() (attributs visibles) :")
    attributs_visibles = [attr for attr in dir(
        obj) if not attr.startswith('__') or attr.endswith('__')]
    for attr in sorted(attributs_visibles)[:10]:  # Limite pour lisibilité
        print(f"      • {attr}")

    print(f"   __dict__ (attributs d'instance) :")
    for attr, valeur in obj.__dict__.items():
        print(f"      • {attr}: {valeur}")


demo_conventions_nommage()

print("\n" + "=" * 50)
print("4. PROPRIÉTÉS ET ACCESSEURS")
print("=" * 50)

print("\n🏠 PROPRIÉTÉS AVEC @property")
print("-" * 27)


class Temperature:
    """Classe démontrant l'utilisation des propriétés"""

    def __init__(self, celsius: float = 0):
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        """Getter pour les degrés Celsius"""
        return self._celsius

    @celsius.setter
    def celsius(self, valeur: float):
        """Setter pour les degrés Celsius avec validation"""
        if valeur < -273.15:
            raise ValueError(
                "La température ne peut pas être inférieure au zéro absolu")
        self._celsius = valeur

    @property
    def fahrenheit(self) -> float:
        """Propriété calculée : conversion en Fahrenheit"""
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, valeur: float):
        """Setter pour Fahrenheit (convertit en Celsius)"""
        celsius = (valeur - 32) * 5/9
        self.celsius = celsius  # Utilise la validation du setter celsius

    @property
    def kelvin(self) -> float:
        """Propriété calculée : conversion en Kelvin"""
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, valeur: float):
        """Setter pour Kelvin (convertit en Celsius)"""
        if valeur < 0:
            raise ValueError(
                "La température en Kelvin ne peut pas être négative")
        self.celsius = valeur - 273.15

    @property
    def description(self) -> str:
        """Propriété en lecture seule : description de la température"""
        if self._celsius < 0:
            return "Température de congélation"
        elif self._celsius < 20:
            return "Température froide"
        elif self._celsius < 30:
            return "Température agréable"
        else:
            return "Température chaude"

    def __str__(self) -> str:
        return f"Température: {self._celsius:.1f}°C ({self.fahrenheit:.1f}°F, {self.kelvin:.1f}K)"


def demo_proprietes():
    """Démonstration des propriétés"""

    print("🏠 Utilisation des propriétés :")

    # Création et utilisation normale
    temp = Temperature(25)
    print(f"   Température initiale : {temp}")
    print(f"   Description : {temp.description}")

    # Modification via propriété celsius
    print(f"\n   Modification via Celsius :")
    temp.celsius = 0
    print(f"   Après changement à 0°C : {temp}")
    print(f"   Description : {temp.description}")

    # Modification via propriété fahrenheit
    print(f"\n   Modification via Fahrenheit :")
    temp.fahrenheit = 100  # 100°F = 37.78°C
    print(f"   Après changement à 100°F : {temp}")
    print(f"   Description : {temp.description}")

    # Modification via propriété kelvin
    print(f"\n   Modification via Kelvin :")
    temp.kelvin = 300  # 300K = 26.85°C
    print(f"   Après changement à 300K : {temp}")
    print(f"   Description : {temp.description}")

    # Tests de validation
    print(f"\n   Tests de validation :")
    try:
        temp.celsius = -300  # Sous le zéro absolu
    except ValueError as e:
        print(f"   ❌ Celsius invalide : {e}")

    try:
        temp.kelvin = -10  # Kelvin négatif
    except ValueError as e:
        print(f"   ❌ Kelvin invalide : {e}")

    # Propriété en lecture seule
    print(f"\n   Propriété en lecture seule :")
    print(f"   Description actuelle : {temp.description}")
    try:
        temp.description = "Nouvelle description"  # Impossible
    except AttributeError as e:
        print(f"   ❌ Modification impossible : {e}")


demo_proprietes()

print("\n🔧 PROPRIÉTÉS AVANCÉES")
print("-" * 21)


class Produit:
    """Classe avec propriétés avancées et validation"""

    def __init__(self, nom: str, prix_unitaire: float, quantite: int = 0):
        self._nom = nom
        self._prix_unitaire = prix_unitaire
        self._quantite = quantite
        self._remise = 0.0
        self._historique_prix = [prix_unitaire]

    @property
    def nom(self) -> str:
        return self._nom

    @nom.setter
    def nom(self, valeur: str):
        if not isinstance(valeur, str) or not valeur.strip():
            raise ValueError("Le nom doit être une chaîne non vide")
        self._nom = valeur.strip()

    @property
    def prix_unitaire(self) -> float:
        return self._prix_unitaire

    @prix_unitaire.setter
    def prix_unitaire(self, valeur: float):
        if not isinstance(valeur, (int, float)) or valeur <= 0:
            raise ValueError("Le prix doit être un nombre positif")

        # Historique des prix
        if valeur != self._prix_unitaire:
            self._historique_prix.append(valeur)

        self._prix_unitaire = float(valeur)

    @property
    def quantite(self) -> int:
        return self._quantite

    @quantite.setter
    def quantite(self, valeur: int):
        if not isinstance(valeur, int) or valeur < 0:
            raise ValueError("La quantité doit être un entier positif")
        self._quantite = valeur

    @property
    def remise(self) -> float:
        return self._remise

    @remise.setter
    def remise(self, valeur: float):
        if not isinstance(valeur, (int, float)) or not (0 <= valeur <= 1):
            raise ValueError("La remise doit être entre 0 et 1")
        self._remise = float(valeur)

    @property
    def prix_avec_remise(self) -> float:
        """Prix unitaire après remise"""
        return self._prix_unitaire * (1 - self._remise)

    @property
    def prix_total(self) -> float:
        """Prix total (quantité × prix avec remise)"""
        return self._quantite * self.prix_avec_remise

    @property
    def en_stock(self) -> bool:
        """Vérifier si le produit est en stock"""
        return self._quantite > 0

    @property
    def economie_remise(self) -> float:
        """Économie réalisée grâce à la remise"""
        return self._quantite * self._prix_unitaire * self._remise

    @property
    def historique_prix(self) -> List[float]:
        """Historique des prix (lecture seule)"""
        return self._historique_prix.copy()

    @property
    def variation_prix(self) -> Dict[str, float]:
        """Variation du prix depuis le début"""
        if len(self._historique_prix) < 2:
            return {"variation_absolue": 0, "variation_pourcentage": 0}

        prix_initial = self._historique_prix[0]
        prix_actuel = self._historique_prix[-1]

        variation_abs = prix_actuel - prix_initial
        variation_pct = (variation_abs / prix_initial) * 100

        return {
            "variation_absolue": variation_abs,
            "variation_pourcentage": variation_pct
        }

    def ajouter_stock(self, quantite: int):
        """Ajouter du stock"""
        if quantite <= 0:
            raise ValueError("La quantité à ajouter doit être positive")
        self.quantite += quantite

    def retirer_stock(self, quantite: int):
        """Retirer du stock"""
        if quantite <= 0:
            raise ValueError("La quantité à retirer doit être positive")
        if quantite > self.quantite:
            raise ValueError("Stock insuffisant")
        self.quantite -= quantite

    def __str__(self) -> str:
        status = "En stock" if self.en_stock else "Rupture"
        return f"{self.nom} - {self.prix_avec_remise:.2f}€ × {self.quantite} = {self.prix_total:.2f}€ ({status})"


def demo_proprietes_avancees():
    """Démonstration des propriétés avancées"""

    print("🔧 Propriétés avancées :")

    # Création d'un produit
    produit = Produit("Ordinateur portable", 1000, 5)
    print(f"   Produit initial : {produit}")

    # Ajout d'une remise
    print(f"\n   Application d'une remise de 15% :")
    produit.remise = 0.15
    print(f"   Produit avec remise : {produit}")
    print(f"   Économie réalisée : {produit.economie_remise:.2f}€")

    # Modification du prix
    print(f"\n   Historique et variation des prix :")
    print(f"   Prix initial : {produit.historique_prix}")

    produit.prix_unitaire = 1200  # Augmentation
    print(f"   Après augmentation : {produit}")

    produit.prix_unitaire = 900   # Baisse
    print(f"   Après baisse : {produit}")

    variation = produit.variation_prix
    print(
        f"   Variation depuis début : {variation['variation_absolue']:.2f}€ ({variation['variation_pourcentage']:.1f}%)")
    print(f"   Historique complet : {produit.historique_prix}")

    # Gestion du stock
    print(f"\n   Gestion du stock :")
    print(f"   En stock : {produit.en_stock}")

    produit.retirer_stock(3)
    print(f"   Après retrait de 3 : {produit}")

    produit.ajouter_stock(10)
    print(f"   Après ajout de 10 : {produit}")

    # Tests de validation
    print(f"\n   Tests de validation :")
    try:
        produit.prix_unitaire = -100
    except ValueError as e:
        print(f"   ❌ Prix négatif : {e}")

    try:
        produit.remise = 1.5  # 150%
    except ValueError as e:
        print(f"   ❌ Remise invalide : {e}")

    try:
        produit.retirer_stock(100)  # Plus que le stock
    except ValueError as e:
        print(f"   ❌ Stock insuffisant : {e}")


demo_proprietes_avancees()

print("\n" + "=" * 50)
print("5. MÉTHODES SPÉCIALES ET INTROSPECTION")
print("=" * 50)

print("\n🔍 MÉTHODES SPÉCIALES (__dunder__)")
print("-" * 32)


class Vecteur:
    """Classe démontrant les méthodes spéciales"""

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """Représentation pour l'utilisateur"""
        return f"Vecteur({self.x}, {self.y})"

    def __repr__(self) -> str:
        """Représentation pour le développeur"""
        return f"Vecteur(x={self.x}, y={self.y})"

    def __add__(self, autre):
        """Addition de vecteurs avec +"""
        if isinstance(autre, Vecteur):
            return Vecteur(self.x + autre.x, self.y + autre.y)
        return NotImplemented

    def __sub__(self, autre):
        """Soustraction de vecteurs avec -"""
        if isinstance(autre, Vecteur):
            return Vecteur(self.x - autre.x, self.y - autre.y)
        return NotImplemented

    def __mul__(self, scalaire):
        """Multiplication par un scalaire avec *"""
        if isinstance(scalaire, (int, float)):
            return Vecteur(self.x * scalaire, self.y * scalaire)
        return NotImplemented

    def __rmul__(self, scalaire):
        """Multiplication à droite (scalaire * vecteur)"""
        return self.__mul__(scalaire)

    def __truediv__(self, scalaire):
        """Division par un scalaire avec /"""
        if isinstance(scalaire, (int, float)) and scalaire != 0:
            return Vecteur(self.x / scalaire, self.y / scalaire)
        elif scalaire == 0:
            raise ZeroDivisionError("Division par zéro")
        return NotImplemented

    def __eq__(self, autre) -> bool:
        """Égalité avec =="""
        if isinstance(autre, Vecteur):
            return self.x == autre.x and self.y == autre.y
        return False

    def __ne__(self, autre) -> bool:
        """Inégalité avec !="""
        return not self.__eq__(autre)

    def __lt__(self, autre) -> bool:
        """Comparaison < (basée sur la magnitude)"""
        if isinstance(autre, Vecteur):
            return self.magnitude() < autre.magnitude()
        return NotImplemented

    def __le__(self, autre) -> bool:
        """Comparaison <= (basée sur la magnitude)"""
        if isinstance(autre, Vecteur):
            return self.magnitude() <= autre.magnitude()
        return NotImplemented

    def __gt__(self, autre) -> bool:
        """Comparaison > (basée sur la magnitude)"""
        if isinstance(autre, Vecteur):
            return self.magnitude() > autre.magnitude()
        return NotImplemented

    def __ge__(self, autre) -> bool:
        """Comparaison >= (basée sur la magnitude)"""
        if isinstance(autre, Vecteur):
            return self.magnitude() >= autre.magnitude()
        return NotImplemented

    def __abs__(self) -> float:
        """Valeur absolue avec abs() (magnitude)"""
        return self.magnitude()

    def __len__(self) -> int:
        """Longueur avec len() (nombre de composantes)"""
        return 2

    def __getitem__(self, index: int) -> float:
        """Accès par indice avec []"""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Index de vecteur hors limites")

    def __setitem__(self, index: int, valeur: float):
        """Modification par indice avec []"""
        if index == 0:
            self.x = valeur
        elif index == 1:
            self.y = valeur
        else:
            raise IndexError("Index de vecteur hors limites")

    def __iter__(self):
        """Itération avec for"""
        yield self.x
        yield self.y

    def __contains__(self, valeur) -> bool:
        """Test d'appartenance avec in"""
        return valeur in (self.x, self.y)

    def __hash__(self) -> int:
        """Hash pour utilisation comme clé de dictionnaire"""
        return hash((self.x, self.y))

    def __bool__(self) -> bool:
        """Vérité avec bool() (vrai si non nul)"""
        return self.x != 0 or self.y != 0

    def __call__(self, operation: str = "magnitude"):
        """Rendre l'objet callable avec ()"""
        if operation == "magnitude":
            return self.magnitude()
        elif operation == "angle":
            return self.angle()
        elif operation == "normalize":
            return self.normalise()
        else:
            raise ValueError(f"Opération '{operation}' non supportée")

    # Méthodes utilitaires
    def magnitude(self) -> float:
        """Calculer la magnitude du vecteur"""
        return math.sqrt(self.x**2 + self.y**2)

    def angle(self) -> float:
        """Calculer l'angle en radians"""
        return math.atan2(self.y, self.x)

    def normalise(self):
        """Retourner un vecteur normalisé"""
        mag = self.magnitude()
        if mag == 0:
            return Vecteur(0, 0)
        return Vecteur(self.x / mag, self.y / mag)


def demo_methodes_speciales():
    """Démonstration des méthodes spéciales"""

    print("🔍 Méthodes spéciales :")

    # Création de vecteurs
    v1 = Vecteur(3, 4)
    v2 = Vecteur(1, 2)
    v3 = Vecteur(0, 0)  # Vecteur nul

    print(f"   v1 = {v1}")
    print(f"   v2 = {v2}")
    print(f"   v3 = {v3}")

    # Opérations arithmétiques
    print(f"\n   Opérations arithmétiques :")
    print(f"   v1 + v2 = {v1 + v2}")
    print(f"   v1 - v2 = {v1 - v2}")
    print(f"   v1 * 2 = {v1 * 2}")
    print(f"   3 * v2 = {3 * v2}")
    print(f"   v1 / 2 = {v1 / 2}")

    # Comparaisons
    print(f"\n   Comparaisons :")
    print(f"   v1 == v2 : {v1 == v2}")
    print(f"   v1 != v2 : {v1 != v2}")
    print(f"   v1 > v2 (magnitude) : {v1 > v2}")
    print(f"   v1 < v2 (magnitude) : {v1 < v2}")

    # Fonctions builtin
    print(f"\n   Fonctions builtin :")
    print(f"   abs(v1) (magnitude) : {abs(v1)}")
    print(f"   len(v1) (composantes) : {len(v1)}")
    print(f"   bool(v1) : {bool(v1)}")
    print(f"   bool(v3) : {bool(v3)}")

    # Accès par indice
    print(f"\n   Accès par indice :")
    print(f"   v1[0] = {v1[0]}")
    print(f"   v1[1] = {v1[1]}")

    v1[0] = 5  # Modification
    print(f"   Après v1[0] = 5 : {v1}")

    # Itération
    print(f"\n   Itération :")
    print("   Composantes de v2 :", end=" ")
    for composante in v2:
        print(composante, end=" ")
    print()

    # Test d'appartenance
    print(f"\n   Test d'appartenance :")
    print(f"   3 in v1 : {3 in v1}")
    print(f"   4 in v1 : {4 in v1}")
    print(f"   10 in v1 : {10 in v1}")

    # Utilisation comme callable
    print(f"\n   Objet callable :")
    print(f"   v1() (magnitude) : {v1()}")
    print(f"   v1('angle') : {v1('angle'):.3f} radians")
    print(f"   v1('normalize') : {v1('normalize')}")

    # Hash (utilisation comme clé de dictionnaire)
    print(f"\n   Utilisation comme clé de dictionnaire :")
    vecteurs = {v1: "Premier vecteur", v2: "Deuxième vecteur"}
    print(f"   Dictionnaire : {vecteurs}")
    print(f"   vecteurs[v1] : {vecteurs[v1]}")


demo_methodes_speciales()

print("\n🔬 INTROSPECTION DE CLASSES")
print("-" * 26)


def demo_introspection():
    """Démonstration de l'introspection de classes"""

    print("🔬 Introspection de classes :")

    # Utilisation de la classe Vecteur créée précédemment
    vecteur = Vecteur(3, 4)

    print(f"\n   Informations de base :")
    print(f"   Type : {type(vecteur)}")
    print(f"   Classe : {vecteur.__class__.__name__}")
    print(f"   Module : {vecteur.__class__.__module__}")
    print(f"   ID : {id(vecteur)}")

    # Attributs et méthodes
    print(f"\n   Attributs d'instance :")
    for attr, valeur in vecteur.__dict__.items():
        print(f"      {attr}: {valeur}")

    print(f"\n   Méthodes spéciales :")
    methodes_speciales = [attr for attr in dir(
        vecteur) if attr.startswith('__') and attr.endswith('__')]
    for methode in sorted(methodes_speciales)[:10]:  # Limite pour lisibilité
        print(f"      {methode}")

    print(f"\n   Méthodes publiques :")
    methodes_publiques = [attr for attr in dir(vecteur) if not attr.startswith(
        '_') and callable(getattr(vecteur, attr))]
    for methode in sorted(methodes_publiques):
        print(f"      {methode}()")

    # Tests d'appartenance
    print(f"\n   Tests d'appartenance :")
    print(f"   isinstance(vecteur, Vecteur) : {isinstance(vecteur, Vecteur)}")
    print(f"   isinstance(vecteur, object) : {isinstance(vecteur, object)}")
    print(f"   hasattr(vecteur, 'x') : {hasattr(vecteur, 'x')}")
    print(
        f"   hasattr(vecteur, 'magnitude') : {hasattr(vecteur, 'magnitude')}")

    # Accès dynamique aux attributs
    print(f"\n   Accès dynamique :")
    print(f"   getattr(vecteur, 'x') : {getattr(vecteur, 'x')}")
    print(
        f"   getattr(vecteur, 'z', 'Attribut inexistant') : {getattr(vecteur, 'z', 'Attribut inexistant')}")

    # Modification dynamique
    setattr(vecteur, 'couleur', 'rouge')
    print(f"   Après setattr(vecteur, 'couleur', 'rouge') : {vecteur.couleur}")

    # Documentation
    print(f"\n   Documentation :")
    print(f"   Docstring de la classe : {Vecteur.__doc__}")
    print(f"   Docstring de __init__ : {Vecteur.__init__.__doc__}")


demo_introspection()

print("\n" + "=" * 50)
print("6. EXERCICES PRATIQUES")
print("=" * 50)

print("""
💪 EXERCICES À IMPLÉMENTER :

🎯 Exercice 1 : Classe Bibliothèque
Créez une classe Bibliothèque complète :
• Attributs : nom, adresse, livres (liste), membres
• Méthodes : ajouter_livre, emprunter_livre, rendre_livre
• Propriétés : nombre_livres, livres_disponibles
• Validation et encapsulation appropriées
• Méthodes spéciales (__str__, __len__, __contains__)

🔧 Exercice 2 : Classe CompteBancaire Avancé
Améliorez la classe CompteBancaire :
• Types de comptes (courant, épargne, pro)
• Limites de découvert par type
• Calcul d'intérêts automatique  
• Historique détaillé avec horodatage
• Méthodes de classe pour statistiques globales
• Sérialisation et désérialisation

🎮 Exercice 3 : Système de Points et Récompenses
Créez un système de gamification :
• Classe Utilisateur avec niveau et expérience
• Classe Récompense avec conditions
• Calcul automatique de niveau
• Déblocage de récompenses
• Statistiques et classements
• Sauvegarde des données

⚡ Exercice 4 : Gestionnaire de Tâches OOP
Créez un gestionnaire de tâches orienté objet :
• Classe Tâche avec priorité, deadline, statut
• Classe Projet regroupant des tâches
• Classe Assigné pour les responsabilités
• Propriétés calculées (progression, temps restant)
• Tri et filtrage intelligent
• Notifications et rappels

🌐 Exercice 5 : Framework de Validation
Créez un framework de validation de données :
• Classe Validator de base abstraite
• Validators spécialisés (EmailValidator, AgeValidator)
• Composition de validateurs
• Messages d'erreur personnalisés
• Validation de classes complètes
• Décorateurs de validation
""")

print("\n" + "=" * 50)
print("7. RÉSUMÉ FINAL")
print("=" * 50)

print("""
🎯 POINTS CLÉS À RETENIR :

1. 🏗️ SYNTAXE DE BASE :
   • class NomClasse: pour définir une classe
   • __init__(self, ...) pour le constructeur
   • self pour référencer l'instance
   • Méthodes d'instance prennent self en premier

2. 🏷️ ATTRIBUTS :
   • Attributs d'instance : spécifiques à chaque objet
   • Attributs de classe : partagés par toutes les instances
   • Accès via self.attribut ou Classe.attribut
   • Modification dynamique possible

3. 🔒 ENCAPSULATION :
   • Public : nom_attribut (accessible partout)
   • Protégé : _nom_attribut (usage interne)
   • Privé : __nom_attribut (name mangling)
   • Conventions, pas de vraie protection

4. 🏠 PROPRIÉTÉS :
   • @property pour créer des getters
   • @nom.setter pour créer des setters
   • Validation et calculs automatiques
   • Propriétés en lecture seule possibles

5. 🔍 MÉTHODES SPÉCIALES :
   • __str__ pour représentation utilisateur
   • __repr__ pour représentation développeur
   • __add__, __sub__, __mul__ pour opérateurs
   • __eq__, __lt__, __le__ pour comparaisons
   • __len__, __getitem__, __iter__ pour intégration Python

💡 BONNES PRATIQUES :
✅ Validation dans les constructeurs et setters
✅ Noms explicites et conventions Python
✅ Docstrings pour classes et méthodes
✅ Encapsulation appropriée selon le contexte
✅ Propriétés pour calculs et validation
✅ Méthodes spéciales pour intégration naturelle

🚨 À ÉVITER :
❌ Attributs publics sans validation
❌ Méthodes trop longues et complexes
❌ Violation des conventions de nommage
❌ Accès direct aux attributs privés
❌ Constructeurs sans validation
❌ Classes trop générales ou trop spécifiques

⚡ CONCEPTS AVANCÉS :
• @classmethod pour méthodes de classe
• @staticmethod pour méthodes utilitaires
• Introspection avec dir(), hasattr(), getattr()
• Métaclasses pour création dynamique
• Descripteurs pour contrôle avancé
• __slots__ pour optimisation mémoire

🔧 OUTILS UTILES :
• dataclasses pour classes simples
• abc pour classes abstraites
• typing pour annotations de type
• property pour encapsulation élégante
• __dict__ pour inspection d'attributs

🎯 DESIGN PATTERNS :
• Factory pour création d'objets
• Singleton pour instance unique
• Observer pour notifications
• Strategy pour algorithmes interchangeables
• Decorator pour enrichissement de fonctionnalités

🎉 Félicitations ! Création de classes maîtrisée !
💡 Prochaine étape : Héritage et polymorphisme !
📚 Classes créées, héritez maintenant !
""")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE - DÉFINITION DES CLASSES MAÎTRISÉE !")
print("=" * 70)
