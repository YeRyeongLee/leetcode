# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_depth_and_diameter(self, root):
        if not root.left:
            left_max_depth, left_max_diameter = -1, -1
        else:
            left_max_depth, left_max_diameter = self.find_depth_and_diameter(root.left)
        
        if not root.right:
            right_max_depth, right_max_diameter = -1, -1
        else:
            right_max_depth, right_max_diameter = self.find_depth_and_diameter(root.right)
        
        curr_max_depth = max(left_max_depth, right_max_depth) + 1
        curr_max_diameter = max(left_max_diameter, right_max_diameter, left_max_depth+right_max_depth+2)
        
        return curr_max_depth, curr_max_diameter

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        max_depth, max_diameter = self.find_depth_and_diameter(root)

        return max_diameter

        
