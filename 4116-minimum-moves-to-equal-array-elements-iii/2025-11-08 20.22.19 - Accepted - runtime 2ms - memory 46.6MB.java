class Solution {
    public int minMoves(int[] nums) {
        int n=nums.length;
        int max=0;
        for (int i=0;i<n;i++){
            if(max<nums[i]) max=nums[i];
        }
        int c=0;
        for(int i=0;i<n;i++){
            while(nums[i]!=max){
                nums[i]+=1;
                c++;
            }
        }
        return c;
    }
}