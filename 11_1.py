def simple_num(num):
    div = 1
    div_list = []
    while div <= num:
        if num % div == 0:
            div_list.append(div)
        div += 1

    return True if len(div_list) == 2 else False


def prime_generator(end):
    number = 1
    while number <= end:
        if simple_num(number):
            yield number
        number += 1


from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
