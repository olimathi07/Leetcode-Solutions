class Solution {
    public int sumOfUnique(int[] nums) {
        int[] c=new int[100];
        for(int i=0;i<nums.length;i++){
            c[nums[i]]++;
        }
        int s=0;
        for(int i=0;i<nums.length;i++){
            if(c[nums[i]]==1){
                s+=nums[i];
            }
        }
        return s;
    }
}