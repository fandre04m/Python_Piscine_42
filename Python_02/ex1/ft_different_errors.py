#!/usr/bin/env python3

def garden_operations():
    try:
        int("abc")
    except ValueError as e:
        print(f"Testing {e.__class__.__name__}...")
        print(f"Caught {e.__class__.__name__}: {e}\n")
    try:
        10 / 0
    except ZeroDivisionError as e:
        print(f"Testing {e.__class__.__name__}...")
        print(f"Caught {e.__class__.__name__}: {e}\n")
    try:
        open("not_a_file.txt")
    except FileNotFoundError as e:
        print(f"Testing {e.__class__.__name__}...")
        print(f"Caught {e.__class__.__name__}: {e}\n")
    try:
        example_dict = {"zero": 0}
        print(example_dict["one"])
    except KeyError as e:
        print(f"Testing {e.__class__.__name__}...")
        print(f"Caught {e.__class__.__name__}: {e}\n")
    try:
        num = int("42")
        res = num / 0
        example_dict = {"Result": res}
        print(example_dict["Result"])
    except (ValueError, ZeroDivisionError, KeyError):
        print("Testing multiple errors together...")
        print("Caught an error, but program continues!")


def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("\nAll error types tested successfully")


if __name__ == "__main__":
    test_error_types()
