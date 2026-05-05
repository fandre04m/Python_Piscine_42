#!/usr/bin/env python3
from collections.abc import Callable
from typing import Tuple


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} DMG"


def whirlwind(target: str, power: int) -> str:
    return f"Whirlwind hits {target} for {power} Break DMG"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> Tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def main() -> None:
    print()
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, whirlwind)
    spell1_res, spell2_res = combined("Dragon", 50)
    print(f"Combined spell result: {spell1_res}, {spell2_res}")


if __name__ == "__main__":
    main()
