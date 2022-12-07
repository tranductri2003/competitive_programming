#include <bits/stdc++.h>
using namespace std;
#define fi first
#define se second

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int n;
    cin >> n;
    cin.ignore();
    string s;
    cin >> s;
    int d = 0;
    long long res = 0;
    for (auto x : s)
    {
        if (d)
        {
            res++;
            d--;
        }
        else if (x == '1')
            res++;
        if (x == '1')
            d = 2;
    }
    cout << res;
}

 