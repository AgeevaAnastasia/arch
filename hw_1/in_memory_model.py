from model_elements import PolygonalModel, Flash, Camera, Scene, Polygon, Texture
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
    def __init__(self, models: [PolygonalModel],
                 scenes: [Scene], flashes: [Flash], camera: [Camera],
                 change_observers: [IModelChangedObserver]):
        self.models = models
        self.models.append(PolygonalModel([Polygon], [Texture]))
        self.scenes = scenes
        self.scenes.append(Scene([PolygonalModel], [Flash], [Camera]))
        self.flashes = flashes
        self.flashes.append(Flash())
        self.camera = camera
        self.camera.append(Camera())
        self.__change_observers = change_observers

    def get_scene(self, num: int) -> Scene:
        return self.scenes.id(num)

    def notify_change(self, sender: IModelChanger):
        return sender
