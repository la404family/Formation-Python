#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
======================================================================
CLASSES ET OBJETS - INTRODUCTION À LA POO
======================================================================

🎯 Ce fichier couvre les bases de la Programmation Orientée Objet :
   • Concepts fondamentaux de la POO
   • Création de classes et d'objets
   • Attributs et méthodes
   • Méthode __init__ (constructeur)

📚 Concepts abordés :
   • Définition de classes
   • Instanciation d'objets
   • Attributs d'instance et de classe
   • Méthodes d'instance

💡 Objectif : Comprendre et créer vos premières classes
"""

print("=" * 70)
print("CLASSES ET OBJETS - INTRODUCTION À LA POO")
print("=" * 70)

print("\n" + "=" * 50)
print("1. QU'EST-CE QUE LA POO ?")
print("=" * 50)

print("\n🎯 PROGRAMMATION ORIENTÉE OBJET")
print("-" * 32)

print("""
La Programmation Orientée Objet (POO) est un paradigme de programmation
basé sur le concept d'objets qui contiennent des données (attributs)
et du code (méthodes).

🏗️ CONCEPTS FONDAMENTAUX :
   📦 CLASSE : Modèle/Plan pour créer des objets
   🎯 OBJET : Instance d'une classe
   📊 ATTRIBUTS : Données stockées dans l'objet
   🔧 MÉTHODES : Fonctions qui agissent sur l'objet

💡 ANALOGIE :
   Classe = Plan d'une maison
   Objet = Maison construite selon ce plan
""")

print("\n" + "=" * 50)
print("2. CRÉER VOTRE PREMIÈRE CLASSE")
print("=" * 50)

print("\n🏗️ DÉFINITION D'UNE CLASSE SIMPLE")
print("-" * 32)


class Personne:
    """Ma première classe représentant une personne"""
    pass  # Classe vide pour l'instant


print("💡 Exemple 1 : Classe vide")
print("class Personne:")
print("    pass")

# Création d'un objet (instance)
personne1 = Personne()
print(f"✅ Objet créé : {personne1}")
print(f"📊 Type de l'objet : {type(personne1)}")

# Plusieurs instances
personne2 = Personne()
personne3 = Personne()

print(f"🔍 Personne1 : {id(personne1)}")
print(f"🔍 Personne2 : {id(personne2)}")
print(f"🔍 Personne3 : {id(personne3)}")
print("   ➡️ Chaque objet a son propre emplacement mémoire")

print("\n" + "=" * 50)
print("3. AJOUTER DES ATTRIBUTS")
print("=" * 50)

print("\n📊 ATTRIBUTS D'INSTANCE")
print("-" * 20)


class PersonneAvecAttributs:
    """Classe avec attributs définis manuellement"""
    pass


print("💡 Exemple 2 : Ajout manuel d'attributs")

# Création et ajout d'attributs
alice = PersonneAvecAttributs()
alice.nom = "Alice"
alice.age = 25
alice.ville = "Paris"

bob = PersonneAvecAttributs()
bob.nom = "Bob"
bob.age = 30
bob.ville = "Lyon"

print(f"👤 {alice.nom}, {alice.age} ans, habite à {alice.ville}")
print(f"👤 {bob.nom}, {bob.age} ans, habite à {bob.ville}")

# Modification d'attributs
alice.age = 26
print(f"🎂 Alice a eu un anniversaire : {alice.age} ans")

print("\n🔍 INSPECTION DES ATTRIBUTS")
print("-" * 25)

print(f"📋 Attributs d'Alice : {alice.__dict__}")
print(f"📋 Attributs de Bob : {bob.__dict__}")

print("\n" + "=" * 50)
print("4. LE CONSTRUCTEUR __init__")
print("=" * 50)

print("\n🏗️ INITIALISATION AUTOMATIQUE")
print("-" * 29)


class PersonneComplete:
    """Classe avec constructeur pour initialiser les attributs"""

    def __init__(self, nom, age, ville="Non spécifiée"):
        """Constructeur de la classe Personne"""
        self.nom = nom
        self.age = age
        self.ville = ville
        print(f"   🎉 Nouvelle personne créée : {nom}")


print("💡 Exemple 3 : Classe avec constructeur")
print("""
class PersonneComplete:
    def __init__(self, nom, age, ville="Non spécifiée"):
        self.nom = nom
        self.age = age
        self.ville = ville
""")

# Création avec le constructeur
charlie = PersonneComplete("Charlie", 28, "Marseille")
diana = PersonneComplete("Diana", 32)  # ville par défaut

print(f"👤 {charlie.nom}, {charlie.age} ans, habite à {charlie.ville}")
print(f"👤 {diana.nom}, {diana.age} ans, habite à {diana.ville}")

print("\n🎯 PARAMÈTRE 'SELF'")
print("-" * 18)

print("""
🔍 Le paramètre 'self' :
   • Référence à l'instance courante
   • Premier paramètre de toute méthode
   • Permet d'accéder aux attributs de l'objet
   • Pas besoin de le passer lors de l'appel
