# №1
user_number = int(input('Enter 4-digit number: '))

first_number = user_number // 1000
second_number = user_number // 100 % 10
third_number = user_number // 10 % 10
fourth_number = user_number % 10

print(first_number)
print(second_number)
print(third_number)
print(fourth_number)

