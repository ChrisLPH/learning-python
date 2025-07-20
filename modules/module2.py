# modules/module2.py
"""
Module 2 : Mon premier jeu - Le pendu
Structure et contenu pédagogique pour créer un jeu complet
"""

LESSONS = {
    1: {
        "title": "Planification du jeu",
        "description": "Concevoir la structure et la logique du pendu",
        "concepts": ["planification", "décomposition", "algorithme", "structure de données"],
        "explanation": """
Salut la dev ! 🎮 Aujourd'hui on attaque le vrai codage avec un projet concret : le JEU DU PENDU !

🎯 **Le but du jeu** :
- L'ordinateur choisit un mot secret
- Le joueur devine lettre par lettre
- S'il se trompe trop, c'est perdu !
- S'il trouve le mot, c'est gagné !

🧠 **Comment on va s'y prendre** :
1. **Choisir un mot** au hasard dans une liste
2. **Afficher des tirets** pour les lettres cachées
3. **Demander une lettre** au joueur
4. **Vérifier** si elle est dans le mot
5. **Mettre à jour** l'affichage ou compter les erreurs
6. **Répéter** jusqu'à victoire ou défaite

💡 **Les outils qu'on va utiliser** :
- `import random` pour choisir un mot
- Listes pour stocker les mots et les lettres trouvées
- Boucles `while` pour le jeu principal
- Conditions `if/else` pour les vérifications
- Fonctions pour organiser le code

C'est parti pour devenir une vraie game dev ! 🚀
        """,
        "challenge": "Réfléchis et écris sur papier (ou dans un commentaire) les étapes principales du jeu du pendu. Qu'est-ce qui se passe à chaque tour ?",
        "hints": [
            "Pense à ce qui se passe au début du jeu, pendant chaque tour, et à la fin",
            "Quelles informations faut-il garder en mémoire ? (mot secret, lettres trouvées, erreurs...)",
            "À quel moment le jeu s'arrête ? (victoire ou défaite)"
        ],
        "solution_pattern": ["planification", "étapes du jeu", "variables nécessaires"],
        "next_concepts": ["listes et mots"]
    },

    2: {
        "title": "Choisir un mot et l'afficher",
        "description": "Gérer le mot secret et son affichage",
        "concepts": ["import random", "listes", "choice()", "join()", "in operator"],
        "explanation": """
On commence par le commencement : choisir un mot secret ! 🎲

🎯 **Import random** - Notre générateur de hasard :
```python
import random

mots = ["python", "ordinateur", "programmation", "jeu"]
mot_secret = random.choice(mots)
print(f"Le mot choisi est : {mot_secret}")  # Pour tester !
```

🎭 **Afficher le mot masqué** :
```python
mot_secret = "python"
mot_affiche = []

for lettre in mot_secret:
    mot_affiche.append("_")

print(" ".join(mot_affiche))  # Affiche : _ _ _ _ _ _
```

🔍 **Vérifier une lettre** :
```python
lettre_joueur = "p"
if lettre_joueur in mot_secret:
    print("Bravo ! Cette lettre est dans le mot !")
else:
    print("Raté ! Cette lettre n'y est pas...")
```

💡 **Astuce de pro** : `" ".join(liste)` colle les éléments d'une liste avec des espaces !
        """,
        "challenge": "Crée un programme qui choisit un mot au hasard et l'affiche sous forme de tirets !",
        "hints": [
            "Commence par importer random et créer une liste de mots",
            "Utilise random.choice() pour choisir un mot",
            "Crée une liste avec autant de '_' que le mot a de lettres",
            "Affiche avec ' '.join() pour avoir des espaces entre les tirets"
        ],
        "solution_pattern": ["import random", "liste de mots", "choice()", "liste tirets", "join()"],
        "next_concepts": ["boucle principale"]
    },

    3: {
        "title": "Boucle de jeu principale",
        "description": "Créer la logique de répétition du jeu",
        "concepts": ["while", "input()", "conditions", "compteurs", "fin de jeu"],
        "explanation": """
Maintenant on fait tourner le jeu ! 🔄

🎮 **La boucle infinie... mais pas trop** :
```python
erreurs = 0
max_erreurs = 6  # Comme un vrai pendu !
jeu_termine = False

while not jeu_termine:
    print(f"Mot : {' '.join(mot_affiche)}")
    print(f"Erreurs : {erreurs}/{max_erreurs}")

    lettre = input("Tape une lettre : ").lower()

    # Ici on vérifiera la lettre...

    # Conditions de fin
    if erreurs >= max_erreurs:
        print("Perdu ! 😭")
        jeu_termine = True
    elif "_" not in mot_affiche:
        print("Gagné ! 🎉")
        jeu_termine = True
```

🎯 **Vérifier et mettre à jour** :
```python
if lettre in mot_secret:
    # Révéler toutes les occurrences de cette lettre
    for i in range(len(mot_secret)):
        if mot_secret[i] == lettre:
            mot_affiche[i] = lettre
else:
    erreurs += 1
```

💡 **Astuce** : `"_" not in mot_affiche` vérifie s'il reste des lettres à trouver !
        """,
        "challenge": "Crée la boucle principale qui demande des lettres et compte les erreurs !",
        "hints": [
            "Utilise while avec une condition qui vérifie si le jeu continue",
            "Demande une lettre avec input() et convertis en minuscule avec .lower()",
            "Si la lettre est bonne, révèle-la dans mot_affiche aux bonnes positions",
            "Sinon, incrémente le compteur d'erreurs"
        ],
        "solution_pattern": ["while loop", "input lettre", "vérification in", "mise à jour positions"],
        "next_concepts": ["fonctions organisation"]
    },

    4: {
        "title": "Organiser avec des fonctions",
        "description": "Structurer le code avec des fonctions",
        "concepts": ["def", "return", "paramètres", "organisation du code"],
        "explanation": """
Un bon code, c'est un code bien rangé ! 🏗️

🎪 **Fonction pour choisir un mot** :
```python
def choisir_mot():
    mots = ["python", "ordinateur", "jeu", "programmation", "fonction"]
    return random.choice(mots)

mot_secret = choisir_mot()
```

🎭 **Fonction pour initialiser l'affichage** :
```python
def creer_affichage(mot):
    return ["_" for _ in mot]  # List comprehension de boss !

mot_affiche = creer_affichage(mot_secret)
```

🔍 **Fonction pour vérifier une lettre** :
```python
def verifier_lettre(lettre, mot_secret, mot_affiche):
    trouve = False
    for i in range(len(mot_secret)):
        if mot_secret[i] == lettre:
            mot_affiche[i] = lettre
            trouve = True
    return trouve

if verifier_lettre(lettre, mot_secret, mot_affiche):
    print("Bien joué !")
else:
    erreurs += 1
```

🎯 **Fonction principale** :
```python
def jouer_pendu():
    # Tout le jeu ici !
    pass

# Lancer le jeu
jouer_pendu()
```
        """,
        "challenge": "Transforme ton code en fonctions organisées : choisir_mot(), creer_affichage(), verifier_lettre() et jouer_pendu() !",
        "hints": [
            "Chaque fonction doit faire UNE chose précise",
            "verifier_lettre() doit modifier mot_affiche ET retourner True/False",
            "jouer_pendu() contient la boucle principale et appelle les autres fonctions",
            "Teste chaque fonction séparément avant de tout assembler"
        ],
        "solution_pattern": ["def choisir_mot", "def creer_affichage", "def verifier_lettre", "def jouer_pendu"],
        "next_concepts": ["améliorations"]
    },

    5: {
        "title": "Améliorations et finitions",
        "description": "Rendre le jeu plus robuste et plus fun",
        "concepts": ["gestion d'erreurs", "validation", "expérience utilisateur", "détails"],
        "explanation": """
Maintenant on peaufine pour un jeu de qualité ! ✨

🛡️ **Gestion des erreurs utilisateur** :
```python
def demander_lettre():
    while True:
        lettre = input("Tape UNE lettre : ").lower().strip()

        if len(lettre) != 1:
            print("Une seule lettre à la fois !")
        elif not lettre.isalpha():
            print("Seulement des lettres !")
        else:
            return lettre

lettre = demander_lettre()  # Garantit une lettre valide
```

🎯 **Éviter les répétitions** :
```python
lettres_essayees = []

def verifier_lettre_deja_essayee(lettre, lettres_essayees):
    if lettre in lettres_essayees:
        print(f"Tu as déjà essayé '{lettre}' !")
        return True
    lettres_essayees.append(lettre)
    return False
```

🎨 **Affichage du pendu** :
```python
def afficher_pendu(erreurs):
    dessins = [
        "  +---+",
        "  |   |",
        "      |",
        "      |",
        "      |",
        "      |",
        "======="
    ]
    # Ajouter des parties du corps selon les erreurs
    if erreurs >= 1:
        dessins[2] = "  O   |"  # Tête
    if erreurs >= 2:
        dessins[3] = "  |   |"  # Corps
    # etc...

    for ligne in dessins:
        print(ligne)
```

🎉 **Messages de fin sympas** :
```python
def message_fin(gagne, mot_secret):
    if gagne:
        print(f"🎉 BRAVO ! Tu as trouvé '{mot_secret}' !")
        print("Tu es un·e champion·ne des mots ! 🏆")
    else:
        print(f"😭 Perdu ! Le mot était '{mot_secret}'")
        print("Retente ta chance, tu vas y arriver ! 💪")
```
        """,
        "challenge": "Ajoute au moins 2 améliorations à ton jeu : gestion des erreurs de saisie ET éviter les lettres répétées !",
        "hints": [
            "Pour valider la saisie : vérifie len(lettre) == 1 et lettre.isalpha()",
            "Garde une liste des lettres déjà essayées et vérifie avant d'ajouter",
            "Utilise while True: avec break pour redemander jusqu'à avoir une entrée valide",
            "BONUS : ajoute un dessin du pendu ou des messages fun !"
        ],
        "solution_pattern": ["validation input", "liste lettres essayées", "messages améliorer"],
        "next_concepts": ["projet final"]
    },

    6: {
        "title": "Projet final : Pendu complet",
        "description": "Assembler tout en un jeu parfait",
        "concepts": ["intégration", "test", "debug", "finition"],
        "explanation": """
C'est l'heure du boss final ! 🏆 On assemble tout pour un jeu de pendu parfait !

🎯 **Cahier des charges final** :
✅ Choisit un mot au hasard
✅ Affiche le mot avec des tirets
✅ Demande des lettres une par une
✅ Révèle les lettres trouvées
✅ Compte les erreurs (max 6)
✅ Gère les erreurs de saisie
✅ Évite les lettres répétées
✅ Affiche un message de fin

🎮 **Structure recommandée** :
```python
import random

def choisir_mot():
    # Liste de mots + random.choice()

def creer_affichage(mot):
    # Retourne ["_", "_", ...]

def demander_lettre(lettres_essayees):
    # Validation + vérification répétition

def verifier_lettre(lettre, mot_secret, mot_affiche):
    # Révèle la lettre, retourne True/False

def afficher_pendu(erreurs):
    # Dessin du pendu (optionnel mais stylé !)

def jouer_pendu():
    # Boucle principale du jeu

def rejouer():
    # Demande si on veut rejouer

# Programme principal
if __name__ == "__main__":
    print("🎮 Bienvenue au JEU DU PENDU ! 🎮")
    rejouer = True
    while rejouer:
        jouer_pendu()
        rejouer = input("Rejouer ? (o/n) : ").lower() == "o"
    print("Merci d'avoir joué ! 👋")
```

💡 **Tips de finition** :
- Teste tous les cas : victoire, défaite, lettres répétées, mauvaises saisies
- Ajoute des emojis et des couleurs dans les messages
- Fais plusieurs parties pour vérifier que tout marche
- Montre ton jeu à quelqu'un et observe ce qui peut être amélioré !

TU VAS ÊTRE FIÈRE DE TON JEU ! 🌟
        """,
        "challenge": """Crée ton jeu du pendu complet avec TOUTES les fonctionnalités :

OBLIGATOIRE :
✅ Mot choisi au hasard
✅ Affichage avec tirets
✅ Boucle de jeu avec compteur d'erreurs
✅ Validation des saisies
✅ Gestion des lettres répétées
✅ Messages de fin

BONUS pour les champion·ne·s :
🎨 Dessin du pendu qui s'affiche
🎮 Possibilité de rejouer
🌈 Messages colorés et fun
📈 Score/statistiques""",
        "hints": [
            "Commence par assembler tes fonctions existantes",
            "Teste chaque partie séparément avant de tout connecter",
            "Si ça bug, utilise des print() pour voir ce qui se passe",
            "N'hésite pas à demander de l'aide pour débugger !",
            "BONUS : regarde comment utiliser les couleurs avec colorama ou des emojis fun"
        ],
        "solution_pattern": ["jeu complet", "toutes fonctions", "gestion erreurs", "expérience utilisateur"],
        "next_concepts": ["bonus extensions"]
    }
}

