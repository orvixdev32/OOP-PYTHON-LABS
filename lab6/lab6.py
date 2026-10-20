import random
import list_utils  


print("ЗАВДАННЯ 1: Калькулятор")


# Функції для калькулятора
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Помилка: ділення на нуль!"
    return x / y

# Лямбда-функція для піднесення до степеня
power = lambda x, y: x ** y

try:
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))

    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")
    print(f"{a} * {b} = {multiply(a, b)}")
    print(f"{a} / {b} = {divide(a, b)}")
    print(f"{a} ^ {b} = {power(a, b)}")
except ValueError:
    print("Помилка: потрібно вводити саме числа!")



print("ЗАВДАННЯ 2: Випадкові числа")


# Генерація списку з 10 випадкових чисел від 1 до 100
random_numbers = [random.randint(1, 100) for _ in range(10)]
print(f"Згенерований список: {random_numbers}")


average = sum(random_numbers) / len(random_numbers)
max_val = max(random_numbers)
min_val = min(random_numbers)
even_count = len([num for num in random_numbers if num % 2 == 0])

print(f"Середнє арифметичне: {average}")
print(f"Максимальне значення: {max_val}")
print(f"Мінімальне значення: {min_val}")
print(f"Кількість парних чисел: {even_count}")



print("ЗАВДАННЯ 3: Робота з модулем list_utils")


# Тестовий список із дублікатами та невідсортованими даними
test_list = [15, 3, 9, 3, 15, 42, 7, 9, 1]
print(f"Початковий список: {test_list}")


sorted_list = list_utils.sort_list(test_list)
print(f"Відсортований список: {sorted_list}")


unique_list = list_utils.remove_duplicates(test_list)
print(f"Список без дублікатів: {unique_list}")

# 3. Пошук максимуму та мінімуму
maximum, minimum = list_utils.find_max_min(test_list)
print(f"Максимум: {maximum}, Мінімум: {minimum}")