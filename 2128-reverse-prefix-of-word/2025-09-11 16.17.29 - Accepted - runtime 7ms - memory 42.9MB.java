class Solution {
    public String reversePrefix(String word, char ch) {
        String r="";
        for(int i=word.indexOf(ch);i>=0;i--){
            char c=word.charAt(i);
            r+=c;
        }
        for(int i=word.indexOf(ch)+1;i<word.length();i++){
            char c=word.charAt(i);
            r+=c;
        }
        return r;
    }
}