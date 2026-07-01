class Solution {
    public int minSplitMerge(int[] nums1, int[] nums2) {
        int n = nums1.length;
        if (n <= 1) {
            return 0;
        }

        Map<Integer, Integer> valToIdxNums2 = new HashMap<>();
        for (int i = 0; i < n; i++) {
            valToIdxNums2.put(nums2[i], i);
        }

        int[] dp = new int[n];
        int maxLength = 0;

        for (int i = 0; i < n; i++) {
            int currentVal = nums1[i];
            if (valToIdxNums2.containsKey(currentVal)) {
                int currentIdxInNums2 = valToIdxNums2.get(currentVal);
                
                if (i > 0 && valToIdxNums2.containsKey(nums1[i - 1])) {
                    int prevIdxInNums2 = valToIdxNums2.get(nums1[i - 1]);
                    if (currentIdxInNums2 == prevIdxInNums2 + 1) {
                        dp[i] = dp[i - 1] + 1;
                    } else {
                        dp[i] = 1;
                    }
                } else {
                    dp[i] = 1;
                }
            } else {
                dp[i] = 0;
            }
            maxLength = Math.max(maxLength, dp[i]);
        }
        
        return n - maxLength;
    }
}