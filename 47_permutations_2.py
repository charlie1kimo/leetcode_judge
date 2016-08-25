"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


class Solution(object):
    """
    Idea:
        - similar to permutation 1, but we skip duplicates.
        - sort the array first, so we can skip the duplicates with the the same
          permutation subset!
        - swap the number from (pos, index)
        - add to result when index reach end
    """
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [list(nums)]

        # sort the array first
        nums.sort()
        ret = []
        perm = []
        self.permute(ret, 0, nums)
        return ret

    def permute(self, ret, index, nums):
        if index >= len(nums):
            row = [nums[i] for i in xrange(len(nums))]
            ret.append(row)
            return

        for i in xrange(index, len(nums)):
            # skip if we have duplicates of current element before i
            skip = False
            for j in xrange(index, i):
                if nums[i] == nums[j]:
                    skip = True
                    break

            if skip:
                continue

            self.swap(nums, index, i)
            self.permute(ret, index + 1, nums)
            # swap back
            self.swap(nums, index, i)

    def swap(self, nums, i, j):
        if i == j:
            return

        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
