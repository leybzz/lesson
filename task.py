#завдання1

month = int(input())

if month == 12 or month == 1 or month == 2:
    print("Winter")
elif 3 <= month <= 5:
    print("Spring")
elif 6 <= month <= 8:
    print("Summer")
elif 9 <= month <= 11:
    print("Autumn")
else:
    print("Помилка")

#завдання2

score = int(input())

if 90 <= score <= 100:
    print("Відмінно")
elif 70 <= score <= 89:
    print("Добре")
elif 50 <= score <= 69:
    print("Задовільно")
elif 0 <= score < 50:
    print("Незадовільно")
else:
    print("Помилка")