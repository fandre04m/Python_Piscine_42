from alchemy import create_air


def main() -> None:
    print("=== Alembic 5 ===")
    print("Using: 'from alchemy import ...' to access the alchemy module")
    print(f"Testing create_air: {create_air()}")


if __name__ == "__main__":
    main()
