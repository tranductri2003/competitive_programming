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
const int N = 1e5 + 9;
const int N1 = 1e3 + 9;
const ll Lim = 1e18;
const int Mod = 998244353;
const int DX[]{0, -1, 0, 1}, DY[]{1, 0, -1, 0};
const double Pi = 3.14159265;
int tc = 1;
int n, x, y, cnt;
I2 a, b, c;
priority_queue<I2, vector<I2>, greater<I2>> PQ;
void solve()
{
    cin >> n;
    fo(i, 1, n)
    {
        cin >> y;
        x = y;
        cnt = 0;
        while (x % 2 == 0)
        {
            x >>= 1;
            ++cnt;
        }
        PQ.push(I2(cnt, y));
    }
    while (PQ.size() > 1)
    {
        a = PQ.top();
        PQ.pop();
        b = PQ.top();
        PQ.pop();
        c = {min(a.ft, b.ft) + 1, __gcd(a.sd, b.sd) * 2};
        PQ.push(c);
    }
    cout << PQ.top().sd << el;
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
