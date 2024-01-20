#include <bits/stdc++.h>
using namespace std;
bool cmp(pair<string, long long> a, pair<string, long long> b)
{
    return a.second > b.second;
}
int main()
{
    long long n;
    cin >> n;
    map<string, long long> d4, d2;
    for (int i = 1; i <= n; i++)
    {
        string s;
        cin >> s;
        string t1 = s.substr(2, 5);
        string t2 = s.substr(4, 5);
        // cout<<t1<<" "<<t2<<endl;
        d4[t1]++;
        d2[t2]++;
    }
    vector<pair<string, long long>> v1, v2;
    long long maxn = 0;
    for (auto x : d4)
        v1.push_back({x.first, x.second});
    for (auto x : d2)
        v2.push_back({x.first, x.second});

    sort(v2.begin(), v2.end(), cmp);
    // for (auto x:v1) cout<<x.first<<" "<<x.second<<endl;
    // for (auto x:v2) cout<<x.first<<" "<<x.second<<endl;

    vector<pair<string, long long>> temp;
    for (auto x : v2)
    {
        temp.push_back(x);
        if (temp.size() == 4)
            break;
    }
    if (temp.size() == 1)
        maxn = max({maxn, (long long)temp[0].second * 500, (long long)300000});
    else if (temp.size() == 4)
        maxn = max({maxn, (long long)500 * (temp[0].second + temp[1].second + temp[2].second) + 300000});
    else
    {
        long long d = 0;
        for (int i = 0; i < temp.size(); i++)
        {
            maxn = max(maxn, (long long)d * 500 + 300000);
            d = (long long)d + temp[i].second;
            maxn = max(maxn, (long long)d * 500);
        }
    }
    // cout<<maxn<<"\n";
    for (auto y : v1)
    {
        vector<pair<string, long long>> temp;
        maxn = max(maxn, (long long)y.second * 4000 + 300000 * (n != y.second));
        long long val = 0;
        for (auto x : v2)
            if (x.first != y.first.substr(2, 3))
            {
                temp.push_back(x);
                val += x.second;
                if (temp.size() == 4)
                    break;
            }

        if (temp.size() != 4 && val + y.second < n)
            maxn = max(maxn, (long long)y.second * 4000 + val * 500 + 300000);

        if (temp.size() == 1)
            maxn = max({maxn, (long long)y.second * 4000 + temp[0].second * 500, (long long)y.second * 4000 + 300000});
        else if (temp.size() == 4)
            maxn = max({maxn, (long long)y.second * 4000 + 500 * (temp[0].second + temp[1].second + temp[2].second) + 300000});
        else
        {
            long long d = 0;
            for (int i = 0; i < temp.size(); i++)
            {
                maxn = max(maxn, (long long)y.second * 4000 + d * 500 + 300000);
                d = (long long)d + temp[i].second;
                maxn = max(maxn, (long long)y.second * 4000 + d * 500);
                // if (d+y.second < n) maxn=max(maxn,(long long)y.second*4000 + d*500 + 300000);
            }
        }
        // cout<<maxn<<"\n";
    }
    cout << maxn;
}