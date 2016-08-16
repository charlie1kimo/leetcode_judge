"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""


class Solution(object):
    """
    Idea:
        - use a hashmap to store ranges
        - get lower bound with smaller (-1) key
        - get upper bound with larger (+1) key
        - update max range with bounds
        - put all possible ranges in the hashmap
        - store num[i]: num[i], low: up, up: low
    """
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_range = 0
        ranges = dict()
        for num in nums:
            # skip duplicates
            if num in ranges:
                continue

            low = ranges.get(num - 1, num)
            up = ranges.get(num + 1, num)
            max_range = max(up - low + 1, max_range)

            # store all possible range
            ranges[num] = num
            ranges[low] = up
            ranges[up] = low

        return max_range
