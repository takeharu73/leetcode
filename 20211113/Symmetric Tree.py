####### 以下でAC

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        else:
            return self.dfs(root,root)
        
    def dfs(self, left, right):
        if left and right:
            return left.val==right.val and self.dfs(left.left, right.right) and self.dfs(left.right, right.left)
        else:
            return left==right
                        
            
            
####### 以下は[1,2,2]でWAとなった
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    left_graph = deque()
    right_graph = deque()
    left_visited = []
    right_visited = []
    
    def dfs(self,l,r):
        if l and r:
            if l not in self.left_visited:
                self.left_graph.append(l.left)
                self.left_graph.append(l.right)
            if r not in self.right_visited:
                self.right_graph.append(r.right)
                self.right_graph.append(r.left)
                
            self.left_visited.append(l)
            self.right_visited.append(r)
            
            # print(self.left_graph, self.right_graph)
            while True:
                if len(self.left_graph)==0 and len(self.right_graph)==0:
                    return True
                    # break
                left = self.left_graph.pop()
                right = self.right_graph.pop()
                # print(self.left_graph, self.right_graph)
                if (left is None and right is not None) or (left is not None and right is None):
                    return False
                    # break
                elif left is None and right is None:
                    continue
                else:
                    # print(left.val, right.val)
                    if left.val == right.val:
                        self.dfs(left, right)
                    else:
                        return False
                        # break
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # print(root)
        if root is None:
            return False
        elif root.left is None and root.right is None:
            return True
        elif root.left is None or root.right is None:
            return False
        else:
            return self.dfs(root.left, root.right)