class Solution {
    public boolean canPartition(int[] nums) {
        
        int s=0;
        for(int i=0;i<nums.length;i++){
             s+=nums[i];
        }
        if (s%2==0){
            return true;
        }
        
        return false;
    }
}