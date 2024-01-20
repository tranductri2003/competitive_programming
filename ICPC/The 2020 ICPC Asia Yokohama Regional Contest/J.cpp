#include <bits/stdc++.h>
using namespace std;
int tree_max[800004], tree_min[800004];
typedef struct
{
    int x, y, pos;
} point;
point a[200004];
int n;
bool cmp(point a, point b)
{
    if (a.x == b.x)
        return a.y < b.y;
    else
        return a.x < b.x;
}
void build_max(int id, int l, int r)
{
    if (l == r)
    {
        tree_max[id] = a[l].y;
        return;
    }
    build_max(id * 2, l, (l + r) / 2);
    build_max(id * 2 + 1, (l + r) / 2 + 1, r);
    tree_max[id] = max(tree_max[id * 2], tree_max[id * 2 + 1]);
}
void build_min(int id, int l, int r)
{
    if (l == r)
    {
        tree_min[id] = a[l].y;
        return;
    }
    build_min(id * 2, l, (l + r) / 2);
    build_min(id * 2 + 1, (l + r) / 2 + 1, r);
    tree_min[id] = min(tree_min[id * 2], tree_min[id * 2 + 1]);
}
int get_max(int id, int l, int r, int u, int v)
{
    if (r < u || v < l)
        return -1e9;
    if (u <= l && r <= v)
        return tree_max[id];
    int mid = (l + r) / 2;
    return max(get_max(id * 2, l, mid, u, v), get_max(id * 2 + 1, mid + 1, r, u, v));
}
int get_min(int id, int l, int r, int u, int v)
{
    if (r < u || v < l)
        return 1e9;
    if (u <= l && r <= v)
        return tree_min[id];
    int mid = (l + r) / 2;
    return min(get_min(id * 2, l, mid, u, v), get_min(id * 2 + 1, mid + 1, r, u, v));
}
int left(int l, int r, int val)
{
    if (l == r)
        return l;
    int mid = (l + r) / 2;
    if (get_max(1, 1, n, l, mid) > val)
        left(l, mid, val);
    else
        left(mid + 1, r, val);
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;

    for (int i = 1; i <= n; i++)
    {
        cin >> a[i].x >> a[i].y;
        a[i].pos = i;
    }
    sort(a + 1, a + n + 1, cmp);
    // for (int i=1; i<=n; i++) cout<<a[i].x<<" "<<a[i].y<<endl; cout<<"\n";
    build_max(1, 1, n);
    build_min(1, 1, n);
    for (int i = 1; i <= n; i++)
        a[i].pos = i;
    vector<point> l, r;

    int maxn = -1e9;
    for (int i = n; i >= 1; i--)
        if (a[i].y >= maxn)
        {
            r.push_back(a[i]);
            maxn = a[i].y;
        }
    sort(r.begin(), r.end(), cmp);

    int minn = 1e9;
    for (int i = 1; i <= n; i++)
        if (a[i].y <= minn)
        {
            l.push_back(a[i]);
            minn = a[i].y;
        }
    sort(l.begin(), l.end(), cmp);

    vector<int> t1, t2, t3;

    for (auto u : l)
    {
        t1.push_back(u.x);
        t2.push_back(u.y);
    }
    t1.push_back(1e9);
    sort(t2.begin(), t2.end());
    // for (auto u:l) cout<<u.x<<" "<<u.y<<endl;
    // cout<<"\n";
    // for (auto u:r) cout<<u.x<<" "<<u.y<<endl;
    // cout<<"\n";

    // for (auto x:t1) cout<<x<<" "; cout<<"\n";
    // for (auto x:t2) cout<<x<<" "; cout<<"\n";

    int res = 0;
    for (auto u : r)
    {
        int pos_min = get_min(1, 1, n, u.pos + 1, n);
        int val_max = get_max(1, 1, n, 1, u.pos - 1);

        int phai = upper_bound(t1.begin(), t1.end(), u.x) - t1.begin();
        phai--;
        int trai = upper_bound(t2.begin(), t2.end(), pos_min) - t2.begin();
        trai--;
        trai = t2.size() - trai - 1;

        if (val_max > u.y)
        {
            // phai=min(trai,left(1,u.pos-1,u.y));
            // cout<<"ok "<<left(1,u.pos-1,u.y)<<"\n";
            // phai = min(phai , (upper_bound())
            int temp = upper_bound(t1.begin(), t1.end(), left(1, u.pos - 1, u.y)) - t1.begin() - 1;
            // cout<<"ok  "<<temp<<"\n";
            phai = min(phai, temp);
        }

        // cout<<trai<<" "<<phai<<"\n";
        res += phai - trai + 1;
    }
    cout << res;
    // cout<<get_max(1,1,n,1,n);
}