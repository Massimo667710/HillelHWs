import string


def is_palindrome(text):
    text = text.lower()
    text_no_punctuation = str.maketrans('', '', string.punctuation)
    new_text = text.translate(text_no_punctuation)
    new_text = ''.join(new_text.split())
    final_text = new_text[::-1]

    if new_text == final_text:
        return True
    else:
        return False

    # return new_text == final_text

    # Дізнався що можна так ще перевірити на True/False без if


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
