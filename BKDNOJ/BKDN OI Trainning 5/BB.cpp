#include <bits/stdc++.h>
using namespace std;

int main()
{

    int n;
    char a, b;
    map<char, char> c;
    cin >> n;
    while (n--)
    {
        cin >> a >> b;
        c[a] = b;
    }
    cin >> n;
    string res;
    while (n--)
    {
        cin >> a;
        if (c.find(a) == c.end())
            res.push_back(a);
        else
            res.push_back(c[a]);
    }
    cout << res;

    return 0;
}