#include <bits/stdc++.h>
using namespace std;

// inline void debugLocal() {
//     if (!fopen("input.txt", "r"))
//         return;
//     freopen("input.txt", "r", stdin);
//     freopen("output.txt", "w", stdout);
// }

int main()
{

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    // debugLocal();

    int s, a, b, c;
    cin >> s >> a >> b >> c;
    int d = s - a - b - c;
    vector<pair<int, int>> odd, even;
    if (a % 2 == 0)
    {
        if (a > 0)
            even.push_back({1, a});
    }
    else
    {
        if (a - 1 > 0)
            even.push_back({1, a - 1});
        odd.push_back({1, 1});
    }
    if (b % 2 == 0)
    {
        if (b > 0)
            even.push_back({2, b});
    }
    else
    {
        if (b - 1 > 0)
            even.push_back({2, b - 1});
        odd.push_back({2, 1});
    }
    if (c % 2 == 0)
    {
        if (c > 0)
            even.push_back({3, c});
    }
    else
    {
        if (c - 1 > 0)
            even.push_back({3, c - 1});
        odd.push_back({3, 1});
    }
    if (d % 2 == 1)
    {
        // if (d - 1 > 0)
        //     even.push_back({0, d - 1});
        d -= 1;
        odd.push_back({0, 1});
    }
    sort(odd.begin(), odd.end(), greater<pair<int, int>>());
    sort(even.begin(), even.end(), greater<pair<int, int>>());
    int sum_even = 0;
    for (auto p : even)
        sum_even += p.second;
    if (odd.size() > 1 || (sum_even == 0 && d > 1))
    {
        cout << "Bedao!" << endl;
        return 0;
    }
    deque<long long> ans;
    for (auto p : odd)
    {
        for (int i = 0; i < p.second; i++)
            ans.push_back(p.first);
    }
    // for (auto p : even) {
    //     for (int i = 0; i < p.second / 2; i++) {
    //         ans.push_back(p.first);
    //         ans.push_front(p.first);
    //     }
    // }
    for (int j = 0; j + 1 < even.size(); j++)
    {
        for (int i = 0; i < even[j].second / 2; i++)
        {
            ans.push_back(even[j].first);
            ans.push_front(even[j].first);
        }
    }
    if (even.size() > 0)
    {
        for (int i = 0; i + 1 < (even.back().second / 2); i++)
        {
            ans.push_back(even.back().first);
            ans.push_front(even.back().first);
        }
    }
    if (d % 2 == 0)
    {
        for (int i = 0; i < d / 2; i++)
        {
            ans.push_back(0);
            ans.push_front(0);
        }
    }
    if (even.size() > 0)
    {
        ans.push_back(even.back().first);
        ans.push_front(even.back().first);
    }
    // cout << "TEST: ";
    // for (int ai : ans)
    //     cout << ai;
    // cout << endl;
    long long mod = 727355608, num = 0, p4 = 1;
    for (int i = 0; i < ans.size(); i++)
    {
        num = (num + ans[i] * p4) % mod;
        p4 = (p4 * 4LL) % mod;
    }
    cout << num << endl;

    return 0;
}
