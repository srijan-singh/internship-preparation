class Data:

    def __init__(self):
        self.profit = int
        self.deadline = int


def job_scheduling(size: int, data: list) -> int:
   
    profit = 0

    memo = set()

    i = size-1

    # Transversing in reverse order to get maximum profit
    while(i >= 0):

        #If deadline is not present in memo
        if data[i].deadline not in memo:

            profit += data[i].profit
            memo.add(data[i].deadline)

        # If deadline is already present in memo
        else:
            
            # Finding smaller deadline
            smaller_deadline = data[i].deadline - 1

            while(smaller_deadline >= 1):

                # If smaller deadline is not present in memo
                if smaller_deadline not in memo:

                    profit += data[i].profit
                    memo.add(smaller_deadline)
                    break 

                smaller_deadline-=1

        i-=1


    return profit


if __name__ == "__main__":
    
    size = 7

    profit = [25, 12, 35, 5, 15, 30, 20]

    deadline = [4, 1, 3, 2, 3, 4, 2]

    data = []

    for i in range(size):
        temp = Data()
        temp.profit = profit[i]
        temp.deadline = deadline[i]
        data.append(temp)


    data = sorted(data, key=lambda Data : Data.profit)

    print(job_scheduling(size, data))

