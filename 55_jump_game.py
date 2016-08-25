"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""


class Solution(object):
    """
    Idea:
        (1) Time: O(n^2), Space: O(n):
            - DP:
            - 1D boolean array to determine if it's reachable
            - a[n] = true if:
                a[n - 1] && nums[n - 1] >= 1 or
                a[n - 2] && nums[n - 2] >= 2 or ...
                ...
                a[0] && nums[0] >= n
            - bulid from top down (from 0 ~ n)
        (2) Time: O(n), Space: O(1):
            - DP
            - traverse through 2nd elements to the 2nd to the last
            - keep track of max_jump, max_jump = A[0]
            *** max_jump @ i = max(max_jump - 1, A[i]) ***
            if max_jump == 0, return false (we cannot reach)
    """
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None or len(nums) == 0:
            return False

        if len(nums) == 1:
            return True

        if nums[0] == 0:
            return False

        max_jump = nums[0]
        for i in xrange(1, len(nums) - 1):
            max_jump = max(max_jump - 1, nums[i])

            if max_jump == 0:
                return False

        return True

    def canJump_n_sqaure(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None or len(nums) == 0:
            return False

        a = [False for i in xrange(len(nums))]
        a[0] = True
        for i in xrange(len(nums)):
            if a[i]:
                for j in xrange(1, nums[i] + 1):
                    if i + j < len(nums):
                        a[i + j] = True

        return a[len(nums) - 1]
