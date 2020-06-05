def zip_practice():
    for num1, num2 in zip(range(0, 10), range(11, 20)):
        print(num1, num2)


def num_dash_insert(nums):
    nums_list = list(str(nums))
    final_nums_list = []

    for index in range(0, len(str(nums)) - 1):
        final_nums_list.append(nums_list[index])
        if is_even(int(nums_list[index])) and is_even(int(nums_list[index + 1])):
            final_nums_list.append("*")
        elif is_even(int(nums_list[index])) is False and is_even(int(nums_list[index + 1])) is False:
            final_nums_list.append("-")

    final_nums_list.append(nums_list[len(nums_list) - 1])

    print(final_nums_list)

    return "".join(final_nums_list)


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
