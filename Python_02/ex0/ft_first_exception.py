#!/usr/bin/env python3

def check_temperature(temp_str: str) -> int | None:
    print(f"\nTesting temperature: {temp_str}")
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None
    else:
        if 0 <= temp <= 40:
            print(f"Temperature {temp}°C is perfect for plants!")
            return temp
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
            return None
        else:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
            return None


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
