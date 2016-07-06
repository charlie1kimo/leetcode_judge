"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_now = nums[0]
        min_now = nums[0]
        ret = max_now

        for n in nums[1:]:
            pre_max = max_now
            pre_min = min_now
            max_now = max(max(n, pre_max * n), pre_min * n)
            min_now = min(min(n, pre_max * n), pre_min * n)
            ret = max(ret, max_now)

        return ret
