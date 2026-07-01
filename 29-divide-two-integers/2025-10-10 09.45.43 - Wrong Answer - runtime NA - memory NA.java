class Solution {
    public int divide(int dividend, int divisor) {
        if(dividend==Integer.MIN_VALUE&&divisor==-1) return Integer.MIN_VALUE;
        int c=dividend/divisor;
        return c;
    }
}