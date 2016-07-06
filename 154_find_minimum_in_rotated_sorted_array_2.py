"""
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
"""
class Solution(object):
    """
    Idea:
        - Binary Search, optimal O(log(n))
        - worst case: O(n), need to iterate through duplicates elements
    """
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        if len(nums) == 1 or nums[left] < nums[right]:
            return nums[0]

        while left <= right:
            # skip all duplicate elements
            k = left
            while k <= right and nums[k] == nums[right]:
                k += 1

            # all duplicated to the end
            if k > right:
                return nums[left]

            # perform binary search
            left = k
            if nums[left] < nums[right]:
                return nums[left]

            mid = (left + right) / 2
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
