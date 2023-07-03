# https://www.hackerrank.com/challenges/count-triplets-1
from collections import deque

from shared.Node import Node


def sort_binary_tree_by_levels(node: Node) -> list[int]:
    if not node:
        return []
    ret = []
    stack = deque()
    stack.append(node)
    while len(stack) > 0:
        n = stack.popleft()
        ret.append(n.value)
        if n.left:
            stack.append(n.left)
        if n.right:
            stack.append(n.right)
    return ret


def test_sort_binary_tree_by_levels():
    assert sort_binary_tree_by_levels(
        Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)) == [1, 2, 3, 4,
                                                                                                            5, 6]
