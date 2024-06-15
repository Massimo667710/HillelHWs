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
    print(f'{num_1} / {num_2} =', num_1 / num_2)
else:
    print('You chose wrong operation! Try again!')

