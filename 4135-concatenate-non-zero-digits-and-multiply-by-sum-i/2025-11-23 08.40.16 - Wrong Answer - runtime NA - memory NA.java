class Solution {
    public long sumAndMultiply(int n) {
       char[] s = String.valueOf(n).toCharArray();

        String r="";
        for(char c:s){
            if (c!='0'){
                r+=c;
            }
        }
        int m=Integer.parseInt(r);
        int l=m;
        int t=0;
        while(l>0){
            t+=l%10;
            l/=10;
        }
        return m*t;
    }
}