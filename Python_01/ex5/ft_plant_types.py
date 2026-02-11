#!/usr/bin/env python3

class Plant:
    """Represents a base plant's values"""
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

    def get_info(self) -> str:
        """Obtain plant type and returns info"""
        plt_type = self.__class__.__name__
        return f"{self.name} ({plt_type}): {self.height}cm, {self.age} days"

    def get_action(self) -> str:
        """Placeholder for loop to be safe"""
        return ""


class Flower(Plant):
    """Represents flower data"""
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Initialize especific flower attributes
        Inherits base Plant data
        """
        super().__init__(name, height, age)
        self.color = color

    def get_info(self) -> str:
        """Returns flower data using inheritance"""
        return f"\n{super().get_info()}, {self.color} color"

    def bloom(self) -> str:
        """Makes flowers bloom"""
        return f"{self.name} is blooming beautifully!"

    def get_action(self) -> str:
        """Triggers the action of blooming"""
        return self.bloom()


class Tree(Plant):
    """Represents tree data"""
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        trunk_diameter: int,
        shade: int
    ) -> None:
        """
        Initialize especific tree attributes
        Inherits base Plant data
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade = shade

    def get_info(self) -> str:
        """Returns tree info using inheritance"""
        return f"\n{super().get_info()}, {self.trunk_diameter}cm diameter"

    def produce_shade(self) -> str:
        """Makes tree produce shade"""
        return f"{self.name} provides {self.shade} square meters of shade"

    def get_action(self) -> str:
        """Triggers the producing of shade"""
        return self.produce_shade()


class Vegetable(Plant):
    """Represents vegetable data"""
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str
    ) -> None:
        """
        Initialize especific vegetable attributes
        Inherits base Plant data
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> str:
        """Returns vegetable info using inheritance"""
        return f"\n{super().get_info()}, {self.harvest_season} harvest"

    def get_nutri_val(self) -> str:
        """Returns nutritional value of Vegetable"""
        return f"{self.name} is rich in {self.nutritional_value}"

    def get_action(self) -> str:
        """Triggers nutritional value action"""
        return self.get_nutri_val()


def ft_plant_types() -> None:
    """Creates plants and displays information after triggering actions"""
    plants = [
        Flower("rose", 25, 30, "red"),
        Flower("tulip", 15, 12, "pink"),
        Tree("oak", 500, 1825, 50, 78),
        Tree("pine", 450, 1600, 45, 56),
        Vegetable("tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("carrot", 40, 50, "fall", "vitamin A")
    ]
    print("=== Garden Plant Types ===")
    for i in range(6):
        print(plants[i].get_info())
        print(plants[i].get_action())


if __name__ == "__main__":
    ft_plant_types()
