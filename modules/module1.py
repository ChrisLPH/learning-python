# modules/module1.py
"""
Module 1 : Les bases de Python
Structure et contenu pédagogique
"""

LESSONS = {
    1: {
        "title": "Print et Variables",
        "description": "Apprendre à afficher du texte et stocker des informations",
        "concepts": ["print()", "variables", "strings", "numbers"],
        "explanation": """
Salut ! 😊 Aujourd'hui on apprend à parler à l'ordinateur !

🖨️ **print()** - C'est ta baguette magique pour afficher des trucs :
```python
print("Salut les humains !")
print(42)
```

📦 **Les variables** - C'est comme des boîtes où tu stockes tes trucs :
```python
nom = "Emma"
age = 13
print("Je m'appelle", nom, "et j'ai", age, "ans")
```

💡 **Astuce de pro** : les guillemets c'est pour le texte, pas besoin pour les nombres !
        """,
        "challenge": "Crée un programme qui affiche ton nom, ton âge et ton animal préféré !",
        "hints": [
            "Commence par créer des variables : nom = \"ton_nom\"",
            "Utilise print() pour afficher. Tu peux mettre plusieurs trucs séparés par des virgules",
            "N'oublie pas les guillemets pour le texte ! print(nom) affiche la valeur, print(\"nom\") affiche le mot 'nom'"
        ],
        "solution_pattern": ["variables", "print avec plusieurs éléments"],
        "next_concepts": ["input()"]
    },

    2: {
        "title": "Input et Interaction",
        "description": "Récupérer ce que tape l'utilisateur",
        "concepts": ["input()", "interaction", "variables dynamiques"],
        "explanation": """
Maintenant on va rendre nos programmes interactifs ! 🎮

🎤 **input()** - Pour récupérer ce que tape l'utilisateur :
```python
nom = input("Comment tu t'appelles ? ")
print("Salut", nom, "!")
```

⚡ **Combo puissant** - Variables + input + print :
```python
couleur = input("Quelle est ta couleur préférée ? ")
print("Cool ! J'adore le", couleur, "aussi !")
```

🤓 **Truc de ninja** : input() retourne toujours du texte, même si tu tapes un nombre !
        """,
        "challenge": "Fais un programme qui demande le nom et l'âge, puis dit un truc sympa !",
        "hints": [
            "Utilise input() pour récupérer le nom et l'âge",
            "Stocke les réponses dans des variables",
            "Affiche un message personnalisé avec les infos récupérées"
        ],
        "solution_pattern": ["deux input()", "variables", "print personnalisé"],
        "next_concepts": ["conditions"]
    },

    3: {
        "title": "Conditions (if/else)",
        "description": "Faire des choix dans le code",
        "concepts": ["if", "else", "elif", "comparaisons", "logique"],
        "explanation": """
C'est l'heure de donner un cerveau à tes programmes ! 🧠

🤔 **if** - Si quelque chose est vrai, fais ça :
```python
age = 16
if age >= 18:
    print("Tu peux voter !")
else:
    print("Encore un peu de patience...")
```

🎯 **Les comparaisons** :
- `==` égal (attention : pas juste `=` !)
- `>=` plus grand ou égal
- `<` plus petit
- `!=` différent

🔥 **elif** pour plus de choix :
```python
note = 15
if note >= 16:
    print("Excellent !")
elif note >= 12:
    print("Bien !")
else:
    print("Tu peux mieux faire !")
```
        """,
        "challenge": "Code un programme qui demande l'âge et dit si la personne peut conduire (18 ans) !",
        "hints": [
            "Demande l'âge avec input(), mais attention : ça donne du texte !",
            "Convertis en nombre avec int() : age = int(input(...))",
            "Utilise if age >= 18: puis else:"
        ],
        "solution_pattern": ["input avec int()", "if/else", "comparaison"],
        "next_concepts": ["boucles"]
    },

    4: {
        "title": "Boucles (for/while)",
        "description": "Répéter des actions automatiquement",
        "concepts": ["for", "while", "range()", "répétition"],
        "explanation": """
Les boucles, c'est le super pouvoir pour éviter de se répéter ! 🔄

🔢 **for avec range()** - Pour répéter un nombre précis de fois :
```python
for i in range(5):
    print("Tour numéro", i)
# Affiche de 0 à 4
```

📝 **for avec du texte** - Pour parcourir chaque lettre :
```python
nom = "Python"
for lettre in nom:
    print(lettre)
```

🔄 **while** - Tant que c'est vrai, continue :
```python
compteur = 0
while compteur < 3:
    print("Encore", compteur)
    compteur = compteur + 1
```

⚠️ **Attention** : avec while, n'oublie pas de modifier la variable sinon ça boucle à l'infini !
        """,
        "challenge": "Fais un compte à rebours de 10 à 1 puis affiche 'Décollage !' 🚀",
        "hints": [
            "Utilise for i in range(10, 0, -1): pour compter à l'envers",
            "Ou range(10) et calcule 10-i pour inverser",
            "N'oublie pas le 'Décollage !' après la boucle"
        ],
        "solution_pattern": ["for range", "compte à rebours", "print final"],
        "next_concepts": ["fonctions"]
    },

    5: {
        "title": "Fonctions simples",
        "description": "Créer ses propres outils réutilisables",
        "concepts": ["def", "paramètres", "return", "réutilisabilité"],
        "explanation": """
Les fonctions, c'est comme créer tes propres sorts magiques ! ✨

🎪 **Fonction simple** :
```python
def dire_bonjour():
    print("Salut tout le monde !")

dire_bonjour()  # Appelle la fonction
```

🎯 **Avec paramètres** - Pour personnaliser :
```python
def saluer(nom):
    print("Coucou", nom, "!")

saluer("Emma")
saluer("Python")
```

💎 **Avec return** - Pour renvoyer un résultat :
```python
def doubler(nombre):
    return nombre * 2

resultat = doubler(5)
print(resultat)  # Affiche 10
```

🤹 **Plusieurs paramètres** :
```python
def additionner(a, b):
    return a + b

somme = additionner(3, 7)
```
        """,
        "challenge": "Crée une fonction qui prend un nom et un âge, et retourne un message de présentation !",
        "hints": [
            "def presentation(nom, age): pour définir la fonction",
            "Utilise return pour renvoyer le message au lieu de print",
            "Teste ta fonction en l'appelant avec différents noms et âges"
        ],
        "solution_pattern": ["def avec paramètres", "return string", "appel fonction"],
        "next_concepts": ["projet final"]
    },

    6: {
        "title": "Projet : Mini-calculatrice",
        "description": "Mettre tout ensemble dans un vrai projet",
        "concepts": ["projet complet", "intégration", "interface utilisateur"],
        "explanation": """
C'est l'heure du boss final ! 🏆 On va créer une vraie calculatrice !

🎯 **Ce qu'elle doit faire** :
- Demander deux nombres
- Demander l'opération (+, -, *, /)
- Afficher le résultat
- Gérer les erreurs (division par zéro)

🛠️ **Les outils dont tu as besoin** :
- `input()` pour récupérer les données
- `int()` ou `float()` pour convertir en nombres
- `if/elif/else` pour choisir l'opération
- `def` pour organiser ton code
- `print()` pour afficher le résultat

💡 **Structure suggérée** :
1. Fonction pour demander les nombres
2. Fonction pour chaque opération
3. Menu principal avec les choix
4. Gestion des erreurs

C'est parti ! Tu vas voir, c'est super satisfaisant de créer un vrai programme ! 🚀
        """,
        "challenge": """Crée ta mini-calculatrice complète ! Elle doit :
1. Demander deux nombres à l'utilisateur
2. Demander quelle opération faire (+, -, *, /)
3. Calculer et afficher le résultat
4. Gérer le cas où on divise par zéro

BONUS : Fais une boucle pour pouvoir faire plusieurs calculs !""",
        "hints": [
            "Commence simple : juste demander 2 nombres et les additionner",
            "Ajoute ensuite le choix de l'opération avec if/elif",
            "Pour la division par zéro : if denominateur == 0:",
            "BONUS : while True: avec un choix 'quitter' pour sortir"
        ],
        "solution_pattern": ["input nombres", "choix opération", "calculs", "gestion erreurs"],
        "next_concepts": ["module 2"]
    }
}