def get_lesson_content(lesson_number):
    """Retourne le contenu d'une leçon spécifique du module 2"""
    return LESSONS.get(lesson_number, {})

def get_hint_for_lesson(lesson_number, hint_level):
    """Retourne l'indice approprié selon le niveau (1, 2, ou 3) pour le module 2"""
    lesson = LESSONS.get(lesson_number, {})
    hints = lesson.get("hints", [])

    if hint_level <= len(hints):
        return hints[hint_level - 1]

    return "Tu es sur la bonne voie ! Le pendu, c'est comme un puzzle : une pièce à la fois ! 🧩"

def is_exercise_complete(code, lesson_number):
    """Vérifie si l'exercice du module 2 est probablement terminé"""
    lesson = LESSONS.get(lesson_number, {})
    patterns = lesson.get("solution_pattern", [])

    code_lower = code.lower()

    pattern_checks = {
        "import random": "import random" in code_lower or "from random import" in code_lower,
        "liste de mots": any(word in code_lower for word in ["mots", "words", "liste"]),
        "choice()": "choice" in code_lower,
        "while loop": "while" in code_lower,
        "input lettre": "input" in code_lower,
        "def choisir_mot": "def choisir_mot" in code_lower or "def choisir" in code_lower,
        "def jouer_pendu": "def jouer" in code_lower or "def pendu" in code_lower,
        "validation input": "len(" in code_lower or "isalpha" in code_lower,
        "jeu complet": all(x in code_lower for x in ["def", "while", "input", "random"])
    }

    # Vérification basique selon les patterns attendus
    for pattern in patterns:
        if pattern in pattern_checks and not pattern_checks[pattern]:
            return False

    return True

# Défis spéciaux pour le module 2
SPECIAL_CHALLENGES = {
    "pendu_facile": "Crée une version simplifiée : just 3 lettres maximum, un seul mot prédéfini",
    "pendu_theme": "Fais un pendu à thème : tous les mots sur les animaux, ou sur la nourriture !",
    "pendu_duo": "Crée une version à 2 joueurs : l'un choisit le mot, l'autre devine !",
    "pendu_graphique": "BONUS EXPERT : utilise Turtle pour dessiner le pendu graphiquement !"
}

def get_special_challenge(challenge_type):
    """Retourne un défi spécial pour le module 2"""
    return SPECIAL_CHALLENGES.get(challenge_type, "Défi mystère à venir ! 🎮")
