def first_and_last(arr : list(), target : int()) -> tuple:

    length = len(arr)

    first = length
    last = 0

    for i in range(length):
        if (arr[i] == target):
            if first > i:
                first = i

            while arr[i] == target:
                last = i
                i+=1
            
    return first, last


if __name__ == "__main__":

    arr = [2,4,5,5,5,5,5,7,9,5,9]
    target = 5

    print(first_and_last(arr, target))