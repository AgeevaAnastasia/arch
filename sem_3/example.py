import zope.interface
from abc import ABC, abstractmethod


class Test1(zope.interface.Interface):
    def test(self):
        pass


class Test2(zope.interface.Interface):
    def test(self):
        pass


class A(object):
    zope.interface.implementer(Test1, Test2)


class ATest(ABC):
    @abstractmethod
    def test_a(self):
        pass


class BTest(ABC):
    @abstractmethod
    def test_b(self):
        pass


class CTest(ATest, BTest):
    def test_a(self):
        print('test a')

    def test_b(self):
        print('test b')


if __name__ == '__main__':
    c = CTest()
    c.test_b()
    c.test_a()
