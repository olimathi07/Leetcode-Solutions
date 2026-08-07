class Solution {
    public int smallestNumber(int n, int t) {
        for(int i=n;i<=100;i++){
        int m=1;
        int temp=i;
            while(temp!=0){
                int r=temp%10;
                m*=r;
                temp/=10;
            
            }
            if(i>=n&&m%t==0){
                return i;
            }
        }
        return -1;
    }
}