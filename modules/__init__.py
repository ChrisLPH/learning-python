# modules/__init__.py
"""
Modules pédagogiques pour l'apprentissage Python
"""

from .module1 import LESSONS as MODULE1_LESSONS
from .module1 import get_lesson_content as get_module1_content
from .module1 import get_hint_for_lesson as get_module1_hint
from .module1 import is_exercise_complete as is_module1_complete

from .module2 import LESSONS as MODULE2_LESSONS
from .module2 import get_lesson_content as get_module2_content
from .module2 import get_hint_for_lesson as get_module2_hint
from .module2 import is_exercise_complete as is_module2_complete
from .module2 import get_special_challenge

# Mapping des modules
MODULES = {
    1: {
        "lessons": MODULE1_LESSONS,
        "get_content": get_module1_content,
        "get_hint": get_module1_hint,
        "is_complete": is_module1_complete
    },
    2: {
        "lessons": MODULE2_LESSONS,
        "get_content": get_module2_content,
        "get_hint": get_module2_hint,
        "is_complete": is_module2_complete
    }
}

def get_lesson_content(module_number, lesson_number):
    """Retourne le contenu d'une leçon selon le module"""
    module = MODULES.get(module_number)
    if module:
        return module["get_content"](lesson_number)
    return {}

def get_hint_for_lesson(module_number, lesson_number, hint_level):
    """Retourne un indice selon le module, leçon et niveau"""
    module = MODULES.get(module_number)
    if module:
        return module["get_hint"](lesson_number, hint_level)
    return "Indice non disponible pour ce module."

__all__ = ['MODULES', 'get_lesson_content', 'get_hint_for_lesson', 'get_special_challenge']
