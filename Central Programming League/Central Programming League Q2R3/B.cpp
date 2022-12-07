#include <bits/stdc++.h>
using namespace std;

string mahoa(string s)
{
    string data = {};
    data = data + s[0];
    char current = s[0];
    for (int i = 1; i < s.length(); i++)
    {
        if (s[i] != current)
        {
            data += s[i];
            current = s[i];
        }
    }
    int j = 0;
    vector<int> num;
    int stack = 0;
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == data[j])
        {
            stack += 1;
        }
        else
        {
            num.push_back(stack);
            stack = 1;
            j += 1;
        }
    }
    num.push_back(stack);
    string res = "";
    for (int i = 0; i < num.size(); i++)
    {
        res += to_string(num[i]) + data[i];
    }
    return res;
}

int main()
{
    int n;
    cin >> n;
    string s;
    cin >> s;
    for (int i = 0; i < n; i++)
    {
        s = mahoa(s);
    }
    cout << s;
}