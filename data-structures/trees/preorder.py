from typing import List, Optional

useful_problems_to_solve = [
    "https://leetcode.com/problems/binary-tree-preorder-traversal",
]

# Definition for a binary tree node:
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

# Visual representation of the tree we are going to use:
#     1
#    / \
#   2   3
#  / \
# 4   5

# Create the nodes
root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

# Connect the nodes
root.left = node2
root.right = node3
node2.left = node4
node2.right = node5

# Complexity analysis:
# Time complexity: O(n), where n is the number of nodes in the tree
# Space complexity: O(h), where h is the height of the tree
class Implementation:
    def preorder_traversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
        preoder = []

        def dfs(root):
            if not root:
                return
            
            preoder.append(root.val)

            dfs(root.left)
            dfs(root.right)
        
        dfs(root)

        return preoder
    
    def preorder_traversal_iterative(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        stack = [root]
        preorder = []

        while stack:
            node = stack.pop()
            
            if node:
                preorder.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        
        return preorder
    

implementation = Implementation()

recursive_result = implementation.preorder_traversal_recursive(root)
iterative_result = implementation.preorder_traversal_iterative(root)

EXPECTED_RESULT = [1, 2, 4, 5, 3]

assert recursive_result == EXPECTED_RESULT
assert iterative_result == EXPECTED_RESULT
    
print("Recursive preorder traversal: ", recursive_result)
print("Iterative preorder traversal: ", iterative_result)
    
print("Useful problems to solve:")
for problem in useful_problems_to_solve:
    print(problem)