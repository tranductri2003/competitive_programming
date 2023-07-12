/*
link submit:
Note:
*/
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef long double ld;

#define MS(s, n) memset(s, n, sizeof(s))
#define All(v) (v).begin(), (v).end()

#define cntBit __builtin_popcount
#define fi first
#define se second
#define pb push_back
#define precision(x) cout << setprecision(x) << fixed;
#define EL cout << endl;

const int dx[4] = {1, 0, -1, 0}, dy[4] = {0, 1, 0, -1};
const long double PI = acos(-1);

mt19937_64 gen(chrono::steady_clock::now().time_since_epoch().count());
ll Rand(ll l, ll r)
{
    uniform_int_distribution<ll> rnd(l, r);
    return rnd(gen);
}

vector<int> adj[200005];
int a[200005];
int dp[200005];

void dfs(int u, int p)
{
    vector<int> x;
    dp[u] = 1;
    for (auto i : adj[u])
    {
        if (i == p)
            continue;
        dfs(i, u);
    }

    for (auto i : adj[u])
    {
        if (i == p)
            continue;
        x.pb(dp[i]);
    }
    sort(All(x));

    for (int i = 0; i < x.size(); i++)
    {
        if (i != x.size() - 1)
        {
            dp[u] = max(dp[u], x[i] + 1);
        }
        else
        {
            dp[u] = max(dp[u], x[i]);
        }
    }
}
void solve()
{

    int n;
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        cin >> a[i];
        if (i == 1)
            continue;
        adj[i].pb(a[i]);
        adj[a[i]].pb(i);
    }

    dfs(1, -1);
    cout << dp[1] << endl;

    for (int i = 0; i <= n; i++)
    {
        adj[i].clear();
        dp[i] = 0;
    }
}

int main()
{
    if (fopen("input.txt", "r"))
    {
        freopen("input.txt", "r", stdin);
        // freopen("output.txt","w",stdout);
    }

    ios::sync_with_stdio(0);
    cin.tie(NULL);

    int t;
    cin >> t;
    while (t--)
        solve();

    return 0;
}