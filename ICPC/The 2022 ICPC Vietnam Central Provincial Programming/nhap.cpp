#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<ll> vi;
typedef pair<ll, ll> ii;
typedef vector<ii> vii;
typedef pair<ll, ii> iii;
#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#define mp make_pair
#define pb push_back
#define sasukeeeee cin.tie(0), cout.tie(0);
#define narutooooo ios_base::sync_with_stdio(false);
#define FOR(i, a, b) for (ll i = a; i <= b; i++)
#define REP(i, a, b) for (ll i = a; i < b; i++)
#define FORD(i, a, b) for (ll i = a; i >= b; i--)
#define DEBUG cout << "___I will become hokage___" << endl;

const ll base = 331;
const ll mod[] = {
    (ll)1e9 + 2277,
    (ll)1e9 + 5277,
    (ll)1e9 + 8277,
    (ll)1e9 + 9277};
const ii dir[] = {
    {0, 1}, {1, 0}, {0, -1}, {-1, 0}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};
const ll N = 1e5 + 1;
const ll M = 1e9 + 7;

ll n, q;
ll a[N], l, r;
vector<ll> vit[N * 4];

void merge_sort(ll id, vector<ll> &a, vector<ll> &b)
{
    ll i = 0, j = 0;
    while (true)
    {
        if (i == a.size() && j == b.size())
            break;
        if (i == a.size())
        {
            vit[id].pb(b[j]);
            j++;
            continue;
        }
        if (j == b.size())
        {
            vit[id].pb(a[i]);
            i++;
            continue;
        }

        if (a[i] < b[j])
        {
            vit[id].pb(a[i]);
            i++;
            continue;
        }
        else
        {
            vit[id].pb(b[j]);
            j++;
            continue;
        }
    }
}

void build(ll id, ll l, ll r)
{
    if (l == r)
    {
        vit[id].pb(a[r]);
        return;
    }

    ll mid = (l + r) / 2;
    build(id * 2, l, mid);
    build(id * 2 + 1, mid + 1, r);

    merge_sort(id, vit[id * 2], vit[id * 2 + 1]);
}

ll get(ll id, ll l, ll r, ll u, ll v, ll key)
{
    if (r < u || l > v)
        return 0;
    if (r <= v && u <= l)
    {
        ll left = 0, right = vit[id].size() - 1, res = -1, mid;
        while (right >= left)
        {
            mid = (left + right) / 2;
            if (vit[id][mid] <= key)
            {
                left = mid + 1;
                res = mid;
            }
            else
                right = mid - 1;
        }

        return res + 1;
    }

    ll mid = (l + r) / 2;
    return get(id * 2, l, mid, u, v, key) + get(id * 2 + 1, mid + 1, r, u, v, key);
}

int main()
{
    narutooooo
            sasukeeeee

                cin >>
        n >> q;
    FOR(i, 1, n)
    cin >> a[i];

    build(1, 1, n);

    while (q--)
    {
        cin >> l >> r;

        ll left = 1, right = 1e5, mid, res = -1;
        while (right >= left)
        {
            mid = (left + right) / 2;

            // cout << mid << " " << get(1, 1, n, l, r, mid) << endl;
            if (get(1, 1, n, l, r, mid) >= (r - l + 2) / 2)
            {
                res = mid;
                right = mid - 1;
            }
            else
                left = mid + 1;
        }

        cout << res << '\n';
    }
    cout << endl;
}