class Solution {
    public int minimumDistance(int[] nums) {
        int n=nums.length;
        int c=0;
        for(int i=0;i<n;i++){
         for(int j=i+1;j<n-1;j++){
          for(int k=j+1;k<n;k++){
              if(nums[i]==nums[j]&&nums[j]==nums[k]&&nums[i]==nums[k]){
                  c=Math.abs(i-j)+Math.abs(j-k)+Math.abs(k-i);
                  
              }
            }
            
            return c;
         }
       }
    
        return -1;
    }
}