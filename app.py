import streamlit as st
import anthropic
import json
import os
from datetime import datetime
from pathlib import Path

# Configuration
st.set_page_config(
    page_title="Coach Python 🐍",
    page_icon="🎮",
    layout="wide"
)

# Initialisation du client Anthropic
@st.cache_resource
# def init_anthropic():
#     # Charger depuis .env en local
#     from dotenv import load_dotenv
#     load_dotenv()

#     api_key = os.getenv("ANTHROPIC_API_KEY")
#     if not api_key:
#         st.error("Clé API Anthropic manquante dans le fichier .env !")
#         st.stop()
#     return anthropic.Anthropic(api_key=api_key)
def init_anthropic():
    # Charger depuis .env en local
    if os.path.exists('.env'):
        from dotenv import load_dotenv
        load_dotenv()
        api_key = os.getenv("ANTHROPIC_API_KEY")
    else:
        # Charger depuis les secrets de Streamlit en production
        api_key = st.secrets.get("api_key")

    if not api_key:
        st.error("Clé API Anthropic manquante !")
        st.stop()

    return anthropic.Anthropic(api_key=api_key)

client = init_anthropic()

# Import des modules
try:
    from modules import MODULES, get_lesson_content, get_hint_for_lesson
except ImportError:
    st.error("Modules pédagogiques non trouvés ! Vérifiez le dossier modules/")
    st.stop()

# Gestion de la progression
PROGRESS_FILE = "progress.json"

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        "current_module": 1,
        "current_lesson": 1,
        "completed_exercises": [],
        "hints_used": {},
        "last_session": None
    }

def save_progress(progress_data):
    progress_data["last_session"] = datetime.now().isoformat()
    with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
        json.dump(progress_data, f, indent=2, ensure_ascii=False)

# Système de prompt pour Claude
def get_coach_prompt(context):
    return f"""Tu es Coach Python, un assistant pédagogique Marg', 13 ans, à apprendre Python.

TON STYLE :
- Parle comme un pote sympa et décontracté
- Utilise des emojis mais pas trop
- Sois encourageant et positif
- Ne donne JAMAIS directement les réponses, mais guide avec des indices
- Explique avec des analogies simples et fun

RÈGLES IMPORTANTES :
- Ne corrige pas son code directement
- Donne des indices progressifs (3 niveaux max)
- Si elle galère, encourage et reformule différemment
- Célèbre ses réussites !
- Quand elle doit aller faire ses tests dans visual studio code ou le terminal, pense à lui dire.
- Si elle demande de l'aide, donne un indice ou reformule la question
- Si elle a fini un exercice, demande-lui si elle veut passer au suivant ou revoir
- Si elle a fini le module, félicite-la et propose de continuer ou de faire un projet
- Si elle demande un défi, propose un exercice adapté à son niveau

CONTEXTE ACTUEL :
{context}

Réponds en français, reste dans ton rôle de coach sympa !"""

