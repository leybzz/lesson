# Завдання 1
a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))

if a > b:
    a, b = b, a

total_sum = 0
count = 0

for i in range(a, b + 1):
    total_sum += i
    count += 1

average = total_sum / count

print("Сума:", total_sum)
print("Середнє арифметичне:", average)

# Завдання 2
n = int(input("Введіть число: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print("Факторіал:", factorial)

# Завдання 3
length = int(input("Введіть довжину лінії: "))
print("*" * length)

# Завдання 4
length = int(input("Введіть довжину лінії: "))
symbol = input("Введіть символ: ")
print(symbol * length)

# Завдання 5
while True:
    print("\n1 — знайти мінімум двох чисел")
    print("2 — знайти максимум двох чисел")
    print("3 — вихід")

    choice = int(input("Оберіть опцію: "))

    if choice == 1:
        x = float(input("Введіть перше число: "))
        y = float(input("Введіть друге число: "))
        print("Мінімум:", min(x, y))
    elif choice == 2:
        x = float(input("Введіть перше число: "))
        y = float(input("Введіть друге число: "))
        print("Максимум:", max(x, y))
    elif choice == 3:
        print("Вихід з програми.")
        break
    else:
        print("Помилка! Некоректна опція. Спробуйте ще раз.")

# Завдання 6
while True:
    print("\n1 — додавання двох чисел")
    print("2 — віднімання двох чисел")
    print("3 — ділення двох чисел")
    print("4 — вихід")

    choice = int(input("Оберіть опцію: "))

    if choice in [1, 2, 3]:
        x = float(input("Введіть перше число: "))
        y = float(input("Введіть друге число: "))

        if choice == 1:
            print("Результат:", x + y)
        elif choice == 2:
            print("Результат:", x - y)
        elif choice == 3:
            if y != 0:
                print("Результат:", x / y)
            else:
                print("Помилка: ділення на нуль!")
    elif choice == 4:
        print("Вихід з програми.")
        break
    else:
        print("Помилка! Некоректна опція. Спробуйте ще раз.")