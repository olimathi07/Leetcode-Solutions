class Solution {
    public boolean isPalindrome(String s) {
        String r = "";
        for (int i = s.length() - 1; i >= 0; i--) {
            r = r + s.charAt(i);
        }
        // Remove non-alphanumeric characters and convert to lowercase
        String sClean = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        String rClean = r.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        return sClean.equals(rClean);
    }
}