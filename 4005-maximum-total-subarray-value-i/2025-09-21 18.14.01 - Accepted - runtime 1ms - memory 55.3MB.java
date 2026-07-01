class Solution {
    public long maxTotalValue(int[] nums, int k) {
          long maxVal = Integer.MIN_VALUE;
        long minVal = Integer.MAX_VALUE;

        for (int num : nums) {
            maxVal = Math.max(maxVal, num);
            minVal = Math.min(minVal, num);
        }

        long bestSubarrayValue = maxVal - minVal;
        return k * bestSubarrayValue;
    
    }
}