#!/usr/bin/env python3

def main() -> None:
    """
    Stores simple data in variables
    Displays information about plants in garden
    """
    name = "rose"
    height = 25
    age = 30
    print("=== Welcome to My Garden ===")
    print("Plant:", name.capitalize())
    print(f"Height: {height}cm")
    print(f"Age: {age} days\n")
    print("=== End of Program ===")


if __name__ == "__main__":
    main()
