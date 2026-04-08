from typing import List
from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> List[str]:
    return (
        ["bats", "frogs", "arsenic", "eyeball"]
    )


def dark_spell_record(spell_name: str,  ingredients: str) -> str:
    valid_string = validate_ingredients(ingredients)
    if valid_string.endswith("VALID"):
        return f"Spell recorded: {spell_name} ({valid_string})"
    return f"Spell rejected: {spell_name} ({valid_string})"
