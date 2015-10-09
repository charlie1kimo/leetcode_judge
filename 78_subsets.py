"""
 Given a set of distinct integers, nums, return all possible subsets.

Note:

    Elements in a subset must be in non-descending order.
    The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = [[]]
        nums.sort()
        self.get_subsets(0, nums, [], ret)
        return ret

    def get_subsets(self, start_ind, nums, array, ret):
      if start_ind >= len(nums):
        return

      for ind in range(start_ind, len(nums)):
        val = nums[ind]
        array.append(val)
        ret.append(list(array))
        self.get_subsets(ind+1, nums, array, ret)
        array.pop()
