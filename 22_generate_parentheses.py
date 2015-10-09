"""
 Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()" 
"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]

        idea:
            DP (Dynamic Programming)
            two choices of parenthesis:
                1. open: "(" DP[n-1] ")"
                2. close: DP[i] + DP[n-i] for i in [1, ..., n-1]
        """
        # DP
        array_len = max(1, n)
        array = [set() for i in range(array_len+1)]
        array[1] = set(["()"])

        for i in range(2, n+1):
            # 1. open
            for mid in array[i-1]:
                array[i].add( "(" + mid + ")" )

            # 2. close
            for j in range(1, i):
                for head in array[j]:
                    for tail in array[i-j]:
                        array[i].add( head + tail )

        return list(array[n])

if __name__ == "__main__":
    sol = Solution()
    res_3 = sol.generateParenthesis(3)
    print res_3

