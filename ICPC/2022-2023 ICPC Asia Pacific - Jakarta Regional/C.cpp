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

const int N = 105;

ll n, b[N], m;
string a[N];

void Input()
{
    cin >> n >> m;
    for (int i = 1; i <= n; i++)
        cin >> b[i] >> a[i];
}

void Solve()
{
    ll cnt = 0;
    string ans = "";
    for (int k = 0; k <= n; k++)
    {
        string s;
        bool c = 1;
        for (int i = 0; i < m; i++)
            s = s + " ";
        for (int i = 1; i <= n; i++)
        {
            if (i == k)
                continue;
            for (int j = 0; j < a[i].size(); j++)
            {
                int p = b[i] + j - 1;
                if (s[p] != ' ')
                {
                    if (s[p] != a[i][j])
                    {
                        c = 0;
                        break;
                    }
                    else
                        continue;
                }
                s[p] = a[i][j];
            }
        }
        if (!c)
            continue;
        for (int i = 0; i < m; i++)
            if (s[i] == ' ')
            {
                c = 0;
                break;
            }
        // cout << k << ' ' << s << endl;
        if (c)
        {
            if (s != ans)
                cnt++;
            ans = s;
        }
    }
    if (cnt == 1)
        cout << ans;
    else if (cnt == 0)
        cout << -1;
    else
        cout << -2;
}

#define task "test"
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    if (fopen(task ".inp", "r"))
    {
        freopen(task ".inp", "r", stdin);
        freopen(task ".out", "w", stdout);
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