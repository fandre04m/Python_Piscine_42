#!/usr/bin/env python3

def water_plants(plant_list: list) -> None:
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant == "None":
                raise NameError(
                    f"Error: Cannot water {plant} - invalid plant!"
                )
            print(f"Watering {plant}")
    except NameError as e:
        print(e)
        return
    finally:
        print("Closing watering system (cleanup)")
    print("Watering completed successfully!")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    good_list = [
        "tomato",
        "lettuce",
        "carrots"
    ]
    bad_list = [
        "tomato",
        "None"
    ]
    print("\nTesting normal watering...")
    water_plants(good_list)
    print("\nTesting with error...")
    water_plants(bad_list)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
