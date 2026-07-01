class Solution {
    public boolean isIsomorphic(String s, String t) {
        if(s.length()!=t.length()) return false; 
       int[] arr=new int[256];
       int[] arr1=new int[256];
       for(int i=0;i<s.length();i++){
       char c=s.charAt(i);
       char c1=t.charAt(i);
       if(arr[c]==0&&arr1[c1]==0){
                arr[c]=c1;
                arr1[c1]=c;
                
            }else{
                if(arr[c]!=c1||arr1[c1]!=c) return false;
            }
        }
       
       return true;
    }
}