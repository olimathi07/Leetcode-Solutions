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

        
        int currentLength = 0;
        int maxLength = 0;

        for (int i = 0; i < n; i++) {
           
            if (valToIdxNums2.containsKey(nums1[i])) {
                if (i > 0 && valToIdxNums2.containsKey(nums1[i - 1])) {
                    if (valToIdxNums2.get(nums1[i]) == valToIdxNums2.get(nums1[i - 1]) + 1) {
                        currentLength++;
                    } else {
                       
                        currentLength = 1;
                    }
                } else {
                    
                    currentLength = 1;
                }
            } else {
                currentLength = 0;
            }
            maxLength = Math.max(maxLength, currentLength);
        }

       
        return n - maxLength;
    }
}