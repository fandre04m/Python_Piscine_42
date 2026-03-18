#!/usr/bin/env python3
import alchemy.transmutation


def ft_pathway_debate() -> None:
    print("\n=== Pathway Debate Mastery ===\n")
    print("Testing Absolute Imports (from basic.py):")
    #    from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
    print(f"lead_to_gold(): {alchemy.transmutation.lead_to_gold()}")
    print(f"stone_to_gem(): {alchemy.transmutation.stone_to_gem()}")
    print()
    print("Testing Relative Imports (from advanced.py):")
#    print(f"philosophers_stone(): {}")


if __name__ == "__main__":
    ft_pathway_debate()
