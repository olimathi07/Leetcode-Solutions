class Solution {
    public int thirdMax(int[] nums) {
       int n=nums.length;
       int f=Integer.MIN_VALUE;
       for(int i=0;i<n;i++){
        if(nums[i]>f){
            f=nums[i];
        }
       }
         int s=Integer.MIN_VALUE;
       for(int i=0;i<n;i++){
        if(nums[i]>s&&nums[i]<f){
            s=nums[i];
        }
       }
         int t=Integer.MIN_VALUE;
       for(int i=0;i<n;i++){
        if(nums[i]<s&&nums[i]>t){
            t=nums[i];
        }
       }
       if(n==2) return f;
       if(n==3) return t;
       return t;
       
    }
}