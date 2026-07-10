class Solution {
    public int maxProduct(int[] nums) {
        PriorityQueue<Integer>p=new PriorityQueue<>(Collections.reverseOrder());
        for(int i:nums){
            p.offer(i);
        }
        int frst=p.poll();
        int sec=p.poll();
        return (frst-1) *(sec-1);  
 }
}