class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        for(int i=0;i<arr.length;i++){
            if (arr[i]==arr[i]){
                return true;
            }
        }
        if(arr[0]!=arr[1]) return false;
        return false;
    }
}