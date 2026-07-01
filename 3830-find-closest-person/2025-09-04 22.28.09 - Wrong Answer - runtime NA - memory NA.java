class Solution {
    public int findClosest(int x, int y, int z) {
        int c=0,c1=0;
       for(int i=0;i<1000;i++){
        if((x+i)==z){
            c++;
        }
       }
        for(int i=0;i<1000;i++){
        if((y+i)==z){
            c1++;
        }
       } 
       return Math.max(c,c1);
    }
}