class Solution {
    public boolean checkRecord(String s) {
        
        int a=0;
        int l=0;
        for(char c:s.toCharArray()){
            if(c!='L') l=0;
            if(c=='L') l++;
            if(c=='A') a++;
            if(l==3||a==2) return false;

        }
        return true;
       
       
        

    }
}