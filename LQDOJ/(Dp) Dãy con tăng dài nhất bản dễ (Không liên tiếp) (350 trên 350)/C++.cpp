int main()
{
    int n;
    cin >> n;

    vector<int> a(n);
    for (int &x : a) cin >> x;

    vector<int> f(n, 1);
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < i; ++j)
            if (a[i] > a[j])
                maximize(f[i], f[j] + 1);

    int res = *max_element(f.begin(), f.end());
    cout << res;
    return 0;
}