class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        """
        1. sort the array
        2. scan through array iterating 'i'
        3. skip duplicates
        3. two pointers starting at left = i+1 & right = end-1
        4. i > 0 skip (cus sorted)
        5. find i + left + right = 0
        """
        results = []
        nums = sorted(nums)
        for index, val in enumerate(nums):
            if val > 0:
                break

            # skip duplicate
            if index > 0 and val == nums[index-1]:
                continue

            left = index + 1
            right = len(nums) - 1
            while left < right:
                # skip duplicates:
                if left > index+1 and nums[left-1] == nums[left]:
                    left += 1
                    continue

                if val + nums[left] > 0:
                    # already > 0
                    break

                calc = val + nums[left] + nums[right]
                if calc > 0:
                    right -= 1
                elif calc < 0:
                    left += 1
                else:
                    results.append([val, nums[left], nums[right]])
                    right -= 1
                    left += 1

        return results
