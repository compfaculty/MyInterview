class Node:
    def __init__(self, left_node, right_node, n):
        self.left = left_node
        self.right = right_node
        self.value = n

    def __str__(self):
        return f"{self.value}--{self.left}--{self.right}"
