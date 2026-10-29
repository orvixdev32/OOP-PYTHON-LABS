
class Worker:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def info(self):
        print(f"Працівник: {self.name}, посада: {self.position}, зарплата: {self.salary} грн")


class Manager(Worker):
    def __init__(self, name, position, salary, department):
        super().__init__(name, position, salary)
        self.department = department

    def info(self):
        print(f"Менеджер: {self.name}, посада: {self.position}, відділ: {self.department}, зарплата: {self.salary} грн")


class Transport:
    def move(self):
        print("Машина засіб рухається")


class Car(Transport):
    def move(self):
        print("Автомобіль їде дорогою")


class Cat:
    def sound(self):
        print("Кіт нявкає")


class Dog:
    def sound(self):
        print("Собака гавкає")


class Parrot:
    def sound(self):
        print("Папуга розмовляє")


worker = Worker("Назар", "Розробник", 80000)
manager = Manager("Андрій", "Керівник", 50000, "Продажі")

worker.info()
manager.info()

transport = Transport()
car = Car()

transport.move()
car.move()

animals = [Cat(), Dog(), Parrot()]

for animal in animals:
    animal.sound()
