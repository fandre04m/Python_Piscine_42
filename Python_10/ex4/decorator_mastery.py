#!/usr/bin/env python3
from typing import Any
from collections.abc import Callable
import functools
import time


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


# def power_validator(min_power: int) -> Callable


# def retry_spell(max_attempts: int) -> Callable


# class MageGuild:
#   @staticmethod
#   def validate_mage_name(name: str) -> bool
#   def cast_spell(self, spell_name: str, power: int) -> str


def main() -> None:
    print("Testing spell timer...")

    @spell_timer
    def fireball(power: int, target: str) -> str:
        return f"Fireball strikes {target} for {power} DMG"
    print(f"Result: {fireball(50, 'Rotten Knight')}")


if __name__ == "__main__":
    main()
