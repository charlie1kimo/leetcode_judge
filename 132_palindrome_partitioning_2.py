"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""


class Solution(object):
    """
    Idea:
        (1) O(n^2) in space:
            - DP: runtime: O(n^2), space: O(n^2)
            - DP array = cut[n] = minimum cuts from substring(0, n)
            - is_palindrome[i][j] = whether substring(i, j) is palindrome
            - i: end_index for substring, j: start_index for substring
            - cut[i] = min(i, cut[j - 1] + 1) for j <= i, if is_palindrome[j][i]
            - if is_palindrome[j][i] = is_palindrome[j+1][i-1] && s[i] == s[j]

        (2) O(n) in space: (optimal)
            - DP: runtime: O(n^2), space: O(n)
            - cut[n] = minimum cuts for palindorme center = n, thus we return cut[n] (not cut[n-1])
            - initialize cut[n] = n-1 (most cuts per center)
            - i: center of palindrome, j: radius of palindrome, j <= i is a must
    """
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        cut = [i - 1 for i in xrange(n + 1)]

        for i in xrange(n):
            # odd palindrome
            for j in xrange(i + 1):
                if i - j < 0 or i + j >= n or s[i - j] != s[i + j]:
                    break

                cut[i + j + 1] = min(cut[i + j + 1], cut[i - j] + 1)

            # even palindrome
            for j in xrange(1, i + 2):
                if i - j + 1 < 0 or i + j >= n or s[i - j + 1] != s[i + j]:
                    break

                cut[i + j + 1] = min(cut[i + j + 1], cut[i - j + 1] + 1)

        return cut[n]

    def minCut_n_square_space(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        cut = [i for i in xrange(length)]
        is_palindrome = [[False for j in xrange(length)] for i in xrange(length)]

        for i in xrange(length):
            for j in xrange(i+1):
                if s[i] == s[j] and (j + 1 > i - 1 or is_palindrome[j + 1][i - 1]):
                    is_palindrome[j][i] = True
                    cut[i] = 0 if j == 0 else min(cut[i], cut[j - 1] + 1)

        return cut[length - 1]
