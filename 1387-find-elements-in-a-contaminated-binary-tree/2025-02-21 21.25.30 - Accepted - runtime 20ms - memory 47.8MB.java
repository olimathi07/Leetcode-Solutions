/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *III2         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
public FindElemen
*/
class FindElements {

        HashSet<Integer> seen;

            public FindElements(TreeNode root) {
                    seen = new HashSet<>();
                            dfs(root, 0);
                                }

                                    public boolean find(int target) {
                                            return seen.contains(target);
                                                }

                                                    private void dfs(TreeNode currentNode, int currentValue) {
                                                            if (currentNode == null) return;
                                                                    // visit current node by adding its value to seen
                                                                            seen.add(currentValue);
                                                                                    dfs(currentNode.left, currentValue * 2 + 1);
                                                                                            dfs(currentNode.right, currentValue * 2 + 2);
                                                                                                }
                                                                                                }
