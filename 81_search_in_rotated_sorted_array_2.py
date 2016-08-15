"""
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
"""


class Solution(object):
    """
    Idea:
        similar to 33.search_in_rotated_sorted_array
        but need to check and iterate through duplicates
    """
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if nums is None and len(nums) == 0:
            return False

        left = 0
        right = len(nums) - 1
        while left <= right:
            duplicated = False
            mid = (left + right) / 2

            if nums[mid] == target:
                return True

            # iterate through duplicates, b/c we cannot be sure about whether:
            # (1) there are all duplicates between left & right
            # (2) there's something other than duplicates between left & right
            if nums[mid] == nums[left] and nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[mid] == nums[left]:
                left = mid + 1
            elif nums[mid] == nums[right]:
                right = mid

            # left part is sorted
            elif nums[mid] > nums[left]:
                if nums[mid] >= target and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            # right part is sorted
            elif nums[mid] < nums[left]:
                if nums[mid] <= target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False
