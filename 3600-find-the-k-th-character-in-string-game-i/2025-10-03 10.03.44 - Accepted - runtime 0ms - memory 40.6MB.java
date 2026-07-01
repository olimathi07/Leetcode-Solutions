class Solution {
    public char kthCharacter(int k) {
     int o=Integer.bitCount(k-1);
     return (char)('a'+(o%26));   
    }
}