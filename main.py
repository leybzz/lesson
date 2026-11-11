import calc

a = int(input("a = "))
b = int(input("b = "))
op = input("+, -, *, /: ")

if op == "+":
    print(calc.add(a, b))
elif op == "-":
    print(calc.dif(a, b))
elif op == "*":
    print(calc.mul(a, b))
elif op == "/":
    print(calc.div(a, b))
else:
    print("Input error.")