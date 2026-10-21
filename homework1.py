num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))

total_sum = num1 + num2 + num3
product = num1 * num2 * num3

print(f"Сума чисел: {total_sum}")
print(f"Добуток чисел: {product}")

d1 = float(input("Введіть довжину першої діагоналі: "))
d2 = float(input("Введіть довжину другої діагоналі: "))

area = (d1 * d2) / 2

print(f"Площа ромба: {area}")

salary = float(input("Введіть зарплату за місяць: "))
credit = float(input("Введіть щомісячний платіж за кредитом: "))
utilities = float(input("Введіть заборгованість за комунальні послуги: "))

remainder = salary - credit - utilities

print(f"Сума, яка залишиться після всіх виплат: {remainder}")

distance = float(input("Введіть відстань у кілометрах: "))
consumption = float(input("Введіть витрату палива на 100 км (у літрах): "))
price_per_liter = float(input("Введіть ціну за літр бензину: "))

total_cost = (distance / 100) * consumption * price_per_liter

print(f"Підсумкова вартість поїздки: {total_cost:.2f}")

bill = float(input("Введіть загальну суму рахунку: "))
people = int(input("Введіть кількість осіб: "))

tips = bill * 0.15
total_bill = bill + tips
per_person = total_bill / people

print(f"Сума чайових (15%): {tips:.2f}")
print(f"Загальна сума з чайовими: {total_bill:.2f}")
print(f"Кожна людина має заплатити: {per_person:.2f}")

daily_rate = float(input("Введіть вартість оренди за день: "))
days = int(input("Введіть кількість днів оренди: "))
deposit = float(input("Введіть суму застави: "))

rent_cost = daily_rate * days
total_with_deposit = rent_cost + deposit
after_return_cost = rent_cost
cost_per_day = rent_cost / days

print(f"Загальна вартість оренди із заставою: {total_with_deposit:.2f}")
print(f"Сума до сплати після повернення застави: {after_return_cost:.2f}")
print(f"Вартість оренди за один день: {cost_per_day:.2f}")
