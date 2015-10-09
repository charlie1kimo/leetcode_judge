"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
{
    1: None,
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
    0: ' '
}

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
class Solution(object):
    """
    Idea:
        back tracking
    """
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.digits_map = {
            '1': [],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
            '0': [],
        }

        ret = []
        self.combinations(ret, [], digits, 0)
        return ret

    def combinations(self, ret, path, digits, index):
        # base case;
        if index == len(digits):
            if len(path) > 0:
                ret.append("".join(list(path)))
            return

        digit_list = self.digits_map[digits[index]]
        for letter in digit_list:
            path.append(letter)
            self.combinations(ret, path, digits, index+1)
            path.pop()


