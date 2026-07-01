class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        int s=1;
        int c=0;
        for(int i=0;i<nums.length;i++){
            s=1;
            for(int j=i;j<nums.length;j++){
                s*=nums[j];
                if(s > k){
                    break;
                }
                if(k > s){
                   c++;
                }
                
            }
            
        }
        return c;
    }
}