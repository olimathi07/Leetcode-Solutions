class Solution {
    public char findTheDifference(String s, String t) {
        int s1=s.length();
        int t1=t.length();
        char[] c=s.toCharArray();
        char[] v=t.toCharArray();
        Arrays.sort(c);
        Arrays.sort(v);
        for(int i=0;i<c.length;i++){
            if(c[i]!=v[i]) return v[i];
        }
        return v[t1-1];
    }
}