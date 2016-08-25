"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""


class Solution(object):
    """
    Idea:
        - Binary Search
        - exit search: return l
    """
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or target is None:
            return -1

        l = 0
        r = len(nums)
        while l < r:
            mid = (l + r) / 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                r = mid
            else:
                l = mid + 1

        return l
