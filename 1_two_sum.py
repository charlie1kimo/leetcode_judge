"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
UPDATE (2016/2/13):
The return format had been changed to zero-based indices. Please read the above updated description carefully.
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        index_map = dict()
        for index, num in enumerate(nums):
            curr_list = index_map.setdefault(num, [])
            curr_list.append(index)
        
        for index, num in enumerate(nums):
            complement = target - num
            if index_map.has_key(complement):
                index1 = index
                index2 = None
                for index_choice in index_map[complement]:
                    if index_choice > index1:
                        index2 = index_choice
                        
                if index2 != None:
                    return index1+1, index2+1