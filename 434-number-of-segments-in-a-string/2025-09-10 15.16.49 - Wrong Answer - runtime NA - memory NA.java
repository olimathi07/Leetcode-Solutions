class Solution {
    public int countSegments(String s) {
        if(s.contains("")) return 0;
        String[] r=s.split(" ");
        int c=0;
        for(int i=0;i<r.length;i++){
            
              c++;
            
        }
        return c;
    }
}