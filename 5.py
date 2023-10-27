def append_nums():
    nums = []
    for i in range(2, 101, 2):
        nums.append(i)
    return nums
nums = append_nums()
print(nums)