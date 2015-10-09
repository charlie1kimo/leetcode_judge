"""
 A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2. 
"""
class Solution(object):
    """
    121212
    1 21212 -> a[1] = 1
    12 1212 -> a[2] = 2 [(1 2), (12)]
    121 212 -> a[3] = a[1] (if 21 <= 26) + a[2] = 3 [(1 2 1), (1 21), (12 1)]
    1212 12 -> a[4] = a[2] (if 12 <= 26) + a[3] = 5 [(1 2 1 2), (1 2 12), (1 21 2), (12 1 2), (12 12)]
    DP solution, equation -> a[n] = a[n-2] if n-2 ~ n <=26 else 0 + a[n-1]
    """
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == None or len(s) == 0:
            return 0
        elif int(s[0]) == 0:
            return 0

        nums = [0 for i in range(len(s)+1)]
        nums[0] = 1                                 # dummpy
        nums[1] = 1 if int(s[0]) > 0 else 0
        for ind in range(2, len(s)+1):
            if int(s[ind-1]) > 0:
                nums[ind] += nums[ind-1]
            if int(s[ind-2:ind]) <= 26 and int(s[ind-2]) > 0:
                nums[ind] += nums[ind-2]

        return nums[len(s)]