""")

print("\n" + "=" * 50)
print("5. MÉTHODES D'INSTANCE")
print("=" * 50)

print("\n🔧 AJOUTER DES MÉTHODES")
print("-" * 21)


class PersonneAvecMethodes:
    """Classe avec méthodes d'instance"""

    def __init__(self, nom, age, ville="Non spécifiée"):
        self.nom = nom
        self.age = age
        self.ville = ville

    def se_presenter(self):
        """Méthode pour se présenter"""
        return f"Bonjour, je suis {self.nom}, j'ai {self.age} ans et j'habite à {self.ville}"

    def avoir_anniversaire(self):
        """Méthode pour vieillir d'un an"""
        self.age += 1
        return f"🎂 {self.nom} a maintenant {self.age} ans !"

    def demenager(self, nouvelle_ville):
        """Méthode pour changer de ville"""
        ancienne_ville = self.ville
        self.ville = nouvelle_ville
        return f"📦 {self.nom} a déménagé de {ancienne_ville} à {nouvelle_ville}"

    def est_majeur(self):
        """Méthode pour vérifier la majorité"""
        return self.age >= 18


print("💡 Exemple 4 : Classe avec méthodes")

eve = PersonneAvecMethodes("Eve", 17, "Toulouse")
frank = PersonneAvecMethodes("Frank", 22, "Nice")

# Utilisation des méthodes
print("🗣️", eve.se_presenter())
print("🗣️", frank.se_presenter())

# Méthodes qui modifient l'état
print("🎯", eve.avoir_anniversaire())
print("🏠", frank.demenager("Bordeaux"))

# Méthodes qui retournent des informations
print(f"👤 Eve majeure ? {eve.est_majeur()}")
print(f"👤 Frank majeur ? {frank.est_majeur()}")

print("\n" + "=" * 50)
print("6. ATTRIBUTS DE CLASSE VS D'INSTANCE")
print("=" * 50)

print("\n📊 DIFFÉRENCE ATTRIBUTS CLASSE/INSTANCE")
print("-" * 36)


class CompteurPersonnes:
    """Classe avec attributs de classe et d'instance"""

    # Attribut de classe (partagé par toutes les instances)
    nombre_personnes = 0
    espece = "Homo sapiens"

    def __init__(self, nom, age):
        # Attributs d'instance (uniques à chaque objet)
        self.nom = nom
        self.age = age

        # Modification de l'attribut de classe
        CompteurPersonnes.nombre_personnes += 1

    def afficher_info(self):
        """Affiche les informations de la personne"""
        return f"{self.nom} ({self.age} ans) - Espèce: {self.espece}"

    @classmethod
    def get_nombre_personnes(cls):
        """Méthode de classe pour obtenir le nombre de personnes"""
        return cls.nombre_personnes


print("💡 Exemple 5 : Attributs de classe")

print(f"👥 Nombre initial de personnes : {CompteurPersonnes.nombre_personnes}")

# Création de plusieurs instances
grace = CompteurPersonnes("Grace", 29)
henri = CompteurPersonnes("Henri", 35)
isabelle = CompteurPersonnes("Isabelle", 27)

print(f"👥 Nombre après création : {CompteurPersonnes.nombre_personnes}")
print(f"👥 Nombre via méthode : {CompteurPersonnes.get_nombre_personnes()}")

# Accès aux attributs
print("📊", grace.afficher_info())
print("📊", henri.afficher_info())

# Modification d'attribut de classe
CompteurPersonnes.espece = "Humain moderne"
print("📊", isabelle.afficher_info())

print("\n🔍 INSPECTION DES ATTRIBUTS")
print("-" * 25)

print(f"📋 Attributs de Grace : {grace.__dict__}")
print(f"📋 Attributs de classe : {CompteurPersonnes.__dict__}")

print("\n" + "=" * 50)
print("7. MÉTHODES SPÉCIALES")
print("=" * 50)

print("\n🔮 MÉTHODES MAGIQUES")
print("-" * 18)


class PersonneComplete2:
    """Classe avec méthodes spéciales"""

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def __str__(self):
        """Représentation lisible de l'objet"""
        return f"{self.nom} ({self.age} ans)"

    def __repr__(self):
        """Représentation technique de l'objet"""
        return f"PersonneComplete2('{self.nom}', {self.age})"

    def __len__(self):
        """Longueur = âge de la personne"""
        return self.age

    def __eq__(self, other):
        """Égalité basée sur nom et âge"""
        if isinstance(other, PersonneComplete2):
            return self.nom == other.nom and self.age == other.age
        return False


print("💡 Exemple 6 : Méthodes spéciales")

jules = PersonneComplete2("Jules", 24)
julie = PersonneComplete2("Julie", 24)
jules2 = PersonneComplete2("Jules", 24)

