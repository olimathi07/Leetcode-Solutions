class Solution {
    public boolean stoneGame(int[] piles) {
      int s=0;
      for(int i=0;i<piles.length;i++){
        s+=piles[i];
      }  
      if(s%2==0) return false;
      return true;
    }
}