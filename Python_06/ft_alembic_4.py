import alchemy


def main() -> None:
    print("=== Alembic 4 ===")
    print("Using: 'import alchemy' to access the alchemy module")
    print(f"Testing create_air: {alchemy.create_air()}")
    print("Example of trying to reach functions not included in __init__.py:")
    print("Testing the hidden create_earth: ", end="")
    print(alchemy.create_earth())
    # try:
    #     print(alchemy.create_earth())
    # except AttributeError as e:
    #     print(f"{e.__class__.__name__}: {e}. Did you mean: 'create_air'?")


if __name__ == "__main__":
    main()
