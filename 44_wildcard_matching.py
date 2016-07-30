"""
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
"""
class Solution(object):
    """
    Idea:
        - Greedy. 4 pointers
        - Two pointers s & p (index of string & pattern)
        - Two pointers for last_asteroid & last_match (for asteroid consumption)
    """
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s is None and p is None:
            return True
        if s is None or p is None:
            return False

        s_ind = p_ind = match_ind = 0
        asteroid_ind = -1

        while s_ind < len(s):
            if p_ind < len(p) and (p[p_ind] == '?' or s[s_ind] == p[p_ind]):
                # regular match (including '?'), increment both pointers
                s_ind += 1
                p_ind += 1
            elif p_ind < len(p) and p[p_ind] == '*':
                # save asteroid index
                asteroid_ind = p_ind
                # save current string index
                match_ind = s_ind
                # only move forward pattern pointer
                p_ind += 1
            elif asteroid_ind != -1:
                # move pattern index to 1 behind last '*'
                p_ind = asteroid_ind + 1
                # move the match index and string index 1 further to test more.
                match_ind += 1
                s_ind = match_ind
            else:
                # don't match, return false
                return False

        # check the remaining pattern, can only be asteroid
        while p_ind < len(p) and p[p_ind] == '*':
            p_ind += 1

        # return True if no remaining, False otherwise.
        return p_ind == len(p)
