# №2
user_number = int(input('Enter 5-digit number: '))

a = user_number % 10
b = user_number % 100 // 10
c = user_number % 1000 // 100
d = user_number % 10000 // 1000
e = user_number // 10000

print(a, b, c, d, e)

