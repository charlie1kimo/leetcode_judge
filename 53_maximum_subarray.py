"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
"""
class Solution(object):
    """
    Idea:
        - Kadane's algorithm
        - DP
    """
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_end_here = nums[0]
        max_so_far = nums[0]
        for num in nums[1:]:
            max_end_here = max(num, max_end_here + num)
            max_so_far = max(max_end_here, max_so_far)

        return max_so_far
