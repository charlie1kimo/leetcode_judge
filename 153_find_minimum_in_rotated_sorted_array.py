"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
"""
class Solution(object):
    """
    Idea:
        - Binary search: O(log(n))
        - eliminate half possible search by comparing left most element with mid
        - if left most element smaller than mid, left part is sorted, search right
        - otherwise search left
        - max will be on the left index at the end
    """
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        # length 1 or sorted array
        if len(nums) == 1 or nums[left] < nums[right]:
            return nums[0]

        while left < right:
            mid = (left + right) / 2
            if nums[mid] > nums[left]:
                left = mid
            else:
                right = mid

        return nums[left + 1]
