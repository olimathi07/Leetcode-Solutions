class Solution {
    public int findNumbers(int[] nums) {
        int c=0;
        for(int i=0;i<nums.length;i++){
            int n=nums[i];
            int ct=0;
         while(n>0){
            ct++;
            n/=10;
            }if(ct%2==0){
                c++;
            }
        }
        return c;
        
    }
}