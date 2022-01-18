/*
Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return null.

The successor of a node p is the node with the smallest key greater than p.val.

 

Example 1:


Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
Example 2:


Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.

*/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        if (root == null) return null;
        
        List<TreeNode> arr = new ArrayList<>();
        inOrder(root, arr);
        int i = 0;
        while (i < arr.size() && arr.get(i).val != p.val) {
            i++; 
        }
        if (i < arr.size() - 1) { 
            return arr.get(i+1);
        }
        return null;
    }
    
    //先中序遍历，再输出后一位
    private void inOrder(TreeNode root, List<TreeNode> arr) {
        if (root == null) return;
        inOrder(root.left, arr);
        arr.add(new TreeNode(root.val));    //注意这里要新建一个root并加入arr
        inOrder(root.right, arr);            
    }
    
}
