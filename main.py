class Shape:
    """
    Model shapes like circle and rectangle using inheritance
    """
    def __init__(self, name):
        self.name = name

    def draw(self):
        print(f"Drawing a {self.name}")

    def calculate_area(self):
        print("Area of a shape")

class Rectangle(Shape):
    """
    Square add two attributes, length and height to the constructor
    """

    def __init__(self, name, length,height):
        super().__init__(name)
        self.length = length  # Directly setting the radius is not allowed
        self.height = height

    def calculate_area(self):
        area = self.length * self.height
        print(f"Area of a rectangle {area:.2f}")

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    @property
    def height(self):
        return self._height


    @height.setter
    def height(self, value):
        self._height = value



class Circle(Shape):
    """
    Circle add new attribute radius and **overrides** calculate area
    """
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius  # Directly setting the radius is not allowed

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    def calculate_area(self, pi=3.14159):
        area = 2 * pi * self._radius
        print(f"Area of the circle: {area:.2f}")



# Call the draw and calculate_area methods
shape = Shape("shape")
shape.draw()
shape.calculate_area()

# Create a Circle object
print("PI is default 3.14159")
circle = Circle("Circle", 5)
circle.draw()
circle.calculate_area()

# overload PI in Circle
print("overloaded PI = 3.14")
circle = Circle("Circle", 5)
circle.draw()
circle.calculate_area(3.14)

rectangle = Rectangle("Rectangle",10,5)
rectangle.draw()
rectangle.calculate_area()