from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    
    def __init__(self):
        self.__shape = "Shape"
    
    @property
    def shape(self):
        return self.__shape
        
    @shape.setter
    def shape(self, new_shape):
        self.__shape = self.__shape + " " + new_shape
        
    @abstractmethod
    def area(self):
        pass
    
class Circle(Shape):
    
    def __init__(self, radius):
        super().__init__()
        self.shape = "Circle"
        self.radius = radius
    
    def area(self):
        return (self.radius**2)*pi
        
class Triangle(Shape):
    
    def __init__(self, a, b, c):
        super().__init__()
        self.shape = "Triangle"
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        half_the_perimeter = (self.a+self.b+self.c) / 2.0
        return (half_the_perimeter * (half_the_perimeter - self.a) * (half_the_perimeter - self.b) * (half_the_perimeter - self.c))**(1/2)
        
class Rectangle(Shape):
    
    def __init__(self, a, b):
        super().__init__()
        self.shape = "Rectangle"
        self.a = a
        self.b = b
    
    def area(self):
        return self.a * self.b
        
class EquilateralTriangle(Triangle):
    
    def __init__(self, a):
        super().__init__(a, a, a)

class Square(Rectangle):
    
    def __init__(self, a):
        super().__init__(a, a)
        
def main():
    figures = []
    figures.append(Circle(3))
    figures.append(Rectangle(1, 2))
    figures.append(Triangle(3, 4, 5))
    figures.append(Square(6))
    figures.append(EquilateralTriangle(3))
    
    figures[3].shape, figures[4].shape = "Square", "Equilateral"
    
    for figure in figures:
        print(figure.shape, figure.area())

if __name__ == "__main__":
    main()
