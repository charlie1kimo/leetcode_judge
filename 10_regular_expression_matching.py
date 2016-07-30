"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true

"""
class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        """
        DP soluiton
        mat[i][j] = True if string 's' up i-th index matches pattern 'p' j-th index
        - 4 cases:
            1. mat[i][j] = mat[i-1][j-1] && s[i] == p[j]
            2. mat[i][j] = mat[i-1][j] (a ) if p[j] == '*'
            3. mat[i][j] = mat[i][j-1] ( *) if p[j] == '*'
            4. mat[i][j] = mat[i][j-2] (a*) if p[j] == '*'
        """
        mat = [[False for j in range(len(p)+1)] for i in range(len(s)+1)]
        mat[0][0] = True
        for j in range(1, len(p)+1):
            if p[j-1] == '*':           # same as previous 2 pattern character
                mat[0][j] = mat[0][j-2]
            else:
                mat[0][j] = False

        # DP
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    # case 1
                    mat[i][j] = mat[i-1][j-1]
                elif p[j-1] == '*':
                    # case 2, 3, 4
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        mat[i][j] = mat[i-1][j] or mat[i][j-1] or mat[i][j-2]
                    else:
                        # match 0 chars
                        mat[i][j] = mat[i][j-2]
                else:
                    # simply don't match
                    mat[i][j] = False

        return mat[len(s)][len(p)]


if __name__ == "__main__":
    s = Solution()
    assert s.isMatch("aa","a") == False
    assert s.isMatch("aa","aa") == True
    assert s.isMatch("aaa","aa") == False
    assert s.isMatch("aa", "a*") == True
    assert s.isMatch("aa", ".*") == True
    assert s.isMatch("ab", ".*") == True
    assert s.isMatch("aab", "c*a*b") == True
    assert s.isMatch("aaa", "aaaa") == False
    assert s.isMatch("ab", ".*c") == False
    assert s.isMatch("c", ".*c") == True
    assert s.isMatch("abc", ".*c") == True
    assert s.isMatch("aaa", "a.a") == True
    assert s.isMatch("aaa", "a*a") == True
    assert s.isMatch("aaa", "ab*a*c*a") == True
    assert s.isMatch("abcd", "d*") == False

