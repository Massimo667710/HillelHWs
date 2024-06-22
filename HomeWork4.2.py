list_of_numbers = [1, 3, 5]

if len(list_of_numbers) == 0:
    print(f'{list_of_numbers}')
else:
    last_number = list_of_numbers[-1]
    result = sum(list_of_numbers[number] for number in range(0, len(list_of_numbers), 2))
    print(f'{list_of_numbers} =>', result * list_of_numbers[-1])
