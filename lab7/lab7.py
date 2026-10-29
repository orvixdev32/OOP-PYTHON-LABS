
# Створюємо класи і описуємо логіку в них

class Student:
    def __init__(self, name, group, rating):
        self.name = name
        self.group = group
        self.rating = rating

    def show_info(self):
        print(
            f"Ім'я: {self.name}, група: {self.group}, "
            f"рейтинг: {self.rating}"
        )

    def change_rating(self, new_rating):
        self.rating = new_rating


class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.is_running = False

    def start(self):
        self.is_running = True
        print(f"{self.brand} {self.model} запущено.")

    def stop(self):
        self.is_running = False
        print(f"{self.brand} {self.model} зупинено.")

    def drive(self, km):
        if not self.is_running:
            print("Спочатку потрібно завести автомобіль.")
            return

        if km <= 0:
            print("Відстань має бути додатною.")
            return

        self.mileage += km
        print(f"{self.brand} {self.model} проїхав {km} км.")

    def info(self):
        print(
            f"Марка: {self.brand}, модель: {self.model}, "
            f"рік: {self.year}, пробіг: {self.mileage} км"
        )


class Book:
    def __init__(self, title, author, pages, year):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def info(self):
        print(
            f"Назва: {self.title}, автор: {self.author}, "
            f"сторінок: {self.pages}, рік видання: {self.year}"
        )

    def is_new(self):
        return self.year > 2015


# Виводимо класи та створюємо їхні об'єкти

print("СТУДЕНТИ")

students = [
    Student("Марія", "ІПЗ-21", 89),
    Student("Олег", "ІПЗ-21", 95),
    Student("Ірина", "ІПЗ-22", 92)
]

students[0].change_rating(91)

print("Список студентів:")
for student in students:
    student.show_info()

students_sorted = sorted(
    students,
    key=lambda student: student.rating,
    reverse=True
)

print("\nСтуденти за рейтингом:")
for student in students_sorted:
    student.show_info()


print("\nАВТОМОБІЛЬ")

car = Car("Toyota", "Corolla", 2018, 85000)

print("До поїздки:")
car.info()

car.start()
car.drive(120)
car.stop()

print("Після поїздки:")
car.info()


print("\nКНИГИ")

books = [
    Book("Основи програмування", "Іван Петренко", 320, 2012),
    Book("Python для початківців", "Олена Коваль", 280, 2022),
    Book("Алгоритми на практиці", "Андрій Мельник", 410, 2018),
    Book("Історія комп'ютерів", "Марія Бондар", 250, 2009)
]

print("Нові книги:")
for book in books:
    if book.is_new():
        book.info()
