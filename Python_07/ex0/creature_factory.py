from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, c_name: str, c_type: str) -> None:
        self.c_name: str = c_name.capitalize()
        self.c_type: str = c_type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        if "/" in self.c_type:
            type_1, type_2 = self.c_type.split("/")
            t = type_1.capitalize() + "/" + type_2.capitalize()
        else:
            t = self.c_type.capitalize()
        return f"{self.c_name} is a {t} type Creature"


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__("flameling", "fire")

    def attack(self) -> str:
        return f"{self.c_name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("pyrodon", "fire/flying")

    def attack(self) -> str:
        return f"{self.c_name} uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__("aquabub", "water")

    def attack(self) -> str:
        return f"{self.c_name} uses Water Gun!"


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__("torragon", "water")

    def attack(self) -> str:
        return f"{self.c_name} uses Hydro Pump!"


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
