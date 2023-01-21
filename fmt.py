class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    # function to add elements to circular linked list
    def append(self, data):
        # is circular linked list is empty then last_node will be none so in if condition head will be created
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        # adding node to the tail of circular linked list
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
            self.last_node.next = self.head

    # function to print the content of circular linked list
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print()


# Driver code
if __name__ == "__main__":
    L = CircularLinkedList()
    L.append(12)
    L.append(56)
    L.append(2)
    L.append(11)

    # Function call
    L.display()

# =================================================
# Binary tree
# pip install binarytree
from binarytree import Node

root = Node(3)
root.left = Node(6)
root.right = Node(8)

# Getting binary tree
print("Binary tree :", root)

# Getting list of nodes
print("List of nodes :", list(root))

# Getting inorder of nodes
print("Inorder of nodes :", root.inorder)

# Checking tree properties
print("Size of tree :", root.size)
print("Height of tree :", root.height)

# Get all properties at once
print("Properties of tree : \n", root.properties)

# =================================================
# Heap tree
# importing "heapq" to implement heap queue
import heapq

# initializing list
li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(li)

# printing created heap
print("The created heap is : ", end="")
print(list(li))

# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li, 4)

# printing modified heap
print("The modified heap after push is : ", end="")
print(list(li))

# using heappop() to pop smallest element
print("The popped and smallest element is : ", end="")
print(heapq.heappop(li))
