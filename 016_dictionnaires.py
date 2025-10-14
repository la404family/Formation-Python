#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
======================================================================
LES DICTIONNAIRES EN PYTHON - GUIDE COMPLET
======================================================================

🎯 Ce fichier couvre les dictionnaires en détail :
   • Création et syntaxe
   • Accès et modification des données
   • Méthodes essentielles
   • Dictionnaires imbriqués
   • Compréhensions de dictionnaires
   • Applications pratiques

📚 Concepts abordés :
   • dict() et {}
   • Clés et valeurs
   • get(), keys(), values(), items()
   • update(), pop(), popitem()
   • Dictionnaires comme bases de données
   • JSON et sérialisation

💡 Objectif : Maîtriser les structures associatives (clé → valeur)
"""

import sys
import random
import time
print("=" * 70)
print("LES DICTIONNAIRES EN PYTHON - GUIDE COMPLET")
print("=" * 70)

print("\n" + "=" * 50)
print("1. CRÉATION ET SYNTAXE")
print("=" * 50)

print("\n📝 DIFFÉRENTES FAÇONS DE CRÉER UN DICTIONNAIRE")
print("-" * 44)

# Création d'un dictionnaire vide
dict_vide1 = {}
dict_vide2 = dict()

print(f"📚 Dict vide avec {{}} : {dict_vide1}")
print(f"📚 Dict vide avec dict() : {dict_vide2}")
print(f"📚 Type : {type(dict_vide1)}")

# Création avec des paires clé-valeur
ages = {"Alice": 25, "Bob": 30, "Charlie": 28}
scores = {1: 100, 2: 85, 3: 92}
mixte = {"nom": "Python", "version": 3.9, "actif": True}

print(f"👥 Ages : {ages}")
print(f"🏆 Scores : {scores}")
print(f"🎭 Mixte : {mixte}")

print("\n🏗️ MÉTHODES DE CONSTRUCTION")
print("-" * 26)

# Avec dict() et des mots-clés
config = dict(host="localhost", port=8080, debug=True)
print(f"⚙️ Config : {config}")

# Avec dict() et une liste de tuples
coordonnees = dict([("x", 10), ("y", 20), ("z", 30)])
print(f"📍 Coordonnées : {coordonnees}")

# Avec dict() et zip()
cles = ["nom", "age", "ville"]
valeurs = ["Alice", 25, "Paris"]
personne = dict(zip(cles, valeurs))
print(f"👤 Personne : {personne}")

# Dict.fromkeys() pour initialiser avec même valeur
etudiants = dict.fromkeys(["Alice", "Bob", "Charlie"], 0)
print(f"📊 Notes initiales : {etudiants}")

print("\n🔑 TYPES DE CLÉS AUTORISÉES")
print("-" * 27)

# Clés valides : immutables et hashables
dict_exemples = {
    "string": "Chaîne comme clé",
    42: "Nombre comme clé",
    (1, 2): "Tuple comme clé",
    True: "Booléen comme clé",
    3.14: "Float comme clé"
}

print("🔑 Exemples de clés valides :")
for cle, valeur in dict_exemples.items():
    print(f"   {cle} ({type(cle).__name__}) → {valeur}")

print("\n❌ Clés invalides (décommentez pour voir l'erreur) :")
print("   # dict_invalid = {[1, 2]: 'liste'}  # TypeError!")
print("   # dict_invalid = {{1: 2}: 'dict'}   # TypeError!")

# try:
#     dict_invalid = {[1, 2]: "liste comme clé"}
# except TypeError as e:
#     print(f"   Erreur : {e}")

print("\n" + "=" * 50)
print("2. ACCÈS AUX DONNÉES")
print("=" * 50)

print("\n🎯 ACCÈS PAR CLÉ")
print("-" * 16)

informations = {
    "nom": "Marie Dupont",
    "age": 28,
    "profession": "Développeuse",
    "langages": ["Python", "JavaScript", "Java"],
    "salaire": 65000
}

print(f"👤 Informations : {informations}")

# Accès direct par clé
print(f"📛 Nom : {informations['nom']}")
print(f"🎂 Age : {informations['age']}")
print(f"💼 Profession : {informations['profession']}")

print("\n🛡️ ACCÈS SÉCURISÉ AVEC get()")
print("-" * 31)

# get() évite les erreurs KeyError
nom = informations.get("nom")
email = informations.get("email")  # Clé inexistante
telephone = informations.get(
    "telephone", "Non renseigné")  # Avec valeur par défaut

print(f"📛 Nom avec get() : {nom}")
print(f"📧 Email avec get() : {email}")
print(f"📞 Téléphone avec défaut : {telephone}")

# Comparaison : accès direct vs get()
print("\n⚖️ Comparaison accès direct vs get() :")
try:
    print(f"   Direct ['email'] : {informations['email']}")
except KeyError as e:
    print(f"   Erreur avec accès direct : {e}")

print(f"   Avec get('email') : {informations.get('email', 'Pas trouvé')}")

print("\n🔍 VÉRIFICATION D'EXISTENCE")
print("-" * 26)

# Opérateur 'in' pour vérifier les clés
print(f"❓ 'nom' dans le dict ? {'nom' in informations}")
print(f"❓ 'email' dans le dict ? {'email' in informations}")

# Vérification des valeurs (moins efficace)
print(f"❓ 28 dans les valeurs ? {28 in informations.values()}")

print("\n" + "=" * 50)
print("3. MODIFICATION DES DONNÉES")
print("=" * 50)

print("\n✏️ AJOUT ET MODIFICATION")
print("-" * 25)

# Création d'un dictionnaire de test
produit = {
    "nom": "MacBook Pro",
    "prix": 2499,
    "stock": 5
}

print(f"🛍️ Produit initial : {produit}")

# Modification d'une valeur existante
produit["prix"] = 2399
print(f"🛍️ Après baisse de prix : {produit}")

# Ajout d'une nouvelle clé-valeur
produit["categorie"] = "Informatique"
produit["promotion"] = True
print(f"🛍️ Après ajouts : {produit}")

print("\n🔄 MÉTHODE update()")
print("-" * 18)

# Update avec un autre dictionnaire
nouvelles_infos = {
    "couleur": "Gris sidéral",
    "garantie": "2 ans",
    "prix": 2299  # Écrase la valeur existante
}

produit.update(nouvelles_infos)
print(f"🛍️ Après update() : {produit}")

# Update avec des mots-clés
produit.update(vendeur="Apple", disponible=True)
print(f"🛍️ Après update avec kwargs : {produit}")

print("\n➖ SUPPRESSION D'ÉLÉMENTS")
print("-" * 25)

# del pour supprimer une clé
del produit["promotion"]
print(f"🛍️ Après del promotion : {produit}")

# pop() pour supprimer et récupérer
couleur_supprimee = produit.pop("couleur")
print(f"🛍️ Après pop couleur : {produit}")
print(f"🎨 Couleur supprimée : {couleur_supprimee}")

# pop() avec valeur par défaut
taille = produit.pop("taille", "Non spécifiée")
print(f"📏 Taille (inexistante) : {taille}")

# popitem() pour supprimer le dernier élément (Python 3.7+)
dernier_element = produit.popitem()
print(f"🛍️ Après popitem() : {produit}")
print(f"🗑️ Dernier élément suppressé : {dernier_element}")

# clear() pour vider complètement
produit_backup = produit.copy()
produit.clear()
print(f"🛍️ Après clear() : {produit}")
print(f"🛍️ Backup : {produit_backup}")

print("\n" + "=" * 50)
print("4. MÉTHODES ESSENTIELLES")
print("=" * 50)

print("\n🔑 ACCÈS AUX CLÉS, VALEURS ET ITEMS")
print("-" * 35)

# Dictionnaire de test
notes = {
    "Mathématiques": 18,
    "Physique": 16,
    "Chimie": 17,
    "Informatique": 19,
    "Anglais": 15
}

print(f"📊 Notes : {notes}")

# Méthodes keys(), values(), items()
cles = notes.keys()
valeurs = notes.values()
items = notes.items()

print(f"🔑 Clés : {list(cles)}")
print(f"📊 Valeurs : {list(valeurs)}")
print(f"🎯 Items : {list(items)}")

print("\n⚡ CES MÉTHODES RETOURNENT DES VUES")
print("-" * 36)

print("📋 Les vues se mettent à jour automatiquement :")
print(f"   Clés avant ajout : {list(cles)}")

notes["Histoire"] = 14  # Ajout d'une nouvelle matière

print(f"   Clés après ajout : {list(cles)}")
print("   → La vue des clés s'est mise à jour !")

print("\n🔄 ITÉRATION SUR DICTIONNAIRES")
print("-" * 29)

print("🎯 Différentes façons d'itérer :")

# Itération sur les clés (par défaut)
print("   Sur les clés :")
for matiere in notes:
    print(f"      {matiere}")

# Itération sur les valeurs
print("   Sur les valeurs :")
for note in notes.values():
    print(f"      {note}/20")

# Itération sur les items (clé, valeur)
print("   Sur les paires clé-valeur :")
for matiere, note in notes.items():
    print(f"      {matiere:<13} : {note:>2}/20")

print("\n📊 CALCULS ET STATISTIQUES")
print("-" * 26)

# Calculs sur les valeurs
moyenne = sum(notes.values()) / len(notes)
note_max = max(notes.values())
note_min = min(notes.values())

print(f"📈 Statistiques des notes :")
print(f"   Moyenne : {moyenne:.2f}/20")
print(f"   Maximum : {note_max}/20")
print(f"   Minimum : {note_min}/20")

# Trouver la matière avec la meilleure note
meilleure_matiere = max(notes, key=notes.get)
print(
    f"   Meilleure matière : {meilleure_matiere} ({notes[meilleure_matiere]}/20)")

# Compter les notes supérieures à la moyenne
bonnes_notes = sum(1 for note in notes.values() if note > moyenne)
print(f"   Notes > moyenne : {bonnes_notes}/{len(notes)}")

print("\n" + "=" * 50)
print("5. DICTIONNAIRES IMBRIQUÉS")
print("=" * 50)

print("\n🏗️ STRUCTURES COMPLEXES")
print("-" * 22)

# Base de données d'entreprise
entreprise = {
    "nom": "TechCorp",
    "secteur": "Informatique",
    "employes": {
        "E001": {
            "nom": "Alice Martin",
            "poste": "Développeuse Senior",
            "departement": "R&D",
            "salaire": 75000,
            "competences": ["Python", "JavaScript", "React"],
            "projets": {
                "P1": {"nom": "Site Web", "statut": "Terminé", "budget": 15000},
                "P2": {"nom": "API REST", "statut": "En cours", "budget": 25000}
            }
        },
        "E002": {
            "nom": "Bob Durand",
            "poste": "Designer UX",
            "departement": "Design",
            "salaire": 60000,
            "competences": ["Figma", "Photoshop", "HTML/CSS"],
            "projets": {
                "P1": {"nom": "Site Web", "statut": "Terminé", "budget": 15000}
            }
        }
    },
    "departements": {
        "R&D": {"budget": 500000, "chef": "Alice Martin"},
        "Design": {"budget": 200000, "chef": "Bob Durand"},
        "Marketing": {"budget": 150000, "chef": "Charlie Leblanc"}
    }
}

print(f"🏢 Entreprise : {entreprise['nom']}")
print(f"🏢 Secteur : {entreprise['secteur']}")

print("\n👥 Employés :")
for id_employe, infos in entreprise["employes"].items():
    nom = infos["nom"]
    poste = infos["poste"]
    departement = infos["departement"]
    nb_projets = len(infos["projets"])

    print(f"   {id_employe} : {nom:<15} | {poste:<20} | {departement:<10} | {nb_projets} projet(s)")

print("\n💼 Détail des projets :")
for id_employe, infos in entreprise["employes"].items():
    nom_employe = infos["nom"]
    print(f"   {nom_employe} :")

    for id_projet, projet in infos["projets"].items():
        nom_projet = projet["nom"]
        statut = projet["statut"]
        budget = projet["budget"]
        print(
            f"      {id_projet} : {nom_projet:<12} | {statut:<10} | {budget:>7}€")

print("\n🏛️ ACCÈS EN PROFONDEUR")
print("-" * 23)

# Accès direct en chaîne
alice_salaire = entreprise["employes"]["E001"]["salaire"]
print(f"💰 Salaire d'Alice : {alice_salaire}€")

# Accès sécurisé avec get()
charlie_salaire = entreprise.get("employes", {}).get(
    "E003", {}).get("salaire", "Non trouvé")
print(f"💰 Salaire de Charlie (inexistant) : {charlie_salaire}")

# Modification en profondeur
entreprise["employes"]["E001"]["salaire"] = 80000
print(
    f"💰 Nouveau salaire d'Alice : {entreprise['employes']['E001']['salaire']}€")

print("\n" + "=" * 50)
print("6. COMPRÉHENSIONS DE DICTIONNAIRES")
print("=" * 50)

print("\n✨ SYNTAXE DE BASE")
print("-" * 17)

# Dict comprehension simple
nombres = [1, 2, 3, 4, 5]
carres = {x: x**2 for x in nombres}
print(f"🔢 Nombres : {nombres}")
print(f"🔢 Carrés : {carres}")

# Avec condition
pairs_carres = {x: x**2 for x in nombres if x % 2 == 0}
print(f"🔢 Carrés des pairs : {pairs_carres}")

print("\n🔄 TRANSFORMATION DE DONNÉES")
print("-" * 28)

# Inversion clé-valeur
original = {"a": 1, "b": 2, "c": 3}
inverse = {valeur: cle for cle, valeur in original.items()}
print(f"📚 Original : {original}")
print(f"📚 Inversé : {inverse}")

# Transformation de valeurs
temperatures_celsius = {"Paris": 20, "Londres": 15, "Rome": 25, "Berlin": 18}
temperatures_fahrenheit = {
    ville: celsius * 9/5 + 32
    for ville, celsius in temperatures_celsius.items()
}

print(f"🌡️ Celsius : {temperatures_celsius}")
print(f"🌡️ Fahrenheit : {temperatures_fahrenheit}")

print("\n🎯 FILTRAGE ET GROUPEMENT")
print("-" * 27)

# Base de données de produits
produits = [
    {"nom": "Laptop", "prix": 1200, "categorie": "Informatique", "stock": 5},
    {"nom": "Souris", "prix": 25, "categorie": "Informatique", "stock": 50},
    {"nom": "Livre Python", "prix": 45, "categorie": "Livre", "stock": 20},
    {"nom": "Chaise", "prix": 150, "categorie": "Mobilier", "stock": 8},
    {"nom": "Clavier", "prix": 80, "categorie": "Informatique", "stock": 15}
]

# Dictionnaire des produits informatiques par nom
info_products = {
    produit["nom"]: produit["prix"]
    for produit in produits
    if produit["categorie"] == "Informatique"
}
print(f"💻 Produits informatiques : {info_products}")

# Groupement par tranche de prix
tranches_prix = {
    "Economique": [p for p in produits if p["prix"] < 50],
    "Moyen": [p for p in produits if 50 <= p["prix"] < 200],
    "Premium": [p for p in produits if p["prix"] >= 200]
}

print(f"\n💰 Répartition par prix :")
for tranche, liste_produits in tranches_prix.items():
    noms = [p["nom"] for p in liste_produits]
    print(f"   {tranche:<12} : {len(liste_produits)} produits - {noms}")

print("\n🔧 COMPRÉHENSIONS AVANCÉES")
print("-" * 27)

# Dictionnaire de fréquences
phrase = "python est un langage de programmation"
frequences = {lettre: phrase.count(lettre)
              for lettre in set(phrase) if lettre != ' '}
print(f"📝 Phrase : '{phrase}'")
print(f"📊 Fréquences : {dict(sorted(frequences.items()))}")

# Matrice sous forme de dictionnaire
matrice_dict = {
    (i, j): i * j
    for i in range(1, 4)
    for j in range(1, 4)
}
print(f"📊 Matrice 3x3 (tables de multiplication) :")
for (i, j), valeur in matrice_dict.items():
    print(f"   ({i},{j}) : {valeur}")

print("\n" + "=" * 50)
print("7. APPLICATIONS PRATIQUES")
print("=" * 50)

print("\n📞 CARNET D'ADRESSES")
print("-" * 19)


class CarnetAdresses:
    def __init__(self):
        self.contacts = {}

    def ajouter_contact(self, nom, **infos):
        """Ajoute un contact avec informations flexibles"""
        self.contacts[nom] = infos
        print(f"✅ Contact '{nom}' ajouté")

    def rechercher(self, terme):
        """Recherche dans noms et informations"""
        resultats = {}
        terme_lower = terme.lower()

        for nom, infos in self.contacts.items():
            # Recherche dans le nom
            if terme_lower in nom.lower():
                resultats[nom] = infos
                continue

            # Recherche dans les valeurs
            for valeur in infos.values():
                if isinstance(valeur, str) and terme_lower in valeur.lower():
                    resultats[nom] = infos
                    break

        return resultats

    def lister_par_ville(self):
        """Groupe les contacts par ville"""
        par_ville = {}

        for nom, infos in self.contacts.items():
            ville = infos.get("ville", "Non renseignée")
            if ville not in par_ville:
                par_ville[ville] = []
            par_ville[ville].append(nom)

        return par_ville

    def statistiques(self):
        """Retourne des statistiques sur le carnet"""
        total = len(self.contacts)
        avec_telephone = sum(
            1 for infos in self.contacts.values() if "telephone" in infos)
        avec_email = sum(1 for infos in self.contacts.values()
                         if "email" in infos)

        return {
            "total_contacts": total,
            "avec_telephone": avec_telephone,
            "avec_email": avec_email,
            "pourcentage_telephone": (avec_telephone / total * 100) if total > 0 else 0
        }


# Test du carnet d'adresses
carnet = CarnetAdresses()

# Ajout de contacts
carnet.ajouter_contact("Alice Martin",
                       telephone="01.23.45.67.89",
                       email="alice@email.com",
                       ville="Paris",
                       profession="Développeuse")

carnet.ajouter_contact("Bob Durand",
                       telephone="01.98.76.54.32",
                       ville="Lyon",
                       profession="Designer")

carnet.ajouter_contact("Charlie Dubois",
                       email="charlie@email.com",
                       ville="Paris",
                       profession="Manager")

# Recherches
print(f"\n🔍 Recherche 'Paris' :")
resultats_paris = carnet.rechercher("Paris")
for nom, infos in resultats_paris.items():
    print(f"   {nom} : {infos}")

print(f"\n🔍 Recherche 'email' :")
resultats_email = carnet.rechercher("email")
for nom in resultats_email.keys():
    print(f"   {nom}")

# Groupement par ville
print(f"\n🏙️ Contacts par ville :")
par_ville = carnet.lister_par_ville()
for ville, noms in par_ville.items():
    print(f"   {ville:<15} : {', '.join(noms)}")

# Statistiques
stats = carnet.statistiques()
print(f"\n📊 Statistiques :")
for cle, valeur in stats.items():
    if "pourcentage" in cle:
        print(f"   {cle:<20} : {valeur:.1f}%")
    else:
        print(f"   {cle:<20} : {valeur}")

print("\n💰 GESTIONNAIRE DE BUDGET")
print("-" * 25)


class GestionnaireBudget:
    def __init__(self):
        self.transactions = {}  # {mois: {categorie: [montants]}}
        self.budget_mensuel = {}  # {categorie: montant_limite}

    def definir_budget(self, categorie, montant):
        """Définit le budget pour une catégorie"""
        self.budget_mensuel[categorie] = montant
        print(f"💰 Budget {categorie} : {montant}€/mois")

    def ajouter_transaction(self, mois, categorie, montant, description=""):
        """Ajoute une transaction"""
        if mois not in self.transactions:
            self.transactions[mois] = {}

        if categorie not in self.transactions[mois]:
            self.transactions[mois][categorie] = []

        self.transactions[mois][categorie].append({
            'montant': montant,
            'description': description
        })

        print(f"💳 Transaction ajoutée : {montant}€ en {categorie} ({mois})")

    def depenses_par_mois(self, mois):
        """Calcule les dépenses par catégorie pour un mois"""
        if mois not in self.transactions:
            return {}

        depenses = {}
        for categorie, transactions in self.transactions[mois].items():
            total = sum(t['montant'] for t in transactions)
            depenses[categorie] = total

        return depenses

    def alerte_budget(self, mois):
        """Vérifie les dépassements de budget"""
        depenses = self.depenses_par_mois(mois)
        alertes = {}

        for categorie, depense in depenses.items():
            if categorie in self.budget_mensuel:
                budget = self.budget_mensuel[categorie]
                if depense > budget:
                    depassement = depense - budget
                    pourcentage = (depassement / budget) * 100
                    alertes[categorie] = {
                        'depense': depense,
                        'budget': budget,
                        'depassement': depassement,
                        'pourcentage': pourcentage
                    }

        return alertes

    def rapport_mensuel(self, mois):
        """Génère un rapport mensuel"""
        depenses = self.depenses_par_mois(mois)
        alertes = self.alerte_budget(mois)
        total_depenses = sum(depenses.values())
        total_budget = sum(self.budget_mensuel.values())

        return {
            'mois': mois,
            'depenses_par_categorie': depenses,
            'total_depenses': total_depenses,
            'total_budget': total_budget,
            'alertes': alertes,
            'respect_budget': total_depenses <= total_budget
        }


# Test du gestionnaire de budget
budget = GestionnaireBudget()

# Définition des budgets
budget.definir_budget("Alimentation", 400)
budget.definir_budget("Transport", 150)
budget.definir_budget("Loisirs", 200)
budget.definir_budget("Logement", 800)

# Ajout de transactions pour janvier
budget.ajouter_transaction("2024-01", "Alimentation",
                           120, "Courses hebdomadaires")
budget.ajouter_transaction("2024-01", "Alimentation", 95, "Restaurant")
budget.ajouter_transaction("2024-01", "Alimentation", 180, "Courses diverses")
budget.ajouter_transaction("2024-01", "Transport", 75, "Métro")
budget.ajouter_transaction("2024-01", "Transport", 85, "Essence")
budget.ajouter_transaction("2024-01", "Loisirs", 250, "Cinéma + sorties")
budget.ajouter_transaction("2024-01", "Logement", 800, "Loyer")

# Rapport mensuel
rapport = budget.rapport_mensuel("2024-01")

print(f"\n📊 Rapport pour {rapport['mois']} :")
print(f"   Total dépenses : {rapport['total_depenses']}€")
print(f"   Total budget   : {rapport['total_budget']}€")
print(f"   Respect budget : {'✅' if rapport['respect_budget'] else '❌'}")

print(f"\n💳 Dépenses par catégorie :")
for categorie, depense in rapport['depenses_par_categorie'].items():
    budget_cat = budget.budget_mensuel.get(categorie, 0)
    pourcentage = (depense / budget_cat * 100) if budget_cat > 0 else 0
    statut = "🟢" if depense <= budget_cat else "🔴"
    print(
        f"   {categorie:<12} : {depense:>6}€ / {budget_cat:>6}€ ({pourcentage:>5.1f}%) {statut}")

# Alertes
if rapport['alertes']:
    print(f"\n🚨 Alertes dépassement :")
    for categorie, alerte in rapport['alertes'].items():
        print(
            f"   {categorie} : dépassement de {alerte['depassement']}€ (+{alerte['pourcentage']:.1f}%)")

print("\n" + "=" * 50)
print("8. OPTIMISATIONS ET BONNES PRATIQUES")
print("=" * 50)

print("\n⚡ PERFORMANCES DES DICTIONNAIRES")
print("-" * 32)


def mesurer_performance(operation, description):
    """Mesure le temps d'exécution"""
    start = time.time()
    operation()
    duree = (time.time() - start) * 1000
    print(f"   {description:<30} : {duree:.3f}ms")


