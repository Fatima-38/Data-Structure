# =========================
# Binary Search Tree (BST)
# Week 15 - Data Structures
# =========================
# This file is intentionally written with very clear comments
# so students can understand every line.

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Node:
    # Each node stores:
    # 1) value: data of the node
    # 2) left : pointer/reference to left child
    # 3) right: pointer/reference to right child
    value: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


class BST:
    def __init__(self) -> None:
        # Start with an empty tree
        self.root: Optional[Node] = None

    # -------------------------
    # INSERT
    # -------------------------
    def insert(self, value: int) -> None:
        # Public method: insert a value into BST
        self.root = self._insert(self.root, value)

    def _insert(self, node: Optional[Node], value: int) -> Node:
        # If we reached an empty spot, create a new node here
        if node is None:
            return Node(value)

        # If value is smaller, go left
        if value < node.value:
            node.left = self._insert(node.left, value)

        # If value is bigger, go right
        elif value > node.value:
            node.right = self._insert(node.right, value)

        # If value is equal, we ignore duplicates (policy choice)
        # (You can also store duplicates on one side, but keep it simple here)
        return node

    # -------------------------
    # SEARCH
    # -------------------------
    def search(self, value: int) -> bool:
        # Return True if value exists, else False
        return self._search(self.root, value)

    def _search(self, node: Optional[Node], value: int) -> bool:
        # If node is None, value not found
        if node is None:
            return False

        # If matches current node, found
        if value == node.value:
            return True

        # Smaller: search left
        if value < node.value:
            return self._search(node.left, value)

        # Bigger: search right
        return self._search(node.right, value)

    # -------------------------
    # MIN / MAX
    # -------------------------
    def min_value(self) -> Optional[int]:
        # Minimum is the left-most node
        node = self.root
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node.value

    def max_value(self) -> Optional[int]:
        # Maximum is the right-most node
        node = self.root
        if node is None:
            return None
        while node.right is not None:
            node = node.right
        return node.value

    # -------------------------
    # COUNT NODES
    # -------------------------
    def count_nodes(self) -> int:
        # Count all nodes in BST
        return self._count_nodes(self.root)

    def _count_nodes(self, node: Optional[Node]) -> int:
        # If empty, count is 0
        if node is None:
            return 0
        # Count = 1 (this node) + left subtree + right subtree
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

    # -------------------------
    # TRAVERSAL (INORDER)
    # -------------------------
    def inorder(self) -> List[int]:
        # Inorder traversal prints BST values in sorted order
        result: List[int] = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node: Optional[Node], result: List[int]) -> None:
        if node is None:
            return
        # 1) visit left
        self._inorder(node.left, result)
        # 2) visit node
        result.append(node.value)
        # 3) visit right
        self._inorder(node.right, result)

    # -------------------------
    # DELETE (3 CASES)
    # -------------------------
    def delete(self, value: int) -> None:
        # Public method: delete a value from BST
        self.root = self._delete(self.root, value)

    def _delete(self, node: Optional[Node], value: int) -> Optional[Node]:
        # If node is empty, nothing to delete
        if node is None:
            return None

        # Step 1: Find the node to delete (same as search path)
        if value < node.value:
            node.left = self._delete(node.left, value)
            return node
        if value > node.value:
            node.right = self._delete(node.right, value)
            return node

        # Now value == node.value, so this is the node to delete.

        # Case 1: Leaf node (no children)
        if node.left is None and node.right is None:
            return None

        # Case 2: One child (right child only)
        if node.left is None:
            return node.right

        # Case 2: One child (left child only)
        if node.right is None:
            return node.left

        # Case 3: Two children
        # Find inorder successor = minimum in right subtree
        successor = self._min_node(node.right)
        assert successor is not None  # for type checker

        # Replace current node's value with successor's value
        node.value = successor.value

        # Delete the successor node from right subtree
        node.right = self._delete(node.right, successor.value)

        return node

    def _min_node(self, node: Optional[Node]) -> Optional[Node]:
        # Return the left-most node of the subtree
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node

# -------------------------
# MINI TEST (Run this)
# -------------------------
if __name__ == "__main__":
    bst = BST()

    # Insert sample values
    for v in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(v)

    print("Inorder (sorted):", bst.inorder())
    print("Search 40:", bst.search(40))
    print("Min:", bst.min_value(), "Max:", bst.max_value())
    print("Count:", bst.count_nodes())

    # Delete examples:
    bst.delete(20)  # leaf
    print("After deleting 20:", bst.inorder())

    bst.delete(30)  # one child (after 20 removed, 30 has child 40)
    print("After deleting 30:", bst.inorder())

    bst.delete(50)  # two children (root)
    print("After deleting 50:", bst.inorder())
