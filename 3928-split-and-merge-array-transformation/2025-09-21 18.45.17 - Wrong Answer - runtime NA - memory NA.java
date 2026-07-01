class Solution {
    public int minSplitMerge(int[] nums1, int[] nums2) {
         int n = nums1.length;
        Map<Integer, Integer> pos = new HashMap<>();
        for (int i = 0; i < n; i++) {
            pos.put(nums2[i], i);
        }
        
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = pos.getOrDefault(nums1[i], -1);
        }
        
        List<Integer> lis = new ArrayList<>();
        for (int num : arr) {
            if (num == -1) continue;
            int idx = Collections.binarySearch(lis, num);
            if (idx < 0) {
                idx = -(idx + 1);
            }
            if (idx == lis.size()) {
                lis.add(num);
            } else {
                lis.set(idx, num);
            }
        }
        
        return n - lis.size();
    }
}