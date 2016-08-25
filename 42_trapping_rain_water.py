"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


                     __
         __         |  |__    __
   __   |  |__    __|  |  |__|  |__
__|__|__|__|__|__|__|__|__|__|__|__|

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
"""


class Solution(object):
    """
    Iead:
        - O(n^2) try:
            - two pointers, start and end
            - initialize start and end to first non-zero index
            - skip the end until end height > start
            - calculate the water block by block from start to end
            - move start to end and continue.
            - if end > len, then don't count water (flow out), start++, and search
        - O(n) try:
            - two pointers, left = 0, right = len - 1
            - calculate all area, and block area as left++ or right--
            - keep track of currLevel
            - iterate through left & right, level = min(A[left], A[right])
            - if level > curr_level, then update all_area & curr_level
            - move lower (left or right) pointer toward center
    """
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height is None or len(height) == 0:
            return 0

        left = 0
        right = len(height) - 1
        curr_level = 0
        all_area = 0
        block = 0

        while left <= right:    # <= including last block
            level = min(height[left], height[right])
            if level > curr_level:
                all_area += (level - curr_level) * (right - left + 1)
                curr_level = level

            if height[left] < height[right]:
                block += height[left]
                left += 1
            else:
                block += height[right]
                right -= 1

        return all_area - block
