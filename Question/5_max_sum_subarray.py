def max_sum_subarray(arr: list(), n: int) -> int :
    
    max_sum = 0
    cur_sum = 0

    for i in range(n):

        cur_sum += arr[i]

        if max_sum < cur_sum:
            max_sum = cur_sum

        if cur_sum < 0:
            cur_sum = 0

    return max_sum


if __name__ == "__main__":


    n = int(input())

    arr = list(map(int, input().strip().split()))

    print(max_sum_subarray(arr, n))