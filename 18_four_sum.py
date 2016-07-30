"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
class Solution(object):
    """
    Idea:
        reduce 4sum to 3sum using one extra loop
    """
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        if nums == None or len(nums) < 4:
            return ret

        nums = sorted(nums)
        for i in xrange(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                # skip duplicate
                continue

            for j in xrange(i+1, len(nums)-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue

                # 2 sums
                new_target = target - nums[i] - nums[j]
                left = j + 1
                right = len(nums) - 1

                while left < right:
                    if left > j + 1 and nums[left] == nums[left-1]:
                        # skip duplicate
                        left += 1
                        continue
                    if right < len(nums) - 1 and nums[right] == nums[right+1]:
                        # skip duplicate
                        right -= 1
                        continue

                    two_sum = nums[left] + nums[right]
                    if two_sum < new_target:
                        left += 1
                    elif two_sum > new_target:
                        right -= 1
                    else:
                        # found a set
                        ret.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

        return ret
