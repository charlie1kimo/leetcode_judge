"""
Given a string S, find the longest palindromic substring in S. 
You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
"""
import re


class Solution:
    """
    (1) Using Manacher's algorithm.
        - Run time: O(n), Space: O(n)
            http://articles.leetcode.com/2011/11/longest-palindromic-substring-part-i.html
            http://articles.leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
    (2) odd-even extend palindrome.
        - Run time: O(n^2)
    """
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if l < 2:
            return s

        self.low = 0
        self.max_len = 0
        for i in xrange(l - 1):
            # odd length
            self.extendPalindrome(s, i, i)
            # even length
            self.extendPalindrome(s, i, i + 1)

        return s[self.low:self.low + self.max_len]

    def extendPalindrome(self, s, j, k):
        while j >= 0 and k < len(s) and s[j] == s[k]:
            j -= 1
            k += 1

        # count the length, start_ind = j+1, end_ind = k-1
        if self.max_len < (k - 1) - (j + 1) + 1:
            self.low = j + 1
            self.max_len = (k - 1) - (j + 1) + 1

    def longestPalindrome_manacher(self, s):
        # @param {string} s
        # @return {string}
        string = self.preprocess(s)
        center = 0
        right = 0
        P = [0 for i in range(len(string))]         # longest palindrome at index 'i' array
        for i in range(2, len(string)-2):
            if i > right:
                P[i] = 0
            else:
                i_mirror = center - (i - center)
                P[i] = min(P[i_mirror], right - i)
                # symmetry, P[i] = P[i_mirror] if (right - i) > P[i], still in symmetry range.
                # otherwise P[i] >= (right - i)
            
            # extend the palindrome as far as possible
            while string[i + 1 + P[i]] == string[i - 1 - P[i]]:
                P[i] += 1
            
            # move the center if i > right (i passed right)
            if i > right:
                center = i
                right = i + P[i]
        
        # find the longest palindrome in P[i] array
        max_ind = 0
        for ind, val in enumerate(P):
            if val > P[max_ind]:
                max_ind = ind
        max_palindrome = string[max_ind-P[max_ind]:max_ind+P[max_ind]+1]
        max_palindrome = re.sub("#", "", max_palindrome)
        return max_palindrome
    
    def preprocess(self, s):
        """
        return ex. "^#a#b#b#a#$"
        """
        string = "^#"
        for char in s:
            string += char + "#"
        string += "$"
        return string
