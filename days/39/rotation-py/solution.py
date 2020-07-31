def is_rotation(word, rotated_word):
    from collections import deque
    d = deque(word)
    count = 0

    while count != len(word):
        d.rotate(1)
        print(d)
        if "".join(d) == rotated_word:
            return True
        else:
            count += 1

    return False

print(is_rotation("Hello", "lloHe"))
print(is_rotation("Basefont", "tBasefon"))