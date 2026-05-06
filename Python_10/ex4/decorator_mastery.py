#!/usr/bin/env python3
from typing import Any
from collections.abc import Callable
import functools
import time
import random


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        time.sleep(0.101)
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {(end - start):.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            power = args[-1]
            if power < min_power:
                res = "Insufficient power for this spell"
            else:
                res = func(*args, **kwargs)
            return res
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            "Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3 and (name.isalpha() or name.isspace()):
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("Testing spell timer...")

    @spell_timer
    def fireball(target: str, power: int) -> str:
        return f"Fireball strikes {target} for {power} DMG"
    print(f"Result: {fireball('Rotten Knight', 50)}")
    print()
    print("Testing power validator...")

    @power_validator(25)
    def whirlwind(target: str, power: int) -> str:
        return f"Whirlwind strikes {target} for {power} break DMG"
    print(f"Result: {whirlwind('Orc King', 30)}")
    print()
    print("Testing retrying spell...")

    @retry_spell(3)
    def corrupt_orb(target: str, power: int) -> str:
        if random.random() < 0.8:
            raise ValueError(
                "Corrupt Orb exploded in the caster's hands"
            )
        return f"Corrupt Orb strikes {target} for {power} DMG"
    print(f"Result: {corrupt_orb('Paladin', 80)}")
    print()
    print("Testing MageGuild...")
    guild_test = MageGuild()
    print(
        f"{guild_test.validate_mage_name('Ember')}\n"
        f"{guild_test.validate_mage_name('NotEmber!')}\n"
        f"{guild_test.cast_spell('Lightning', 15)}\n"
        f"{guild_test.cast_spell('Lightning', 5)}"
    )


if __name__ == "__main__":
    main()
