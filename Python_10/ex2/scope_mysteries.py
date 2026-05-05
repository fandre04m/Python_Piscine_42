#!/usr/bin/env python3
from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    counter = 0

    def increment_counter() -> int:
        nonlocal counter
        counter += 1
        return counter
    return increment_counter


def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power

    def accumulate_power(extra_power: int) -> int:
        nonlocal power
        power += extra_power
        return power
    return accumulate_power


def enchantment_factory(enchantment_type: str) -> Callable:

    def enchant_item(item: str) -> str:
        return enchantment_type + " " + item
    return enchant_item


def memory_vault() -> dict[str, Callable]:
    mem_arch = {}

    def store_mem(key: str, value: Any) -> None:
        mem_arch[key] = value

    def recall_mem(key: str) -> Any:
        if key in mem_arch.keys():
            return mem_arch[key]
        return "Memory not found"
    return dict(store=store_mem, recall=recall_mem)


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(
        f"Counter-A call 1: {counter_a()}\n"
        f"Counter-A call 2: {counter_a()}\n"
        f"Counter-B call 1: {counter_b()}\n"
        f"Counter-A call 3: {counter_a()}\n"
        f"Counter-B call 2: {counter_b()}"
    )
    print()
    print("Testing spell accumulator...")
    base_power = 100
    powerup = spell_accumulator(base_power)
    print(
        f"Base {base_power}, add 20: {powerup(20)}\n"
        f"Now  {powerup(0)}, add 30: {powerup(30)}"
    )
    print()
    print("Testing enchantment factory...")
    ice_factory = enchantment_factory("Frozen")
    fire_factory = enchantment_factory("Flaming")
    print(
        f"Fire factory created: {fire_factory('Sword')}\n"
        f"Ice factory created: {ice_factory('Shield')}"
    )
    print()
    print("Testing memory vault...")
    mem_arch = memory_vault()
    print("Store 'secret' = 42")
    mem_arch["store"]("secret", 42)
    print(f"Recall 'secret': {mem_arch['recall']('secret')}")
    print(f"Recall 'unknown': {mem_arch['recall']('unknown')}")


if __name__ == "__main__":
    main()
