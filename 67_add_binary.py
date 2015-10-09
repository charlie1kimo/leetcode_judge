"""
 Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100". 
"""
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        length = len(a) if len(a) > len(b) else len(b)
        array = []
        carry_over = 0
        for ind in range(1, length+1):
            a_ind = len(a) - ind
            b_ind = len(b) - ind
            if a_ind < 0:
                val = int(b[b_ind]) + carry_over
            elif b_ind < 0:
                val = int(a[a_ind]) + carry_over
            else:
                val = int(a[a_ind]) + int(b[b_ind]) + carry_over

            if val > 1:
                val %= 2
                carry_over = 1
            else:
                carry_over = 0

            array.insert(0, str(val))

        if carry_over > 0:
            array.insert(0, str(carry_over))

        return "".join(array)
