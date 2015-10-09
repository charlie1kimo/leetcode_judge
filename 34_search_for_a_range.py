"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4]. 
"""
class Solution(object):
    """
    Idea:
        two path binary search.
        1) search first occurance equals to target
        2) search last occurance equals to target
    """
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums == None or len(nums) == 0:
            return [-1, -1]

        return [
            self.searchFirst(nums, target),
            self.searchLast(nums, target)
        ]

    def searchFirst(self, nums, target):
        ind = -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

            if nums[mid] == target:
                ind = mid
        return ind

    def searchLast(self, nums, target):
        ind = -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

            if nums[mid] == target:
                ind = mid
        return ind