def get_lesson_content(lesson_number):
    """Retourne le contenu d'une leçon spécifique"""
    return LESSONS.get(lesson_number, {})

def get_hint_for_lesson(lesson_number, hint_level):
    """Retourne l'indice approprié selon le niveau (1, 2, ou 3)"""
    lesson = LESSONS.get(lesson_number, {})
    hints = lesson.get("hints", [])

    if hint_level <= len(hints):
        return hints[hint_level - 1]

    return "Tu es sur la bonne voie ! Essaie encore un peu, ou demande de l'aide à nouveau."

def is_exercise_complete(code, lesson_number):
    """Vérifie si l'exercice est probablement terminé (analyse basique)"""
    lesson = LESSONS.get(lesson_number, {})
    patterns = lesson.get("solution_pattern", [])

    # Analyse très basique - peut être améliorée
    code_lower = code.lower()

    pattern_checks = {
        "variables": any(op in code_lower for op in ["=", "nom", "age"]),
        "print": "print" in code_lower,
        "input": "input" in code_lower,
        "if": "if" in code_lower,
        "for": "for" in code_lower,
        "def": "def" in code_lower,
        "return": "return" in code_lower
    }

    # Vérification basique
    for pattern in patterns:
        if pattern in pattern_checks and not pattern_checks[pattern]:
            return False

    return True
