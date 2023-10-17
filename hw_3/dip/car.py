from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass


class PetrolEngine(Engine):
    def start_engine(self):
        print('Petrol engine starts now')

    def stop_engine(self):
        print('Petrol engine stops now')


class DieselEngine(Engine):
    def start_engine(self):
        print('Diesel engine starts now')

    def stop_engine(self):
        print('Diesel engine stops now')


class Car:
    def __init__(self, engine: Engine):
        self.engine = engine

    def start_car(self):
        self.engine.start_engine()

    def stop_car(self):
        self.engine.stop_engine()


if __name__ == '__main__':
    car1 = DieselEngine()
    car2 = PetrolEngine()
    car1.start_engine()
    car1.stop_engine()
    car2.start_engine()
    car2.stop_engine()
