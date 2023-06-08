class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def build_tree_helper(s, index):
    if index >= len(s):
        return None


    value = 0
    while index < len(s) and s[index].isdigit():
        value = value * 10 + int(s[index])
        index += 1

    node = TreeNode(value)


    if index < len(s) and s[index] == '(':
        index += 1
        node.left, index = build_tree_helper(s, index)


    if index < len(s) and s[index] == '(':
        index += 1
        node.right, index = build_tree_helper(s, index)

 
    if index < len(s) and s[index] == ')':
        index += 1

    return node, index

def build_tree(s):
    root, _ = build_tree_helper(s, 0)
    return root

s = "4(2(3)(1))(6(5))"
root = build_tree(s)
print(root)