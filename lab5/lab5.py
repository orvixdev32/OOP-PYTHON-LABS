# Завдання 1
try:
    a = float(input("Введіть a = "))
    b = float(input("Введіть b = "))
    
    result = a / b
    print(f"Результат ділення: {result}")
    
except ZeroDivisionError:
    print("Помилка: ділення на нуль!")
except ValueError:
    print("Помилка: потрібно вводити саме числа!")
# Завдання 2
try:
    number_str = input("Введіть число: ")
    number = int(number_str)
except ValueError:
    print("Помилка: введено нечислове значення!")
finally:
    print("Програма завершена.")
# Завдання 3
filename = "example.txt"
file = None

try:
    print("Спроба відкрити файл...")
    file = open(filename, "r", encoding="utf-8")
except FileNotFoundError:
    print("Файл не знайдено. Створюємо новий.")
    file = open(filename, "w", encoding="utf-8")
    file.write("Файл створено автоматично.")
finally:
    if file is not None:
        file.close()
    print("Файл закрито.")