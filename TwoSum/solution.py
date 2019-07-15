"""
 Write a function that takes in a non-empty array of distinct integers
 representing a target sum. If any two numbers in the input array sum up
 to the target sum, the function should return them in an array, in sorted order.
 If no two numbers sum up to the target sum, the function should return an empty
 array.
 Sample input  : [1,2,3,4,5], 5
 Sample output : [2,3]
 or [1,4]
"""

"""
    Solution 1
    ==========
    Time  complexity O(N^2)
    Space complexity O(1)
    ==========
"""
def twoSum_1(nums, target):
    size = len(nums)
    for i in range(size):
        for j in range(i+1, size):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]
    return []


"""
    Solution 2
    ==========
    Time  complexity O(N)
    Space complexity O(N)
    ==========
"""
def twoSum_2(nums, target):
    hash_map = dict()
    for elm in nums:
        if (target - elm) in hash_map:
            return [target - elm, elm]
        else:
            hash_map[elm] = True
    return []

"""
    Solution 3
    ==========
    Time  complexity O(N log N)
    Space complexity O(1)
    ==========
"""
def twoSum_3(nums, target):
    nums.sort()
    left = 0
    right = len(nums) - 1
    while left < right:
        if nums[left] + nums[right] == target:
            return [nums[left],nums[right]]
        elif nums[left] + nums[right] > target:
            right = right - 1
        else:
            left = left + 1
    return []



# nums = [1,2,3,4]
# target = 5
# print(twoSum_2(nums,target))
