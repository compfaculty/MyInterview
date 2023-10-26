# https://leetcode.com/problems/path-sum/
# Given the root of a binary tree and an integer targetSum,
# return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
from typing import Optional

from shared import TreeNode


def hasPathSum(root: Optional[TreeNode], target_sum: int) -> bool:
    if root is None:
        return False
    if root.left is None and root.right is None:
        return root.val == target_sum
    return hasPathSum(root.left, target_sum - root.val) or hasPathSum(root.right, target_sum - root.val)


def test_isPathSum():
    root = TreeNode(5, None, None)
    root.left = TreeNode(4,
                         TreeNode(11,
                                  TreeNode(7, None, None),
                                  TreeNode(2, None, None)), None)
    root.right = TreeNode(8,
                          TreeNode(13, None, None), TreeNode(4, None, TreeNode(1, None, None)))

    assert hasPathSum(root, 22) is True
    assert hasPathSum(None, 22) is False
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert hasPathSum(root, 5) is False
