#!/usr/bin/env python3

class SecurePlant:
    """Represents a secure plant with validate data"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize each attribute"""
        self.name = name.capitalize()
        self.__height = height
        self.__age = age

    def set_height(self, height: int) -> bool:
        """
        Validates and updates height
        Outputs message based on behavior
        """
        if height >= 0:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")
            return True
        print(f"\nInvalid operation attempted: height {height}cm [REJECTED]")
        print("Security: Negative height rejected\n")
        return False

    def set_age(self, age: int) -> bool:
        """
        Validates and updates age
        Outputs message based on behavior
        """
        if age >= 0:
            self.__age = age
            print(f"Age updated: {age} days [OK]")
            return True
        print(f"\nInvalid operation attempted: age {age} days [REJECTED]")
        print("Security: Negative age rejected\n")
        return False

    def get_height(self) -> int:
        """Acess and return private height property"""
        return self.__height

    def get_age(self) -> int:
        """Acess and return private age property"""
        return self.__age

    def get_info(self) -> str:
        """Returns information on current plant"""
        return f"{self.name} ({self.get_height()}cm, {self.get_age()} days)"


def ft_garden_security() -> None:
    """
    Update plant values
    Demonstrates behavior with invalid height
    """
    plant = SecurePlant("rose", 0, 0)
    print("=== Garden Security System ===")
    print(f"Plant created: {plant.name}")
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)
    print(f"Current plant: {plant.get_info()}")


if __name__ == "__main__":
    ft_garden_security()
