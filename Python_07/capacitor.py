#!/usr/bin/env python3
from ex1 import (
    HealingCreatureFactory,
    TransformCreatureFactory,
    HealCapability,
    TransformCapability
)


def healing_test(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    print(" base:")
    base = factory.create_base()
    evo = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    if isinstance(base, HealCapability):
        print(base.heal("itself"))
    print(" evolved:")
    print(evo.describe())
    print(evo.attack())
    if isinstance(evo, HealCapability):
        print(evo.heal("itself and others"))


def tranform_test(factory: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")
    print(" base:")
    base = factory.create_base()
    evo = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    if isinstance(base, TransformCapability):
        print(base.transform())
    print(base.attack())
    if isinstance(base, TransformCapability):
        print(base.revert())
    print(" evolved:")
    print(evo.describe())
    print(evo.attack())
    if isinstance(evo, TransformCapability):
        print(evo.transform())
    print(evo.attack())
    if isinstance(evo, TransformCapability):
        print(evo.revert())


def main() -> None:
    h_factory = HealingCreatureFactory()
    t_factory = TransformCreatureFactory()
    try:
        healing_test(h_factory)
        print()
        tranform_test(t_factory)
    except Exception as e:
        print(f"An error as occurred: {e}")


if __name__ == "__main__":
    main()
