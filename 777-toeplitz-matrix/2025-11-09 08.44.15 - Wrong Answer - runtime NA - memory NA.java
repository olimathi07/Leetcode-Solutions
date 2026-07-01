class Solution {
    public boolean isToeplitzMatrix(int[][] matrix) {
        int n=matrix.length;
        int m=matrix[0].length;
      for(int i=0;i<n-1;i++){
        for(int j=0;j<m-1;j++){
            if(i==j&&matrix[i][j]==matrix[i+1][j+1]){
              return true;
            }
        }
      }  
      return false;
    }
}