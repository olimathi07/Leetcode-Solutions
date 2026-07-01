class Solution {
    public int numberOfBeams(String[] bank) {
        int p=0;
        int t=0;
        int n=bank.length;
        for(int i=0;i<n;i++){
            int c=0;
            for(int j=0;j<bank[i].length();j++){
                if(bank[i].charAt(j)=='1'){
                c++;
                }
            }
            if(c>0){
                t+=p*c;
                p=c;
            }
        }
        return t;
    }
}