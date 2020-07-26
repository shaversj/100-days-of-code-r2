def array_diff(a, b):
    if not b:
        return a

    for num in b:
        for occurrence in range(0, a.count(num)):
            a.remove(num)

    return a