# Comparaison : recherche dans liste vs dictionnaire
taille = 100000
liste_data = list(range(taille))
dict_data = {i: f"valeur_{i}" for i in range(taille)}

cible = random.randint(0, taille-1)

print(f"🏃 Test de performance (recherche de {cible} dans {taille} éléments) :")


def recherche_liste():
    return cible in liste_data


def recherche_dict():
    return cible in dict_data


mesurer_performance(recherche_liste, "Recherche dans liste")
mesurer_performance(recherche_dict, "Recherche dans dictionnaire")

print(f"   → Les dictionnaires sont O(1), les listes O(n)")

print("\n💾 OPTIMISATION MÉMOIRE")
print("-" * 23)

# __slots__ pour optimiser la mémoire (avec classe)


class PersonneDict:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age


class PersonneSlots:
    __slots__ = ['nom', 'age']

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age


# Comparaison mémoire
p1 = PersonneDict("Alice", 25)
p2 = PersonneSlots("Bob", 30)

print(f"💾 Mémoire PersonneDict : {sys.getsizeof(p1.__dict__)} bytes")
print(f"💾 Mémoire PersonneSlots : {sys.getsizeof(p2)} bytes (pas de __dict__)")

print("\n🎯 BONNES PRATIQUES")
print("-" * 19)

