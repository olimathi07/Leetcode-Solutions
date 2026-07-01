class Solution {
    public String removeOccurrences(String s, String part) {
         while (s.contains(part)) {      // repeat until no 'part' found
            s = s.replace(part, "");    // remove all occurrences
        }
        return s;
    }
}