class Solution {
    public String removeDuplicates(String s) {
     int[] f=new int[256];
     
     for(char c:s.toCharArray()){
        f[c]++;
     }
     StringBuilder r=new StringBuilder();
     for(char c:s.toCharArray()){
        if(f[c]==1){
            r.append(c);
        }
     }
     return r.toString();
    }
}