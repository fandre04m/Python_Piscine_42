from .spellbook import record_spell
__all__ = ["record_spell"]


def validate_ingredients(ingredients: str) -> str:
    valid_ingredients = ["fire", "water", "earth", "air"]
    words = ingredients.split()
    if any(word in valid_ingredients for word in words):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
