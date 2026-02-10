#!/usr/bin/env python3

class Plant:
    def __init__(
        self,
        name: str,
        height: int
    ) -> None:
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
    def __init__(
        self,
        name: str,
        height: int,
        flower_color: str
    ) -> None:
        super().__init__(name, height)
        self.flower_color = flower_color

    def get_info(self) -> str:
        return f"{super().get_info()}, {self.flower_color} flowers (blooming)"

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
    def __init__(
        self,
        owner: str
    ) -> None:
        self.owner = owner.capitalize()
        self.__plants = []
        self.total_growth = 0

    def add_plant(self, plant: Plant) -> None:
        self.__plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_all_grow(self) -> None:
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.__plants:
            growth = plant.grow(1)
            self.total_growth += growth
            print(f"{plant.name} grew {growth}cm")

    def calculate_score(self) -> int:
        garden_score = 0
        for plant in self.__plants:
            garden_score += 10
            garden_score += plant.height
            if plant.get_type() == "prize flowers":
                garden_score += plant.prize_points
        return garden_score

    def get_statistics(self) -> 'GardenManager.GardenStats':
        stats = GardenManager.GardenStats()
        stats.total_growth = self.total_growth
        for plants in self.__plants:
            stats.total_plants += 1
            plant_type = plants.get_type()
            if plant_type == "regular":
                stats.t_regular += 1
            elif plant_type == "flowering":
                stats.t_flowering += 1
            elif plant_type == "prize flowers":
                stats.t_prized += 1
        return stats

    def generate_report(self) -> None:
        stats = self.get_statistics()
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plants in self.__plants:
            print(f"- {plants.get_info()}")
        print(
            f"\nPlants added: {stats.total_plants}, "
            f"Total growth: {stats.total_growth}cm"
        )
        print(
            f"Plant types: {stats.t_regular} regular, "
            f"{stats.t_flowering} flowering, "
            f"{stats.t_prized} prized flowers\n"
        )


class GardenManager:
    class GardenStats:
        def __init__(self) -> None:
            self.total_plants = 0
            self.total_growth = 0
            self.t_regular = 0
            self.t_flowering = 0
            self.t_prized = 0

    def __init__(self) -> None:
        self.gardens = []

    def add_garden(self, garden: Garden) -> None:
        self.gardens.append(garden)

    def get_garden_scores(self) -> str:
        output = "Garden scores - "
        for garden in self.gardens:
            score = garden.calculate_score()
            output += f"{garden.owner}: {score}, "
        output = output[:-2]
        return output

    def total_gardens(self) -> int:
        total = 0
        for gardens in self.gardens:
            total += 1
        return total

    @classmethod
    def create_garden_network(cls) -> 'GardenManager':
        manager = cls()
        alice_garden = Garden("alice")
        bob_garden = Garden("bob")
        pine = Plant("pine tree", 62)
        tulip = FloweringPlant("tulip", 10, "purple")
        bob_garden.add_plant(pine)
        bob_garden.add_plant(tulip)
        manager.add_garden(alice_garden)
        manager.add_garden(bob_garden)
        return manager

    @staticmethod
    def validate_height(height: int) -> bool:
        return height >= 0


if __name__ == "__main__":
    def garden_test() -> None:
        print("=== Garden Management System Demo ===\n")
        manager = GardenManager.create_garden_network()
        alice_garden = manager.gardens[0]
        oak = Plant("oak tree", 100)
        rose = FloweringPlant("rose", 25, "red")
        sunflower = PrizeFlower("sunflower", 50, "yellow", 10)
        alice_garden.add_plant(oak)
        alice_garden.add_plant(rose)
        alice_garden.add_plant(sunflower)
        alice_garden.help_all_grow()
        alice_garden.generate_report()
        print(f"Height validation test: {manager.validate_height(100)}")
        print(manager.get_garden_scores())
        print(f"Total gardens managed: {manager.total_gardens()}")

    garden_test()
