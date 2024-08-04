import codecs


def delete_html_tags(html_file: str, result_file: str = 'cleaned.txt') -> None:

    with codecs.open(html_file, 'r', 'utf-8') as file:
        html_code = file.read()

    cleaned_text = []
    tag = False

    for char in html_code:
        if char == '<':
            tag = True
        elif char == '>':
            tag = False
        elif not tag:
            cleaned_text.append(char)

    cleaned_text = ''.join(cleaned_text)
    cleaned_text = '\n'.join(line.lstrip() for line in cleaned_text.splitlines() if line.strip())

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(cleaned_text)


delete_html_tags('draft.html', 'cleaned.txt')
