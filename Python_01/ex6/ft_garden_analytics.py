#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name.title()
        self.height = height

    def grow(self, amount: int) -> int:
        self.height += amount
        return amount

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm"

    def get_type(self) -> str:
        return "regular"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, flower_color: str) -> None:
        super().__init__(name, height)
        self.flower_color = flower_color

    def get_info(self) -> str:
        return f"{super().get_info()}, {flower_color} flowers (blooming)"

    def get_type(self) -> str:
        return "flowering"


class PrizeFlower(FloweringPlant):
    def __init__(
        self,
        name: str,
        height: int,
        flower_color: str,
        prize_points: int
    ) -> None:
        super().__init__(name, height, flower_color)
        self.prize_points = prize_points

    def get_info(self) -> str:
        return f"{super().get_info()}, Prize points: {self.prize_points}"

    def get_type(self) -> str:
        return "prize flowers"


class Garden:
    def __init__(self, owner: str) -> None:
        self.owner = owner.capitalize()
        self.__plants = []
        self.__total_growth = 0

    def add_plant(self, plant: Plant) -> None:
        self.__plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_all_grow(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.__plants:
            growth = plant.grow(1)
            self.__total_growth += growth
            print(f"{plant.name} grew {growth}cm")


plant = [
    oak = Plant("oak tree", 100),
    rose = FloweringPlant("rose", 25, "red"),
    sunflower = PrizeFlower("sunflower", 50, "yellow", 10)
]
