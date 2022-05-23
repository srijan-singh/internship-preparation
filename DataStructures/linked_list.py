class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

# To print data
def print_data(head_ref):
    # First Node
    print(head_ref.data)
    # print_datata
    while(head_ref.next != None):
        head_ref = head_ref.next
        print(head_ref.data)
    print('\n')


# Adding element at the last
def append(head_ref, new_node):
    head = head_ref

    while(True):
        if (head_ref.next == None):
            head_ref.next = new_node
            break
        
        head_ref = head_ref.next

    return head

# Insering element at particular position    
def insert(head_ref, new_node, node_position):

    position = 1

    while(True):

        if(position == node_position-1):
            temp = head_ref.next
            head_ref.next=new_node
            new_node.next = temp
            break

        position+=1
        head_ref = head_ref.next


# Removing element at the last
def pop(head_ref):

    while((head_ref.next).next != None):
        head_ref = head_ref.next

    head_ref.next = None

# Removing element at particular position    
def remove(head_ref, node_position):

    position = 1

    while(head_ref.next != None):

        if position == node_position-1:
            
            temp = head_ref.next
            temp = temp.next

            head_ref.next = temp

        position+=1
        head_ref=head_ref.next

    return        


if __name__ == "__main__":
    
    a = Node(3)
   
    # Populating nodes
    prev = a

    for i in range(4,10):
        temp = Node(i)
        prev.next = temp
        prev = temp

    print_data(a)

    # Insert
    insert(a, Node(11), 3)

    # print_data
    print_data(a)

    # Append
    append(a, Node(33))

    # print_data
    print_data(a)

    # pop
    pop(a)

    # print_data
    print_data(a)

    # remove
    remove(a, 4)

    # print_data
    print_data(a)





