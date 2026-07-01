class Solution {
    public long maxTotalValue(int[] nums, int k) {
        
    
        int n = nums.length;

        int[] nge = new int[n]; // Next Greater Element
        int[] pge = new int[n]; // Previous Greater Element
        int[] nse = new int[n]; // Next Smaller Element
        int[] pse = new int[n]; // Previous Smaller Element

        Arrays.fill(nge, n);
        Arrays.fill(pge, -1);
        Arrays.fill(nse, n);
        Arrays.fill(pse, -1);

        // Next Greater Element
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && nums[stack.peek()] < nums[i]) {
                nge[stack.pop()] = i;
            }
            stack.push(i);
        }

        // Previous Greater Element
        stack.clear();
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && nums[stack.peek()] <= nums[i]) {
                pge[stack.pop()] = i;
            }
            stack.push(i);
        }

        // Next Smaller Element
        stack.clear();
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && nums[stack.peek()] > nums[i]) {
                nse[stack.pop()] = i;
            }
            stack.push(i);
        }

        // Previous Smaller Element
        stack.clear();
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && nums[stack.peek()] >= nums[i]) {
                pse[stack.pop()] = i;
            }
            stack.push(i);
        }

        // Calculate contributions
        long[] contributions = new long[n];
        for (int i = 0; i < n; i++) {
            long countMax = (long)(i - pge[i]) * (nge[i] - i);
            long countMin = (long)(i - pse[i]) * (nse[i] - i);
            contributions[i] = (countMax - countMin) * (long)nums[i];
        }

        // Sort contributions descending
        Arrays.sort(contributions);
        long total = 0;
        for (int i = n - 1; i >= n - k && i >= 0; i--) {
            total += contributions[i];
        }

        return total;
    }
}