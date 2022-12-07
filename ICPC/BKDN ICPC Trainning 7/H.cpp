#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;

    vector<pair<int, int>> rect;
    long long ans = 0;
    for (int i = 0; i < n; ++i)
    {
        int a, b;
        cin >> a >> b;
        if (a > b)
            swap(a, b);
        rect.emplace_back(a, b);
        ans = max(ans, 1LL * a * b);
    }
    sort(rect.begin(), rect.end());
    reverse(rect.begin(), rect.end());
    int temp = 0;
    for (auto hcn : rect)
    {
        ans = max(ans, 2LL * hcn.first * min(temp, hcn.second));
        temp = max(temp, hcn.second);
    }
    if (ans % 2)
    {
        ans /= 2;
        cout << ans << ".5";
    }
    else
    {
        ans /= 2;
        cout << ans << ".0";
    }
}