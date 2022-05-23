#include<bits/stdc++.h>

using namespace std;

void print(vector<int> list)
{
    for(auto elm: list)
    {
        cout<<elm<<" ";
    }
    cout<<endl;
}

vector<int> optimal_merge_pattern(vector<vector<int>> lists)
{
    vector<int> result;
    vector<int> buffer_list;

    int list_length = lists.size();

    for(int i=0; i<list_length; i++)
    {
        if(buffer_list.size() == 0)
        {
            auto list1 = lists[0];
            auto list2 = lists[1];

            int length1 = list1.size();
            int length2 = list2.size();

            int i1=0, i2=0;

            while(i1<length1 and i2<length2)
            {
                if(list1[i1]<list2[i2])
                {
                    buffer_list.push_back(list1[i1]);
                    i1++;
                }

                else
                {
                    buffer_list.push_back(list2[i2]);
                    i2++;
                }
            }

            while(i1<length1)
            {
                buffer_list.push_back(list1[i1]);   
                i1++;
            }

            while(i2<length2)
            {
                buffer_list.push_back(list2[i2]);   
                i2++;
            }        

            i++;
        }
    
        else
        {
            auto list = lists[i];

            int length1 = buffer_list.size();
            int length2 = list.size();

            int i1=0, i2=0;

            while(i1<length1 and i2<length2)
            {
                if(buffer_list[i1] < list[i2])
                {
                    result.push_back(buffer_list[i1]);
                    i1++;
                }
                else
                {
                    result.push_back(list[i2]);
                    i2++;
                }
            }

            while(i1<length1)
            {
                result.push_back(buffer_list[i1]);
                i1++;
            }

            while(i2<length2)            
            {
                result.push_back(list[i2]);
                i2++;
            }

            buffer_list = result;

            result.clear();
        }
    }

    result = buffer_list;

    buffer_list.empty();

    return result;
}

int main()
{
    vector<int> list1 = {1,3,9};
    vector<int> list2 = {0,2,4};
    vector<int> list3 = {5,8,10};
    vector<int> list4 = {4,6,7};

    vector<vector<int>> lists = {list1, list2, list3, list4};

    print(optimal_merge_pattern(lists));
}