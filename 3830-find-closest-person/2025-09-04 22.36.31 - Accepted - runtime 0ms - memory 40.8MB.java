class Solution {
    public int findClosest(int x, int y, int z) {
       int c=Math.abs(x-z);
       int c1=Math.abs(y-z);
       if(c>c1)return 2;
       if(c<c1)return 1;
       return 0;
    }
}