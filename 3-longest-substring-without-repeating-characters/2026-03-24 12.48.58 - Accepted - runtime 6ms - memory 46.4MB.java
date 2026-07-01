class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> h=new HashSet<>();
        int m=0,l=0;
        for(int r=0;r<s.length();r++){
            char c=s.charAt(r);
            while(h.contains(c)){
                h.remove(s.charAt(l));
                l++;
            }
            h.add(c);
            m=Math.max(m,r-l+1);


        }
        return m;
    }
}