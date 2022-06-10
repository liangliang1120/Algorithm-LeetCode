"""
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

 

Example 1:


Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
Example 2:

Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]
 

Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.

"""
we update res as we traverse the tree. we append a node into res if two conditions are satisfied:
1. the node should not be deleted; 2. the node has not parent (meaning it's the root of a forest).
In order to check if a node has parent or not, we need to pass has_parent bool into dfs arguments.
if a node is in to_delete list, then the node should pass the information to it's children that it has been
deleted and it's children has no parent now.
"""

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        ds = set(to_delete)   # search more efficient
        
        def process(root):
            if not root:
                return None
            root.left, root.right = process(root.left), process(root.right)  #if root.left root.right == none means they are both processed
            if root.val not in to_delete:
                return root    #can contact with parent
            # in this step indicate root in to_delete, so we need add left or right to ans
            if root.left:
                ans.append(root.left)
            if root.right:
                ans.append(root.right)
            return None
        
        root = process(root)
        if root:
            ans.append(root)
            
        return ans
    

