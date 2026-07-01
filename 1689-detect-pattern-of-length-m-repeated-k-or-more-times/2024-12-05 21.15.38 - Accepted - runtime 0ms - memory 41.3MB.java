class Solution {
    public boolean containsPattern(int[] arr, int m, int k) {
        int c=0;
        for (int i=0;i<arr.length-m;i++){
            if(arr[i]==arr[i+m])
            {
                c++;
            }else{
                c=0;
            }
        
            if(c==m*(k-1)){
               return true;
            }
        }



        
        return false;
    }
        
    
}