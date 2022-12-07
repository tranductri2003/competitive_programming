#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<ll> vi;
typedef pair<ll, ll> ii;
typedef vector<ii> vii;
typedef pair<ll, ii> iii;

#define mp make_pair
#define sasukeeeee cin.tie(0), cout.tie(0);
#define narutooooo ios_base::sync_with_stdio(false);
#define FOR(i, a, b) for (ll i = a; i <= b; i++)
#define REP(i, a, b) for (ll i = a; i < b; i++)
#define FORD(i, a, b) for (ll i = a; i >= b; i--)

const ll base = 331;
const ll mod[] = {
    (ll)1e9 + 2277,
    (ll)1e9 + 5277,
    (ll)1e9 + 8277,
    (ll)1e9 + 9277};
const ii dir[] = {
    {0, 1}, {1, 0}, {0, -1}, {-1, 0}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};
const ll N = 1e6 + 1;
const ll M = 1e9 + 7;

ll n, k;
ll f[N][2];
ll s[N], a[N];

int main()
{

    int test;
    cin >> test;
    while (test--)
    {
        cin >> n >> k;
        FOR(i, 1, n)
        cin >> a[i];
        FOR(i, 1, n)
        s[i] = s[i - 1] + a[i];

        f[0][0] = f[0][1] = 0;
        for (int i = 0; i < N; i++)
        {
            f[i][0] = 0;
            f[i][1] = 0;
        }

        FOR(i, k, n)
        {
            f[i][0] = max(f[i - 1][0], f[i - k][1] + (s[i] - s[i - k]));
            f[i][1] = max(f[i - 1][1], f[i - k][0] + (-1LL) * (s[i] - s[i - k]));
        }

        cout << max(f[n][0], f[n][1]) << '\n';
    }

    cout << endl;
}