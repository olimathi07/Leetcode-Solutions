class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        for(int i=0;i<arr.length-1;i++){
            if (arr[i]==arr[i+1]||arr[0]==arr[1]){
                return true;
            }
        }
       // if(arr[0]!=arr[1]) return false;
        return false;
    }
}