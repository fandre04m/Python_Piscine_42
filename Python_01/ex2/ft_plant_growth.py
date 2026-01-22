#!/usr/bin/env python3

class Plant:
    """Stores the data of each plant."""
    def __init__(self, name: str, height: int, plt_age: int) -> None:
        """Initialize each attribute."""
        self.name = name.capitalize()
        self.height = height
        self.plt_age = plt_age

    def grow(self) -> None:
        """Grows plant when called."""
        self.height += 1

    def age(self) -> None:
        """Ages the plant when called."""
        self.plt_age += 1

    def get_info(self) -> None:
        """Pulls the info from PlantData and prints."""
        print(f"{self.name}: {self.height}cm, {self.plt_age} days old")


plants = [
    Plant("rose", 25, 30),
    Plant("sunflower", 80, 45),
    Plant("cactus", 15, 120),
]


def ft_plant_growth():
    """Grows and ages plants, and prints info."""
    print("=== Day 1 ===")
    plants[1].get_info()
    curr_height = plants[1].height
    for i in range(1, 7):
        plants[1].grow()
        plants[1].age()
    print("=== Day 7 ===")
    plants[1].get_info()
    print(f"Growth this week: +{plants[1].height - curr_height}cm")


if __name__ == "__main__":
    ft_plant_growth()
