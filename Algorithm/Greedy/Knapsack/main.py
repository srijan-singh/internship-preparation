class Data:
    def __init__(self):
        self.profit = float
        self.weight = float
        self.profit_weight_ratio = float

# Knapsack Solution
def Knapsack(size: int, data: list, weight_constraint: int) -> float:
    
    profit = 0

    # Starting in descending order to get maximum weight to profit first
    for i in range(size-1, -1, -1):

        if(weight_constraint >= data[i].weight):
            # Add the whole object
            profit += data[i].profit
            weight_constraint -= data[i].weight

        else:
            # Reduce the quantity            
            for max_weight in range(data[i].weight-1, 0, -1):
                
                if(weight_constraint >= max_weight):
                    # Add the partial object
                    profit += data[i].profit/max_weight
                    weight_constraint -= max_weight

    return profit

if __name__ == "__main__":
    # Size of objects
    size = 7
    # Weight constraint
    weight_constraint = 15
    # Data structure to hold all the data
    data = []
    # Given Data
    profit = [10, 5, 15, 7, 6, 18, 3]
    weight = [2, 3, 5, 7, 1, 4, 1]
    # Prepairing Input
    for i in range(7):
        # Variable to hold the data
        temp = Data()
        temp.profit = profit[i]
        temp.weight = weight[i]
        temp.profit_weight_ratio = temp.profit/temp.weight
        # Appending data in the list
        data.append(temp)

    # Sort on the basis of profit to weight ratio
    data = sorted(data, key=lambda Data : Data.profit_weight_ratio)

    #  Required Solution
    print(Knapsack(size, data, weight_constraint))

    

