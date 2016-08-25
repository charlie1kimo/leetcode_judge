"""
Given a collection of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""


class Solution(object):
    """
    Idea:
        - backtracing
    """
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if candidates is None or len(candidates) == 0 or target == 0:
            return []

        ret = []
        candidates.sort()
        self.combinationSum2_helper(candidates, target, 0, [], ret)
        return ret

    def combinationSum2_helper(self, candidates, target, ind, curr, ret):
        skip_duplicates = False

        # base case, found
        if target == 0:
            ret.append(list(curr))
            return

        for i in xrange(ind, len(candidates)):
            # skip duplicates
            if i > 0 and candidates[i] == candidates[i - 1] and skip_duplicates:
                continue

            skip_duplicates = False
            new_target = target - candidates[i]
            if new_target >= 0:
                curr.append(candidates[i])
                self.combinationSum2_helper(candidates, new_target, i + 1, curr, ret)
                curr.pop()
            else:
                break

            if i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                skip_duplicates = True
