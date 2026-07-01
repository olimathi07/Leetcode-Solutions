class Solution {
    public boolean containsPattern(int[] arr, int m, int k) {
        int c=0;
        for (int i=0;i<arr.length;i++){
            if(m==arr[i])
            {
                c++;
            }
            if(c<k&&c==0){
                System.out.println("false");
            }
            else{
                System.out.println("true");
            }



        }
        return true;
    }
        
    
}