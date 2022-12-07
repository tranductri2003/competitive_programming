#include <bits/stdc++.h>
#include <iostream>
#include <map>
using namespace std;

int main()
{
    std::map<std::string, string> map;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        string a, b;
        cin >> a >> b;
        map[a] = b;
    }

    int m;
    cin >> m;
    for (int i = 0; i < m; i++)
    {
        string s;
        cin >> s;
        if (map[s] != "0")
        {
            cout << s;
        }
        else
        {
            cout << map[s];
        }
    }
}