# Interface principale
def main():
    # Chargement de la progression
    if 'progress' not in st.session_state:
        st.session_state.progress = load_progress()

    # Header avec style
    st.markdown("""
    <div style='text-align: center; padding: 20px; background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); border-radius: 10px; margin-bottom: 30px;'>
        <h1 style='color: white; margin: 0;'>🐍 Coach Python 🎮</h1>
        <p style='color: white; margin: 10px 0 0 0;'>Ton assistant pour apprendre Python en s'amusant !</p>
    </div>
    """, unsafe_allow_html=True)

    # Sidebar avec progression et contrôles
    with st.sidebar:
        st.markdown("### 📊 Ta progression")

        progress = st.session_state.progress
        module = progress["current_module"]
        lesson = progress["current_lesson"]

        st.markdown(f"**Module actuel :** {module}")
        st.markdown(f"**Leçon :** {lesson}")

        # Sélecteur de module
        st.markdown("---")
        st.markdown("### 🎯 Modules disponibles")

        # Module 1
        module1_status = "✅" if module > 1 or (module == 1 and lesson > 6) else "🔥" if module == 1 else "🔒"
        st.markdown(f"{module1_status} **Module 1** - Les bases")
        if module >= 1:
            display_module_lessons(1, progress)

        # Module 2
        if module >= 2 or (module == 1 and lesson > 6):
            module2_status = "🔥" if module == 2 else "✅" if module > 2 else "🔒"
            st.markdown(f"{module2_status} **Module 2** - Jeu du pendu")
            if module >= 2:
                display_module_lessons(2, progress)
        else:
            st.markdown("🔒 **Module 2** - Jeu du pendu (verrouillé)")

        st.markdown("---")

        # Boutons d'action
        st.markdown("### 🛠️ Actions")

        if st.button("🎯 Demander un défi"):
            challenge = get_challenge(st.session_state.progress)
            st.session_state.messages.append({"role": "assistant", "content": challenge})
            st.rerun()

        if st.button("💡 J'ai besoin d'aide"):
            hint = get_hint(st.session_state.progress)
            st.session_state.messages.append({"role": "assistant", "content": hint})
            st.rerun()

        if st.button("✅ J'ai fini l'exercice"):
            completion_msg = handle_exercise_completion(st.session_state.progress)
            st.session_state.messages.append({"role": "assistant", "content": completion_msg})
            save_progress(st.session_state.progress)
            st.rerun()

        st.markdown("---")
        st.markdown("### 🏆 Exercices terminés")
        for ex in progress["completed_exercises"]:
            st.markdown(f"✅ {ex}")

    # Zone de chat principale - une seule colonne
    st.markdown("### 💬 Discute avec ton Coach")

    # Initialize chat history
    if 'messages' not in st.session_state:
        st.session_state.messages = []
        # Message d'accueil
        welcome_msg = get_welcome_message(st.session_state.progress)
        st.session_state.messages.append({"role": "assistant", "content": welcome_msg})

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("Écris ton message ici..."):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Get coach response with spinner
        with st.spinner("Coach réfléchit... 🤔"):
            context = build_context(st.session_state.progress, prompt)
            response = get_coach_response(context, prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

def display_module_lessons(module_number, progress):
    """Affiche les leçons d'un module donné"""
    module_data = MODULES.get(module_number)
    if not module_data:
        return

    lessons_data = module_data["lessons"]
    current_module = progress["current_module"]
    current_lesson = progress["current_lesson"]

    for lesson_num, lesson_data in lessons_data.items():
        lesson_title = lesson_data["title"]

        # Déterminer le statut de la leçon
        if module_number < current_module:
            status = "✅"
        elif module_number == current_module:
            if lesson_num < current_lesson:
                status = "✅"
            elif lesson_num == current_lesson:
                status = "🔥"
            else:
                status = "🔒"
        else:
            status = "🔒"

        # Affichage
        if status == "🔥":
            st.markdown(f"　{status} **{lesson_num}. {lesson_title}** ← Tu es ici !")
        else:
            st.markdown(f"　{status} {lesson_num}. {lesson_title}")

def get_welcome_message(progress):
    module = progress["current_module"]
    lesson = progress["current_lesson"]

    if progress["last_session"]:
        if module == 1:
            return f"""Salut ! 😊 Content de te revoir !

Tu es dans le Module {module}, leçon {lesson}. On continue là où on s'était arrêté !

Tu peux me dire ce que tu as envie de faire :
- Continuer la leçon en cours
- Me poser une question sur Python
- Demander un nouveau défi
- Ou juste discuter !

Alors, on fait quoi ? 🚀"""
        else:
            return f"""Re-salut la dev ! 👋

Tu attaques le Module {module} - le jeu du pendu ! C'est là que ça devient vraiment fun ! 🎮

On va créer un vrai jeu ensemble, étape par étape. Tu es prête à devenir une game developer ?

Dis-moi comment tu te sens ou demande un défi pour commencer ! 🔥"""
    else:
        return """Coucou ! 👋 Bienvenue dans l'aventure Python !

Je suis ton Coach Python, et je suis là pour t'aider à apprendre en t'amusant. On va créer des trucs cool ensemble, sans prise de tête !

On commence par le Module 1 avec les bases : comment parler à l'ordinateur avec `print()` et récupérer ce que tu tapes avec `input()`.

Tu es prête à commencer ? Dis-moi juste "go" et on y va ! 🚀"""

def build_context(progress, user_message):
    module = progress["current_module"]
    lesson = progress["current_lesson"]

    return f"""
MODULE: {module}
LEÇON: {lesson}
EXERCICES TERMINÉS: {progress['completed_exercises']}
MESSAGE UTILISATEUR: {user_message}

MODULE INFO: {"Module 1 - Les bases de Python" if module == 1 else "Module 2 - Création du jeu du pendu"}
"""

def get_coach_response(context, user_message):
    try:
        response = client.messages.create(
            model="claude-3-7-sonnet-latest",
            max_tokens=1000,
            messages=[
                {"role": "user", "content": get_coach_prompt(context) + f"\n\nUtilisateur: {user_message}"}
            ]
        )
        return response.content[0].text
    except Exception as e:
        return f"Oups ! J'ai eu un petit bug... 🤖 Peux-tu réessayer ? (Erreur: {str(e)})"

def get_challenge(progress):
    module = progress["current_module"]
    lesson = progress["current_lesson"]

    # Module 1 challenges
    if module == 1:
        challenges = {
            1: "Crée un programme qui affiche ton nom et ton âge avec `print()` ! Fais-le joli avec des emojis 😊",
            2: "Fais un programme qui demande le nom de l'utilisateur et lui dit bonjour personnalisé !",
            3: "Code un petit programme qui demande l'âge et dit si la personne est majeure ou mineure.",
            4: "Fais un compteur qui affiche les nombres de 1 à 10 avec une boucle `for` !",
            5: "Crée une fonction qui prend un nom en paramètre et retourne un message de bienvenue.",
            6: "C'est parti pour la mini-calculatrice ! Elle doit faire +, -, *, / avec deux nombres."
        }
    # Module 2 challenges
    elif module == 2:
        challenges = {
            1: "Réfléchis et écris les étapes principales du jeu du pendu. Qu'est-ce qui se passe à chaque tour ?",
            2: "Crée un programme qui choisit un mot au hasard et l'affiche sous forme de tirets !",
            3: "Crée la boucle principale qui demande des lettres et compte les erreurs !",
            4: "Transforme ton code en fonctions organisées : choisir_mot(), verifier_lettre(), jouer_pendu() !",
            5: "Ajoute au moins 2 améliorations : gestion des erreurs de saisie ET éviter les lettres répétées !",
            6: "Crée ton jeu du pendu complet avec TOUTES les fonctionnalités ! C'est le boss final ! 🏆"
        }
    else:
        challenges = {1: "Nouveau module bientôt disponible ! 🚀"}

    challenge_text = challenges.get(lesson, 'Nouveau défi bientôt disponible !')
    return f"🎯 **Défi Module {module} - Leçon {lesson}** :\n\n{challenge_text}"

def get_hint(progress):
    module = progress["current_module"]
    lesson = progress["current_lesson"]

    # Pour l'instant, système simple - à améliorer avec les vrais indices des modules
    try:
        hint = get_hint_for_lesson(module, lesson, 1)  # Premier niveau d'indice
        return f"💡 **Indice pour Module {module}, Leçon {lesson}** :\n\n{hint}"
    except:
        return "💡 Voici un petit indice... Continue comme ça, tu es sur la bonne voie ! 💪"

def handle_exercise_completion(progress):
    current_module = progress["current_module"]
    current_lesson = progress["current_lesson"]
    exercise_name = f"Module {current_module} - Leçon {current_lesson}"

    if exercise_name not in progress["completed_exercises"]:
        progress["completed_exercises"].append(exercise_name)

        # Logique de progression
        if current_module == 1 and current_lesson < 6:
            progress["current_lesson"] += 1
            return f"🎉 Bravo ! Tu as terminé la leçon {current_lesson} du Module 1 ! On passe à la leçon {current_lesson + 1} !"
        elif current_module == 1 and current_lesson == 6:
            progress["current_module"] = 2
            progress["current_lesson"] = 1
            return """🏆 FÉLICITATIONS ! Tu as terminé tout le Module 1 ! 🎉

Tu maîtrises maintenant les bases de Python ! C'est énorme ! 💪

🎮 **Prête pour le Module 2 ?** On va créer un vrai jeu : le PENDU !
Tu vas devenir une vraie game developer ! 🚀

Dis-moi quand tu es prête à commencer cette nouvelle aventure !"""
        elif current_module == 2 and current_lesson < 6:
            progress["current_lesson"] += 1
            return f"🎮 Excellent ! Étape {current_lesson} du pendu terminée ! On passe à l'étape {current_lesson + 1} !"
        elif current_module == 2 and current_lesson == 6:
            return """🏆🎮 INCROYABLE ! Tu as créé ton premier JEU COMPLET ! 🎮🏆

Tu es officiellement une VRAIE PROGRAMMEUSE ! 👩‍💻✨

Ton jeu du pendu fonctionne, c'est fou ! Tu peux être super fière de toi !
Montre-le à tes parents, tes amis... Tu as créé quelque chose d'awesome !

Prête pour de nouveaux défis ? D'autres modules arrivent bientôt ! 🚀"""

    return "Tu as déjà validé cette leçon ! Tu veux passer à la suivante ?"

if __name__ == "__main__":
    main()
