class Solution {
    public int distributeCandies(int[] candyType) {
        Set<Integer> h=new HashSet<>();
        for(int n:candyType){
            h.add(n);
        }
      int n=candyType.length/2;
      if(n>=h.size()){
        return h.size();
      }
      else{
      return n;
      }
    }
}