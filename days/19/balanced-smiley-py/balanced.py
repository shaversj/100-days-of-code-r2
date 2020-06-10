
def balanced_smiles(message: str):
    open_parentheses = []

    for index in range(0, len(message)):
        letter = message[index]
        if letter == "(":
            if index > 0:
                prev_letter = message[index - 1]
                if prev_letter == ":":
                    continue
                else:
                    open_parentheses.append(letter)
            else:
                open_parentheses.append(letter)
        elif letter == ")":
            if index > 0:
                prev_letter = message[index - 1]
                if prev_letter == ":":
                    continue
                else:
                    if len(open_parentheses) is 0 or open_parentheses.pop() != "(":
                        return "NO"
                    else:
                        continue
            else:
                if len(open_parentheses) is 0 or open_parentheses.pop() != "(":
                    return "NO"
                else:
                    continue

    if len(open_parentheses) == 0:
        return "YES"
    else:
        return "NO"
