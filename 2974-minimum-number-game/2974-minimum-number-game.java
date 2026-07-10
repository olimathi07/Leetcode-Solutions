class Solution {
    public int[] numberGame(int[] nums) {
        PriorityQueue<Integer>p=new PriorityQueue<>();
        for(int i:nums){
            p.add(i);
        }
        int[] res=new int[nums.length];
        int i=0;
        while(!p.isEmpty()){
            int alice=p.poll();
            int bob=p.poll();

            res[i++]=bob;
            res[i++]=alice;
        }
        return res;
    }
}