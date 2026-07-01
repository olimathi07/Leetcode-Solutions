class Solution {
    public int maximizeExpressionOfThree(int[] nums) {
        int m1=Integer.MIN_VALUE;
        int m2=Integer.MIN_VALUE;
        int m3=Integer.MAX_VALUE;
        int n=nums.length;
        for(int i:nums){
            if(i>m1){
                m2=m1;
                m1=i;
            }else if(i>m2){
                m2=i;
            }
            if(i<m3)
                m3=i;
        }
       
        return m1+m2-m3;
    }
}