#include<iostream>
#include<set>

using namespace std;

bool isUnique(string str)
{
    set<char> memo;

    for(auto ch : str)
    {
        if(memo.find(ch) != memo.end())
        {
            return false;
        }
        else
        {
            memo.insert(ch);
        }
    }

    return true;
}

bool isUniqueRestricted(string str)
{
    int length = str.size();

    for(int i=0; i<length; i++)
    {
        for(int j=i+1; j<length; j++)
        {
            if(str[i] == str[j])
            {
                return false;
            }
        }
    }
    return true;
}

int main()
{
    string str = "abcdefg";
    cout<<boolalpha<<isUnique(str);
    //cout<<boolalpha<<isUniqueRestricted(str);
    return 0;
}