#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        long long n;
        cin >> n;
        vector<long long> a(n);
        a[0] = 2;
        a[n - 1] = 3;
        a[n / 2] = 1;
        long long counter = 4;
        for (int i = 1; i < n - 1; i++)
        {
            if (i == n / 2)
            {
                continue;
            }
            a[i] = counter++;
        }
        for (int i = 0; i < n; i++)
        {
            cout << a[i] << " ";
        }
        cout << endl;
    }
}