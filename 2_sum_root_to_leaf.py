# Sum root to leaf 50%

# Binary tree node class for reference:
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
global_arr = []

def sum_up(root, value):
    
    if (root.left != None and root.right!= None):
        
        left_value = value*10 + (root.left).data
        right_value = value*10 + (root.right).data
        
        sum_up(root.left, left_value)
        sum_up(root.right, right_value)
    
    
    elif (root.left != None):
        
        left_value = value*10 + (root.left).data
        sum_up(root.left, left_value)
        
    elif(root.right != None):
        
        right_value = value*10 + (root.right).data
        sum_up(root.right, right_value)

    else:
        global_arr.append(value)
        return

        
def rootToLeafSum(root):
	# Write your code here.
    global_arr.clear()
    #print(global_arr)
    sum_up(root, root.data)
   # print(global_arr)
    return sum(global_arr)
