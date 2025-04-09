class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = self.right = None
    
def insert(root: Node, value: int):
    if root is None:
        return Node(value)

    if root.value == value:
        return root

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    
    return root

def inOrder(root: Node):
    if root is None:
        return
    
    inOrder(root.left)
    print(root.value, end=" ")
    inOrder(root.right)

def levelOrder(root: Node):
    queue = [ root ]

    while queue:
        node = queue.pop(0)
        print(f"{node.value}", end=" ")

        if node.left:
            queue.append(node.left)
        
        if node.right:
            queue.append(node.right)

if __name__ == "__main__":
    numbers = [30, 39, 21, 36, 43, 10]
    print(f"Original array: {numbers}")
    
    root = Node(numbers[0])
    for number in numbers[1:]:
        insert(root, number)

    print("In-order traversal: ", end=" ")
    inOrder(root)

    print("\nLevel-order traversal: ", end=" ")
    levelOrder(root)