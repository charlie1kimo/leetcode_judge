"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
class Solution(object):
    """
    Idea:
        1. keep a min
        2. sort the arrays
        3. iterate the array through i
        4. for each i, set left = i+1 & right = end-1
        5. scan through left and right to find the closest, update
    """
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        closest = 0
        if nums == None:
            return closest

        closest = sum(nums[:3])
        if len(nums) < 4:
            return closest

        nums = sorted(nums)
        for index in xrange(len(nums)):
            left = index + 1
            right = len(nums) - 1
            while left < right:
                this_sum = nums[index] + nums[left] + nums[right]
                if abs(target - this_sum) < abs(target - closest):
                    closest = this_sum
                    if closest == target:
                        return closest

                if target > this_sum:
                    left += 1
                else:
                    right -= 1

        return closest
