#include <bits/stdc++.h>
#define fov(i, a) for (auto i : a)
#define fos(i, a, b) for (auto i = a; i * i <= b; ++i)
#define foc(i, a, b) for (auto i = a; i * i * i <= b; ++i)
#define fo(i, a, b) for (auto i = a; i <= b; ++i)
#define fod(i, a, b) for (auto i = a; i >= b; --i)
#define Fo(i, a, b, c) for (auto i = a; i <= b; i += c)
#define ar(a, n) a + 1, a + n + 1
#define all(a) a.begin(), a.end()
#define ft first
#define sd second
#define pf push_front
#define pof pop_front
#define pb push_back
#define pob pop_back
#define eb emplace_back
#define el '\n'
#define file "1"
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> I2;
typedef pair<int, I2> I3;
typedef pair<I2, I2> I4;
typedef vector<int> VI;
const int N = 2e5 + 9;
const int N1 = 1e3 + 9;
const ll Lim = 1e18;
const int Mod = 998244353;
const int DX[]{0, -1, 0, 1}, DY[]{1, 0, -1, 0};
const double Pi = 3.14159265;
int tc = 1;
int n, m, P[2][N], x, y, cnt, val, Pa[N][18], H[N], Ma[N][18];
bool DD[N];
I3 E[N];
ll aw;
vector<I2> V[N];
int dsu(int type, int u)
{
    return (P[type][u] ? P[type][u] = dsu(type, P[type][u]) : u);
}
void dfs(int u)
{
    fo(i, 1, 17)
    {
        Pa[u][i] = Pa[Pa[u][i - 1]][i - 1];
        Ma[u][i] = max(Ma[u][i - 1], Ma[Pa[u][i - 1]][i - 1]);
    }
    fov(v, V[u]) if (v.sd != Pa[u][0])
    {
        Pa[v.sd][0] = u;
        Ma[v.sd][0] = v.ft;
        H[v.sd] = H[u] + 1;
        dfs(v.sd);
    }
}
int lca(int u, int v)
{
    if (H[u] < H[v])
        swap(u, v);
    int ans = 0;
    fod(i, 17, 0) if (H[Pa[u][i]] >= H[v])
    {
        ans = max(ans, Ma[u][i]);
        u = Pa[u][i];
    }
    if (u == v)
        return ans;
    fod(i, 17, 0) if (Pa[u][i] != Pa[v][i])
    {
        ans = max({ans, Ma[u][i], Ma[v][i]});
        u = Pa[u][i];
        v = Pa[v][i];
    }
    return max({ans, Ma[u][0], Ma[v][0]});
}
void solve()
{
    cin >> n >> m;
    fo(i, 1, m) cin >> E[i].sd.ft >> E[i].sd.sd >> E[i].ft;
    sort(ar(E, m));
    fo(i, 1, m)
    {
        x = dsu(0, E[i].sd.ft);
        y = dsu(0, E[i].sd.sd);
        if (x != y)
        {
            P[0][x] = y;
            DD[i] = 1;
        }
    }
    fo(i, 1, m) if (!DD[i])
    {
        x = dsu(1, E[i].sd.ft);
        y = dsu(1, E[i].sd.sd);
        if (x != y)
        {
            V[E[i].sd.ft].pb({E[i].ft, E[i].sd.sd});
            V[E[i].sd.sd].pb({E[i].ft, E[i].sd.ft});
            P[1][x] = y;
            ++cnt;
        }
        if (cnt == n - 1)
            break;
    }
    if (cnt < n - 1)
    {
        cout << -1;
        return;
    }
    H[1] = 1;
    dfs(1);
    fo(i, 1, m) if (DD[i])
    {
        val = lca(E[i].sd.ft, E[i].sd.sd);
        aw += max(0, val - E[i].ft + 1);
    }
    cout << aw;
}
int32_t main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    //    freopen(file".inp", "r", stdin);
    //    freopen(file".out", "w", stdout);
    //    cin>>tc;
    while (tc--)
        solve();
    return 0;
}
