import alchemy


def main() -> None:
    print("=== Alembic 4 ===")
    print("Using: 'import alchemy' to access the alchemy module")
    print(f"Testing create_air: {alchemy.create_air()}")
    print("Example of trying to reach functions not included in __init__.py:")
    print("Testing the hidden create_earth: ", end="")
    print(alchemy.create_earth())


if __name__ == "__main__":
    main()
