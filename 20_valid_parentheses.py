"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""
class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        stack_parentheses = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack_parentheses.append(char)

            elif char == ')':
                pop = stack_parentheses.pop() if len(stack_parentheses) > 0 else None
                if pop != '(':
                    return False
            elif char == ']':
                pop = stack_parentheses.pop() if len(stack_parentheses) > 0 else None
                if pop != '[':
                    return False
            elif char == '}':
                pop = stack_parentheses.pop() if len(stack_parentheses) > 0 else None
                if pop != '{':
                    return False

        if len(stack_parentheses) > 0:
            return False
        else:
            return True
