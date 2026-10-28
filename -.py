#1завдання

a = int(input())
b = int(input())

if a > b:
    a, b = b, a

for i in range(a, b + 1):
    print(i)
    
#2завдання

for i in range(a, b + 1):
    if i % 2 != 0:
        print(i)
        
#3завдання

for i in range(b, a - 1, -1):
    if i % 2 == 0:
        print(i)
#4завдання

mode = int(input())

if mode == 1:
    for i in range(a, b + 1):
        print(i)
elif mode == 2:
    for i in range(b, a - 1, -1):
        print(i)

