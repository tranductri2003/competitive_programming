void solve() {
    ll n, c, q;
    cin >> n >> c >> q;
    string s; cin >> s; s = "#" + s;
    For(c) {
        cin >> a[i].fi >> a[i].se;
        pref[i] = a[i].se - a[i].fi + 1;
    }
    pref[0] = n;
    For(c) pref[i] += pref[i - 1];
    For(_, q) {
        ll k; cin >> k;
        ll pos = -1;
        For(i, 0, c) if (pref[i] >= k) {
            pos = i;
            break;
        }
        while (pos > 0) {
            ll num = k - pref[pos - 1];
            num = a[pos].fi + num - 1;
            ll cpos = pos - 1;
            while (1) {
                if (pref[cpos - 1] + 1 <= num && num <= pref[cpos]) {
                    k = num;
                    pos = cpos;
                    break;
                } else {
                    cpos--;
                }
            }
        }
        cout << s[k] << "\n";
    }
}