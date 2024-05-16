import json
import os


# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`)
# и методы (`make_sound()`, `eat()`) для всех животных.
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass


# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы,
# если требуется (например, различный звук для `make_sound()`).
class Bird(Animal):
    def __init__(self, name, age, can_fly=False):
        super().__init__(name, age)
        self.can_fly = can_fly

    def make_sound(self):
        return "Крик птицы"

    def eat(self):
        return "Клюет зерно"


class Mammal(Animal):
    def __init__(self, name, age, is_predator=False):
        super().__init__(name, age)
        self.is_predator = is_predator

    def make_sound(self):
        return "Голос млекопитающего"

    def eat(self):
        return "Ест мясо" if self.is_predator else "Ест траву"


class Reptile(Animal):
    def __init__(self, name, age, is_poisonous=False):
        super().__init__(name, age)
        self.is_poisonous = is_poisonous

    def make_sound(self):
        return "Шипение рептилии"

    def eat(self):
        return "Ест насекомых"


# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
def animal_sound(animals):
    for animal in animals:
        print(f'{animal.name} издает звук: {animal.make_sound()}')


# 4. Используйте композицию для создания класса `Zoo`, который
# будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def save_to_file(self, filename):
        zoo_data = {
            "animals": [{"type": type(a).__name__, "name": a.name, "age": a.age,
                         "specific": {"can_fly": a.can_fly} if isinstance(a, Bird) else
                         {"is_predator": a.is_predator} if isinstance(a, Mammal) else
                         {"is_poisonous": a.is_poisonous}} for a in self.animals],
            "employees": [{"type": type(e).__name__, "name": e.name, "age": e.age} for e in self.employees]
        }
        with open(filename, 'w') as file:
            json.dump(zoo_data, file)

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            zoo_data = json.load(file)
            for animal_data in zoo_data['animals']:
                if animal_data['type'] == 'Bird':
                    animal = Bird(animal_data['name'], animal_data['age'], animal_data['specific']['can_fly'])
                elif animal_data['type'] == 'Mammal':
                    animal = Mammal(animal_data['name'], animal_data['age'], animal_data['specific']['is_predator'])
                elif animal_data['type'] == 'Reptile':
                    animal = Reptile(animal_data['name'], animal_data['age'], animal_data['specific']['is_poisonous'])
                self.add_animal(animal)
            for employee_data in zoo_data['employees']:
                if employee_data['type'] == 'ZooKeeper':
                    employee = ZooKeeper(employee_data['name'], employee_data['age'])
                elif employee_data['type'] == 'Veterinarian':
                    employee = Veterinarian(employee_data['name'], employee_data['age'])
                self.add_employee(employee)


# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые
# могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
class ZooKeeper:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def feed_animal(self):
        return "Животные покормлены"


class Veterinarian:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def heal_animal(self):
        return "Животные пролечены"


# Пример использования:
if __name__ == "__main__":
    # Создаем экземпляры животных
    bird_1 = Bird("Воробей", 1, True)
    bird_2 = Bird("Ястреб", 1.5, True)
    bird_3 = Bird("Страус", 3.5, False)
    mammal_1 = Mammal("Лев", 5, True)
    mammal_2 = Mammal("Слон", 35, False)
    mammal_3 = Mammal("Горилла", 15, False)
    reptile_1 = Reptile("Змея", 2, True)
    reptile_2 = Reptile("Ящерица", 1, False)
    reptile_3 = Reptile("Варан", 1, True)

    # Создаем экземпляры сотрудников
    zookeeper = ZooKeeper("Анна", 34)
    veterinarian = Veterinarian("Иван", 40)

    # Создаем зоопарк и добавляем в него животных и сотрудников
    zoo = Zoo()
    animals = [bird_1, bird_2, bird_3, mammal_1, mammal_2, mammal_3, reptile_1, reptile_2, reptile_3]
    employees = [zookeeper, veterinarian]

    for animal in animals:
        zoo.add_animal(animal)

    for employee in employees:
        zoo.add_employee(employee)

    # Демонстрируем звуки животных
    print("Демонстрируем звуки животных:\n")
    animal_sound(zoo.animals)

    # Сохраняем состояние зоопарка в файл
    print("\nСохраняем состояние зоопарка в файл....\n")
    zoo.save_to_file("zoo_data.json")

    # Загружаем состояние зоопарка из файла
    print("Загружаем состояние зоопарка из файла....\n")
    new_zoo = Zoo()
    new_zoo.load_from_file("zoo_data.json")
    animal_sound(new_zoo.animals)

    # Выводим текущую рабочую директорию

    print("\nСохранено в рабочую директорию:", os.getcwd())
