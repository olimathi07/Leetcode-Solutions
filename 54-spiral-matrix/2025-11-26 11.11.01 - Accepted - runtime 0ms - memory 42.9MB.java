class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List <Integer> res=new ArrayList<>();
        if(matrix==null||matrix.length==0) return res;
        int m=matrix.length;
        int n=matrix[0].length;
        int t=0,b=m-1;
        int l=0,r=n-1;
        while(t<=b && l<=r){

        for(int j=l;j<=r;j++){
         res.add(matrix[t][j]);
        }
        t++;
        for(int i=t;i<=b;i++){
            res.add(matrix[i][r]);
        }
        r--;
         if (t <= b) {
                for (int j = r; j >= l; j--) {
                    res.add(matrix[b][j]);
                }
                b--;
            }

           
            if (l <= r) {
                for (int i = b; i >= t; i--) {
                    res.add(matrix[i][l]);
                }
                l++;
            }
        }
        return res;
    }
}