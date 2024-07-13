import string

user_str = input('Enter your arrange of letters: ').split('-')

start = string.ascii_letters.find(user_str[0])
finish = string.ascii_letters.find(user_str[-1])

print(string.ascii_letters[start:finish + 1])
