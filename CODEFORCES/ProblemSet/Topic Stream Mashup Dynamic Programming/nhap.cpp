#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
ll nck(ll n, ll k) {
	ll r = 1;
	for (ll i = n; i > n - k; i--) {
		r *= i;
	}
	for (ll i = 2; i <= k; i++) {
		r /= i;
	}
	
	return r;
}
int main()
{
    ll n,k;
    cin >> n >> k;
    cout << nck(n,k) << endl;
}