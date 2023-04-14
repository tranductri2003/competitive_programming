#include <bits/stdc++.h>
using namespace std;

vector<int> f;

int cal(int n, int k, int num)
{
    if (num == 0)
        return 0;
    if (f[num] != -1)
        return f[num];
    int ans = 1 - cal(n, k, num - 1);
    if (num >= k)
        ans = max(ans, 1 - cal(n, k, num - k));
    f[num] = ans;
    return ans;
}

int main()
{

    int t;
    cin >> t;
    while (t--)
    {
        int n, k;
        cin >> n >> k;
        f.assign(n * k + 1, -1);
        cout << ((cal(n, k, n * k) == 1) ? "Omda" : "Teemo") << endl;
    }

    return 0;
}