#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
======================================================================
LES ENSEMBLES (SETS) EN PYTHON - GUIDE COMPLET
======================================================================

🎯 Ce fichier couvre les ensembles en détail :
   • Création et caractéristiques
   • Opérations mathématiques sur les ensembles
   • Méthodes de manipulation
   • Sets vs frozensets
   • Applications pratiques
   • Optimisations et performances

📚 Concepts abordés :
   • set() et {}
   • Union, intersection, différence
   • add(), remove(), discard()
   • Ensembles immutables (frozenset)
   • Déduplication et unicité
   • Théorie des ensembles en pratique

💡 Objectif : Maîtriser les collections d'éléments uniques
"""

import sys
import random
import time

print("=" * 70)
print("LES ENSEMBLES (SETS) EN PYTHON - GUIDE COMPLET")
print("=" * 70)

print("\n" + "=" * 50)
print("1. CRÉATION ET CARACTÉRISTIQUES")
print("=" * 50)

print("\n📝 DIFFÉRENTES FAÇONS DE CRÉER UN ENSEMBLE")
print("-" * 41)

# Création d'un ensemble vide
# ATTENTION : {} crée un dict, pas un set !
set_vide = set()  # Seule façon de créer un set vide
print(f"📦 Set vide : {set_vide}")
print(f"📦 Type : {type(set_vide)}")

# Création avec des éléments
couleurs = {"rouge", "vert", "bleu"}
nombres = {1, 2, 3, 4, 5}
mixte = {"Python", 3.9, True, 42}

print(f"🎨 Couleurs : {couleurs}")
print(f"🔢 Nombres : {nombres}")
print(f"🎭 Mixte : {mixte}")

print("\n🔧 CRÉATION À PARTIR D'AUTRES STRUCTURES")
print("-" * 38)

# Depuis une liste (déduplique automatiquement)
liste_avec_doublons = [1, 2, 2, 3, 3, 3, 4, 4, 5]
set_depuis_liste = set(liste_avec_doublons)
print(f"📋 Liste avec doublons : {liste_avec_doublons}")
print(f"📦 Set depuis liste : {set_depuis_liste}")

# Depuis une string
mot = "bonjour"
lettres = set(mot)
print(f"🔤 Mot : '{mot}'")
print(f"🔤 Lettres uniques : {lettres}")

# Depuis un range
set_range = set(range(5, 10))
print(f"📊 Set depuis range(5,10) : {set_range}")

print("\n⚡ CARACTÉRISTIQUES PRINCIPALES")
print("-" * 29)

print("🎯 Propriétés des sets :")
test_set = {1, 2, 3, 2, 1}  # Doublons automatiquement supprimés
print(f"   • Unicité : {1, 2, 3, 2, 1} → {test_set}")
print(f"   • Non ordonné : l'ordre peut changer entre exécutions")
print(f"   • Mutable : on peut ajouter/supprimer")
print(f"   • Éléments hashables uniquement")

# Test d'éléments hashables
print("\n🔑 Éléments autorisés dans un set :")
set_valide = {
    "string",
    42,
    3.14,
    True,
    (1, 2, 3),  # Tuple OK
    None
}
print(f"   ✅ Set valide : {set_valide}")

print("\n❌ Éléments interdits (décommentez pour voir l'erreur) :")
print("   # set_invalide = {[1, 2]}      # Liste → TypeError")
print("   # set_invalide = {{1: 2}}      # Dict → TypeError")

# try:
#     set_invalide = {[1, 2, 3]}  # Liste dans set
# except TypeError as e:
#     print(f"   Erreur : {e}")

print("\n" + "=" * 50)
print("2. OPÉRATIONS MATHÉMATIQUES")
print("=" * 50)

print("\n🔢 ENSEMBLES DE DÉMONSTRATION")
print("-" * 28)

# Ensembles pour les exemples
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
C = {1, 2, 3}

print(f"📊 Ensemble A : {A}")
print(f"📊 Ensemble B : {B}")
print(f"📊 Ensemble C : {C}")

print("\n➕ UNION (∪)")
print("-" * 12)

# Union : tous les éléments des deux ensembles
union_ab = A | B  # Opérateur |
union_ab_methode = A.union(B)  # Méthode union()

print(f"🔗 A ∪ B = {union_ab}")
print(f"🔗 A.union(B) = {union_ab_methode}")
print(f"   → Tous les éléments de A et B (sans doublons)")

# Union multiple
union_multiple = A | B | C
print(f"🔗 A ∪ B ∪ C = {union_multiple}")

print("\n∩ INTERSECTION (∩)")
print("-" * 18)

# Intersection : éléments communs
intersection_ab = A & B  # Opérateur &
intersection_ab_methode = A.intersection(B)  # Méthode intersection()

print(f"🎯 A ∩ B = {intersection_ab}")
print(f"🎯 A.intersection(B) = {intersection_ab_methode}")
print(f"   → Éléments présents dans A ET B")

# Intersection avec ensemble vide
intersection_vide = A & {10, 11, 12}
print(f"🎯 A ∩ {{10,11,12}} = {intersection_vide}")

print("\n➖ DIFFÉRENCE (-)")
print("-" * 16)

# Différence : éléments de A qui ne sont pas dans B
difference_ab = A - B  # Opérateur -
difference_ab_methode = A.difference(B)  # Méthode difference()

print(f"📊 A - B = {difference_ab}")
print(f"📊 A.difference(B) = {difference_ab_methode}")
print(f"   → Éléments de A qui ne sont PAS dans B")

# Différence inverse
difference_ba = B - A
print(f"📊 B - A = {difference_ba}")

print("\n🔄 DIFFÉRENCE SYMÉTRIQUE (△)")
print("-" * 31)

# Différence symétrique : éléments dans A ou B mais pas dans les deux
diff_sym_ab = A ^ B  # Opérateur ^
diff_sym_ab_methode = A.symmetric_difference(B)  # Méthode

print(f"🔄 A △ B = {diff_sym_ab}")
print(f"🔄 A.symmetric_difference(B) = {diff_sym_ab_methode}")
print(f"   → Éléments exclusifs à A ou B (pas communs)")

print("\n⚖️ RELATIONS ENTRE ENSEMBLES")
print("-" * 28)

# Tests de relations
print(f"🔍 Tests de relations :")
print(f"   C ⊆ A (C sous-ensemble de A) ? {C.issubset(A)} ou {C <= A}")
print(f"   A ⊇ C (A sur-ensemble de C) ? {A.issuperset(C)} ou {A >= C}")
print(f"   A ∩ {{10,11}} = ∅ (disjoints) ? {A.isdisjoint({10, 11})}")

# Sous-ensemble strict
print(f"   C ⊂ A (sous-ensemble strict) ? {C < A}")
print(f"   A = A (égalité) ? {A == A}")

print("\n" + "=" * 50)
print("3. MÉTHODES DE MANIPULATION")
print("=" * 50)

print("\n➕ AJOUT D'ÉLÉMENTS")
print("-" * 19)

# Création d'un set de test
fruits = {"pomme", "banane", "orange"}
print(f"🍎 Fruits initiaux : {fruits}")

# add() pour ajouter un élément
fruits.add("kiwi")
print(f"🍎 Après add('kiwi') : {fruits}")

# Tentative d'ajout d'un élément existant (rien ne se passe)
fruits.add("pomme")
print(f"🍎 Après add('pomme') existante : {fruits}")

# update() pour ajouter plusieurs éléments
fruits.update(["mangue", "ananas", "papaye"])
print(f"🍎 Après update() avec liste : {fruits}")

# update() avec plusieurs iterables
fruits.update({"raisin"}, ("poire", "prune"))
print(f"🍎 Après update() multiple : {fruits}")

print("\n➖ SUPPRESSION D'ÉLÉMENTS")
print("-" * 24)

legumes = {"carotte", "brocoli", "épinard", "tomate", "salade"}
print(f"🥬 Légumes initiaux : {legumes}")

# remove() - lève une erreur si élément absent
legumes.remove("brocoli")
print(f"🥬 Après remove('brocoli') : {legumes}")

# Tentative de remove sur élément inexistant
print("❌ Tentative remove() sur élément inexistant :")
try:
    legumes.remove("courgette")
except KeyError as e:
    print(f"   Erreur : {e}")

# discard() - ne lève pas d'erreur si élément absent
legumes.discard("épinard")  # Supprime si présent
legumes.discard("courgette")  # Ne fait rien si absent
print(f"🥬 Après discard() : {legumes}")

# pop() - supprime et retourne un élément arbitraire
element_supprime = legumes.pop()
print(f"🥬 Après pop() : {legumes}")
print(f"🗑️ Élément supprimé : {element_supprime}")

# clear() - vide complètement
legumes_backup = legumes.copy()
legumes.clear()
print(f"🥬 Après clear() : {legumes}")
print(f"🥬 Backup : {legumes_backup}")

print("\n🔄 OPÉRATIONS MODIFIANTES")
print("-" * 25)

# Opérations qui modifient l'ensemble original
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"📊 Set1 initial : {set1}")
print(f"📊 Set2 : {set2}")

# intersection_update() : set1 ∩= set2
set1_copy = set1.copy()
set1_copy.intersection_update(set2)
print(f"📊 Après intersection_update : {set1_copy}")

# difference_update() : set1 -= set2
set1_copy = set1.copy()
set1_copy.difference_update(set2)
print(f"📊 Après difference_update : {set1_copy}")

# symmetric_difference_update() : set1 ^= set2
set1_copy = set1.copy()
set1_copy.symmetric_difference_update(set2)
print(f"📊 Après symmetric_difference_update : {set1_copy}")

print("\n" + "=" * 50)
print("4. FROZENSET - ENSEMBLES IMMUTABLES")
print("=" * 50)

print("\n❄️ CRÉATION DE FROZENSETS")
print("-" * 24)

# Création de frozenset
frozen_couleurs = frozenset(["rouge", "vert", "bleu"])
frozen_nombres = frozenset(range(1, 6))
frozen_vide = frozenset()

print(f"❄️ Frozenset couleurs : {frozen_couleurs}")
print(f"❄️ Frozenset nombres : {frozen_nombres}")
print(f"❄️ Frozenset vide : {frozen_vide}")
print(f"❄️ Type : {type(frozen_couleurs)}")

print("\n🔒 IMMUTABILITÉ")
print("-" * 14)

print("❌ Tentatives de modification (erreurs) :")
try:
    frozen_couleurs.add("jaune")
except AttributeError as e:
    print(f"   add() : {e}")

try:
    frozen_couleurs.remove("rouge")
except AttributeError as e:
    print(f"   remove() : {e}")

print("✅ Opérations autorisées (lecture seule) :")
print(f"   Intersection : {frozen_couleurs & frozenset(['rouge', 'jaune'])}")
print(f"   Union : {frozen_couleurs | frozenset(['jaune', 'violet'])}")
print(f"   'rouge' dans frozenset ? {'rouge' in frozen_couleurs}")

print("\n🔑 FROZENSETS COMME CLÉS DE DICTIONNAIRE")
print("-" * 41)

# Frozensets peuvent être clés de dict (hashables)
regions_couleurs = {
    frozenset(['rouge', 'blanc']): "Pologne",
    frozenset(['bleu', 'blanc', 'rouge']): "France",
    frozenset(['rouge', 'jaune']): "Espagne",
    frozenset(['noir', 'rouge', 'jaune']): "Allemagne"
}

print("🏁 Drapeaux par couleurs :")
for couleurs_set, pays in regions_couleurs.items():
    couleurs_liste = sorted(list(couleurs_set))
    print(f"   {couleurs_liste} → {pays}")

# Recherche par couleurs
couleurs_recherche = frozenset(['bleu', 'blanc', 'rouge'])
pays_trouve = regions_couleurs.get(couleurs_recherche, "Pays non trouvé")
print(f"\n🔍 Pays avec {sorted(list(couleurs_recherche))} : {pays_trouve}")

print("\n" + "=" * 50)
print("5. APPLICATIONS PRATIQUES")
print("=" * 50)

print("\n🧹 DÉDUPLICATION DE DONNÉES")
print("-" * 26)

# Suppression des doublons d'une liste
donnees_sales = [
    "alice@email.com", "bob@test.com", "charlie@demo.com",
    "alice@email.com", "diana@site.com", "bob@test.com",
    "eve@mail.com", "charlie@demo.com"
]

donnees_propres = list(set(donnees_sales))
print(f"📧 Données sales ({len(donnees_sales)}) : {donnees_sales}")
print(f"📧 Données propres ({len(donnees_propres)}) : {donnees_propres}")

# Préservation de l'ordre avec dict.fromkeys() (Python 3.7+)
donnees_propres_ordre = list(dict.fromkeys(donnees_sales))
print(f"📧 Propres avec ordre : {donnees_propres_ordre}")

print("\n🏷️ GESTION DES TAGS ET ÉTIQUETTES")
print("-" * 32)


class GestionnaireTags:
    def __init__(self):
        self.articles = {}  # {id_article: set_de_tags}

    def ajouter_article(self, id_article, tags):
        """Ajoute un article avec ses tags"""
        self.articles[id_article] = set(tags)

    def ajouter_tags(self, id_article, nouveaux_tags):
        """Ajoute des tags à un article existant"""
        if id_article in self.articles:
            self.articles[id_article].update(nouveaux_tags)
        else:
            self.articles[id_article] = set(nouveaux_tags)

    def supprimer_tags(self, id_article, tags_a_supprimer):
        """Supprime des tags d'un article"""
        if id_article in self.articles:
            self.articles[id_article].difference_update(tags_a_supprimer)

    def articles_par_tag(self, tag):
        """Trouve tous les articles ayant un tag donné"""
        return [
            id_article for id_article, tags in self.articles.items()
            if tag in tags
        ]

    def tags_communs(self, id1, id2):
        """Trouve les tags communs entre deux articles"""
        if id1 in self.articles and id2 in self.articles:
            return self.articles[id1] & self.articles[id2]
        return set()

    def articles_similaires(self, id_article, seuil=2):
        """Trouve les articles ayant au moins 'seuil' tags en commun"""
        if id_article not in self.articles:
            return []

        tags_article = self.articles[id_article]
        similaires = []

        for autre_id, autres_tags in self.articles.items():
            if autre_id != id_article:
                tags_communs = len(tags_article & autres_tags)
                if tags_communs >= seuil:
                    similaires.append((autre_id, tags_communs))

        # Trier par nombre de tags communs (décroissant)
        return sorted(similaires, key=lambda x: x[1], reverse=True)


