def simple_insertion_sort(arr):
    print(arr)
    for i in range(1, len(arr)):
        while arr[i - 1] > arr[i] and i > 0:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            print(arr)
            i -= 1



arr_1 = [5, 2, 4, 6, 3, 1]
# [2, 4, 5, 6]

simple_insertion_sort(arr_1)