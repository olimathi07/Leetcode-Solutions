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
    public boolean isBalanced(TreeNode root) {
        if(root==null)return true;
        
           
        if(Height(root)==-1)return false;
    return true;

        
        
    }
    public int Height(TreeNode root){
        if(root==null)return 0;
        int l=Height(root.left);
        int r=Height(root.right);
        //if(l==r)return -1;
        if(l==-1||r==-1)return -1;
        if(Math.abs(l-r)>1)return -1;
        return Math.max (l,r)+1;
    }

}