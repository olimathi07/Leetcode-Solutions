class Solution {
    public boolean isPowerOfFour(int n) {
        if(n==1)return true;
        if(n>0){
        if(n%4==0){
            return true;
        }
        }
        return false;
    }
}