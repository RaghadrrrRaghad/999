class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def display(self):
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")
        print(f"Perimeter: {self.perimeter()}")
        print(f"Area: {self.area()}")


class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height
