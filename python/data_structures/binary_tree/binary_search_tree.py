from enum import Enum
from typing import Optional


class Node:
    """
    Node for a Binary Tree
    """

    def __init__(self, value: int = None):
        """
        Initialise an instance of Node

        @param value: Value of this node
        """
        self.value = value
        self.left = None
        self.right = None

class left_or_right(Enum):
    LEFT = "left"
    RIGHT = "right"

def _count_nodes(self, node) -> int:
    """
    Count the number of nodes recursively.

    @param self:
    @param node:
    @return:
    """
    return 1 + _count_nodes(node.left) + _count_nodes(node.right)


def _max_depth(node) -> int:
    """
    Find the max depth of the BST recursively.

    @param node: current node to count from
    @return: depth of tree from current node
    """
    if node is None:
        return 0

    else:
        left_depth = _max_depth(node.left)
        right_depth = _max_depth(node.right)

    if left_depth > right_depth:
        return left_depth + 1
    else:
        return right_depth + 1


class BinarySearchTree:
    def __init__(self):
        """
        Initialise the class Binary Search Tree
        """
        self.root: Node = Node()

    def is_in_tree(self, value: int):
        """
        Checks if a value is in the tree

        @param value: value to check if in tree
        @return: True if in tree
        """
        current_node = self.root

        while current_node is not None:
            if value == current_node.value:
                return True
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return False

    def insert(self, value) -> None:
        """
        Create a new node with given value and insert it into the BST.

        @param value: value to insert
        """
        current_node = self.root
        previous_node = None

        while current_node is not None:
            if current_node.value == value:
                raise ValueError("Value {value} already present in Binary Search Tree.")

            elif current_node.value > value:
                previous_node = current_node
                current_node = current_node.left

            else:
                current_node = current_node.right

        if previous_node.value > value:
            previous_node.left = Node(value)
        else:
            previous_node.right = Node(value)

    def get_node_count(self) -> int:
        """
        Count the number of nodes in the BST.

        @return: number of nodes
        """
        return _count_nodes(self.root)

    def get_height(self) -> int:
        """
        Get height of the BST.

        @return: height of the BST
        """
        _max_depth(self.root)

    def get_min(self, node: Optional[Node]) -> int:
        """
        Return minimum value that exists in the tree

        @return: minimum value
        """
        if not node:
            node = self.root

        while node.left:
            node = node.left

        return node

    def get_max(self, node=None) -> int:
        """
        Returns maximum value that exists in the tree.

        @return: maximum value
        """
        if not node:
            node = self.root

        while node.right:
            node = node.right

        return node

    def is_binary_search_tree(self, node=None) -> bool:
        """
        Is the tree a binary search tree?

        @return: True if a BST
        """
        if not node:
            node = self.root

        self._is_binary_search_tree(node)

    def _is_binary_search_tree(self, node: Optional[Node]):
        if not node:
            return True

        if node.left is not None and self.get_max(node.left) > node.value:
            return False

        if node.right is not None and self.get_min(node.right) < node.value:
            return False

        if self._is_binary_search_tree(node.left) is False or self._is_binary_search_tree(node.right) is False:
            return False

        return True

    def delete_value(self, value: int) -> None:
        """
        Delete value form binary search tree

        @return: None
        """
        prev, node = None, self.root
        lr = None

        while node and node.value is not value:
            if node.value > value:
                prev, node, lr = node, node.right, left_or_right.RIGHT
            elif node.value < value:
                prev, node, lr = node, node.left, left_or_right.LEFT

        if not node:
            raise ValueError(f"{value} not in tree")

        if node.left is None and node.right is None:
            prev[lr] = None

        elif node.left is None:
            pass



    def get_successor(self) -> int:
        """
        Returns next-highest value in tree after given value,

        @return: Returns next highest value, or -1 if none
        """
        pass
