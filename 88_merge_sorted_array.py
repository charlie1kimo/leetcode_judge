"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
The number of elements initialized in nums1 and nums2 are m and n respectively.
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.

        ideas:
            have the space at the end. so fill the biggest number first.
        """
        curr_ind = m + n - 1

        # index
        m -= 1
        n -= 1
        while m >= 0 or n >= 0:
            if m < 0:
                nums1[curr_ind] = nums2[n]
                n -= 1
            elif n < 0:
                nums1[curr_ind] = nums1[m]
                m -= 1
            elif nums1[m] > nums2[n]:
                nums1[curr_ind] = nums1[m]
                m -= 1
            else:
                nums1[curr_ind] = nums2[n]
                n -= 1

            curr_ind -= 1
