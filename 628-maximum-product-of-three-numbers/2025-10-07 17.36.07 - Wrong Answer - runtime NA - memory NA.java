class Solution {
    public int maximumProduct(int[] nums) {
        int s=1;
        for(int i=0;i<nums.length;i++){
            s*=nums[i];
        }
        return s;
    }
}