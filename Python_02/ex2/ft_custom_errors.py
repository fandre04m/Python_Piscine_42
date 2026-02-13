#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __init__(self, plant: str) -> None:
        self.plant_name = plant
        message = f"The {self.plant_name} plant is wilting!"
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self) -> None:
        message = f"Not enough water in the tank!"
        super().__init__(message)


def check_plant(plant: str) -> None:
    raise PlantError(plant)


def water_plant() -> None:
    raise WaterError()


def garden_error_demo() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        check_plant("tomato")
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
    print("\nTesting WaterError...")
    try:
        water_plant()
    except WaterError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
    print("\nTesting catching all garden errors...")
    try:
        check_plant("tomato")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        water_plant()
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    garden_error_demo()
