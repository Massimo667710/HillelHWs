num_1 = int(input('Enter your First number: '))
num_2 = int(input('Enter your Second number: '))
operation = input('Enter operation you want to do (+; -; *; /): ')

if operation == '+':
    print(f'{num_1} + {num_2} =', num_1 + num_2)
elif operation == '-':
    print(f'{num_1} - {num_2} =', num_1 - num_2)
elif operation == '*':
    print(f'{num_1} * {num_2} =', num_1 * num_2)
elif operation == '/':
    if num_2 == 0:
        print('Your denominator = 0, this is incorrect! Rewrite your numbers!')
    else:
        print(f'{num_1} / {num_2} =', num_1 / num_2)
else:
    print('You chose wrong operation! Try again!')

