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
typedef pair<int, ll> I2;
typedef pair<int, I2> I3;
typedef pair<I2, I2> I4;
typedef vector<int> VI;
const int N = 4e5 + 9;
const int N1 = 1e3 + 9;
const ll Lim = 1e18;
const int Mod = 998244353;
const int DX[]{0, -1, 0, 1}, DY[]{1, 0, -1, 0};
const double Pi = 3.14159265;
int tc = 1;
int n, q, x, y;
ll A[N], B[N];
void solve()
{
    cin >> n >> q;
    fo(i, 1, n) cin >> A[i];
    fo(i, 1, n) cin >> B[i % n + 1];
    fo(i, 1, n) if (A[i] + B[i % n + 1] < 0)
    {
        while (q--)
            cout << "flawed\n";
        return;
    }
    fo(i, 1, n)
    {
        A[i + n] = A[i];
        B[i + n] = B[i];
    }
    fo(i, 2, 2 * n)
    {
        A[i] += A[i - 1];
        B[i] += B[i - 1];
    }
    if (A[n] < 0 || B[n] < 0)
    {
        while (q--)
            cout << "flawed\n";
        return;
    }
    while (q--)
    {
        cin >> x >> y;
        if (x < y)
            cout << min(A[y - 1] - A[x - 1], B[x + n] - B[y]) << el;
        else
            cout << min(A[y + n - 1] - A[x - 1], B[x] - B[y]) << el;
    }
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
