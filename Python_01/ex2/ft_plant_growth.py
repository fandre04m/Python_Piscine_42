#!/usr/bin/env python3

class Plant:
    """Represents a plant in a garden"""
    def __init__(
        self,
        name: str,
        height: int,
        plt_age: int
    ) -> None:
        """Initialize each attribute."""
        self.name = name.capitalize()
        self.height = height
        self.plt_age = plt_age

    def grow(self) -> None:
        """Grows plant by 1cm"""
        self.height += 1

    def age(self) -> None:
        """Ages the plant by 1 day"""
        self.plt_age += 1

    def get_info(self) -> str:
        """Returns plant information"""
        return f"{self.name}: {self.height}cm, {self.plt_age} days old"


plants = [
    Plant("rose", 25, 30),
    Plant("sunflower", 80, 45),
    Plant("cactus", 15, 120),
]


def ft_plant_growth() -> None:
    """Simulates a week of growth for all plants"""
    init_height = []
    print("=== Day 1 ===")
    for plant in plants:
        print(plant.get_info())
        init_height.append(plant.height)
        for i in range(1, 7):
            plant.grow()
            plant.age()
    print("=== Day 7 ===")
    for i in range(3):
        print(plants[i].get_info())
        growth = plants[i].height - init_height[i]
        print(f"Growth this week: {growth}cm")


if __name__ == "__main__":
    ft_plant_growth()