bonnes_pratiques = {
    "Clés": [
        "Utilisez des types immutables (str, int, tuple)",
        "Évitez les clés trop longues ou complexes",
        "Soyez cohérent dans le naming"
    ],
    "Valeurs": [
        "Pas de restriction de type",
        "Attention aux références mutables partagées",
        "Utilisez None pour les valeurs optionnelles"
    ],
    "Performance": [
        "get() au lieu de [] pour éviter KeyError",
        "setdefault() pour initialiser si absent",
        "Dict comprehension pour créer efficacement"
    ],
    "Lisibilité": [
        "Noms de clés explicites",
        "Structure cohérente pour dicts similaires",
        "Évitez l'imbrication trop profonde"
    ]
}

print("💡 Guide des bonnes pratiques :")
for categorie, conseils in bonnes_pratiques.items():
    print(f"\n   📋 {categorie} :")
    for conseil in conseils:
        print(f"      • {conseil}")

print("\n🚨 PIÈGES COURANTS")
print("-" * 17)

print("⚠️ Attention aux références mutables :")

# Piège : valeur par défaut mutable


def mauvais_exemple():
    # Ne jamais faire ça !
    def ajouter_item(item, liste_dict={}):  # Piège !
        if 'items' not in liste_dict:
            liste_dict['items'] = []
        liste_dict['items'].append(item)
        return liste_dict

    # Problème : même dict réutilisé !
    resultat1 = ajouter_item("pomme")
    resultat2 = ajouter_item("banane")
    print(f"❌ Résultat1 : {resultat1}")
    print(f"❌ Résultat2 : {resultat2}")  # Contient aussi "pomme" !


