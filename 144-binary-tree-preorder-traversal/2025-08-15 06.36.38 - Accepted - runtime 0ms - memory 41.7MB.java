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
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> c= new ArrayList<>();
         preorder(root, c);
        return c;
    }
        public void preorder(TreeNode node,List<Integer> c){
            if(node==null){
            return;
        }
          c.add(node.val);
          preorder(node.left,c);
          preorder(node.right,c);

        
      
    }
}