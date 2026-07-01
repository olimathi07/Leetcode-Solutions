class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int c=nums[0]+nums[1]+nums[2];
        int n=nums.length;
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n-1;j++){
                for(int k=j+1;k<n;k++){
                    int s=nums[i]+nums[j]+nums[k];
                    if(Math.abs(s-target)<Math.abs(c-target)){
                        c=s;
                    }
                }
            }
        }
        return c;
    }
}