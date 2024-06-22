list_of_numbers = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

for zero in list_of_numbers:
    if zero == 0:
        list_of_numbers.remove(zero)
        list_of_numbers.append(zero)

print(list_of_numbers)
