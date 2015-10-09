"""
 Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:

    All numbers (including target) will be positive integers.
    Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
    The solution set must not contain duplicate combinations.

For example, given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3]
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if candidates == None or len(candidates) == 0:
            return []

        # sort candidates if not yet
        candidates.sort()

        ret = []
        self.dfs(candidates, target, 0, ret, [])

        return ret

    def dfs(self, candidates, target, pos, ret, combinations):
        # base case 1: found a combination
        if target == 0:
            ret.append(list(combinations))
            return

        for i in range(pos, len(candidates)):
            c = candidates[i]
            new_target = target - c

            # only start from i - improved backtracking.
            if new_target >= 0:
                combinations.append(c)
                self.dfs(candidates, new_target, i, ret, combinations)
                combinations.pop()
