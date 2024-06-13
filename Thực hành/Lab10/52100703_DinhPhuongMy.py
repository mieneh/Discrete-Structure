#Exercise 1:
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None 
#(a)
root1 = Node(2)
root1.left = Node(7)
root1.right = Node(5)
root1.left.left = Node(2)
root1.left.right = Node(6)
root1.right.right = Node(9)
root1.left.right.left = Node(5)
root1.left.right.right = Node(11)
root1.right.right.left = Node(4)
#(b)
root2 = Node(50)
root2.left = Node(17)
root2.right = Node(76)
root2.left.left = Node(9)
root2.left.right = Node(23)
root2.right.left = Node(54)
root2.left.left.right = Node(14)
root2.left.right.left = Node(19)
root2.right.left.right = Node(72)
root2.left.left.right.left = Node(12)
root2.right.left.right.left = Node(67)

#Exercise 2:
prev = None
def BinaryTree2DoubleLinkedList(root):
    if root is None:
        return root
    head = BinaryTree2DoubleLinkedList(root.left)
    global prev
    if prev is None : 
        head = root      
    else:
        root.left = prev
        prev.right = root
    prev = root; 
    BinaryTree2DoubleLinkedList(root.right)
    return head
print("\nExercise 2:")
print("(a)")
head = BinaryTree2DoubleLinkedList(root1)
while head is not None:
    print(head.data, end=" ")
    head = head.right  
print("(b)")   
head = BinaryTree2DoubleLinkedList(root2)
while head is not None:
    print(head.data, end=" ")
    head = head.right 
      
#Exercise 3:
def NLR(root):
    if root is not None:
        print(root.val, end = " ")
        NLR(root.left)
        NLR(root.right)     
def LNR(root):
    if root is not None:
        LNR(root.left)
        print(root.val, end = " ")
        LNR(root.right)       
def LRN(root):
    if root is not None:
        LRN(root.left)
        LRN(root.right)
        print(root.val, end = " ")
print("\nExercise 3:")
#(a)
print("(a)")
print("NLR (pre-order)")
NLR(root1)
print("\nLNR (in-order)")
LNR(root1)
print("\nLRN (post-order)")
LRN(root1)
print()
#(b)
print("(b)")
print("NLR (pre-order)")
NLR(root2)
print("\nLNR (in-order)")
LNR(root2)
print("\nLRN (post-order)")
LRN(root2)
print()

#Exercise 4:
def breadthFirstSearch(node, data):
    if node is None:
        return None
    queue = [node] 
    while len(queue) > 0:
        current_node = queue.pop(0) 
        if current_node.data == data:
            return current_node
        if current_node.left is not None:
            current_node.left.parent = current_node # keep track of the parent
            queue.append(current_node.left)
        if current_node.right is not None:
            current_node.right.parent = current_node # keep track of the parent
            queue.append(current_node.right)
    return None
def depthFirstSearch(node, data, path=[]):
    if node is None:
        return None    
    path = path + [node.data] 
    if node.data == data:
        return path
    left_path = depthFirstSearch(node.left, data, path)
    if left_path is not None:
        return left_path
    right_path = depthFirstSearch(node.right, data, path)
    if right_path is not None:
        return right_path
    return None
print("\nExercise 4:")
node = breadthFirstSearch(root1, 9)
if node is not None:
    path = []
    while node is not None:
        path.insert(0, node.data)
        node = node.parent
    print(path)
path = depthFirstSearch(root2, 54)
if path is not None:
    print(path)

#Exercise 5:
def breadthFirstSearchV(tree, data):
    queue = [0]
    visited = {0: None}
    while queue:
        node = queue.pop(0)
        if tree[node] == data:
            path = []
            while node is not None:
                path.append(str(tree[node]))
                node = visited[node]
            print(" -> ".join(path[::-1]))
            return
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        if left_child < len(tree) and tree[left_child] is not None:
            queue.append(left_child)
            visited[left_child] = node
        if right_child < len(tree) and tree[right_child] is not None:
            queue.append(right_child)
            visited[right_child] = node
print("\nExercise 5:")
tree = [10, 5, 15, 3, 7, 12, 20, None, None, None, None, None, None, None, 18]
print("\nFinding H (8):")
breadthFirstSearchV(tree, 8)
print("\nFinding 11 in the left tree:")
breadthFirstSearchV(tree, 11)
print("\nFinding 19 in the right tree:")
breadthFirstSearchV(tree, 19)