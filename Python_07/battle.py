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
    f_factory: ex0.CreatureFactory,
    a_factory: ex0.CreatureFactory
) -> None:
    print("Testing battle")
    flameling = f_factory.create_base()
    aquabub = a_factory.create_base()
    print(flameling.describe())
    print(" vs.")
    print(aquabub.describe())
    print(" fight!")
    print(flameling.attack())
    print(aquabub.attack())
    return


def main() -> None:
    flame_factory = ex0.FlameFactory()
    aqua_factory = ex0.AquaFactory()
    factory_test(flame_factory)
    factory_test(aqua_factory)
    battle_test(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
