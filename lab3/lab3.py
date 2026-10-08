grades = [85, 90, 78, 92, 88]

print("Початкові оцінки:", grades)
print("Максимальна оцінка:", max(grades))
print("Мінімальна оцінка:", min(grades))

average = sum(grades) / len(grades)
print("Середня оцінка:", average)

grades.sort()
print("Відсортовані оцінки:", grades)

grades.append(95)
print("Після додавання:", grades)

grades.remove(min(grades))
print("Після видалення найнижчої:", grades)

count = 0
for grade in grades:
    if grade > 80:
        count += 1

print("Кількість студентів з оцінкою вище 80:", count)


phonebook = {
    "Олег": "0951234567",
    "Марія": "0677654321",
    "Іван": "0987654321"
}

phonebook["Анна"] = "0501234567"

print("Телефонний довідник:")
for name, phone in phonebook.items():
    print(name, "-", phone)

name = input("Введіть ім'я для пошуку: ")
if name in phonebook:
    print("Номер телефону:", phonebook[name])
else:
    print("Такої людини немає у довіднику.")

name = input("Введіть ім'я для видалення: ")
if name in phonebook:
    del phonebook[name]
    print("Запис видалено.")
else:
    print("Такої людини немає у довіднику.")

print("Оновлений довідник:")
for name, phone in phonebook.items():
    print(name, "-", phone)


numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)

print("Список:", numbers)
print("Кількість унікальних елементів:", len(unique_numbers))
print("Унікальні елементи:", unique_numbers)

repeated = []
for number in unique_numbers:
    if numbers.count(number) > 1:
        repeated.append(number)

print("Повторюються:", repeated)