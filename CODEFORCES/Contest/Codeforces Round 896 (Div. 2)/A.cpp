#include <bits/stdc++.h>
using namespace std;

int main()
{

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; i++)
            cin >> a[i];
        if (n % 2 == 0)
        {
            cout << 2 << endl;
            cout << 1 << ' ' << n << endl;
            cout << 1 << ' ' << n << endl;
            continue;
        }
        cout << 4 << endl;
        cout << 1 << ' ' << n - 1 << endl;
        cout << 1 << ' ' << n - 1 << endl;
        cout << 2 << ' ' << n << endl;
        cout << 2 << ' ' << n << endl;
    }

    return 0;
}
