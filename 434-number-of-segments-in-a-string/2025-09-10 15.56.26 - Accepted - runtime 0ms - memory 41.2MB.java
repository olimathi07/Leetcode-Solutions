class Solution {
    public int countSegments(String s) {
        if(s==null) return 0;
        
        String[] r=s.split(" ");
        int c=0;
        for(int i=0;i<r.length;i++){
            if(!r[i].isEmpty()){
              c++;
            }
            
        }
        return c;
    }
}