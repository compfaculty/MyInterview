# https://leetcode.com/problems/minimum-depth-of-binary-tree/
from typing import Optional

from shared import TreeNode


def minDepthV1(root: Optional[TreeNode]) -> int:
    """recursion"""
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    if root.left is None:
        return minDepthV1(root.right) + 1
    if root.right is None:
        return minDepthV1(root.left) + 1
    return min(minDepthV1(root.left), minDepthV1(root.right)) + 1


def minDepthV2(root: Optional[TreeNode]) -> int:
    """ no recursion """
    if root is None:
        return 0

    depth = 1
    stack = [(root, depth)]
    min_depth = float('inf')

    while stack:
        node, depth = stack.pop()

        if node.left is None and node.right is None:
            min_depth = min(min_depth, depth)

        if node.left:
            stack.append((node.left, depth + 1))

        if node.right:
            stack.append((node.right, depth + 1))

    return min_depth


root = TreeNode(3)
root.left = TreeNode(9, None, None)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))


def test_minDepthV1(benchmark):
    # benchmark something

    result = benchmark.pedantic(minDepthV1,
                                args=(root,),
                                iterations=10000, rounds=100)

    # Extra code, to verify that the run completed correctly.
    # Sometimes you may want to check the result, fast functions
    # are no good if they return incorrect results :-)
    assert result == 2


def test_minDepthV2(benchmark):
    # benchmark something
    result = benchmark.pedantic(minDepthV2,
                                args=(root,),
                                iterations=10000, rounds=100)

    # Extra code, to verify that the run completed correctly.
    # Sometimes you may want to check the result, fast functions
    # are no good if they return incorrect results :-)
    assert result == 2
