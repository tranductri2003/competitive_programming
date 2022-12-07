#include "bits/stdc++.h"
using namespace std;

struct SegTree
{

    pair<int, int> SKIP_VALUE = {1e9 + 7, 1e9 + 7};
    int ts;
    vector<pair<int, int>> ST;

    SegTree(int tsize)
    {
        ts = 1;
        while (ts < tsize)
            ts *= 2;
        ST.assign(2 * ts + 2, SKIP_VALUE);
    }

    pair<int, int> mergeN(pair<int, int> n1, pair<int, int> n2)
    {
        if (n1.first <= n2.first)
            return n1;
        return n2;
    }

    void build(int id, int l, int r, vector<int> &a, int n)
    {
        if (l >= n)
        {
            ST[id] = SKIP_VALUE;
            return;
        }
        if (l == r)
        {
            ST[id] = make_pair(a[l], l);
            return;
        }
        int mid = (l + r) / 2;
        build(id * 2, l, mid, a, n);
        build(id * 2 + 1, mid + 1, r, a, n);
        ST[id] = mergeN(ST[id * 2], ST[id * 2 + 1]);
    }

    void build(vector<int> &a, int n)
    {
        build(1, 0, ts, a, n);
    }

    pair<int, int> get(int id, int l, int r, int u, int v)
    {
        if (v < l || r < u)
        {
            return SKIP_VALUE;
        }
        if (u <= l && r <= v)
        {
            return ST[id];
        }
        int mid = (l + r) / 2;
        return mergeN(get(id * 2, l, mid, u, v), get(id * 2 + 1, mid + 1, r, u, v));
    }

    pair<int, int> get(int l, int r)
    {
        return get(1, 0, ts, l, r);
    }
};

int main()
{

    int t, k;
    string s;
    cin >> t;
    while (t--)
    {
        cin >> s;
        cin >> k;
        int n = s.length();
        vector<int> a(n), ans;
        for (int i = 0; i < n; i++)
            a[i] = (s[i] - '0');
        SegTree st = SegTree(n);
        st.build(a, n);
        int pos = 0, del_rm = k;
        int tmin = a[0];
        for (int i = 0; i <= k; i++)
        {
            if (a[i] != 0)
                tmin = min(tmin, a[i]);
        }
        for (int i = 0; i < n; i++)
        {
            if (a[i] != tmin)
            {
                del_rm--;
                pos++;
            }
            else
                break;
        }
        ans.push_back(a[pos]);
        pos++;
        // cout << "START " << ans.back() << endl;
        while (pos < n)
        {
            if (del_rm == 0)
            {
                ans.push_back(a[pos]);
                pos++;
                continue;
            }
            pair<int, int> next_pos = st.get(pos, pos + del_rm);
            // cout << pos << '|' << next_pos.first << '|' << next_pos.second << '|' << del_rm << endl;
            ans.push_back(a[next_pos.second]);
            del_rm -= (next_pos.second - pos);
            pos = next_pos.second + 1;
        }
        while (del_rm > 0)
        {
            ans.pop_back();
            del_rm--;
        }
        for (int i = 0; i < ans.size(); i++)
            cout << ans[i];
        cout << endl;
    }

    return 0;
}