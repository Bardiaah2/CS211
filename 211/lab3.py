'''This lab focuses on the concept of inheritance in object-oriented programming using Python. The
lab requires the creation of concrete classes that inherit from an abstract class called Shape3D.
The abstract class defines methods but does not implement them; each concrete subclass must
implement those methods with specific functionality. The lab covers creating concrete
subclasses, defining class attributes, and implementing class methods. The lab culminates in
testing the classes using a provided code snippet.'''

class Shape3D:
    def __init__(self):
        raise NotImplementedError("Abstract class cannot be instantiated")
    
    def volume(self) -> float:
        raise NotImplementedError("Not implemented for abstractclass")
    
    def area(self) -> float:
        '''Calculates as if a closed shape'''
        raise NotImplementedError("Not implemented for abstractclass")
    
    def print_info(self):
        return f'Area: {self.area()}, Volume: {self.volume()}'


class Cylinder(Shape3D):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self) -> float:
        from math import pi
        return pi * (self.radius ** 2) * self.height
    
    def area(self) -> float:
        from math import pi
        return 2 * pi * self.radius * (self.radius + self.height)
    

class Cuboid(Shape3D):
    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height

    def volume(self) -> float:
        return self.height * self.length * self.width
    
    def area(self) -> float:
        return 2 * (self.width * self.length + self.height * self.length + self.width * self.height)
    
class Cube(Cuboid):
    def __init__(self, a):
        super().__init__(a, a, a)


if __name__ == '__main__':
    cyl = Cylinder(3,5)
    cuboid = Cuboid(6,4,9)
    lst = [Cube(3), cyl, cuboid]
    for shape in lst:
        print(shape.print_info())