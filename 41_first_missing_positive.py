"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""


class Solution(object):
    """
    Idea:
        (1) Only works with no duplicates in the array:
            - Run time: O(n), Space: O(1)
            - keep track of:
                - (1) # of positive number
                - (2) sum of all positive number
            - calculate sum_all from [1, ..., # of positive number]
            - return sum_all - sum_positive
        (2) in-place swapping & use length of array:
            - notice there can only be (length - 1) positive integers
            - in-place swapping makes the duplicates (at most 1) skipped.
            - after O(n) iteration, the array should be [1, 2, ..., n]
            - scan through array to find missing one or A[n] + 1

    """
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 1

        n = len(nums)
        for i in xrange(n):
            num = nums[i]
            while num <= n and num > 0 and nums[num - 1] != num:
                # swap
                nums[i] = nums[num - 1]
                nums[num - 1] = num
                num = nums[i]

        for i in xrange(n):
            if nums[i] != i + 1:
                return i + 1

        return nums[n-1] + 1

    def firstMissingPositive_no_duplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return 0

        length = 0
        sum_positive = 0
        for i in xrange(len(nums)):
            if nums[i] > 0:
                length += 1
                sum_positive += nums[i]

        sum_all = sum([i for i in xrange(1, length+2)])
        return sum_all - sum_positive
