class Solution {
    public boolean isPowerOfTwo(int n) {
     // double  a=Math.pow(2,n);
     return n > 0 && (n & (n - 1)) == 0;
    }
}