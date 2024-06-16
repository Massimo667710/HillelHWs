ourList = [1, 2, 3, 4, 5, 6]

if len(ourList) % 2 == 0:
    a = len(ourList)
    b = a // 2
    list_1 = ourList[:b]
    list_2 = ourList[-b:]
    print(f'{ourList} => [{list_1}, {list_2}]')
elif len(ourList) == 1:
    new_list = []
    print(f'{ourList} => [{ourList}, {new_list}]')
elif len(ourList) % 2 != 0:
    import math
    a = len(ourList)
    b = math.ceil(a/2)                               # округление до ближайшего большего числа.
    list_1 = ourList[:b]
    list_2 = ourList[b:]
    print(f'{ourList} => [{list_1}, {list_2}]')
elif len(ourList) == 0:
    print(f'{ourList} => [{ourList}, {ourList}]')
else:
    print('Your operation is out of exercise!')
