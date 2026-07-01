class Solution {
    public int findKthNumber(int m, int n, int k) {
        int[] arr=new int[n*m];
        int l=0;
        for(int i=1;i<=m;i++){
            for(int j=1;j<=n;j++){
                arr[l++]=i*j;
            }
        }
        Arrays.sort(arr);
       return arr[k-1];
    }
}