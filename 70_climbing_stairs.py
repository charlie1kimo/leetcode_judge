"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? 

idea:
ways[0] = 0
ways[1] = 1
ways[2] = 2
ways[3] = ways[1] + ways[2] = 3 [ (1,1,1), (1, 2), (2, 1) ]
ways[4] = ways[2] + ways[3] = 5 [ (1,1,1,1), (1,1,2), (1,2,1), (2,1,1), (2,2) ]
...
ways[n] = ways[n-2] + ways[n-1]
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        ways = [0 for i in range(n+1)]
        ways[0] = 0
        ways[1] = 1
        ways[2] = 2
        for stair_num in range(3, n+1):
            ways[stair_num] = ways[stair_num-2] + ways[stair_num-1]

        return ways[n]
