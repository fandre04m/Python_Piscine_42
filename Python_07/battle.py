#!/usr/bin/env python3
import ex0


def factory_test(factory: ex0.CreatureFactory) -> None:
    print(f"Testing {factory.__class__.__name__}")
    base = factory.create_base()
    evol = factory.create_evolved()
    print(
        f"{base.describe()}\n"
        f"{base.attack()}\n"
        f"{evol.describe()}\n"
        f"{evol.attack()}\n"
    )


def battle_test(
    mob_1: ex0.CreatureFactory,
    mob_2: ex0.CreatureFactory
) -> None:
    return


def main() -> None:
    flame_factory = ex0.FlameFactory()
    aqua_factory = ex0.AquaFactory()
    factory_test(flame_factory)
    factory_test(aqua_factory)


if __name__ == "__main__":
    main()
