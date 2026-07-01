class Solution {
    public char kthCharacter(long k, int[] operations) {
        long o=Long.bitCount(k-2);
        return (char)('a'+(o%26));
    }
}