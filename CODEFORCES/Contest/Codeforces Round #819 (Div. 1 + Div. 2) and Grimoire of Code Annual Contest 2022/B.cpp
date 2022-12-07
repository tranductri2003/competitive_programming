#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, m;
        cin >> n >> m;
        if (n == 1)
        {
            cout << "Yes" << endl;
            cout << m << endl;
        }
        else
        {
            if (m < n)
            {
                cout << "No" << endl;
            }
            else
            {
                if (m % n == 0)
                {
                    cout << "Yes" << endl;
                    for (int i = 0; i < n; i++)
                    {
                        cout << m / n << " ";
                    }
                    cout << endl;
                }
                else
                {
                    if (n % 2 == 1)
                    {
                        cout << "Yes" << endl;
                        cout << 1 + m - n << " ";
                        for (int i = 1; i < n; i++)
                        {
                            cout << 1 << " ";
                        }
                        cout << endl;
                    }
                    if (n % 2 == 0)
                    {
                        if ((m % n) % 2 == 1)
                        {
                            cout << "No" << endl;
                        }
                        else
                        {
                            int temp = m / n;
                            cout << "Yes" << endl;
                            cout << temp + (m - temp * n) / 2 << " ";
                            cout << temp + (m - temp * n) / 2 << " ";
                            for (int i = 2; i < n; i++)
                            {
                                cout << temp << " ";
                            }
                            cout << endl;
                        }
                    }
                }
            }
        }
    }
}