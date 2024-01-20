#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef pair<ll, ll> pll;

#define pb push_back
#define X first
#define Y second
#define endl "\n"

const ll LINF = 1E18;
const int INF = 1E9;
const int MOD = 1E9 + 7;
const double pi = acos(-1);

const int N = 5005;

ll n, a[N], F[N][N];

void Input()
{
    cin >> n;
    for (int i = 1; i <= n; i++)
        cin >> a[i];
}

void Solve()
{
    sort(a + 1, a + n + 1);
    F[0][0] = 1;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 5000; j >= 0; j--)
        {
            // F[i][j] = (F[i - 1][j - a[i]] + F[i - 1][j]) % MOD;
            F[i][j] = F[i - 1][j];
            if (j - a[i] >= 0)
                F[i][j] = (F[i][j] + F[i - 1][j - a[i]]) % MOD;
        }
    }

    for (int i = 1; i <= n; i++)
    {
        for (int j = 5000; j >= 0; j--)
            F[i][j] = (F[i][j] + F[i][j + 1]) % MOD;
    }

    //    for(int i = 1; i <= n; i++) {
    //        for(int j = 1; j <= 10; j++) cout << F[i][j] << ' '; cout << endl;
    //    }

    ll ans = 0;
    for (int i = 1; i <= n; i++)
        ans = (ans + F[i - 1][a[i] + 1]) % MOD;
    cout << ans;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    if (fopen("test.inp", "r"))
    {
        freopen("test.inp", "r", stdin);
        freopen("test.out", "w", stdout);
    }
    int t = 1;
    // cin >> t;
    while (t--)
    {
        Input();
        Solve();
    }
    return 0;
}