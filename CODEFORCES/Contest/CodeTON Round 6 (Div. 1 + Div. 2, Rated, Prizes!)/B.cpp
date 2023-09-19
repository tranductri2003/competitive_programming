#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, m, x = 0;
        cin >> n >> m;
        vector<int> a(n), b(m);
        int c[32] = {0};
        for (int &i : a)
        {
            cin >> i;
            x = x ^ i;
            for (int j = 0; i < 31; j++)
            {
                if ((1 << j) & i == 1)
                {
                    c[j]++;
                }
            }
        }
        for (int &i : b)
            cin >> i;
        if (n % 2 == 0)
        {
            for (int i = 0; i < 31; i++)
            {
                if (c[i] % 2 == 1)
                {
                    for (int j : b)
                    {
                        if ((1 << i) & j == 1)
                        {
                            for (int k = 0; k < n; k++)
                            {
                                a[k] = a[k] | j;
                            }
                            break;
                        }
                    }
                }
            }
            int y = 0;
            for (int i = 0; i < n; i++)
            {
                y = y ^ a[i];
            }
            cout << y << " " << x << endl;
        }
        else
        {
            for (int i = 0; i < 31; i++)
            {
                if (c[i] % 2 == 0)
                {
                    for (int j : b)
                    {
                        if ((1 << i) & j == 1)
                        {
                            for (int k = 0; k < n; k++)
                            {
                                a[k] = a[k] | j;
                            }
                            break;
                        }
                    }
                }
            }
            int y = 0;
            for (int i = 0; i < n; i++)
            {
                y = y ^ a[i];
            }
            cout << x << " " << y << endl;
        }
    }
    return 0;
}