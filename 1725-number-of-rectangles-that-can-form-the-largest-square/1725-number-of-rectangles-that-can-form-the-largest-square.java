class Solution {
    public int countGoodRectangles(int[][] rectangles) {
        int n=rectangles.length;
        int[] arr=new int[n];
        int m=0;
        for(int i=0;i<n;i++){
            m=Math.min(rectangles[i][0],rectangles[i][1]);
            arr[i] =m;
        }
        int k=0;
        for(int i=0;i<arr.length;i++){
            k = Math.max(k,arr[i]);
        }
        int c=0;
        for(int i=0;i<arr.length;i++){
            if(arr[i]==k){
                c++;
            }
        }
        return c;

    }
}