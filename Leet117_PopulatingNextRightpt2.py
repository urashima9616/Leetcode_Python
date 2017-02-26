# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return 
        cur = root
        leftmost = root.left or root.right
        prev_pt = None
        while cur:
            while cur: #Layer traversal
                if prev_pt and (cur.right or cur.left):
                    prev_pt.next = cur.left or cur.right
                    prev_pt = cur.right or cur.left
                if not prev_pt:
                    prev_pt = cur.right or cur.left
                    leftmost = cur.left or cur.right
                if cur.right and cur.left:
                    cur.left.next = cur.right
                cur = cur.next
            cur = leftmost
            prev_pt = None
            leftmost = None
Solve = Solution()
root = TreeLinkNode(1)
root.left = TreeLinkNode(2)
root.right = TreeLinkNode(3)
root.left.left = TreeLinkNode(4)
root.left.right = TreeLinkNode(5)
Solve.connect(root)