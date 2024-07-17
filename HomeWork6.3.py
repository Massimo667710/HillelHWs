user_number = int(input('Enter your number: '))

result = 1

while user_number > 9:
    for digit in str(user_number):
        result *= int(digit)
    user_number = result
    result = 1

print(user_number)


