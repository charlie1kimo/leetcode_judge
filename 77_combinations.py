"""
 Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

"""
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ret = []
        self.combination(1, n, k, [], ret)
        return ret

    def combination(self, start, n, k, array, ret):
        if len(array) == k:
            ret.append(list(array))
            return

        for i in range(start, n+1):
            array.append(i)
            self.combination(i+1, n, k, array, ret)
            array.pop()
