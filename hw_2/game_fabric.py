from random import choice
from abc import ABC, abstractmethod


class ItemFabric(ABC):
    def __init__(self):
        self.game_item = None

    @abstractmethod
    def create_item(self):
        pass

    def open_reward(self):
        self.game_item = self.create_item()
        self.game_item.open()


class IGameItem(ABC):
    @abstractmethod
    def open(self):
        pass


class GoldReward(IGameItem):
    def open(self):
        print('Gold')


class GoldGenerator(ItemFabric):
    def create_item(self):
        print('Create new box')
        return GoldReward()


class GemReward(IGameItem):
    def open(self):
        print('Gem')


class GemGenerator(ItemFabric):
    def create_item(self):
        print('Create new box')
        return GemReward()


class DiamondReward(IGameItem):
    def open(self):
        print('Diamond')


class DiamondGenerator(ItemFabric):
    def create_item(self):
        print('Create new box')
        return DiamondReward()


class FoodReward(IGameItem):
    def open(self):
        print('Food')


class FoodGenerator(ItemFabric):
    def create_item(self):
        print('Create new box')
        return FoodReward()


class OldShoeReward(IGameItem):
    def open(self):
        print('Old shoe')


class OldShoeGenerator(ItemFabric):
    def create_item(self):
        print('Create new box')
        return OldShoeReward()


# ДЗ. Добавить новые предметы. Сундуки с новыми предметами.

if __name__ == '__main__':
    # gold_generator = GoldGenerator()
    # gold_generator.open_reward()
    lst = [GoldGenerator(), GemGenerator(), DiamondGenerator(), FoodGenerator(), OldShoeGenerator()]
    for _ in range(20):
        choice(lst).open_reward()
