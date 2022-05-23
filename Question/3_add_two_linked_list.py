# Linked List 75%

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

# Following is the linked list node structure:
class Node:
    def __init__(self, data):
        
        self.data = data
        self.next = None
        
global_arr = []
        
def get_value(node, value=0):
    
    if(node != None):
        new_value = value*10 + node.data
        get_value(node.next, new_value)
    
    else:
        global_arr.append(value)
        return

def addTwoLists(first, second):
    # Write your code here.
    global_arr.clear()
    get_value(first)
    get_value(second)
    
    result = str(sum(global_arr))
    
    head = Node(result[0])
    
    head_ref = head
    
    for i in range(1, len(result)):
        
        head_ref.next = Node(result[i])
        head_ref = head_ref.next
    
    return head

# Taking input.
def takeInput():

    firstList = None
    secondList = None

    arr = list(map(int, stdin.readline().strip().split(" ")))
    if(arr[0] != -1):

        firstList = Node(arr[0])
        last = firstList
        for data in arr[1:]:

            if(data == -1):
                break

            last.next = Node(data)
            last = last.next

    arr = list(map(int, stdin.readline().strip().split(" ")))
    if(arr[0] != -1):

        secondList = Node(arr[0])
        last = secondList
        for data in arr[1:]:

            if(data == -1):
                break

            last.next = Node(data)
            last = last.next

        return firstList, secondList

# Function to print the node values of the linked list.
def printLinkedList(head):

    while head:
        print(head.data, end=' ')
        head = head.next

    print(-1)

# Main.
T = int(stdin.readline().strip())
for i in range(T):
    first, second = takeInput()
    answerList = addTwoLists(first, second)
    printLinkedList(answerList)