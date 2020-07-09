def persistence(n):
    product_of_digits = 1
    new_n = n
    multiplicative_persistence = 0

    while len(str(new_n)) != 1:
        for num in str(new_n):
            product_of_digits *= int(num)

        new_n = product_of_digits
        product_of_digits = 1
        multiplicative_persistence += 1

    return multiplicative_persistence