def bon_exemple():
    def ajouter_item(item, liste_dict=None):
        if liste_dict is None:
            liste_dict = {}
        if 'items' not in liste_dict:
            liste_dict['items'] = []
        liste_dict['items'].append(item)
        return liste_dict

    resultat1 = ajouter_item("pomme")
    resultat2 = ajouter_item("banane")
    print(f"✅ Résultat1 : {resultat1}")
    print(f"✅ Résultat2 : {resultat2}")


print("Exemple du piège :")
mauvais_exemple()
print("\nCorrection :")
bon_exemple()

print("\n" + "=" * 50)
print("9. EXERCICES PRATIQUES")
print("=" * 50)

print("""
💪 EXERCICES À FAIRE (décommentez pour tester) :

# Exercice 1 : Analyseur de texte
# def analyser_texte(texte):
#     \"\"\"Analyse un texte et retourne des statistiques\"\"\"
#     mots = texte.lower().split()
#     
#     # Fréquence des mots
#     freq_mots = {}
#     for mot in mots:
#         # Nettoyer la ponctuation
#         mot_propre = ''.join(c for c in mot if c.isalnum())
#         if mot_propre:
#             freq_mots[mot_propre] = freq_mots.get(mot_propre, 0) + 1
#     
#     # Fréquence des lettres
#     freq_lettres = {}
#     for char in texte.lower():
#         if char.isalpha():
#             freq_lettres[char] = freq_lettres.get(char, 0) + 1
#     
#     # Statistiques
#     total_mots = len(mots)
#     mots_uniques = len(freq_mots)
#     mot_plus_frequent = max(freq_mots, key=freq_mots.get) if freq_mots else ""
#     
#     return {
#         'total_mots': total_mots,
#         'mots_uniques': mots_uniques,
#         'mot_plus_frequent': mot_plus_frequent,
#         'freq_mots': freq_mots,
#         'freq_lettres': freq_lettres
#     }
# 
# # Test
# texte_test = "Python est un langage de programmation. Python est facile à apprendre."
# analyse = analyser_texte(texte_test)
# 
# print(f"Texte : {texte_test}")
# print(f"Total mots : {analyse['total_mots']}")
# print(f"Mots uniques : {analyse['mots_uniques']}")
# print(f"Mot le plus fréquent : {analyse['mot_plus_frequent']}")

# Exercice 2 : Gestionnaire d'inventaire
# class Inventaire:
#     def __init__(self):
#         self.produits = {}  # {code: {nom, prix, stock, categorie}}
#     
#     def ajouter_produit(self, code, nom, prix, stock, categorie):
#         self.produits[code] = {
#             'nom': nom,
#             'prix': prix,
#             'stock': stock,
#             'categorie': categorie
#         }
#     
#     def vendre(self, code, quantite):
#         if code in self.produits:
#             if self.produits[code]['stock'] >= quantite:
#                 self.produits[code]['stock'] -= quantite
#                 return self.produits[code]['prix'] * quantite
#             else:
#                 return None  # Stock insuffisant
#         return None  # Produit inexistant
#     
#     def stock_faible(self, seuil=5):
#         return {
#             code: infos for code, infos in self.produits.items()
#             if infos['stock'] <= seuil
#         }
#     
#     def valeur_inventaire(self):
#         return sum(
#             infos['prix'] * infos['stock']
#             for infos in self.produits.values()
#         )
#     
#     def rapport_par_categorie(self):
#         categories = {}
#         for infos in self.produits.values():
#             cat = infos['categorie']
#             if cat not in categories:
#                 categories[cat] = {'produits': 0, 'valeur': 0}
#             categories[cat]['produits'] += 1
#             categories[cat]['valeur'] += infos['prix'] * infos['stock']
#         return categories
# 
# # Test
# inv = Inventaire()
# inv.ajouter_produit("LAP001", "MacBook Pro", 2500, 3, "Informatique")
# inv.ajouter_produit("SOU001", "Souris Logitech", 45, 25, "Informatique")
# inv.ajouter_produit("LIV001", "Python Guide", 35, 50, "Livre")
# inv.ajouter_produit("CHA001", "Chaise Bureau", 200, 2, "Mobilier")
# 
# print(f"Valeur totale : {inv.valeur_inventaire()}€")
# print(f"Stock faible : {inv.stock_faible()}")

# Exercice 3 : Cache LRU (Least Recently Used)
# class CacheLRU:
#     def __init__(self, capacite):
#         self.capacite = capacite
#         self.cache = {}
#         self.ordre_acces = []  # Plus récent à la fin
#     
#     def get(self, cle):
#         if cle in self.cache:
#             # Mettre à jour l'ordre d'accès
#             self.ordre_acces.remove(cle)
#             self.ordre_acces.append(cle)
#             return self.cache[cle]
#         return None
#     
#     def put(self, cle, valeur):
#         if cle in self.cache:
#             # Mise à jour
#             self.cache[cle] = valeur
#             self.ordre_acces.remove(cle)
#             self.ordre_acces.append(cle)
#         else:
#             # Nouvelle entrée
#             if len(self.cache) >= self.capacite:
#                 # Supprimer le moins récemment utilisé
#                 cle_ancienne = self.ordre_acces.pop(0)
#                 del self.cache[cle_ancienne]
#             
#             self.cache[cle] = valeur
#             self.ordre_acces.append(cle)
#     
#     def info(self):
#         return {
#             'taille': len(self.cache),
#             'capacite': self.capacite,
#             'contenu': self.cache.copy(),
#             'ordre': self.ordre_acces.copy()
#         }
# 
# # Test
# cache = CacheLRU(3)
# cache.put("a", 1)
# cache.put("b", 2)
# cache.put("c", 3)
# print("Après ajout a,b,c :", cache.info())
# 
# cache.get("a")  # "a" devient le plus récent
# cache.put("d", 4)  # "b" doit être supprimé
# print("Après get(a) et put(d,4) :", cache.info())

# Exercice 4 : Graphe avec dictionnaire
# class Graphe:
#     def __init__(self):
#         self.adjacence = {}
#     
#     def ajouter_sommet(self, sommet):
#         if sommet not in self.adjacence:
#             self.adjacence[sommet] = []
#     
#     def ajouter_arete(self, sommet1, sommet2, bidirectionnel=True):
#         self.ajouter_sommet(sommet1)
#         self.ajouter_sommet(sommet2)
#         
#         if sommet2 not in self.adjacence[sommet1]:
#             self.adjacence[sommet1].append(sommet2)
#         
#         if bidirectionnel and sommet1 not in self.adjacence[sommet2]:
#             self.adjacence[sommet2].append(sommet1)
#     
#     def voisins(self, sommet):
#         return self.adjacence.get(sommet, [])
#     
#     def degre(self, sommet):
#         return len(self.voisins(sommet))
#     
#     def chemin_existe(self, debut, fin, visites=None):
#         if visites is None:
#             visites = set()
#         
#         if debut == fin:
#             return True
#         
#         if debut in visites:
#             return False
#         
#         visites.add(debut)
#         
#         for voisin in self.voisins(debut):
#             if self.chemin_existe(voisin, fin, visites):
#                 return True
#         
#         return False
#     
#     def statistiques(self):
#         nb_sommets = len(self.adjacence)
#         nb_aretes = sum(len(voisins) for voisins in self.adjacence.values()) // 2
#         degre_moyen = (sum(len(v) for v in self.adjacence.values()) / nb_sommets) if nb_sommets > 0 else 0
#         
#         return {
#             'sommets': nb_sommets,
#             'aretes': nb_aretes,
#             'degre_moyen': degre_moyen
#         }
# 
# # Test - réseau social simplifié
# reseau = Graphe()
# reseau.ajouter_arete("Alice", "Bob")
# reseau.ajouter_arete("Alice", "Charlie")
# reseau.ajouter_arete("Bob", "Diana")
# reseau.ajouter_arete("Charlie", "Eve")
# 
# print("Voisins d'Alice :", reseau.voisins("Alice"))
# print("Chemin Alice → Diana :", reseau.chemin_existe("Alice", "Diana"))
# print("Statistiques :", reseau.statistiques())
""")

