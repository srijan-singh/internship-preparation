# Two Sum 100%


def res(a:int, b:int) -> str:
    if (a < b):
        return str(a)+" "+str(b)
    return str(b)+" "+str(a)

def twoSum(arr, target, n):
    # Write your code here.
    memo = {}
    
    result = []
    
    for index in range(n):

        i = arr[index]
        
        elm = target - i


        if elm in memo:            

            if memo[elm] >= 1:                
                memo[elm] -= 1   
                result.append(res(elm,i))   


            else:
                #print("be maarde",index)

                if i in memo:
                    #print("badhal")
                    memo[i] += 1
                
                else:
                    memo[i] = 1

        else:
            if i in memo:
                #print("badhal")
                memo[i] += 1
                
            else:
                memo[i] = 1

            
            
 
	
    if len(result) == 0:
        print('-1 -1')
	
    else:        
        for i in result:
            print(i)


def takeInput() :

    n, tar = map(int, input().strip().split(" "))
    arr = list(map(int, input().strip().split(" ")))
    return n, tar, arr


t = int(input().strip())
for i in range(t) :

    n, target, arr = takeInput()

    twoSum(arr, target, n)