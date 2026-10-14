#1
h = int(input("Введіть кількість годин: "))
m = int(input("Введіть кількість хвилин: "))
s = int(input("Введіть кількість секунд: "))

total = h * 3600 + m * 60 + s
remaining = 24 * 3600 - total

hours = remaining // 3600
minutes = remaining % 3600 // 60
seconds = remaining % 60

print("До опівночі залишилося:", hours, "годин,", minutes, "хвилин,", seconds, "секунд")
#2
import math

d = float(input("Введіть діаметр кола: "))

print("1 - Площа кола")
print("2 - Довжина кола")

choice = int(input("Ваш вибір: "))

if choice == 1:
    area = math.pi * (d / 2) ** 2
    print("Площа кола:", area)
elif choice == 2:
    perimeter = math.pi * d
    print("Довжина кола:", perimeter)
else:
    print("Неправильний вибір")
#3
price = float(input("Введіть вартість однієї приставки: "))
quantity = int(input("Введіть кількість приставок: "))
discount = float(input("Введіть відсоток знижки: "))

total = price * quantity
final_price = total - total * discount / 100

print("Загальна сума зі знижкою:", final_price)
#4
size = float(input("Введіть розмір файлу в ГБ: "))
speed = float(input("Введіть швидкість інтернету в бітах за секунду: "))

bits = size * 8 * 1024 ** 3
total_seconds = int(bits / speed)

hours = total_seconds // 3600
minutes = total_seconds % 3600 // 60
seconds = total_seconds % 60

print("Час завантаження:", hours, "годин,", minutes, "хвилин,", seconds, "секунд")
#5
h = int(input("Введіть кількість годин: "))

if 0 <= h < 6:
    print("Good Night")
elif 6 <= h < 13:
    print("Good Morning")
elif 13 <= h < 17:
    print("Good Day")
elif 17 <= h < 24:
    print("Good Evening")
else:
    print("Неправильне значення")