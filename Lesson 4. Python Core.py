# Завдання 1
a = float(input("Число 1: "))
b = float(input("Число 2: "))
c = float(input("Число 3: "))
d = input("1 - сума, 2 - добуток: ")

if d == "1":
    print(a + b + c)
else:
    print(a * b * c)


# Завдання 2
a = float(input("Число 1: "))
b = float(input("Число 2: "))
c = float(input("Число 3: "))
d = input("1 - макс, 2 - мін, 3 - середнє: ")

if d == "1":
    print(max(a, b, c))
elif d == "2":
    print(min(a, b, c))
else:
    print((a + b + c) / 3)