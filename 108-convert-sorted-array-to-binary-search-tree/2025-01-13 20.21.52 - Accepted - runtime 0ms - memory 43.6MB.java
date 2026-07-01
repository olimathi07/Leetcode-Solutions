/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        // Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    
    TreeNode(int val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}


   
        return buildBST(nums, 0, nums.length - 1);
    }
    
    private TreeNode buildBST(int[] nums, int start, int end) {
        // Base case: If start index is greater than end index, return null
        if (start > end) {
            return null;
        }
        
        // Find the middle element to make it the root
        int mid = start + (end - start) / 2; // Avoids overflow compared to (start + end) / 2
        
        // Create the root node
        TreeNode root = new TreeNode(nums[mid]);
        
        // Recursively build the left and right subtrees
        root.left = buildBST(nums, start, mid - 1); // Left half of the array
        root.right = buildBST(nums, mid + 1, end);  // Right half of the array
        
        return root; // Return the constructed tree
    }
}

        
    
