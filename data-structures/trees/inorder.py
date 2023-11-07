from typing import List, Optional

useful_problems_to_solve = [
    "https://leetcode.com/problems/binary-tree-inorder-traversal",
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
    def inorder_traversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
        inoder = []

        def dfs(root):
            if not root:
                return

            dfs(root.left)
            inoder.append(root.val)
            dfs(root.right)
        
        dfs(root)

        return inoder
    
    def inorder_traversal_iterative(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        inorder = []

        while True:
            if root:
                stack.append(root)
                root = root.left
            else:
                if not stack:
                    break
                
                root = stack.pop()
                inorder.append(root.val)
                root = root.right
        
        return inorder

implementation = Implementation()

recursive_result = implementation.inorder_traversal_recursive(root)
iterative_result = implementation.inorder_traversal_iterative(root)

EXPTECTED_RESULT = [4, 2, 5, 1, 3]

assert recursive_result == EXPTECTED_RESULT
assert iterative_result == EXPTECTED_RESULT

print("Recursive inorder traversal: ", recursive_result)
print("Iterative inorder traversal: ", iterative_result)
    
print("Useful problems to solve:")
for problem in useful_problems_to_solve:
    print(problem)