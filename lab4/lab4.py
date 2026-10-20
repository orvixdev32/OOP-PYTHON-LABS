with open("lab4_report.txt", "w", encoding="utf-8") as f:
    f.write("Це перший рядок файлу.\nА це другий рядок з більшою кількістю слів.\nТретій рядок.\n")

# Завдання 1
with open("lab4_report.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    line_count = len(lines)
    word_count = 0
    for line in lines:
        word_count += len(line.split())

print(f"Кількість рядків: {line_count}")
print(f"Кількість слів: {word_count}\n")

# Завдання 2
name = input("Введіть ім'я: ")
while not name.replace(" ", "").isalpha():
    name = input("Помилка! Введіть ім'я літерами: ")

grade = input("Введіть оцінку (0-12): ")
while not (grade.isdigit() and 0 <= int(grade) <= 12):
    grade = input("Помилка! Введіть число від 0 до 12: ")

date = input("Введіть дату (ДД.ММ.РРРР): ")
while not (len(date) == 10 and date[2] == '.' and date[5] == '.'):
    date = input("Помилка! Формат дати має бути 00.00.0000: ")

with open("lab4_report.txt", "a", encoding="utf-8") as file:
    file.write(f"Ім'я: {name} | Оцінка: {grade} | Дата: {date}\n")

print("Дані успішно збережено.\n")

# Завдання 3
with open("lab4_report.txt", "r", encoding="utf-8") as file:
    first_line = file.readline()
    print("Зчитано перший рядок:", first_line.strip())
    
    current_position = file.tell()
    print(f"Позиція курсора: {current_position}")
    
    file.seek(0)
    print("Курсор переміщено на позицію 0.\n")
    
    print("Увесь текст файлу:")
    print(file.read())