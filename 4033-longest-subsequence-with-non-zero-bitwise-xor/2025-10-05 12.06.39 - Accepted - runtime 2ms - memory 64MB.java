class Solution {
    public int longestSubsequence(int[] nums) {
        int t = 0;
        boolean a=true;
        for (int i : nums) {
            t^= i; 
            if(i!=0)  a=false;
        }
        if(a) return 0;
        if (t== 0) return nums.length - 1; 
        return nums.length;
    }
}