print("\n" + "=" * 50)
print("10. RÉSUMÉ FINAL")
print("=" * 50)

print("""
🎯 POINTS CLÉS À RETENIR :

1. 📚 CRÉATION DE DICTIONNAIRES :
   • {} ou dict() pour vides
   • {"clé": valeur} pour directs
   • dict(zip()) pour construction
   • Dict comprehensions {k: v for ...}

2. 🔑 CLÉS ET VALEURS :
   • Clés immutables et hashables
   • get() pour accès sécurisé
   • in pour vérifier l'existence
   • keys(), values(), items() pour itération

3. ✏️ MODIFICATION :
   • dict[clé] = valeur pour ajout/modif
   • update() pour fusion
   • pop() et del pour suppression
   • clear() pour vider

4. 🎯 MÉTHODES ESSENTIELLES :
   • get(clé, défaut) - accès sécurisé
   • setdefault(clé, défaut) - init si absent
   • keys(), values(), items() - vues dynamiques
   • update() - fusion de dictionnaires

5. 🏗️ STRUCTURES COMPLEXES :
   • Dictionnaires imbriqués
   • Listes de dictionnaires
   • Dictionnaires comme BDD

💡 USAGES RECOMMANDÉS :
✅ Mapping clé → valeur
✅ Configurations et paramètres
✅ Compteurs et statistiques  
✅ Cache et mémoïsation
✅ Bases de données simples
✅ Groupement de données

🚨 PIÈGES À ÉVITER :
❌ Clés mutables (listes, dicts)
❌ Valeurs par défaut mutables
❌ Accès direct sans vérification
❌ Modification pendant itération

⚡ PERFORMANCES :
• Accès O(1) en moyenne
• Recherche très rapide
• Plus lourd que listes en mémoire
• Pas d'ordre avant Python 3.7

🎉 Félicitations ! Vous maîtrisez les dictionnaires !
💡 Prochaine étape : Ensembles (sets) !
📚 Dictionnaires maîtrisés, explorez les collections !
""")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE - DICTIONNAIRES MAÎTRISÉS !")
print("=" * 70)
