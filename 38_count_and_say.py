"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string. 
"""
class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        if n == 0:
            return ""

        result = "1"
        n -= 1
        while n > 0:
            temp_saying = ""
            index = 0
            while index < len(result):
                count = 1
                while index + 1 < len(result) and result[index] == result[index+1]:
                    index += 1
                    count += 1

                temp_saying += str(count) + result[index]
                index += 1

            result = temp_saying
            n -= 1

        return result


if __name__ == "__main__":
    sol = Solution()
    print sol.countAndSay(1)
    print sol.countAndSay(2)
    print sol.countAndSay(3)
    print sol.countAndSay(4)
    print sol.countAndSay(5)
    print sol.countAndSay(6)
