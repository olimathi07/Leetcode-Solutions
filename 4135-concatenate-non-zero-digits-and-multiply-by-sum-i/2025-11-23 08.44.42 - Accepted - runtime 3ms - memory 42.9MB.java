class Solution {
    public long sumAndMultiply(int n) {
       char[] s = String.valueOf(n).toCharArray();

               StringBuilder sb = new StringBuilder();

       
        for (char c : s) {
            if (c != '0') sb.append(c);
        }

       
        if (sb.length() == 0) return 0;

        long m = Long.parseLong(sb.toString());  
        Long l=m;
        int t=0;
        while(l>0){
            t+=l%10;
            l/=10;
        }
        return m*t;
    }
}