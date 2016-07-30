"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""
class Solution:
    """
    Idea:
        - merge sort idea, compare both curr_ind for nums1 & nums2 and iterate
    """
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        total_len = len(nums1) + len(nums2)
        mid_ind = total_len / 2
        ind_1 = ind_2 = 0
        
        if len(nums1) == 0 and len(nums2) == 1:
            return nums2[0]
        elif len(nums1) == 1 and len(nums2) == 0:
            return nums1[0]
        
        if len(nums1) == 0:
            previous_num = nums2[len(nums2)/2-1]
            median = nums2[len(nums2)/2]
            if len(nums2) % 2 == 0:
                median = (previous_num + median)/2.0
            return median
        elif len(nums2) == 0:
            previous_num = nums1[len(nums1)/2-1]
            median = nums1[len(nums1)/2]
            if len(nums1) % 2 == 0:
                median = (previous_num + median)/2.0
            return median
        
        curr_ind = 0
        while curr_ind <= mid_ind:
            if ind_2 >= len(nums2) or (ind_1 < len(nums1) and nums1[ind_1] <= nums2[ind_2]):
                if curr_ind + 1 == mid_ind:
                    previous_num = nums1[ind_1]
                if curr_ind == mid_ind:
                    median = nums1[ind_1]
                ind_1 += 1
            else:
                if curr_ind + 1 == mid_ind:
                    previous_num = nums2[ind_2]
                if curr_ind == mid_ind:
                    median = nums2[ind_2]
                ind_2 += 1
            curr_ind += 1

        # even length
        if total_len % 2 == 0:
            median = (previous_num + median) / 2.0
        
        return median
