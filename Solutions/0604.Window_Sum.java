/*
Description
Given an array of n integers, and a moving window(size k), move the window at each iteration from the start of the array, find the sum of the element inside the window at each moving.

Example
Example 1

Input：array = [1,2,7,8,5], k = 3
Output：[10,17,20]
Explanation：
1 + 2 + 7 = 10
2 + 7 + 8 = 17
7 + 8 + 5 = 20

*/


public class Solution {
    /**
     * @param nums: a list of integers.
     * @param k: length of window.
     * @return: the sum of the element inside the window at each moving.
     */
    public int[] winSum(int[] nums, int k) {
        // write your code here
        if (nums == null || nums.length == 0) {
            return new int[0];
        }
        int n = nums.length;
        int[] sum = new int[n];
        sum[0] = nums[0];
        //计算前缀和
        for (int i = 1; i < n; i++) {
            sum[i] = sum[i-1] + nums[i];
        }
        k--;
        int[] result = new int[n - k];
        result[0] = sum[k];
        for (int i = k; i < n; i++) {
            result[i - k] = sum[i] - sum[i - k] + nums[i - k];
        }
        return result;
    }
}


