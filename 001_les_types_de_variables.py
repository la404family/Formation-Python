# Description: Les types de variables en Python

#Les chaines de caractères

# Avec des guillemets simples ou doubles
les_chaines_de_caracteres1 = "Bonjour"
# Avec des guillemets simples ou doubles
les_chaines_de_caracteres2 = 'Bonjour'
# Avec un "echappement" de caractère
les_chaines_de_caracteres3 = 'Bonjour je m\' appele'
# Avec trois guillemets simples ou doubles (multi-lignes)
les_chaines_de_caracteres4 = '''Bonjour
je m'appelle
Jean'''
les_chaines_de_caracteres5 = """Bonjour
je m'appelle
Jean"""
# Pour éviter l'échapement de caractère
les_chaines_de_caracteres6 = r"Bonjour je m'appelle Jean et nom du fichier est C:\nom_du_fichier.txt"
# Pour les chaines de caractères longues
les_chaines_de_caracteres7 = ("Bonjour je m'appelle Jean"
                            " et je suis un programmeur")

# Les nombres entiers et flottants (décimaux)

# Les entiers
les_entiers = 5
# Les grands nombres entiers
les_grands_entiers = 1_000_000_000
# Les flottants
les_flottants = 5.5
# Flottant meme si c'est 0
les_flottants = 5.0


# Les booléens (True ou False) 
les_booleens = True
# Tous les types de variables peuvent être évalués en booléen
bool(0) # False
bool(1) # True
bool("Bonjour") # True
bool("") # False
bool(0.0) # False

# On peut creer des types avec des fonctions
str(1) # "5"
int("1") # 5
float("1") # 5.0
bool(1) # True

# Les listes, les tuples, les dictionnaires, les ensembles et None

les_listes = [1, 2, 3]
les_tuples = (1, 2, 3)
les_dictionnaires = {"cle1": 1, "cle2": 2, "cle3": 3}
les_ensembles = {1, 2, 3}
les_none = None

 # exemples de print 
 
print(les_chaines_de_caracteres1)
print(les_chaines_de_caracteres2)
print(les_chaines_de_caracteres3)
print(les_chaines_de_caracteres4)
print(les_chaines_de_caracteres5)
print(les_chaines_de_caracteres6)
print(les_chaines_de_caracteres7)
print(les_entiers)
print(les_grands_entiers)
print(les_flottants)
print(les_booleens)
print(les_listes)