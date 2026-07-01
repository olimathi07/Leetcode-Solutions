class Solution {
public:
    int missingNumber(vector<int>& nums) {
        
        int missingNumber(List<int> nums) { 
            nums.sort(); 
            int result; 
            f (nums.first != 0) {
                 result = 0; 
                 }
         else {
             result = nums.last + 1;
          } 
        for (int i = 0; i < nums.length - 1; i++) { 
            if (nums[i] + 1 != nums[i + 1]) {
                 result = nums[i] + 1;
         break;
        } 
        }
         return result;
          }
    }
};