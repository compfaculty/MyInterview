# Definition for a binary tree node.
from queue import Queue
from typing import List

from shared.Node import Node


class Solution:
    def isSymmetric(self, root: Node) -> bool:
        ret = False
        if not root: return True
        q = Queue()
        q.put(root.left)
        q.put(root.right)
        while q.qsize():
            left = q.get()
            right = q.get()
            if not left and not right:
                ret = True
                continue
            if left and right and left.val == right.val:
                q.put(left.left)
                q.put(right.right)
                q.put(left.right)
                q.put(right.left)
                continue
            ret = False
            break
        return ret

    def levelOrderBottom(self, root: Node) -> List[List[int]]:
        levels = []

        def _getlevels(root: Node, level: int):
            if not root: return
            if len(levels) <= level:
                levels.append([])
            levels[level].append(_getlevels(root.left, level + 1))
            levels[level].append(_getlevels(root.right, level + 1))
            return root.val

        _getlevels(root, 0)
        return [a for a in (list(filter(None, arr)) for arr in levels[:: -1]) if a] + [[root.val]]


def test_Solution():
    p = Node(1, left=Node(2), right=Node(2))
    q = Node(1, left=Node(2, left=Node(3), right=Node(5)), right=Node(4))
    s = Solution()
    assert s.isSymmetric(p)
    assert s.levelOrderBottom(q) == [[3, 5], [2, 4], [1]]
