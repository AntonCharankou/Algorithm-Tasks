# Given the root of a binary tree, 
# return the average value of the nodes on each level in the form of an array. 
# Answers within 10^-5 of the actual answer will be accepted.

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        answer = []
        curLevel = [root]
        temp = []
        while curLevel:
            n = 0
            s = 0
            for node in curLevel:
                s += node.val
                n += 1

                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            answer.append(s / n)
            curLevel = temp.copy()
            temp.clear()

        return answer

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
result = solution.averageOfLevels(root)

print(result)