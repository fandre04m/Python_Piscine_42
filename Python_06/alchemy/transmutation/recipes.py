import alchemy
from elements import create_fire


def lead_to_gold() -> str:
    return (
        f"Recipe transmuting Lead to Gold: brew '{alchemy.create_air()}' and"
        f"'{alchemy.strength_potion()}' mixed with '{create_fire()}'"
    )
