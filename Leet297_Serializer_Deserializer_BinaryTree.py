# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def serializer(root):
            if not root:
                res.append("#")
            else:
                res.append(root.val)
                serializer(root.left)
                serializer(root.right)
            return
        serializer(root)
        return res
                
                
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def treeConstructor():
            val = next(vals)
            if val == "#":
                return None
            node = TreeNode(val)
            node.left = treeConstructor()
            node.right = treeConstructor()
            return node
        vals = iter(data)
        treeConstructor()
codec = Codec()
