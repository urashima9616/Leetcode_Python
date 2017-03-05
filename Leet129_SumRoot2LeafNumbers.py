# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return None
        [weight, rootsum, carry] = self.PathSum(root)
        res = rootsum + carry*(10**max(weight))
        return res

    def PathSum(self, root):
        if not root:
            return [None, None, None]
        lweight, lsum, lcarry = self.PathSum(root.left)
        rweight, rsum, rcarry = self.PathSum(root.right)
        maxrweight, maxlweight = (0,0)
        if not lweight and not rweight: # Leaf node
            return [[1], root.val, 0]
        if not lweight:
            #calc sum
            rootsum = rsum
            for i in xrange(len(rweight)):
                weight = 10**rweight[i]
                rootsum += (root.val)*weight 
                rweight[i] += 1
                if maxrweight < weight:
                    maxrweight = weight
            rootsum += maxrweight * rcarry
        elif not rweight:
             #calc sum
            rootsum = lsum
            for i in xrange(len(lweight)):
                weight = 10**lweight[i]
                rootsum += (root.val)*weight 
                lweight[i] += 1
                if maxlweight < weight:
                    maxlweight = weight
            rootsum += maxlweight * lcarry
        else:
            rootsum = lsum + rsum
            for i in xrange(len(lweight)):
                weight = 10**lweight[i]
                rootsum += (root.val)*weight 
                lweight[i] += 1
                if maxlweight < weight:
                    maxlweight = weight
            rootsum += maxlweight * lcarry
            for i in xrange(len(rweight)):
                weight = 10**rweight[i]
                rootsum += (root.val)*weight 
                rweight[i] += 1
                if maxrweight < weight:
                    maxrweight = weight
            rootsum += maxrweight * rcarry
        
        weight = max(maxrweight, maxlweight) + 1
        carry = 0
        if rootsum > 10**weight:
            carry = 1
            rootsum -= 10**weight
        nextweight = lweight + rweight if lweight and rweight else lweight or rweight
        return [nextweight, rootsum, carry]
            