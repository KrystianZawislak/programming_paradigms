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
        self.sides = 3

class Square(Rectangle):
    
    def __init__(self, a):
        super().__init__(a, a)
        self.sides = 4
        
class GeometricSolid(Shape):
    
    def __init__(self, figures):
        super().__init__()
        self.figures = figures 
        
    def area(self):
        total_area = 0
        for figure in self.figures:
            total_area += figure.area()
        return total_area
    
    @abstractmethod 
    def walls(self):
        pass
    
class Plato:
    
    def vertices(self):
        
        total_vertices = 2 - len(self.walls()) + (len(self.walls()) * self.walls()[0].sides) // 2
        return total_vertices

class Tetrahedron(GeometricSolid, Plato):
    
    def __init__(self, a):
        figures = [EquilateralTriangle(a) for _ in range(4)]
        super().__init__(figures)
        self.shape = "Tetrahedron"
        
    def walls(self):
        return self.figures
        
class Cube(GeometricSolid, Plato):
    
    def __init__(self, a):
        figures = [Square(a) for _ in range(6)]
        super().__init__(figures)
        self.shape = "Cube"
        
    def walls(self):
        return self.figures
        
class Pyramid(GeometricSolid):
    
    def __init__(self, a):
        figures = [Square(a)] + [EquilateralTriangle(a) for _ in range(4)]
        super().__init__(figures)
        self.shape = "Pyramid"
        
    def walls(self):
        return self.figures
        
    def vertices(self):
        return 5
        
    
def main():
    figures = []
    figures.append(Tetrahedron(4))
    figures.append(Cube(3))
    figures.append(Pyramid(1))
    
    for figure in figures:
        print(figure.shape, figure.area(), figure.vertices())

if __name__ == "__main__":
    main()
