#!/usr/bin/env python3

class Plant:
    """Stores the data of each plant."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize each attribute."""
        self.name = name.capitalize()
        self.__height = height
        self.__age = age

    def set_height(self, height: int) -> str:
        """Validates before updating height."""
        if height >= 0:
            self.__height = height
            return "[OK]"
        else:
            return "[REJECTED]"

    def set_age(self, age: int) -> str:
        """Validates before updating age."""
        if age >= 0:
            self.__age = age
            return "[OK]"
        else:
            return "[REJECTED]"

    def get_height():

    def get_age():


plant_data = [
    Plant("rose", 0, 0),
    Plant("sunflower", 80, 45),
    Plant("cactus", 15, 120),
]


def ft_garden_security():


if __name__ == "__main__":
    ft_garden_security()
