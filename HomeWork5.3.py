import string

hashtag = '#'
input_string = input('Enter your sentence: ')

clean_string = input_string.translate(str.maketrans('', '', string.punctuation))

words = clean_string.split()
capitalized_words = [word.capitalize() for word in words]

hashtag_word = hashtag + ''.join(capitalized_words)

if len(hashtag_word) > 140:
    hashtag_word = hashtag_word[:140]

print(hashtag_word)
