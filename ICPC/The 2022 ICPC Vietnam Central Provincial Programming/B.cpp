#include <bits/stdc++.h>
using namespace std;

inline void debugLocal()
{
    if (!fopen("input.txt", "r"))
        return;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
}

vector<int> prefix_function(string s)
{
    int n = (int)s.length();
    vector<int> pi(n);
    for (int i = 1; i < n; i++)
    {
        int j = pi[i - 1];
        while (j > 0 && s[i] != s[j])
            j = pi[j - 1];
        if (s[i] == s[j])
            j++;
        pi[i] = j;
    }
    return pi;
}

int main()
{

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    debugLocal();

    string s;
    cin >> s;
    vector<int> pf = prefix_function(s);
    // for (int i = 0; i < s.length(); i++)
    //     cout << pf[i] << ' ';
    // cout << endl;
    vector<int> tmp = pf;
    sort(tmp.begin(), tmp.end());
    int q, l;
    cin >> q;
    while (q--)
    {
        cin >> l;
        int pos = lower_bound(tmp.begin(), tmp.end(), l) - tmp.begin();
        int cnt = tmp.size() - pos + 1;
        // cout << l << '|' << cnt << endl;
        if (pf[s.length() - 1] < l || cnt < 3)
        {
            cout << "NO" << endl;
            continue;
        }
        cout << "YES " << cnt << endl;
    }

    return 0;
}
