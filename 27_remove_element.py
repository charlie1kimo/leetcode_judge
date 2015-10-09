"""
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length. 
"""
class Solution(object):
    """
    idea:
        2 index pointers:
        new_index, points at new ends
        curr_index, walk through the array

        return new_index
    """
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        old_size = len(nums)
        new_index = 0
        for curr_index in range(old_size):
            curr_val = nums[curr_index]
            if curr_val != val:
                nums[new_index] = curr_val
                new_index += 1

        return new_index
