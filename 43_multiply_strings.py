"""
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
"""
class Solution(object):
    """
    Idea:
        elementary school math
        1 2 3
    x   4 5 6
    -----------
        7 3 8
      6 1 5
    4 9 2
    +
    -----------
    5 6 0 8 8

    use integer array to store the result then convert to str
    """
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)

        result_array = [0 for i in range(m + n)]

        # build result_array reversely
        for i in reversed(range(len(num1))):
            for j in reversed(range(len(num2))):
                result_array[m + n - i - j - 2] += int(num1[i]) * int(num2[j])
                result_array[m + n - i - j - 1] += result_array[m + n - i -j - 2] / 10
                result_array[m + n - i -j - 2] %= 10

        # build the string from the end
        result_str_array = []
        for i in reversed(range(len(result_array))):
            if result_array[i] > 0:
                for j in reversed(range(i+1)):
                    result_str_array.append(str(result_array[j]))
                return "".join(result_str_array)
