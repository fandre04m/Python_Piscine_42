

def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access alchemy/grimoire/dark_spellbook.py directly")
    ingr = "tears, blood, eyeballs"
    print("Testing for circular import with dark spell record:")
    from alchemy.grimoire.dark_spellbook import dark_spell_record
    print(f"{dark_spell_record('Dark Ball', ingr)}")


if __name__ == "__main__":
    main()
