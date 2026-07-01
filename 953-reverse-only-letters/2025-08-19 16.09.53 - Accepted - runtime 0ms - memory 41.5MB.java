class Solution {
    public String reverseOnlyLetters(String s) {
        int st=0;
        int e=s.length()-1;
        char[] c=s.toCharArray();
        while(st<e){
            if(!Character.isLetter(c[st])){
                st++;
                continue;
              }
            else if(!Character.isLetter(c[e])){
                e--;
                continue;
             }
             char t=c[st];
             c[st]=c[e];
             c[e]=t;
             st++;
             e--;
        }
        return new String(c);
    }
}