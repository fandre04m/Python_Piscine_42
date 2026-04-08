from elements import create_water


def main() -> None:
    print("=== Alembic 1 ===")
    print("Using: 'from ... import ...' structure to acess elements.py")
    print(f"Testing create_water: {create_water()}")


if __name__ == "__main__":
    main()
