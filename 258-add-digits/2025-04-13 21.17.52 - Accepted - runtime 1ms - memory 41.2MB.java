class Solution {
    public int addDigits(int num) {
        
     if(num==0)return 0;
        while(num>=10)
    {
        int s=0;
     while(num!=0)
     {
        int r=num%10;
        s+=r;
        num/=10;
        
       }
        num=s;
    }
     return num; 
    }
}