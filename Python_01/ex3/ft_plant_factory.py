#!/usr/bin/env Python3

class Plant:
    """Stores the data of each plant"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize each attribute"""
        self.name = name.capitalize()
        self.height = height
        self.age = age


plant_data = [
    Plant("rose", 25, 30),
    Plant("sunflower", 80, 45),
    Plant("cactus", 15, 120),
]
