from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Shape3d(ABC):
    @abstractmethod
    def volume(self):
        pass


class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return self.side * 4

    def __str__(self):
        return (f'Square with side = {self.side} u.e. has perimeter = {self.perimeter()} u.e., '
                f'area = {self.area()} u.e.^2')


class Cube(Shape, Shape3d):
    def __init__(self, side: float):
        self.side = side

    def area(self):
        return (self.side ** 2) * 6

    def perimeter(self):
        return self.side * 12

    def volume(self):
        return self.side ** 3

    def __str__(self):
        return (f'Cube with side = {self.side} u.e. has perimeter = {self.perimeter()} u.e., '
                f'area = {self.area()} u.e.^2, volume = {self.volume()} u.e.^3')


if __name__ == '__main__':
    square = Square(3)
    cube = Cube(3)
    print(square)
    print(cube)
