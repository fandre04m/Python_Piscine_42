#!/usr/bin/env python3

class Plant:
    """Stores the data of each plant."""
    def __init__(
        self,
        name: str,
        height: int,
        age: int
    ) -> None:
        """Initialize each attribute."""
        self.name = name.capitalize()
        self.height = height
        self.age = age


plant_data = [
    Plant("rose", 25, 30),
    Plant("sunflower", 80, 45),
    Plant("cactus", 15, 120),
]


def ft_garden_data() -> None:
    """Prints each plant's data iteratively."""
    print("=== Garden Plant Registry ===")
    for i in range(3):
        plant = plant_data[i]
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


if __name__ == "__main__":
    ft_garden_data()
