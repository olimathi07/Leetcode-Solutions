class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int s=0;
        int j=0;
        int m=Integer.MAX_VALUE;
        for(int i=0;i<nums.length;i++){
                s+=nums[i];
                while(target<=s){
                    m=Math.min(m,i-j+1);
                    s-=nums[j];
                    j++;
                }
            
        }
        return m ==Integer.MAX_VALUE?0:m;
    }
}