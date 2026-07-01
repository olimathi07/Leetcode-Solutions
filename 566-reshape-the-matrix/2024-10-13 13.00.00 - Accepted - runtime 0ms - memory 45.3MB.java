class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        int f=mat.length;
        int h=mat[0].length;
        if(r*c!=f*h){
            return mat;
        }
        int [][] re= new int [r][c];
        int index =0;
        for (int i=0;i<f;i++){
            for (int j=0;j<h;j++){
                re[index / c][index % c] = mat[i][j];
                index++;
               
            }
        }
        return re;
        
    }
}