from model_elements import PolygonalModel, Flash, Camera, Scene
from abc import ABC, abstractmethod


class IModelChangedObserver(ABC):
    @abstractmethod
    def apply_update_model(self):
        pass


class IModelChanger(ABC):
    @abstractmethod
    def notify_change(self, sender):
        pass


class ModelStore:
    def __init__(self):
        self.models = PolygonalModel()
        self.scenes = Scene()
        self.flashes = Flash()
        self.camera = Camera()
        self.__change_observers = IModelChangedObserver()

    def get_scena(self, num: int) -> Scene:
        return self.scenes.id(num)

    def notify_change(self, sender: IModelChanger):
        return sender
