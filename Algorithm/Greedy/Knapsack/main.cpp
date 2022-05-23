#include <iostream>
#include <algorithm>

using std::sort;
using std::cout;

struct Data
{
    float profit;
    float weight;
    float profit_weight_ratio;
};

// To sort structure on the basis of profit to weight ratio
bool sort_profit_weight_ratio(Data d1, Data d2)
{
    return d1.profit_weight_ratio < d2.profit_weight_ratio;
}

// Knapsack Solution
float Knapsack(int size, Data *data, float weight_constraint)
{
    float profit = 0;

    // Starting in descending order to get maximum weight to profit first
    for(int i = size-1; i>=0; i--)
    {
        if(weight_constraint >= data[i].weight)
        {
            // Add the whole object
            profit+=data[i].profit;
            weight_constraint-=data[i].weight;
        }

        else
        {
            // Reduce the quantity            
            for(int max_weight = data[i].weight-1; i>=1; i--)
            {
                if(weight_constraint >= max_weight)
                {
                    // Add the partial object
                    profit+=data[i].profit/max_weight;
                    weight_constraint-=max_weight;
                }   
            }
            
        }
    }    

    return profit;
}


int main()
{
    // Size of input data
    int size = 7;
    // Constraint
    float weight_constraint = 15;
    // Data structure to hold data
    Data data[size];

    int profit[size] = {10, 5, 15, 7, 6, 18, 3};

    int weight[size] = {2, 3, 5, 7, 1, 4, 1};

    // Prepairing Input
    for(int i=0; i<size; i++)
    {
        data[i].profit = profit[i];
        data[i].weight = weight[i];
        data[i].profit_weight_ratio = data[i].profit/data[i].weight;
    }

    sort(data, data+size, sort_profit_weight_ratio);

    // Required Solution
    cout<<Knapsack(size, data, weight_constraint);    

    return 0;
}