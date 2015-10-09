"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]
"""
class Solution(object):
    """
    Idea:
        back tracking.
    """
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ret = []
        return self.partition_helper(ret, [], s)

    def partition_helper(self, ret, curr_list, string):
        if len(string) == 0:
            ret.append(curr_list)
            return

        for end in reversed(range(1, len(string)+1)):
            substring = string[:end]
            if self.isPalindrome(substring):
                new_list = list(curr_list)
                new_list.append(substring)
                self.partition_helper(ret, new_list, string[end:])

        return ret

    def isPalindrome(self, string):
        start = 0
        end = len(string)-1

        while start <= end:
            if string[start] != string[end]:
                return False
            start += 1
            end -= 1

        return True
