from .dark_spellbook import dark_spell_allowed_ingredients
from typing import List


def validate_ingredients(ingredients: str) -> str:
    valid_ingr: List[str] = dark_spell_allowed_ingredients()
    ingr_list: List[str] = ingredients.lower().split(", ")
    ret = ""
    if not ingr_list:
        ret = ""
    elif len(ingr_list) == 1:
        ret = ingr_list[0]
    else:
        ret = ", ".join(ingr_list[:-1]) + " and " + ingr_list[-1]
    if any(ingr in valid_ingr for ingr in ingr_list):
        return f"{ret} - VALID"
    return f"{ret} - INVALID"
