class Solution {
    public boolean detectCapitalUse(String word) {
        
        int c=0;
        int n=word.length();
        for(int i=0;i<n;i++){
            if(Character.isUpperCase(word.charAt(i))){
              c++;
            }
        }
        if(c==1&&Character.isUpperCase(word.charAt(0))) return true;
        if(c==0||c==n) return true;
        return false;
    }
}