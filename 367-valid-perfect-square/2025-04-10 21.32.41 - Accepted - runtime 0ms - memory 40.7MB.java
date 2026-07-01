class Solution {
    public boolean isPerfectSquare(int num) {
        //int s=0;
       // for(int i=1;i<num;i++){
        //     for(int j=1;j<num;j++){
        //         s=i*j;
                
        //     }
        // }
        int s=(int)Math.sqrt(num);
         return s*s==num;

        
    }
}