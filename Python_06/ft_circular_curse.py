#!/usr/bin/env python3
import alchemy.grimoire as grim


def ft_circular_curse() -> None:
    print("\n=== Circular Curse Breaking ===\n")
    print("Testing ingredient validation:")
    print(
        f"validate_ingredients(\"fire air\"): "
        f"{grim.validate_ingredients('fire air')}"
    )
    print(
        f"validate_ingredients(\"dragon scales\"): "
        f"{grim.validate_ingredients('dragon scales')}"
    )
    print("\nTesting spell recording with validation:")
    print(
        "record_spell(\"Fireball\", \"fire air\"): "
        f"{grim.record_spell('Fireball', 'fire air')}"
    )
    print(
        "record_spell(\"Dark Magic\", \"shadow\"): "
        f"{grim.record_spell('Dark Magic', 'shadow')}"
    )
    print("\nTesting late import technique:")
    print(
        "record_spell(\"Lightning\", \"air\"): "
        f"{grim.record_spell('Lightning', 'air')}"
    )
    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    ft_circular_curse()