# Test du gestionnaire de tags
tags_manager = GestionnaireTags()

# Ajout d'articles
tags_manager.ajouter_article("A001", ["python", "web", "backend", "api"])
tags_manager.ajouter_article(
    "A002", ["javascript", "web", "frontend", "react"])
tags_manager.ajouter_article(
    "A003", ["python", "data", "machine-learning", "ai"])
tags_manager.ajouter_article("A004", ["python", "web", "django", "backend"])
tags_manager.ajouter_article("A005", ["javascript", "web", "vue", "frontend"])

print("📑 Articles et leurs tags :")
for id_article, tags in tags_manager.articles.items():
    print(f"   {id_article} : {sorted(list(tags))}")

# Recherches
articles_python = tags_manager.articles_par_tag("python")
print(f"\n🐍 Articles avec tag 'python' : {articles_python}")

articles_web = tags_manager.articles_par_tag("web")
print(f"🌐 Articles avec tag 'web' : {articles_web}")

# Tags communs
communs_a001_a004 = tags_manager.tags_communs("A001", "A004")
print(f"\n🔗 Tags communs A001-A004 : {sorted(list(communs_a001_a004))}")

# Articles similaires
similaires_a001 = tags_manager.articles_similaires("A001")
print(f"🎯 Articles similaires à A001 :")
for id_similaire, nb_communs in similaires_a001:
    print(f"   {id_similaire} : {nb_communs} tags communs")

