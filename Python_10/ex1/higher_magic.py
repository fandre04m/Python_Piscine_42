#!/usr/bin/env python3
from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} DMG"


def whirlwind(target: str, power: int) -> str:
    return f"Whirlwind hits {target} for {power} Break DMG"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplify(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplify


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        spell_effects: list[str] = []
        for spell in spells:
            spell_effects.append(spell(target, power))
        return spell_effects
    return sequence


def main() -> None:
    print()
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, whirlwind)
    spell1_res, spell2_res = combined("Dragon", 50)
    print(f"Combined spell result: {spell1_res}, {spell2_res}")
    print()
    print("Testing spell multiplier...")
    base_fireball = fireball("Dark Templar", 50)
    mega_spell = power_amplifier(fireball, 3)
    print(
        f"Original: {base_fireball}\n"
        f"Implified: {mega_spell('Dark Templar', 50)}"
    )
    print()
    print("Testing conditional casting...")
    condition_spell = conditional_caster(
        lambda target, power: power >= 25 and len(target) > 1,
        whirlwind
    )
    print(
        f"Valid spell: {condition_spell('Wyvern', 25)}\n"
        f"Invalid spell: {condition_spell('Wyvern', 20)}"
    )
    print()
    print("testing spell sequence...")
    sequence_spell = spell_sequence([
        fireball,
        whirlwind,
        mega_spell,
        condition_spell
    ])
    sequence = sequence_spell("orc", 20)
    for spell in sequence:
        print(spell)
    print()


if __name__ == "__main__":
    main()
