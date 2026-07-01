class Solution {
    public int sumDivisibleByK(int[] nums, int k) {
       
     
        
        int sum = 0;

        
        for (int i = 0; i < nums.length; i++) {
            boolean isVisited = false;

            
            for (int j = 0; j < i; j++) {
                if (nums[i] ==  nums[j]) {
                    isVisited = true;
                    break;
                }
            }

            if (!isVisited) {
               
                int count = 0;
                for (int j = 0; j < nums.length; j++) {
                    if (nums[i] == nums[j]) {
                        count++;
                    }
                }

                
                if (count % k == 0) {
                    sum += nums[i] * count;
                }
            }
        }

  
  return sum;
    }
}