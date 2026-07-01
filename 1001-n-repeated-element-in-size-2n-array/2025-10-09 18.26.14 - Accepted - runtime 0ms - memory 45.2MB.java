class Solution {
    public int repeatedNTimes(int[] nums) {
       HashSet<Integer> h=new HashSet<>();
       for(int i:nums)
       {if(!h.add(i)) return i;}

        return 0;
    }
}