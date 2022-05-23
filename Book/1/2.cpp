#include<iostream>
#include<unordered_map>

using namespace std;

bool isPermutation(string str1, string str2)
{
    int length1 = str1.size();
    int length2 = str2.size();

    // If string is not equal in length
    if(length1 != length2)
    {
        return false;
    }

    unordered_map<char, int> memo1;
    unordered_map<char, int> memo2;

    for(int i=0; i<length1; i++)
    {
        // if element already exist in memo increament it's occurenece 
        if(memo1.find(str1[i]) != memo1.end())
        {
            memo1[str1[i]] += 1;
        }

        else
        {
           memo1[str1[i]] = 1; 
        }

        // if element already exist in memo increament it's occurenece
        if(memo2.find(str2[i]) != memo2.end())
        {
            memo2[str2[i]] += 1;
        }

        else
        {
           memo2[str2[i]] = 1; 
        }
    }

    if(memo1 != memo2)
    {
        return false;
    }

    return true;
}

int main()
{
    string str1 = "abcdaa";
    string str2 = "dabca";


    cout<<boolalpha<<isPermutation(str1, str2);

    return 0;
}