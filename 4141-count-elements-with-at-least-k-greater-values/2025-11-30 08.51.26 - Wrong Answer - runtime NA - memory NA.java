class Solution {
    public int countElements(int[] nums, int k) {
        int n=nums.length;
        if(k==0) return n;
        if(k>=n) return 0;
        Arrays.sort(nums);
      
        int v=nums[n-k];
        int c=0;
        int i=0;
        while(i<n){
            int val=nums[i];
            int j=i;
            while(j+1<n &&nums[j+1]==val){
                j++;
            }
            int g=n-(j+1);
            if(g>=k){
                c+=(j-1+1);
            }
            i=j+1;
        }
        
        return c;
    }
}