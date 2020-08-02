def find_mth_to_last_element(arr, k):

    # for num in range(-1, -k - 1, -1):
    #     print(num)
    return arr[-k]


print(find_mth_to_last_element(["a", "b", "c", "d"], 4) == "a")
print(find_mth_to_last_element(["e", "f", "g", "h"], 2) == "g")