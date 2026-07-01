class Solution {
    public int firstUniqChar(String s) {
       
    int[] count = new int[26];  // count of each letter

    // 1. Count frequency of each character
    for (char ch : s.toCharArray()) {
        count[ch - 'a']++;
    }

    // 2. Find the first character with count 1
    for (int i = 0; i < s.length(); i++) {
        if (count[s.charAt(i) - 'a'] == 1) {
            return i;
        }
    }

    return -1;  // no unique character found
}

    
}