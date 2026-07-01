class Solution {
    public int countElements(int[] nums, int k) {
        int n=nums.length;
        if(k==0) return n;
        if(k>=n) return 0;
        Arrays.sort(nums);
        int t=n-k-1;
        int v=nums[t];
        int c=0;
        for (int num:nums){
            if(num<v)c++;
        }
       
        return c;
    }
}