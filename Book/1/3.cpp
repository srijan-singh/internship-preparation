#include<iostream>

using namespace std;

string URLify(string str)
{
    string result;

    int extra_white_space = 0;

    int length = str.size();

    // Removing extra whitespace from back
    for(int i = length-1; i>=0; i--)
    {
        if(str[i] != ' ')
        {
            break;
        }

        str.pop_back();
        extra_white_space+=1;
    }

    // Updated length
    length = length - extra_white_space;

    // Replacing the whitespace with %20
    for(int i=0; i<length; i++)
    {
        if(str[i] == ' ')
        {
            result.append("%20");
        }
        else
        {
            string temp = "";
            temp+=str[i];
            result.append(temp);
        }
    }
    

    return result;
}

int main()
{
    string str = "Srijan Singh from Varanasi   ";
    cout<<URLify(str);
    return 0;
}