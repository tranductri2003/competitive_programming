#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define fi first

#define int long long 
const int N = (int)1e7 + 1;

int32_t main(){

	ios_base::sync_with_stdio(false);
    cin.tie(NULL);

	//freopen("inp.txt", "r", stdin);

	int n; cin>>n;

	vector<ll> a(n);

	map<ll, ll> mp;

	for (auto &x:a) { cin>>x; mp[x]++; }

	ll cnt = 0;

	
	for (auto [x,y]:mp){
		if (y > 1) { cnt += ((y) * (y - 1)) / 2; }
	}

	vector<ll> b(N, 0);

	for (ll i = 2;i*i<N;++i){
			
			if (b[i] == 0) {

				b[i] = i;

				for (ll j = i * 2; j<N;j+=i) {

					b[j] = i;
					// if (i * i % j == 0 && j * j % i == 0 && m[to_string(i) + " " + to_string(j)] == 0) {
					// 	cnt += mp[i] * mp[j];
					// 	 m[to_string(i) + " " + to_string(j)]  = 1;
					// 	// if (mp[i] > 0 && mp[j] > 0)
					// 	// cout << i << " " << j << "\n";
					// }

					// if ((j - i) * (j - i) % j == 0 && (j) * (j) % (j - i) == 0 && m[to_string(j - i) + " " + to_string(j)] == 0) {
					// 	cnt += mp[j - i] * mp[j];
						
					// 	m[to_string(j - i) + " " + to_string(j)] = 1;
					// 	// if (mp[i] > 0 && mp[j] > 0)
					// 	// 	cout << i << " " << j << "\n";
					// }


				}
		}
	}

	map< ll, vector<ll> > m;

	for (auto [x,y]:mp) {
		m[b[x]].push_back(x);
	}

	for (auto [x,y]:mp){

		int sz = m[x].size();

		for (ll i = 0;i<sz; ++i) 
			for (ll j = i + 1; j<sz;++j) {
				ll k1 = m[x][i];
				ll k2 = m[x][j];

				if (k1 * k1 %  k2 == 0 && k2 * k2 %  k1 == 0) cnt += mp[k1]*mp[k2];
			}


	}

	cout << cnt << "\n";

}
