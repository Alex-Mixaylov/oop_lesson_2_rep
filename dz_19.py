# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`)
# и методы (`make_sound()`, `eat()`) для всех животных.
#
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы,
# если требуется (например, различный звук для `make_sound()`).
#
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
#
# 4. Используйте композицию для создания класса `Zoo`, который
# будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
#
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые
# могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
#
# Добавьте дополнительные функции в вашу программу, такие как
# сохранение информации о зоопарке в файл и возможность её загрузки,
# чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def animal_sound(self):
        pass
    def animal_eat(self):
        pass

class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def animal_sound(self):
        return "Пение пиц"
    def animal_eat(self):
        return "Зерно"
    def animal_move(self):
        return "Летает"

class Mammal(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def animal_sound(self):
        return "Звуки млекопитающих"
    def animal_eat(self):
        return "Молоко"
    def animal_move(self):
        return "Бегает"

class Reptile(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def animal_sound(self):
        return "Не издает звуков"
    def animal_eat(self):
        return "Насекомые"
    def animal_move(self):
        return "Ползает"