def delete_nth(order, max_e):
    new_list = []

    for num in order:
        if new_list.count(num) < max_e:
            new_list.append(num)
        else:
            pass

    return new_list