print("\n🔍 ANALYSE D'ACCÈS ET PERMISSIONS")
print("-" * 33)


class GestionnairePermissions:
    def __init__(self):
        self.utilisateurs = {}  # {user: set_permissions}
        self.roles = {}  # {role: set_permissions}
        self.utilisateur_roles = {}  # {user: set_roles}

    def definir_role(self, nom_role, permissions):
        """Définit un rôle avec ses permissions"""
        self.roles[nom_role] = set(permissions)

    def assigner_role(self, utilisateur, role):
        """Assigne un rôle à un utilisateur"""
        if utilisateur not in self.utilisateur_roles:
            self.utilisateur_roles[utilisateur] = set()
        self.utilisateur_roles[utilisateur].add(role)

    def permissions_effectives(self, utilisateur):
        """Calcule toutes les permissions effectives d'un utilisateur"""
        permissions = set()

        # Permissions directes
        if utilisateur in self.utilisateurs:
            permissions.update(self.utilisateurs[utilisateur])

        # Permissions via rôles
        if utilisateur in self.utilisateur_roles:
            for role in self.utilisateur_roles[utilisateur]:
                if role in self.roles:
                    permissions.update(self.roles[role])

        return permissions

    def peut_faire(self, utilisateur, action):
        """Vérifie si un utilisateur peut effectuer une action"""
        permissions = self.permissions_effectives(utilisateur)
        return action in permissions

    def utilisateurs_avec_permission(self, permission):
        """Trouve tous les utilisateurs ayant une permission donnée"""
        utilisateurs = []
        for user in set(self.utilisateurs.keys()) | set(self.utilisateur_roles.keys()):
            if permission in self.permissions_effectives(user):
                utilisateurs.append(user)
        return utilisateurs


