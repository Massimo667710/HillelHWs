def common_elements():
    list_1 = {x for x in range(100) if x % 3 == 0}
    list_2 = {x for x in range(100) if x % 5 == 0}
    list_3 = list_1.intersection(list_2)
    print(list_3)                                   # Щоб бачити що отримали в list_3
    return list_3


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
