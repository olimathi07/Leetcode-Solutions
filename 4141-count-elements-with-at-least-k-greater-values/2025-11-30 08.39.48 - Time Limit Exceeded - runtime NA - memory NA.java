class Solution {
    public int countElements(int[] nums, int k) {
        int n=nums.length;
        int c=0;
       for(int i=0;i<n;i++){
           int t=0;
           for(int j=0;j<n;j++){
               if(nums[j]>nums[i]) t++;
           }
           if(t>=k)c++;
       }
        return c;
    }
}