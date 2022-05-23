#include<bits/stdc++.h>

using namespace std;

class Solution {
    
    int max_index(vector<int> arr, int index=0)
    {
    int max = index;
    int length = arr.size();

    for(int i=max+1; i<length; i++)
    {
        if(arr[max] < arr[i])
        {
            max = i;
        }
    }

    if(max == index)
    {
        return -1;
    }

    return max;
}
public:
    int maxProfit(vector<int>& arr) {
        int max = 0;

        int length = arr.size();

        vector<int> result(length, 0);  

        for(int i=0; i<length; i++)
        {
            int max = max_index(arr, i);

            if(max > -1)
            {
                result[i] = arr[max] - arr[i];
            }
        }

        max = max_index(result);
        
        int max_profit = 0;
        
        if(max < 0)
        {
            max_profit = result[0];
        }
        
        else
        {
            max_profit = result[max];   
        }
        
        result.clear();
        
        return max_profit;
    }
};


int main()
{
    Solution s;
    return 0;
}