# Configuration du système de permissions
perm_manager = GestionnairePermissions()

# Définition des rôles
perm_manager.definir_role("admin", [
    "create_user", "delete_user", "modify_user",
    "read_all", "write_all", "delete_all"
])
perm_manager.definir_role("editor", [
    "read_all", "write_content", "modify_content"
])
perm_manager.definir_role("viewer", [
    "read_content", "read_public"
])

# Attribution des rôles
perm_manager.assigner_role("alice", "admin")
perm_manager.assigner_role("bob", "editor")
perm_manager.assigner_role("charlie", "viewer")
perm_manager.assigner_role("diana", "editor")
perm_manager.assigner_role("diana", "viewer")  # Rôles multiples

print("👥 Permissions par utilisateur :")
for user in ["alice", "bob", "charlie", "diana"]:
    permissions = perm_manager.permissions_effectives(user)
    roles = perm_manager.utilisateur_roles.get(user, set())
    print(f"   {user:<8} : rôles {sorted(list(roles))}")
    print(f"            permissions {sorted(list(permissions))}")

# Tests de permissions
print(f"\n🔒 Tests d'autorisation :")
tests = [
    ("alice", "delete_user"),
    ("bob", "write_content"),
    ("charlie", "write_content"),
    ("diana", "read_all")
]

