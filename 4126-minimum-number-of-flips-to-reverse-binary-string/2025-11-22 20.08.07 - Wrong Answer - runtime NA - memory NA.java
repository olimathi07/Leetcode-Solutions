class Solution {
    public int minimumFlips(int n) {
       
        String s = Integer.toBinaryString(n); 
        int l = 0, r= s.length() - 1;
        int f = 0;

        while (l < r) {
            if (s.charAt(l) != s.charAt(r)) {
                f++;
            }
            l++;
            r--;
        }
        return f;
    }
}