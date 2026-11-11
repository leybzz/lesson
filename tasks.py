def draw_line(length, direction, symbol):
  if direction == "h":
    print(symbol * length)
  elif direction == "v":
    for _ in range(length):
      print(symbol)
  else:
    print("Невірний напрямок. Використовуйте 'h' або 'v'.")

def get_max_of_four(a, b, c, d):
  max_num = a
  if b > max_num:
    max_num = b
  if c > max_num:
    max_num = c
  if d > max_num:
    max_num = d
  return max_num

def is_prime(num):
  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

def is_lucky_ticket(number):
  s = str(number)
  if len(s) != 6:
    return "Число має бути шестизначним!"
  sum_first = int(s[0]) + int(s[1]) + int(s[2])
  sum_second = int(s[3]) + int(s[4]) + int(s[5])
  return sum_first == sum_second