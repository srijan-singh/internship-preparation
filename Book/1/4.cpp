#include<iostream>
#include<unordered_map>

using namespace std;

string filteredString(string str)
{
    string result = "";

    for(auto ch : str)
    {
        if(ch == ' ')
        {
            continue;
        }

        result+=ch;
    }

    return result;
}

bool palindromePermutation(string str)
{
    str = filteredString(str);

    int length = str.size();

    unordered_map<char, int> memo;

    for(auto ch : str)
    {
        if(memo.find(ch) != memo.end())
        {
            memo[ch] += 1;
        }

        else
        {
            memo[ch] = 1;
        }
    }

    if(length%2 == 0)
    {
        for(auto elm : memo)
        {
            if(elm.second%2 != 0)
            {
                return false;
            }
        }
    }

    else
    {
        int odd = 0;

        for(auto elm : memo)
        {
            if(elm.second%2 != 0)
            {
                odd+=1;
            }
        }

        if(odd%2 == 0)
        {
            return false;
        }
    }

    return true;
}

int main()
{
    string str = "taco bocat";

    cout<<boolalpha<<palindromePermutation(str);

    return 0;
}