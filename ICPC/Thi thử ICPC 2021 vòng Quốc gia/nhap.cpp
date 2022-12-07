#include<bits/stdc++.h>

using namespace std;
int t, m;
vector<pair<long long, int>> a;
long long n;

void calc(int i) {
    for (int j = 0; j < a[i].second; j++) {}
}

void solve() {
    cin >> n;
    if (n &1) {
        cout << -1 << '\n';
        return;
    }
    long long tmp = n, i = 2, d=0;
    while (i*i <= tmp) {
        while (tmp % i == 0) {
            tmp /= i;
            d++;
        }
        if (d > 0) {
            a.push_back({i, d});
            d = 0;
        } 
        i++;
    }
    if (tmp != 1) a.push_back({tmp, 1});
    for (int i = 0; i < a.size(); i++) 
        for (int j = 0; j < a[i].second; j++)
    for (long long i = 1; i*i*i < n; i++) {
        if (n % i == 0 && n % (i+1) == 0){
            cout << i << ' ';
        } else i++;
    }
    long long m = sqrt(n);
    if (m != 1 && m*(m+1) == n) {
        cout << m ;
    }
    cout << '\n';    
}

int main() {
    cin >> t;
    while (t--) {
        solve();
    }
    return 0; 
}

