class Solution {
    public int oddCells(int m, int n, int[][] indices) {
        int[][] a=new  int[m][n];
        for(int[] in:indices){
            int r=in[0];
            int c=in[1];
        
        for(int j=0;j<n;j++){
            a[r][j]++;
        }
        for(int i=0;i<m;i++){
            a[i][c]++;
        }
        }
        int c=0;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(a[i][j]%2!=0){
                    c++;
                }
            }
        }
        return c;
    }
}