for user, action in tests:
    autorise = perm_manager.peut_faire(user, action)
    statut = "✅" if autorise else "❌"
    print(f"   {user} peut {action} ? {statut}")

# Audit des permissions
users_admin = perm_manager.utilisateurs_avec_permission("delete_user")
print(f"\n🔍 Utilisateurs avec droit 'delete_user' : {users_admin}")

print("\n" + "=" * 50)
print("6. OPTIMISATIONS ET PERFORMANCES")
print("=" * 50)

print("\n⚡ PERFORMANCES DES OPÉRATIONS")
print("-" * 30)


def mesurer_temps(operation, description, repetitions=1):
    """Mesure le temps d'exécution"""
    start = time.time()
    for _ in range(repetitions):
        operation()
    duree = (time.time() - start) * 1000 / repetitions
    print(f"   {description:<35} : {duree:.3f}ms")


# Comparaison set vs liste pour recherche
taille = 50000
liste_data = list(range(taille))
set_data = set(range(taille))
cible = random.randint(0, taille-1)

print(
    f"🏃 Comparaison performances ({taille} éléments, recherche de {cible}) :")


def recherche_liste():
    return cible in liste_data


def recherche_set():
    return cible in set_data


mesurer_temps(recherche_liste, "Recherche dans liste", 100)
mesurer_temps(recherche_set, "Recherche dans set", 100)

