#!/usr/bin/env python3
from alchemy.grimoire.validator import validate_ingredients
from alchemy.grimoire.spellbook import record_spell


def ft_circular_curse() -> None:
    print("\n=== Circular Curse Breaking ===\n")
    print("Testing ingredient validation:")
    print(
        f"validate_ingredients(\"fire air\"): "
        f"{validate_ingredients('fire air')}"
    )
    print(
        f"validate_ingredients(\"dragon scales\"): "
        f"{validate_ingredients('dragon scales')}"
    )
    print("\nTesting spell recording with validation:")
    print(
        "record_spell(\"Fireball\", \"fire air\"): "
        f"{record_spell("Fireball", "fire air")}"
    )
    print(
        "record_spell(\"Dark Magic\", \"shadow\"): "
        f"{record_spell("Dark Magic", "shadow")}"
    )


if __name__ == "__main__":
    ft_circular_curse()
