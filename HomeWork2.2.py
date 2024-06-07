# №2
user_number = int(input('Enter 5-digit number: '))

first_number = user_number % 10
second_number = user_number % 100 // 10
third_number = user_number % 1000 // 100
fourth_number = user_number % 10000 // 1000
fifth_number = user_number // 10000

print(f'{first_number}{second_number}{third_number}{fourth_number}{fifth_number}')

