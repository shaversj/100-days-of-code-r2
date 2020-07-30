def find_missing_number(nums):
    # TODO: Write your code here

    idx = 0
    while idx != len(nums):
        j = nums[idx]
        if nums[idx] < len(nums) and nums[idx] != nums[j]:
            nums[idx], nums[j] = nums[j], nums[idx]
        else:
            idx += 1

    # i, n = 0, len(nums)
    # while i < n:
    #     j = nums[i]
    #     if nums[i] < n and nums[i] != nums[j]:
    #         nums[i], nums[j] = nums[j], nums[i]  # swap
    #     else:
    #         i += 1

    print(nums)
    for i in range(len(nums)):
        if nums[i] != i:
            return i


    return nums


#print(find_missing_number([4, 0, 3, 1]))
print(find_missing_number([2, 0, 4, 1]))