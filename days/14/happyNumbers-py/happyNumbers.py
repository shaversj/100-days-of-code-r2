def is_happy_number(n):
    fast = 0
    slow = 0
    fast_num = n
    slow_num = n

    while fast != 1:
        print(f"fast_num = {fast_num}, slow_num = {slow_num}")
        fast = sum_square_of_digits(sum_square_of_digits(fast_num))
        fast_num = fast
        slow = sum_square_of_digits(slow_num)
        slow_num = slow
        if fast_num == slow_num:
            print("cycle")
            return False

    return True


def sum_square_of_digits(number):
    sum_of_squares = 0

    for num in str(number):
        sum_of_squares += int(num) * int(num)

    return sum_of_squares
