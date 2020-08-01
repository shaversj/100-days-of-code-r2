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

# print(is_rotation("Hello", "lloHe"))
# print(is_rotation("Basefont", "tBasefon"))


def rotate_left(data, k):
    # [10, 20, 30]
    # rotate to the right by 1: [20, 30, 10]
    l = len(data)
    for i in range(0, k):
        temp = data[0]
        print(i)
        for num in range(0, l - 1):
            #print(num)
            data[num] = data[num + 1]
            print(data)

        data[l - 1] = temp

    return data


print(rotate_left([10, 20, 30], 1))



