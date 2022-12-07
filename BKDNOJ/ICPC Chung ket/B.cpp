#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> ans;
    for (int i = 0; i < 2; i++)
    {
        vector<int> a(10);
        for (int i = 0; i < 10; i++)
            cin >> a[i];
        sort(a.begin(), a.end(), greater<int>());
        ans.push_back(a[0] + a[1] + a[2]);
    }
    for (int a : ans)
        cout << a << ' ';
    return 0;
}