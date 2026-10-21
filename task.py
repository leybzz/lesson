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

 #завдання3

salary = float(input())
experience = float(input())

if experience < 1:
    print("Премія не передбачена")
elif 1 <= experience <= 3:
    bonus = salary * 0.05
    print(f"Сума премії: {bonus}")
elif 3 < experience <= 5:
    bonus = salary * 0.10
    print(f"Сума премії: {bonus}")
elif experience > 5:
    bonus = salary * 0.15
    print(f"Сума премії: {bonus}")
else:
    print("Помилка")
#завдання4

number_str = input()

if len(number_str) == 6 and number_str.isdigit():
    first_sum = int(number_str[0]) + int(number_str[1]) + int(number_str[2])
    second_sum = int(number_str[3]) + int(number_str[4]) + int(number_str[5])
    
    if first_sum == second_sum:
        print("Щасливе число")
    else:
        print("Нещасливе число")
else:
    print("Помилка")
