"""
 Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1]. 
"""
class Solution(object):
    """
    idea:
        recursion. back tracking
    """
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == None or len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [list(nums)]

        ret_list = []
        perm_list = []
        self.backtrack(ret_list, perm_list, 0, nums)

        return ret_list

    def backtrack(self, ret, perm, index, nums):
        if index == len(nums):
            ret.append(list(perm))
            return

        new_perm = list(perm)
        for j in range(index+1):
            new_perm.insert(j, nums[index])
            self.backtrack(ret, new_perm, index+1, nums)
            new_perm.pop(j)      # remove
