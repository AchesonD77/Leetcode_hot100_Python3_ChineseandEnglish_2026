class Solution:
    def twoSum(self, nums, target):
        num_dict = {} # hashmap
        for i, num in enumerate(nums):
            wewant = target - num 
            if wewant in num_dict:
                return [num_dict[wewant], i]
            num_dict[num] = i