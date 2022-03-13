def kth_largest_element(arr:list, k:int) -> None:

    length = len(arr)

    memo = set()

    for i in range(k):

        largest_elm = -99999999

        for j in range(length):

            if arr[j] not in memo and largest_elm <= arr[j]:
                largest_elm = arr[j]
                
        print(largest_elm)
        memo.add(largest_elm) 
    
    return

if __name__ == "__main__":

    arr = [4,2,9,7,5,6,7,1,3]

    k = 4

    kth_largest_element(arr, k)

    