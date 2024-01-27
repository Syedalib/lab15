class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Function to calculate the height of a binary tree
def calculate_height(root):
    if root is None:
        return 0
    left_height = calculate_height(root.left)
    right_height = calculate_height(root.right)
    return 1 + max(left_height, right_height)

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def is_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True
    if not (min_val <= root.key <= max_val):
        return False
    return is_bst(root.left, min_val, root.key - 1) and is_bst(root.right, root.key + 1, max_val)

def lowest_common_ancestor(root, node1, node2):
    if root is None:
        return None
    if root.key > node1 and root.key > node2:
        return lowest_common_ancestor(root.left, node1, node2)
    elif root.key < node1 and root.key < node2:
        return lowest_common_ancestor(root.right, node1, node2)
    else:
        return root.key

def kth_smallest_element(root, k):
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.key
        root = root.right

def level_order_traversal(root):
    if root is None:
        return []

    result = []
    queue = [root]

    while queue:
        current_node = queue.pop(0)
        result.append(current_node.key)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return result


bst_root = TreeNode(10)
bst_root.left = TreeNode(5)
bst_root.right = TreeNode(15)
bst_root.left.left = TreeNode(3)
bst_root.left.right = TreeNode(7)
bst_root.right.left = TreeNode(12)
bst_root.right.right = TreeNode(18)


print("Height of the binary tree:", calculate_height(bst_root))


print("Number of nodes in the binary tree:", count_nodes(bst_root))

print("Is the binary tree a BST?", is_bst(bst_root))


node1, node2 = 3, 7
print(f"Lowest common ancestor of {node1} and {node2}:", lowest_common_ancestor(bst_root, node1, node2))


k = 3
print(f"{k}-th smallest element in the BST:", kth_smallest_element(bst_root, k))

print("Level order traversal:", level_order_traversal(bst_root))
