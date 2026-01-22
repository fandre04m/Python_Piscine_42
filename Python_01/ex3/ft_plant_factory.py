#!/usr/bin/env python3

class Plant:
    """Stores the data of each plant."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize each attribute."""
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def get_info(self) -> str:
        """Get information from stored plants."""
        return f"{self.name} ({self.height}cm, {self.age} days)"


def ft_plant_factory() -> None:
    """Creates plant data and prints them"""
    plant_data = [
        Plant("rose", 25, 30),
        Plant("oak", 200, 365),
        Plant("cactus", 5, 90),
        Plant("sunflower", 80, 45),
        Plant("fern", 15, 120),
    ]
    count = 0
    print("=== Plant Factory Output ===")
    for i in range(5):
        print(f"Created: {plant_data[i].get_info()}")
        count += 1
    print(f"\nTotal plants created: {count}")


if __name__ == "__main__":
    ft_plant_factory()
