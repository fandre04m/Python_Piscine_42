from abc import ABC, abstractmethod
from ex0.creature_factory import Creature
from ex1.creature_capabilities import HealCapability, TransformCapability


class BattleError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise BattleError(
                f"Invalid Creature '{creature.__class__.__name__}' "
                "for this normal strategy"
            )
        print(creature.attack())

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)


class AgressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise BattleError(
                f"Invalid Creature '{creature.__class__.__name__}' "
                "for this agressive strategy"
            )
        if hasattr(creature, 'transform') and hasattr(creature, 'revert'):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise BattleError(
                f"Invalid Creature '{creature.__class__.__name__}' "
                "for this defensive strategy"
            )
        if hasattr(creature, 'heal'):
            print(creature.attack())
            print(creature.heal())

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)
