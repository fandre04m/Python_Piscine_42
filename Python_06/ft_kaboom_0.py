import alchemy.grimoire


def main() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    ingr = "wind, wood, Fire"
    print(
        "Testing record light spell: "
        f"{alchemy.grimoire.light_spell_record('Fire Ball', ingr)}"
    )


if __name__ == "__main__":
    main()
