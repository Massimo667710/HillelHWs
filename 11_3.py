def is_even(number):
    list_num = list(str(number))

    # 1st Option
    # num_list = ('0', '2', '4', '6', '8')

    # if list_num[-1] in num_list:
    #     result = True
    # else:
    #     result = False

    # return result

    # 2nd Option
    return list_num[-1] in ('0', '2', '4', '6', '8')


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('Ok')
