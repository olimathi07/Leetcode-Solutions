class Solution {
    public boolean checkRecord(String s) {
        
        int a=0;
        int l=0;
        int p=0;
        for(int i=0;i<s.length();i++){
                  char c=s.charAt(i);
            if(c=='A'){ a++; if(a>=2) return false;}
            else if(c=='P'){ p++;}
            else if(c=='L') {l++;if(l>=3) return false;}
            else {l=0;}
        }
       
        return true;

    }
}