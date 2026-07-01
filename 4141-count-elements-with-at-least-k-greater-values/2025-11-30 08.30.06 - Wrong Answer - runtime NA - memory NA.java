class Solution {
    public int countElements(int[] nums, int k) {
        int n=nums.length;
        int c=0;
        if(n>k){
            for(int i=0;i<nums.length;i++){
                if(nums[i]>k) c++;
            }
        }
        return c;
    }
}