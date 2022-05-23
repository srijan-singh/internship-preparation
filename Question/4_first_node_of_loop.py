# 

#    List Node Class
class Node:
    def __init__(self, data):

        self.data = data
        self.next = None
        self.pos = []

    def __del__(self):
        if (self.next):
            del self.next



def firstNode(head):
    #    Write your code here
    global_set = set()
    
    while(head != None):
        
        if head.data in global_set:
            return head
        
        global_set.add(head.data)    
        
        head = head.next
    #    Return the node where the cycle begins
    pass