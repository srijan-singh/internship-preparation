class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(parent):

    if (parent == None):
        return

    print(parent.data)

    # Traverse
    traverse(parent.left)
    traverse(parent.right)


def left_child(parent, length):

    result = 2*parent + 1

    if result < length:
        return result

    else:
        return 0


def right_child(parent, length):

    result = 2*parent + 2

    if result < length:
        return result

    else:
        return 0


def symmetric(node1, node2):
    if node1 == node2: 
        return True

    return False


if __name__ == "__main__":
    value = True

    list_1 = list(map(int, input().strip().split()))
    list_2 = list(map(int, input().strip().split()))

    length = len(list_1)
    #print(length)

    for i in range(length):

        left = list_1[left_child(i, length)]
        right = list_2[right_child(i, length)]

        print("\nLeft Index: ",left_child(i, length),"\nRight Index: ",right_child(i, length))
        print(left, right)
    
        if (not symmetric(left, right)):
            value = False
            print("Break: ",i)
            break
    
    if value:
        print("Symmetric")
    else:
        print("Not Symmetric")


    """
    # Parent
    parent = Node(4)

    list_1 = [5, 2, 8]
    list_2 = []

    # Left Child
    left_child = Node(5)
    parent.left = left_child

    # Right Child
    right_child = Node(5)
    parent.right = right_child

    inorder(parent)
    """


