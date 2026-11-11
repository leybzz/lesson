import calc

op = input("*, /, sqrt, square: ")

if op == "sqrt" or op == "square":
    a = int(input("a = "))
    if op == "sqrt":
        print(calc.sqrt_num(a))
    elif op == "square":
        print(calc.square_num(a))

elif op == "*" or op == "/":
    a = int(input("a = "))
    b = int(input("b = "))

    if op == "*":
        print(calc.mul(a, b))
    elif op == "/":
        print(calc.div(a, b))

else:
    print("Input error.")
