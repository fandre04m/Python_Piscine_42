#!/usr/bin/env python3
import alchemy


def ft_sacred_scroll() -> None:
    print()
    print("=== Sacred Scroll Mastery ===")
    print()
    print("Testing direct module access:")
    print(
        f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}\n"
        f"alchemy.elements.create_water(): {alchemy.elements.create_water()}\n"
        f"alchemy.elements.create_earth(): {alchemy.elements.create_earth()}\n"
        f"alchemy.elements.create_air(): {alchemy.elements.create_air()}"
    )
    print()
    print("Testing package-level access (controlled by __init__.py):")
    try:
        print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    except AttributeError as e:
        print(f"alchemy.create_fire(): {e.__class__.__name__} - not exposed")
    try:
        print(f"alchemy.create_water(): {alchemy.create_water()}")
    except AttributeError as e:
        print(f"alchemy.create_water(): {e.__class__.__name__} - not exposed")
    try:
        print(f"alchemy.create_earth(): {alchemy.create_earth()}")
    except AttributeError as e:
        print(f"alchemy.create_earth(): {e.__class__.__name__} - not exposed")
    try:
        print(f"alchemy.create_air(): {alchemy.create_air()}")
    except AttributeError as e:
        print(f"alchemy.create_air(): {e.__class__.__name__} - not exposed")
    print()
    print("Package metadata:")
    print(
        f"Version: {alchemy.__version__}\n"
        f"Author: {alchemy.__author__}"
    )


if __name__ == "__main__":
    ft_sacred_scroll()
