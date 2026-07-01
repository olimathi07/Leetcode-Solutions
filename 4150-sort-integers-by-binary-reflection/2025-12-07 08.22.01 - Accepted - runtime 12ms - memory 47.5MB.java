class Solution {

    int reflection(int n) {
        String b = Integer.toBinaryString(n);
        String r = new StringBuilder(b).reverse().toString();
        return Integer.parseInt(r, 2);
    }

    public int[] sortByReflection(int[] nums) {
        int n = nums.length;
        int[][] ar = new int[n][2];

        for (int i = 0; i < n; i++) {
            ar[i][0] = nums[i];
            ar[i][1] = reflection(nums[i]);
        }

        Arrays.sort(ar, (a, b) -> {
            if (a[1] == b[1]) 
                return a[0] - b[0];
            return a[1] - b[1];
        });

        for (int i = 0; i < n; i++) {
            nums[i] = ar[i][0];
        }

        return nums;
    }
}
