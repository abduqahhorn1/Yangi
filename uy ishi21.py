def two_sum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return []

nums = [2, 7, 11, 15]
target = 9
output1 = two_sum(nums, target)
nums = [3, 2, 4]
target = 6
output2 = two_sum(nums, target)
nums = [3, 3]
target = 6
output3 = two_sum(nums, target)
print(output1,output2,output3)  