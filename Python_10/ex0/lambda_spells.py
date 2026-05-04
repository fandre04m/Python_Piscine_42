#!/usr/bin/env python3


artifacts = [
    {'name': 'Ice Wand', 'power': 71, 'type': 'accessory'},
    {'name': 'Ice Wand', 'power': 112, 'type': 'armor'},
    {'name': 'Fire Staff', 'power': 104, 'type': 'weapon'},
    {'name': 'Lightning Rod', 'power': 80, 'type': 'relic'},
    {'name': 'Fire Staff', 'power': 118, 'type': 'focus'}
]

mages = [
    {'name': 'Rowan', 'power': 53, 'element': 'ice'},
    {'name': 'Luna', 'power': 50, 'element': 'shadow'},
    {'name': 'Ash', 'power': 76, 'element': 'lightning'},
    {'name': 'Luna', 'power': 70, 'element': 'wind'},
    {'name': 'Riley', 'power': 68, 'element': 'lightning'}
]

spells = ['flash', 'tsunami', 'blizzard', 'lightning']


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return (
        sorted(artifacts, key=lambda item: item["power"], reverse=True)
    )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return (
        list(filter(lambda mage: mage["power"] >= min_power, mages))
    )


def spell_transformer(spells: list[str]) -> list[str]:
    return (
        list(map(lambda spell: "* " + spell + " *", spells))
    )


def mage_stats(mages: list[dict]) -> dict:
    stats_dict = {}
    stats_dict["max_power"] = max(map(lambda mage: mage["power"], mages))
    stats_dict["min_power"] = min(map(lambda mage: mage["power"], mages))
    stats_dict["avg_power"] = (
        round(sum(map(lambda mage: mage["power"], mages)) / len(mages), 2)
    )
    return stats_dict


def main() -> None:
    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    art_0 = sorted_artifacts[0]
    art_1 = sorted_artifacts[1]
    print(
        f"{art_0['name']} ({art_0['power']} power) comes before "
        f"{art_1['name']} ({art_1['power']} power)"
    )
    print()
    print("Testing mage filter...")
    min_power = 60
    valid_mages = power_filter(mages, min_power)
    print(f"Mages with mininimum power of {min_power}:")
    for mage in valid_mages:
        print(f"{mage['name']} ({mage['power']} power)")
    print()
    print("Testing spell transformer...")
    transformed_spells = spell_transformer(spells)
    print(" ".join(transformed_spells))
    print()
    print("Testing mage stats...")
    stats = mage_stats(mages)
    for stat, val in stats.items():
        print(f"{stat}: {val}")


if __name__ == "__main__":
    main()
