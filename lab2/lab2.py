import math

# 1. Обчислити факторіал числа 8
number = 8
if number < 0:
    print("Факторіал мінусового числа не існує")
else:
    factorial = math.factorial(number)
    print(f"Факторіал числа {number} дорівнює: {factorial}\n")

# 2. Перевірити число 7 (на те, чи воно просте)
num = 7
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"Число {num} є простим числом.\n")
else:
    print(f"Число {num} є складеним числом.\n")

# 3. Таблиця множення від 1 до 10
print("--- Таблиця множення від 1 до 10 ---")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}\t", end="")
    print()