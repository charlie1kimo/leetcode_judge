"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""
class Solution(object):
    """
    Idea:
        find sorted half, then do regular binary search.
        if the element is in the unsorted half, then reverse the binary search logic
    """
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == None or len(nums) == 0:
            return -1

        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) / 2

            if target == nums[mid]:
                return mid

            # left part is sorted
            if nums[left] <= nums[mid]:
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1

            # right part is sorted
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

