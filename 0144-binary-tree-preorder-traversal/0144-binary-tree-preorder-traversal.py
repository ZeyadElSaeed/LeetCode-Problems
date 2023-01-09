# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        myStack = list()
        answer = list()

        if root == None:
            return myStack
        myStack.append(root)

        while ( len(myStack) > 0):
            node = myStack.pop()
            answer.append(node.val)
            if (node.right != None):
                myStack.append(node.right)
            if (node.left != None):
                myStack.append(node.left)
            
        return answer
        