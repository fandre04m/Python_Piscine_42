#!/usr/bin/env python3

class PlantData:
    """Stores the data of each plant"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize each attribute"""
        self.name = name.capitalize()
        self.height = height
        self.age = age

plants = [
    PlantData("tulip", 23, 14),
    PlantData("cactus", 121, 678),
    PlantData("magnolia", 44, 8),
    PlantData("orchid", 37, 11),
]


def main():
    """Prints each plant's data iteratively"""
    print("=== Garden Plant Registry ===")
    for i in range(4):
        plant = plants[i]
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


if __name__ == "__main__":
    main()
