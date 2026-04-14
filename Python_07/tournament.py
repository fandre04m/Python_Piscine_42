#!/usr/bin/env python3
from typing import List, Tuple
from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import TransformCreatureFactory, HealingCreatureFactory
from ex2 import (
    BattleError,
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy
)

BattleSetup = Tuple[CreatureFactory, BattleStrategy]


def run_tournament(t_setup: List[BattleSetup]):
    print("*** Tournament ***")
    print(f"{len(t_setup)} opponents involved")
    opponents = []
    for factory, strategy in t_setup:
        creature = factory.create_base()
        opponents.append((creature, strategy))
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            opponent_1, strategy_1 = opponents[i]
            opponent_2, strategy_2 = opponents[j]
            print("\n* Battle *")
            print(
                f"{opponent_1.describe()}\n"
                " vs.\n"
                f"{opponent_2.describe()}"
            )
            print(" now fight!")
            try:
                strategy_1.act(opponent_1)
                strategy_2.act(opponent_2)
            except BattleError as e:
                print(f"Battle error, aborting tournament: {e}")


def main() -> None:
    print("-" * 10 + " Tournament 0 (basic) " + "-" * 10)
    t0_setup = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    run_tournament(t0_setup)
    print()
    print("-" * 10 + " Tournament 1 (error) " + "-" * 10)
    t1_setup = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]
    print(" [ (Flameling+Agressive), (Healing+Defensive) ]")
    run_tournament(t1_setup)
    print()
    print("-" * 10 + " Tournament 2 (multiple) " + "-" * 10)
    t2_setup = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())
    ]
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    run_tournament(t2_setup)


if __name__ == "__main__":
    main()
