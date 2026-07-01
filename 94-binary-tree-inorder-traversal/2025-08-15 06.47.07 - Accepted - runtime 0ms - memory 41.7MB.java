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
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> c= new ArrayList<>();
         preorder(root, c);
        return c;
    }
        public void preorder(TreeNode node,List<Integer> c){
            if(node==null){
            return;
        }
          preorder(node.left,c);
          c.add(node.val);
          preorder(node.right,c);

    }
}