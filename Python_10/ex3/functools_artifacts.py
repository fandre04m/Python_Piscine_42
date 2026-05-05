#!/usr/bin/env python3
from collections.abc import Callable
from operator import add, mul
from functools import lru_cache, singledispatch
import functools
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {
        "add": add,
        "multiply": mul,
        "max": lambda a, b: max(a, b),
        "min": lambda a, b: min(a, b)
    }
    if not spells:
        return 0
    if operation not in operations.keys():
        raise ValueError("operation unknown")
    return functools.reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire_enchant = functools.partial(base_enchantment, 50, "Flaming")
    ice_enchant = functools.partial(base_enchantment, 50, "Frozen")
    light_enchant = functools.partial(base_enchantment, 50, "Sparkling")
    return dict(fire=fire_enchant, ice=ice_enchant, light=light_enchant)


@lru_cache(maxsize=128)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def spell_system(spell_type: Any) -> str:
        return "Unknown spell type"

    @spell_system.register(int)
    def damage(spell_type: int) -> str:
        return f"Dealt {spell_type} damage"

    @spell_system.register(str)
    def enchant(spell_type: str) -> str:
        return f"Aplied enchantment {spell_type}"

    @spell_system.register(list)
    def multi_cast(spell_type: list) -> str:
        results = [spell_system(spell) for spell in spell_type]
        return ", ".join(results)
    return spell_system


spells = [10, 20, 30, 40]


def main() -> None:
    print()
    print("Testing spell reducer...")
    try:
        print(
            f"Sum: {spell_reducer(spells, 'add')}\n"
            f"Product: {spell_reducer(spells, 'multiply')}\n"
            f"Max: {spell_reducer(spells, 'max')}"
        )
    except ValueError as e:
        print(f"Error: {e}")
    print()
    print("Testing partial enchanter...")

    def base_enchantment(power: str, element: str, target: str) -> str:
        return f"Hit {target} with {element} Orb for {power} DMG"
    ele_enchants = partial_enchanter(base_enchantment)
    print(
        f"Fire enchant: {ele_enchants['fire']('Orc King')}\n"
        f"Ice enchant: {ele_enchants['ice']('Orc King')}\n"
        f"Light enchant: {ele_enchants['light']('Orc King')}"
    )
    print()
    print("Testing memoized fibonacci...")
    # print(memoized_fibonacci.cache_info())
    print(
        f"Fib(0): {memoized_fibonacci(0)}\n"
        f"Fib(1): {memoized_fibonacci(1)}\n"
        f"Fib(10): {memoized_fibonacci(10)}\n"
        f"Fib(15): {memoized_fibonacci(15)}"
    )
    # print(memoized_fibonacci.cache_info())
    print()


if __name__ == "__main__":
    main()
