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
def init_anthropic():
    api_key = st.secrets.get("ANTHROPIC_API_KEY", os.getenv("ANTHROPIC_API_KEY"))
    if not api_key:
        st.error("Clé API Anthropic manquante !")
        st.stop()
    return anthropic.Anthropic(api_key=api_key)

client = init_anthropic()

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
    return f"""Tu es Coach Python, un assistant pédagogique super cool qui aide une fille de 13 ans à apprendre Python.

TON STYLE :
- Parle comme un grand frère sympa et décontracté
- Utilise des emojis mais pas trop
- Sois encourageant et positif
- Ne donne JAMAIS directement les réponses, mais guide avec des indices
- Explique avec des analogies simples et fun

RÈGLES IMPORTANTES :
- Ne corrige pas son code directement
- Donne des indices progressifs (3 niveaux max)
- Si elle galère, encourage et reformule différemment
- Célèbre ses réussites !

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

    # Sidebar avec progression
    with st.sidebar:
        st.markdown("### 📊 Ta progression")

        progress = st.session_state.progress
        module = progress["current_module"]
        lesson = progress["current_lesson"]

        st.markdown(f"**Module actuel :** {module}")
        st.markdown(f"**Leçon :** {lesson}")

        # Barre de progression
        total_lessons = 6  # Module 1 a 6 leçons
        progress_pct = min((lesson - 1) / total_lessons * 100, 100)
        st.progress(progress_pct / 100)
        st.markdown(f"{int(progress_pct)}% du Module 1")

        st.markdown("---")
        st.markdown("### 🎯 Exercices terminés")
        for ex in progress["completed_exercises"]:
            st.markdown(f"✅ {ex}")

    # Zone principale
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### 💬 Discute avec ton Coach")

        # Zone de chat
        if 'messages' not in st.session_state:
            st.session_state.messages = []
            # Message d'accueil
            welcome_msg = get_welcome_message(st.session_state.progress)
            st.session_state.messages.append({"role": "assistant", "content": welcome_msg})

        # Affichage des messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Input utilisateur
        if prompt := st.chat_input("Écris ton message ici..."):
            st.session_state.messages.append({"role": "user", "content": prompt})

            with st.chat_message("user"):
                st.markdown(prompt)

            # Réponse du coach
            with st.chat_message("assistant"):
                with st.spinner("Coach réfléchit..."):
                    context = build_context(st.session_state.progress, prompt)
                    response = get_coach_response(context, prompt)
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})

    with col2:
        st.markdown("### 🎯 Module 1 - Les bases")

        lessons = [
            "1. Print et variables",
            "2. Input et interaction",
            "3. Conditions (if/else)",
            "4. Boucles (for/while)",
            "5. Fonctions simples",
            "6. Projet : Mini-calculatrice"
        ]

        current_lesson = st.session_state.progress["current_lesson"]

        for i, lesson in enumerate(lessons, 1):
            if i < current_lesson:
                st.markdown(f"✅ {lesson}")
            elif i == current_lesson:
                st.markdown(f"🔥 **{lesson}** ← Tu es ici !")
            else:
                st.markdown(f"🔒 {lesson}")

        st.markdown("---")

        # Boutons d'action
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

def get_welcome_message(progress):
    if progress["last_session"]:
        return """Salut ! 😊 Content de te revoir !

On continue là où on s'était arrêté. Tu peux me dire ce que tu as envie de faire :
- Continuer la leçon en cours
- Me poser une question sur Python
- Demander un nouveau défi
- Ou juste discuter !

Alors, on fait quoi ? 🚀"""
    else:
        return """Coucou ! 👋 Bienvenue dans l'aventure Python !

Je suis ton Coach Python, et je suis là pour t'aider à apprendre en t'amusant. On va créer des trucs cool ensemble, sans prise de tête !

Pour commencer, on va voir les bases : comment parler à l'ordinateur avec `print()` et récupérer ce que tu tapes avec `input()`.

Tu es prête à commencer ? Dis-moi juste "go" et on y va ! 🚀"""

def build_context(progress, user_message):
    return f"""
MODULE: {progress['current_module']}
LEÇON: {progress['current_lesson']}
EXERCICES TERMINÉS: {progress['completed_exercises']}
MESSAGE UTILISATEUR: {user_message}
"""

def get_coach_response(context, user_message):
    try:
        response = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=1000,
            messages=[
                {"role": "user", "content": get_coach_prompt(context) + f"\n\nUtilisateur: {user_message}"}
            ]
        )
        return response.content[0].text
    except Exception as e:
        return f"Oups ! J'ai eu un petit bug... 🤖 Peux-tu réessayer ? (Erreur: {str(e)})"

def get_challenge(progress):
    lesson = progress["current_lesson"]
    challenges = {
        1: "Crée un programme qui affiche ton nom et ton âge avec `print()` ! Fais-le joli avec des emojis 😊",
        2: "Fais un programme qui demande le nom de l'utilisateur et lui dit bonjour personnalisé !",
        3: "Code un petit programme qui demande l'âge et dit si la personne est majeure ou mineure.",
        4: "Fais un compteur qui affiche les nombres de 1 à 10 avec une boucle `for` !",
        5: "Crée une fonction qui prend un nom en paramètre et retourne un message de bienvenue.",
        6: "C'est parti pour la mini-calculatrice ! Elle doit faire +, -, *, / avec deux nombres."
    }
    return f"🎯 **Défi de la leçon {lesson}** :\n\n{challenges.get(lesson, 'Nouveau défi bientôt disponible !')}"

def get_hint(progress):
    # Système d'indices progressifs à implémenter
    return "💡 Voici un petit indice... (système d'indices en cours de développement)"

def handle_exercise_completion(progress):
    current = progress["current_lesson"]
    exercise_name = f"Leçon {current}"

    if exercise_name not in progress["completed_exercises"]:
        progress["completed_exercises"].append(exercise_name)

        if current < 6:  # Module 1 a 6 leçons
            progress["current_lesson"] += 1
            return f"🎉 Bravo ! Tu as terminé la leçon {current} ! On passe à la leçon {current + 1} !"
        else:
            return "🏆 Félicitations ! Tu as terminé tout le Module 1 ! Tu es devenue une vraie pythonista ! 🐍✨"

    return "Tu as déjà validé cette leçon ! Tu veux passer à la suivante ?"

if __name__ == "__main__":
    main()
