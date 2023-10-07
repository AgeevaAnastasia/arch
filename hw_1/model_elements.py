class Angle3D:
    pass


class Color:
    pass


class Point3D:
    pass


class Polygon:
    def __init__(self):
        self.point3d = Point3D


class Texture:
    pass


class Type:
    pass


class PolygonalModel:
    def __int__(self):
        self.polygon = Polygon()
        self.texture = Texture()


class Flash:
    def __int__(self):
        self.location = Point3D()
        self.angle = Angle3D()
        self.color = Color()
        self.power = float()

    def rotate(self, angle3d):
        pass

    def move(self, point3d):
        pass


class Camera:
    def __init__(self):
        self.location = Point3D()
        self.angle = Angle3D()

    def rotate(self, angle3d):
        pass

    def move(self, point3d):
        pass



class Scene:
    def __init__(self):
        self.id = int()
        self.models = PolygonalModel()
        self.flashes = Flash()
        self.camera = Camera()

    def method_one(self, type_1: Type) -> Type:
        return type_1

    def method_two(self, type_2: Type, type_3: Type) -> Type:
        return type_2
