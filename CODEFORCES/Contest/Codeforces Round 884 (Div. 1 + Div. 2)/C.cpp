#include <bits/stdc++.h>
using namespace std;

int max(int a, int b)
{
    if (a >= b)
    {
        return a;
    }
    return b;
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        vector<long long> charges(n);
        int maxi = INT_MIN;
        for (int i = 0; i < n; i++)
        {
            cin >> charges[i];
            maxi = max(maxi, charges[i]);
        }

        if (maxi <= 0)
        {
            cout << maxi << endl;
        }
        else
        {
            long long ans = maxi;
            long long sum = 0;
            for (int i = 0; i < n; i += 2)
            {
                if (charges[i] >= 0)
                {
                    sum += charges[i];
                }
            }
            ans = max(ans, sum);
            sum = 0;
            for (int i = 1; i < n; i += 2)
            {
                if (charges[i] >= 0)
                {
                    sum += charges[i];
                }
            }
            cout << max(ans, sum) << endl;
        }
    }
}