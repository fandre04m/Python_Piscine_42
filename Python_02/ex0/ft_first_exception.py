#!/usr/bin/env python3

def check_temperature(temp_str: str) -> int:
    print(f"\nTesting temperature: {temp_str}")
    try:
        temp = int(temp_str)
    except ValueError:
        raise ValueError(f"'{temp_str}' is not a valid number")
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    elif temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    print(f"Temperature {temp}°C is perfect for plants!")
    return temp


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    try:
        check_temperature("25")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        check_temperature("abc")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        check_temperature("100")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        check_temperature("-50")
    except ValueError as e:
        print(f"Error: {e}")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
