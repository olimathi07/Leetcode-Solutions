
class Solution {
    public int[] twoSum(int[] numbers, int sum) {
        for(int i=0;i<numbers.length;i++){
            for(int j=1;j<numbers.length;j++){
                if(numbers[i]+numbers[j]==sum)
                  return new int []{i,j};
            }
        }
        return new int[] {};
        
    }
}