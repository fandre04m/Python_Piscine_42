#!/usr/bin/env python3

def check_plant_health(
    plant_name: str,
    water_level: int,
    sunlight_hours: int
) -> str:
    if not plant_name:
        raise ValueError("Error: Plant name cannot be empty!")
    elif water_level < 1:
        raise ValueError(
            f"Error: Water level {water_level} is too low (min 1)"
        )
    elif water_level > 10:
        raise ValueError(
            f"Error: Water level {water_level} is too high (max 10)"
        )
    elif sunlight_hours < 2:
        raise ValueError(
            f"Error: Sunlight hours {sunlight_hours} is too low (min 2)"
        )
    elif sunlight_hours > 12:
        raise ValueError(
            f"Error: Sunlight hours {sunlight_hours} is too high (max 12)"
        )
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")
    print("\nTesting good values...")
    plant_status = check_plant_health("tomato", 5, 6)
    print(plant_status)
    print("\nTesting empty plant name...")
    try:
        plant_status = check_plant_health("", 5, 6)
    except ValueError as e:
        print(e)
    print("\nTesting bad water level...")
    try:
        plant_status = check_plant_health("tomato", 15, 6)
    except ValueError as e:
        print(e)
    print("\nTesting bad sunlight hours...")
    try:
        plant_status = check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(e)
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
