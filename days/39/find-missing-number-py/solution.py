def find_missing_number(arr):
    # [4, 0, 3, 1] ...2

    # sort array with one pass
    idx = 0
    arr_len = len(arr)
    print(arr)
    while idx != arr_len:
        current_value = arr[idx]
        print(idx, current_value)
        if arr[idx] < arr_len and arr[idx] != arr[current_value]:
            arr[idx], arr[current_value] = arr[current_value], arr[idx]
            print(arr)
        else:
            idx += 1

    for idx, num in enumerate(arr):
        if idx != num:
            return idx

    return arr[len(arr) - 1]


def find_duplicate_number(arr):
    # [1, 4, 4, 3, 2] ... 4

    idx = 0
    arr_len = len(arr)
    count = 0
    print(arr)
    while idx != arr_len:

        if arr[idx] != idx + 1:
            current_value = arr[idx] - 1
            if arr[idx] != arr[current_value]:
                arr[idx], arr[current_value] = arr[current_value], arr[idx]
                print(arr)
                count += 1
            else:
                return arr[idx]
        else:
            idx += 1
            count += 1
    print(arr)

#print(find_missing_number([4, 0, 3, 1]))
print(find_duplicate_number([2, 3, 1, 8, 2, 3, 5, 1]))