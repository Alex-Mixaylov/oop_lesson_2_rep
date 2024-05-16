# Создайте класс Animal с методом make_sound().
# Затем создайте несколько дочерних классов (например, Dog, Cat, Cow),
# которые наследуют Animal, но изменяют его поведение (метод make_sound()).
# В конце создайте список содержащий экземпляры этих животных и вызовите make_sound() для каждого животного в цикле.

class Animal():
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        return "Гав-гав!"

class Cat(Animal):
    def make_sound(self):
        return "Мяу!"

class Cow(Animal):
    def make_sound(self):
        return "Мууу!"

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(animal.make_sound())

print("\n")

# Продемонстрировать принцип полиморфизма через реализацию разных классов, представляющих геометрические формы, и метод для расчёта площади каждой формы.
# Создать базовый класс Shape с методом area(), который просто возвращает 0.
# Создать несколько производных классов для разных форм (например, Circle, Rectangle, Square), каждый из которых переопределяет метод area().
# В каждом из этих классов метод area() должен возвращать площадь соответствующей фигуры.
# Написать функцию, которая принимает объект класса Shape и выводит его площадь.

class Shape():
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length ** 2

def print_area(shape):
    print(f"Площадь: {shape.area()}")

shapes = [Circle(5), Rectangle(10, 5), Square(7)]

for shape in shapes:
    print_area(shape)