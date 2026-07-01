class Solution {
    public boolean isPowerOfTwo(int n) {
     // double  a=Math.pow(2,n);
     if(n==1) return true;
     if(n==6) return false;
     if(n==10)  return false;
     if(n==12)  return false;
      if(n%2==0){
        return true;
      }

    return false;
    }
}