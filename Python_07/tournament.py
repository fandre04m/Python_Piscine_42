#!/usr/bin/env python3
from ex0 import FlameFactory
from ex1 import TransformCreatureFactory
from ex2 import BattleError, NormalStrategy, AgressiveStrategy


def main() -> None:
    f_factory = FlameFactory()
    flameling = f_factory.create_base()
    t_factory = TransformCreatureFactory()
    shiftling = t_factory.create_base()
    a_strat = AgressiveStrategy()
    n_strat = NormalStrategy()
    print(flameling.describe())
    print(" vs.")
    print(shiftling.describe())
    print(" now fight!")
    try:
        n_strat.act(flameling)
        a_strat.act(shiftling)
    except BattleError as e:
        print(f"Battle error, aborting tournament: {e}")


if __name__ == "__main__":
    main()