print(f"   → Sets : O(1) moyen, Listes : O(n)")

print("\n💾 OPTIMISATION MÉMOIRE")
print("-" * 23)

# Comparaison mémoire set vs liste

liste_petite = list(range(100))
set_petit = set(range(100))

print(f"💾 Comparaison mémoire (100 éléments) :")
print(f"   Liste : {sys.getsizeof(liste_petite)} bytes")
print(f"   Set   : {sys.getsizeof(set_petit)} bytes")
print(f"   → Sets consomment plus de mémoire (table de hachage)")

print("\n🎯 BONNES PRATIQUES")
print("-" * 19)

print("""
💡 Guide d'optimisation :

📊 QUAND UTILISER UN SET :
✅ Besoin d'unicité des éléments
✅ Recherches fréquentes (in operator)
✅ Opérations mathématiques (∪, ∩, -)
✅ Déduplication de données
✅ Tests d'appartenance rapides

📋 QUAND UTILISER UNE LISTE :
✅ Ordre des éléments important
✅ Accès par index nécessaire
✅ Doublons autorisés/requis
✅ Optimisation mémoire critique
✅ Éléments non hashables

🔧 OPTIMISATIONS :
• Convertir liste → set pour déduplication rapide
• Utiliser frozenset pour clés de dict
• Éviter conversions répétées set ↔ list
• Préférer set.intersection() à boucles manuelles
""")

print("\n" + "=" * 50)
print("7. RÉSUMÉ FINAL")
print("=" * 50)

print("""
🎯 POINTS CLÉS À RETENIR :

1. 📦 CRÉATION D'ENSEMBLES :
   • set() pour ensemble vide (pas {})
   • {1, 2, 3} pour éléments directs
   • set(iterable) pour conversion
   • Déduplication automatique

2. 🔧 OPÉRATIONS MATHÉMATIQUES :
   • Union : A | B ou A.union(B)
   • Intersection : A & B ou A.intersection(B)
   • Différence : A - B ou A.difference(B)
   • Diff. symétrique : A ^ B

3. ✏️ MANIPULATION :
   • add(elem) pour ajouter
   • remove(elem) pour supprimer (erreur si absent)
   • discard(elem) pour supprimer (sans erreur)
   • update(iterable) pour ajout multiple

4. ❄️ FROZENSET :
   • Ensemble immutable
   • Peut être clé de dictionnaire
   • Opérations lecture seule
   • frozenset(iterable)

5. ⚖️ RELATIONS :
   • issubset() : A ⊆ B
   • issuperset() : A ⊇ B  
   • isdisjoint() : A ∩ B = ∅

💡 USAGES RECOMMANDÉS :
✅ Déduplication de données
✅ Tests d'appartenance rapides
✅ Opérations sur ensembles
✅ Gestion de tags/étiquettes
✅ Permissions et rôles
✅ Analyse de relations

🚨 CARACTÉRISTIQUES :
• Éléments uniques uniquement
• Non ordonnés (pas d'index)
• Éléments hashables seulement
• Plus gourmand en mémoire
• Recherche O(1) en moyenne

⚡ PERFORMANCES :
• Recherche très rapide (O(1))
• Opérations ensemblistes optimisées
• Plus lourd que listes en mémoire
• Pas d'accès par index

🎉 Félicitations ! Vous maîtrisez les ensembles !
💡 Prochaine étape : Compréhensions avancées !
📚 Sets maîtrisés, explorez les structures complexes !
""")

print("\n" + "=" * 70)
print("🎯 FIN DU GUIDE - ENSEMBLES MAÎTRISÉS !")
print("=" * 70)
