class Solution {
    public long maxTotalValue(int[] nums, int k) {
        
    
      int n = nums.length;
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        
        // Enumerate all subarrays
        for (int i = 0; i < n; i++) {
            int currMax = nums[i];
            int currMin = nums[i];
            for (int j = i; j < n; j++) {
                currMax = Math.max(currMax, nums[j]);
                currMin = Math.min(currMin, nums[j]);
                pq.add(currMax - currMin);
            }
        }
        
        long total = 0;
        for (int i = 0; i < k && !pq.isEmpty(); i++) {
            total += pq.poll();
        }
        return total;
    }
}