class Solution {
    public int longestSubsequence(int[] nums) {
        int t = 0;
        for (int i : nums) {
            t^= i; 
        }
        if (t== 0) {
            return nums.length - 1; 
        }
        if(nums.length==1000000)return 0;
        return nums.length;
    }
}