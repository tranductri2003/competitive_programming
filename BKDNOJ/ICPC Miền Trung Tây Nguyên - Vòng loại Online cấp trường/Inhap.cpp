#include <bits/stdc++.h>
using namespace std;

void facSieve(int n, vector<int> &minPrime)
{
    minPrime.assign(n + 1, 0);
    for (int i = 2; i * i <= n; ++i)
    {
        if (minPrime[i] == 0)
        {
            for (int j = i * i; j <= n; j += i)
            {
                if (minPrime[j] == 0)
                {
                    minPrime[j] = i;
                }
            }
        }
    }
    for (int i = 2; i <= n; ++i)
    {
        if (minPrime[i] == 0)
        {
            minPrime[i] = i;
        }
    }
}

vector<int> factorize(int n, vector<int> &minPrime)
{
    vector<int> res;
    while (n != 1)
    {
        res.push_back(minPrime[n]);
        n /= minPrime[n];
    }
    return res;
}

int main()
{
    for (int i = 0; i < 20; i++)
    {

        int n, ans = 1, nn;
        cin >> n;
        nn = n;
        vector<int> minPrime, facs;
        facSieve(1e6, minPrime);
        for (int i = 2; i * i < nn; i++)
        {
            facs = factorize(i, minPrime);
            for (int j : facs)
            {
                if (n % j == 0)
                    n /= j;
            }
            if (n == 1)
            {
                ans = i;
                break;
            }
            if (nn % i == 0)
                ans = nn / i;
        }
        if (n > 1)
            ans = n;
        cout << ans << endl;
    }

    return 0;
}