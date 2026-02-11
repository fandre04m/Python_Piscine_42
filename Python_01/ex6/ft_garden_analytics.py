#!/usr/bin/env python3

class Plant:
    """Represents the base values common for each base plant"""
    def __init__(
        self,
        name: str,
        height: int
    ) -> None:
        """Initializes base values"""
        self.name = name.title()
        self.height = height

    def grow(self, amount: int) -> int:
        """Grows plant by amount"""
        self.height += amount
        return amount

    def get_info(self) -> str:
        """Returns base plant info"""
        return f"{self.name}: {self.height}cm"

    def get_type(self) -> str:
        """Returns plant type"""
        return "regular"


class FloweringPlant(Plant):
    """Represents a flowering plant"""
    def __init__(
        self,
        name: str,
        height: int,
        flower_color: str
    ) -> None:
        """
        Initializes common values using inheritance
        Initializes specific value for flower color
        """
        super().__init__(name, height)
        self.flower_color = flower_color

    def get_info(self) -> str:
        """
        Overrides returning common information using inheritance
        Includes flower color in the overwriten information
        """
        return f"{super().get_info()}, {self.flower_color} flowers (blooming)"

    def get_type(self) -> str:
        """Returns plant type"""
        return "flowering"


class PrizeFlower(FloweringPlant):
    """Represents a prize flower"""
    def __init__(
        self,
        name: str,
        height: int,
        flower_color: str,
        prize_points: int
    ) -> None:
        """
        Initializes common values using inheritance
        Initializes specific value for prize points
        """
        super().__init__(name, height, flower_color)
        self.prize_points = prize_points

    def get_info(self) -> str:
        """
        Overrides returning common information using inheritance
        Includes prize points in the overwriten information
        """
        return f"{super().get_info()}, Prize points: {self.prize_points}"

    def get_type(self) -> str:
        """Returns plant type"""
        return "prize flowers"


class Garden:
    """Represents a garden"""
    def __init__(
        self,
        owner: str
    ) -> None:
        """Initializes the values of garden"""
        self.owner = owner.capitalize()
        self.__plants = []
        self.total_growth = 0

    def add_plant(
        self,
        plant: Plant
    ) -> None:
        """
        Adds each new plant to the garden list
        Outputs confirmation of added plant to the correct garden
        """
        self.__plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_all_grow(self) -> None:
        """
        Grown all plants in the garden
        Updates total growth value of the garden
        """
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.__plants:
            growth = plant.grow(1)
            self.total_growth += growth
            print(f"{plant.name} grew {growth}cm")

    def calculate_score(self) -> int:
        """Calculates and returns total score points of the garden"""
        garden_score = 0
        for plant in self.__plants:
            garden_score += 10
            garden_score += plant.height
            if plant.get_type() == "prize flowers":
                garden_score += plant.prize_points
        return garden_score

    def get_statistics(self) -> 'GardenManager.GardenStats':
        """Fetches needed statistics for the garden report"""
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
        """Outputs a report for a garden"""
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
    """Represents a manager for a garden"""
    class GardenStats:
        """Initializes the stats for the garden to later create report"""
        def __init__(self) -> None:
            self.total_plants = 0
            self.total_growth = 0
            self.t_regular = 0
            self.t_flowering = 0
            self.t_prized = 0

    def __init__(self) -> None:
        """Initializes the list of gardens"""
        self.gardens = []

    def add_garden(self, garden: Garden) -> None:
        """Adds new garden to list"""
        self.gardens.append(garden)

    def get_garden_scores(self) -> str:
        """Returns the score points for all gardens"""
        output = "Garden scores - "
        for garden in self.gardens:
            score = garden.calculate_score()
            output += f"{garden.owner}: {score}, "
        output = output[:-2]
        return output

    def total_gardens(self) -> int:
        """Returns the total number of gardens managed"""
        total = 0
        for gardens in self.gardens:
            total += 1
        return total

    @classmethod
    def create_garden_network(cls) -> 'GardenManager':
        """Blueprint for the initial state of the managed garden network"""
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
        """Validaes values without the need of specific garden data"""
        return height >= 0


def garden_demo() -> None:
    """Manipulates and reports garden data"""
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


if __name__ == "__main__":
    garden_demo()
