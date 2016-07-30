/*
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
*/
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        if (nums == null || nums.length < 4) {
            return ret;
        }
        Arrays.sort(nums);

        for (int i = 0; i < nums.length - 3; i++) {
            if (i > 0 && nums[i] == nums[i-1]) continue;    // skip duplicates
            for (int j = i + 1; j < nums.length - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j-1]) continue;    // skip duplicates

                // 2 sum
                int newTarget = target - nums[i] - nums[j];
                int l = j + 1;
                int r = nums.length - 1;
                while (l < r) {
                    if (l > j + 1 && nums[l] == nums[l-1]) {
                        l++;
                        continue;
                    }
                    if (r < nums.length - 1 && nums[r] == nums[r+1]) {
                        r--;
                        continue;
                    }
                    int twoSum = nums[l] + nums[r];
                    if (twoSum < newTarget) {
                        l++;
                    }
                    else if (twoSum > newTarget) {
                        r--;
                    }
                    else {
                        ret.add(new ArrayList<Integer>(Arrays.asList(nums[i], nums[j], nums[l], nums[r])));
                        l++;
                        r--;
                    }
                }
            }
        }
        return ret;
    }
}