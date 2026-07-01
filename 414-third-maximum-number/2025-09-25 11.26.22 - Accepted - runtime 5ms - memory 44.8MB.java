import java.util.*;
class Solution {
    public int thirdMax(int[] nums) {
       TreeSet<Integer> n=new TreeSet<>();
       for(int num:nums){
        n.add(num);
        if(n.size()>3){
            n.pollFirst();
        }
       }if(n.size()==3){
        return n.first();
       }
       return n.last();
    }
}