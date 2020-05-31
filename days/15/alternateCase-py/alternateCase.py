

def alternate_case(words):
    raise_next_letter = True
    result = []
    if len(words) == 0:
        return ""

    for letter in words:
        if letter.isalpha():
            if raise_next_letter:
                result.append(letter.upper())
                raise_next_letter = False
            else:
                result.append(letter.lower())
                raise_next_letter = True
        else:
            result.append(letter)

    return "".join(result)