# Utilisation des méthodes spéciales
print(f"📝 str(jules) : {str(jules)}")
print(f"🔧 repr(jules) : {repr(jules)}")
print(f"📏 len(jules) : {len(jules)}")

# Comparaisons
print(f"⚖️ jules == julie : {jules == julie}")
print(f"⚖️ jules == jules2 : {jules == jules2}")

print("\n" + "=" * 50)
print("8. EXEMPLE PRATIQUE COMPLET")
print("=" * 50)

print("\n💼 CLASSE COMPTE BANCAIRE")
print("-" * 23)


class CompteBancaire:
    """Classe représentant un compte bancaire"""

    # Attribut de classe
    taux_interet = 0.02

    def __init__(self, titulaire, solde_initial=0):
        """Initialise un nouveau compte"""
        self.titulaire = titulaire
        self.solde = solde_initial
        self.historique = []
        self._ajouter_historique(f"Ouverture du compte avec {solde_initial}€")

    def deposer(self, montant):
        """Dépose de l'argent sur le compte"""
        if montant > 0:
            self.solde += montant
            self._ajouter_historique(f"Dépôt de {montant}€")
            return f"✅ Dépôt de {montant}€ effectué"
        return "❌ Montant invalide"

    def retirer(self, montant):
        """Retire de l'argent du compte"""
        if montant > 0 and montant <= self.solde:
            self.solde -= montant
            self._ajouter_historique(f"Retrait de {montant}€")
            return f"✅ Retrait de {montant}€ effectué"
        return "❌ Montant invalide ou solde insuffisant"

    def calculer_interets(self):
        """Calcule et ajoute les intérêts"""
        interets = self.solde * self.taux_interet
        self.solde += interets
        self._ajouter_historique(f"Intérêts de {interets:.2f}€ ajoutés")
        return f"💰 Intérêts de {interets:.2f}€ ajoutés"

    def _ajouter_historique(self, operation):
        """Méthode privée pour ajouter à l'historique"""
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.historique.append(f"{timestamp}: {operation}")

    def afficher_solde(self):
        """Affiche le solde actuel"""
        return f"💳 Solde de {self.titulaire}: {self.solde:.2f}€"

    def afficher_historique(self):
        """Affiche l'historique des opérations"""
        print(f"\n📊 Historique du compte de {self.titulaire}:")
        for operation in self.historique[-5:]:  # 5 dernières opérations
            print(f"   {operation}")

    def __str__(self):
        return f"Compte de {self.titulaire}: {self.solde:.2f}€"

    def __repr__(self):
        return f"CompteBancaire('{self.titulaire}', {self.solde})"


print("💡 Exemple 7 : Classe complète")

# Création de comptes
compte_alice = CompteBancaire("Alice Dupont", 1000)
compte_bob = CompteBancaire("Bob Martin", 500)

print("🏦", compte_alice.afficher_solde())
print("🏦", compte_bob.afficher_solde())

# Opérations sur les comptes
print("💰", compte_alice.deposer(250))
print("💸", compte_alice.retirer(100))
print("🏦", compte_alice.afficher_solde())

print("💰", compte_bob.deposer(300))
print("💸", compte_bob.retirer(1000))  # Tentative de retrait excessif
print("🏦", compte_bob.afficher_solde())

# Calcul d'intérêts
print("📈", compte_alice.calculer_interets())
print("📈", compte_bob.calculer_interets())

# Historique
compte_alice.afficher_historique()

print("\n" + "=" * 50)
print("9. RÉSUMÉ FINAL")
print("=" * 50)

print("""
🎯 POINTS CLÉS À RETENIR :

1. 🏗️ CLASSES ET OBJETS :
   • class MonNom: pour définir une classe
   • objet = MonNom() pour créer une instance
   • Chaque objet a ses propres attributs

2. 🔧 CONSTRUCTEUR __init__ :
   • Méthode appelée à la création de l'objet
   • self représente l'instance courante
   • Initialise les attributs de l'objet

3. 📊 ATTRIBUTS :
   • Instance : uniques à chaque objet
   • Classe : partagés par toutes les instances
   • Accès avec objet.attribut

4. 🎯 MÉTHODES :
   • Fonctions définies dans la classe
   • Premier paramètre toujours 'self'
   • Agissent sur les données de l'objet

5. 🔮 MÉTHODES SPÉCIALES :
   • __str__ : représentation lisible
   • __repr__ : représentation technique
   • __eq__ : comparaison d'égalité

💡 FORMULE MAGIQUE :
   Classe = Plan, Objet = Réalisation du plan

🎉 Félicitations ! Vous savez créer des classes et objets !
💡 Prochaine étape : Héritage et polymorphisme !
📚 POO maîtrisée, explorez l'héritage !
""")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE - CLASSES ET OBJETS MAÎTRISÉS !")
print("=" * 70)
