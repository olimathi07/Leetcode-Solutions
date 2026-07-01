class Solution {
    public int longestSubsequence(int[] nums) {
        int t = 0;
        for (int i : nums) {
            t^= i; 
        }
        if (t== 0) return nums.length - 1; 
        return nums.length;
    }
}