"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
"""
class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        """
        area as the square area.
        greedy approach with 2 pointers.
        """
        start_ind = 0
        end_ind = len(height)-1

        max_area = 0
        while start_ind < end_ind:
            area = (end_ind - start_ind) * min(height[start_ind], height[end_ind])
            if area > max_area:
                max_area = area

            if height[start_ind] < height[end_ind]:
                start_ind += 1
            else:
                end_ind -= 1

        return max_area
