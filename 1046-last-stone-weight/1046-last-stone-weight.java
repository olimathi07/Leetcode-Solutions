class Solution {
    public int lastStoneWeight(int[] stones) {
       PriorityQueue<Integer> p=new PriorityQueue<>(Collections.reverseOrder());
       for (int i:stones){
        p.add(i);
       }
       while(p.size()>1){
        int f=p.poll();
        int s=p.poll();
        if(f!=s){
            int r=f-s;
            p.add(r);
        }
       }
       return p.isEmpty()?0:p.peek();

    }
}