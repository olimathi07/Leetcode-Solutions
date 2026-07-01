class Solution {
    public boolean isIsomorphic(String s, String t) {
       int arr[]=new int[256];
       int arr1[]=new int[256];
       for(int i=0;i<s.length();i++){
        arr[s.charAt(i)]++;
       }
       for(int i=0;i<t.length();i++){
        arr1[t.charAt(i)]++;
       }
       for(int i=0;i<arr.length;i++){
        for(int j=0;j<arr1.length;j++){
            if(arr[i]==arr1[j]){
                return true;
            }
        }
       }
       return false;
    }
}