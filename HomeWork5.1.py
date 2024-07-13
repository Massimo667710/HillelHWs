import keyword, string

# our_str = '_'
our_str = '__'
# our_str = '___'
# our_str = 'x'
# our_str = 'get_value'
# our_str = 'get value'
# our_str = 'get!value'
# our_str = 'some_super_puper_value'
# our_str = 'Get_value'
# our_str = 'get_Value'
# our_str = 'getValue'
# our_str = '3m'
# our_str = 'm3'
# our_str = 'assert'
# our_str = 'assert_exception'

result = True

if our_str[0].isdigit() or our_str in keyword.kwlist:        # Чи починається змінна на цифру or зарезервовані слова
    result = False

elif our_str.count('_') == len(our_str) and len(our_str) > 1:
    result = False
else:
    for letter in our_str:
        if letter.isupper():                # Чи починається слово з Верхнього регістру
            result = False
            break

        if letter[0] == '_':
            continue

        if letter in string.punctuation:        # Знаки пунктуації
            result = False
            break

        elif letter.isspace():               # Чи є пробіли
            result = False
            break


print(result)





