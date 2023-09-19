#include <bits/stdc++.h>
#define int long long

using namespace std;

const int N = 1e6 + 5;

int trie[N << 1][30], sum[N << 1][30], cnt[30][30], pos[30], idx = 0;

void Add(const string &s)
{
    int now = 0, l = s.size();
    for (int i = 0; i < l; ++i)
    {
        int id = s[i] - 'a' + 1;
        if (!trie[now][id])
            trie[now][id] = ++idx;
        for (int j = 0; j <= 26; ++j)
        {
            if (j != id)
                cnt[j][id] += sum[now][j];
        }
        sum[now][id]++;
        now = trie[now][id];
    }
}

signed main()
{

    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int n, q;
    cin >> n >> q;
    for (int i = 1; i <= n; ++i)
    {
        string s;
        cin >> s;
        s += char('a' - 1);
        Add(s);
    }

    while (q--)
    {
        string s;
        cin >> s;
        s = char('a' - 1) + s;
        for (int i = 0; i <= 26; ++i)
            pos[s[i] - 'a' + 1] = i;
        int res = 0;
        for (int i = 0; i <= 26; ++i)
        {
            for (int j = 0; j <= 26; ++j)
            {
                if (pos[i] > pos[j])
                    res += cnt[i][j];
            }
        }
        cout << res << "\n";
    }

    return 0;
}
