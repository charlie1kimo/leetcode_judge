"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        retval = []
        if len(s) < 4 or len(s) > 12:
            return retval

        self.backtrack(s, 3, retval, "")
        return retval

    def backtrack(self, string, dots, retval, ip):
        if dots == 0:
            if self.is_valid(string):
                ip += string
                retval.append(ip)

            return

        for end_ind in xrange(1, 4):
            s = string[:end_ind]
            if self.is_valid(s):
                self.backtrack(string[end_ind:], dots - 1, retval, ip + s + ".")

    def is_valid(self, string):
        if len(string) == 0 or \
           len(string) > 1 and string[0] == "0" or \
           int(string) > 255:
            return False

        return True
