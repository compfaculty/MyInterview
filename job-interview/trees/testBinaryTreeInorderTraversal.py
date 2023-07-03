from typing import Optional, List

from shared.Node import Node


class Solution:
    def inorderTraversal(self, root: Optional[Node]) -> List[int]:
        stack = []
        result = []
        curr = root

        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                result.append(curr.val)
                curr = curr.right

        return result
