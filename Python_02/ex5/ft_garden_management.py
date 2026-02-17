#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __init__(self) -> None:
        message = "Plant name cannot be empty!"
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self) -> None:
        message = "Not enough water in the tank!"
        super().__init__(message)


class Plant:
    def __init__(
        self,
        name: str,
        water: int,
        sunlight: int
    ) -> None:
        self.name = name
        self.water = water
        self.sun = sunlight

    def check_health(self) -> str:
        if self.water < 1:
            raise ValueError(
                f"Water level {self.water} is too low (min 1)"
            )
        elif self.water > 10:
            raise ValueError(
                f"Water level {self.water} is too high (max 10)"
            )
        elif self.sun < 2:
            raise ValueError(
                f"Sunlight hours {self.sun} is too low (min 2)"
            )
        elif self.sun > 12:
            raise ValueError(
                f"Sunlight hours {self.sun} is too high (max 12)"
            )
        return f"{self.name}: healthy (water: {self.water}, sun: {self.sun})"


class GardenManager:
    def __init__(self) -> None:
        self.plants = []
        self.water_tank = 10

    def add_plant(
        self,
        plant: Plant
    ) -> None:
        if not plant.name:
            raise PlantError()
        self.plants.append(plant)
        print(f"Added {plant.name} successfully")

    def water_plants(
        self,
        amount: int
    ) -> None:
        for plant in self.plants:
            if self.water_tank < amount:
                raise WaterError()
            plant.water += amount
            self.water_tank -= amount
            print(f"Watering {plant.name} - success")

    def check_plant_health(self) -> None:
        for plant in self.plants:
            try:
                status = plant.check_health()
                print(status)
            except ValueError as e:
                print(f"Error checking {plant.name}: {e}")


def test_garden_management() -> None:
    plant_list = [
            Plant("tomato", 0, 8),
            Plant("lettucce", 10, 6),
            Plant("", 8, 8)
    ]
    print("=== Garden Management System ===")
    garden = GardenManager()
    print("\nAdding plants to garden...")
    for plant in plant_list:
        try:
            garden.add_plant(plant)
        except PlantError as e:
            print(f"Error adding plant: {e}")
    print("\nWatering plants...")
    try:
        print("Opening water system")
        garden.water_plants(5)
    except WaterError as e:
        print(f"Error watering plants: {e}")
    finally:
        print("Closing watering system (cleanup)")
    print("\nChecking plant health...")
    garden.check_plant_health()
    print("\nTesting error recovery...")
    try:
        garden.water_plants(5)
    except GardenError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
    finally:
        print("System recovered and continuing...")
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
