nums = [2, 3, 6, 1, 9, 8]
nums_len = len(nums)

for i in range(nums_len):
    min_val = 100000000
    i_min = -1
    for j in range(i, nums_len):
        if nums[j] < min_val:
            min_val = nums[j]
            i_min = j
    temp = nums[i]
    nums[i] = nums[i_min]
    nums[i_min] = temp

print(nums)
