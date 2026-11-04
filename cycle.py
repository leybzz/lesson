#завдання1
number = ""


while True:
    print("\n1. Ввести число")
    print("2. Аналіз числа")
    print("0. Вихід")

    choice = input("Виберіть пункт: ")

    if choice == "0":
        break
    elif choice == "1":
        number = input("Введіть число: ")
    elif choice == "2":
        if number == "":
            print("Спершу введіть число!")
        else:
            clean = number.lstrip("-")
            count = len(clean)
            total = 0
            zeros = 0

            for digit in clean:
                total += int(digit)
                if digit == "0":
                    zeros += 1

            average = total / count if count > 0 else 0

            print(f"Кількість цифр: {count}")
            print(f"Сума цифр: {total}")
            print(f"Середнє арифметичне: {average}")
            print(f"Кількість нулів: {zeros}")

#завдання2
size = 3
for r in range(4):
    for _ in range(size):
        line = ""
        for c in range(4):
            if (r + c) % 2 == 0:
                line += "*" * size
            else:
                line += "-" * size
        print(line)