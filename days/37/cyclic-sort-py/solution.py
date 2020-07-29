def cyclic_sort(nums):
    # TODO: Write your code here

    idx = 0
    count = 0
    while count != len(nums):
        if nums[idx] != nums[nums[idx] - 1]:
            new_num = nums[nums[idx] - 1]
            nums[nums[idx] - 1] = nums[idx]
            nums[idx] = new_num

        else:
            idx += 1

        count += 1

    return nums

# Input: [3, 1, 5, 4, 2]
# Output: [1, 2, 3, 4, 5]

print(cyclic_sort([3, 1, 5, 4, 2]))
print(cyclic_sort([2, 6, 4, 3, 1, 5]))