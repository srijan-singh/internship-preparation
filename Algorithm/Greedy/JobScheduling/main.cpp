#include<iostream>
#include<set>
#include<algorithm>

using std::sort;
using std::set;
using std::cout;

struct Data
{
    int profit;
    int deadline;
};

bool sort_profit(Data d1, Data d2)
{
    return d1.profit < d2.profit;
}

int job_scheduling(int size, Data *data)
{
    int profit = 0;

    set<int> memo;

    int i = size-1; 

    while(i>=0)
    {
        // If deadline is not present in memo
        if(memo.find(data[i].deadline) == memo.end())
        {
            profit+=data[i].profit;
            memo.insert(data[i].deadline);
        }

        // If deadline is already present in memo
        else
        {
            // Finding smaller deadline
            int smaller_deadline = data[i].deadline-1;
            
            while(smaller_deadline >= 1)
            {
                // If smaller deadline is not present in memo
                if(memo.find(smaller_deadline) == memo.end())
                {
                    profit+=data[i].profit;
                    memo.insert(smaller_deadline);
                    break;
                }
                smaller_deadline--;
            }
        }
        i--;
    }


    return profit;
}

int main()
{
    int size = 7;

    int profit[size] = {25, 12, 35, 5, 15, 30, 20};

    int deadline[size] = {4, 1, 3, 2, 3, 4, 2};

    Data data[size];

    for(int i=0; i<size; i++)
    {
        data[i].profit = profit[i];
        data[i].deadline = deadline[i];
    }

    sort(data, data+size, sort_profit);

    cout<<job_scheduling(size, data);    

    return 0;
}