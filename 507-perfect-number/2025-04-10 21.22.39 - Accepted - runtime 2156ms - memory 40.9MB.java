class Solution {
    public boolean checkPerfectNumber(int num) {
        int s=0;
        int t=num;
        //boolean flag=false;
        for(int i=1;i<num;i++){
            if(num%i==0){
                s+=i;
            }
        }
        return s==num;
        
    }
}