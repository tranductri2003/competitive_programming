#include <iostream>
#include <unordered_map>

using namespace std;
using ll = long long;

unordered_map<ll, ll> pisano_periods;

ll calculate_pisano_period_large(ll p)
{
    ll a = 0, b = 1, c = a + b;
    for (ll i = 0; i < p * p; i++)
    {
        c = (a + b) % p;
        a = b;
        b = c;
        if (a == 0 && b == 1)
            return i + 1;
    }
    return 0;
}

void precompute_pisano_periods()
{
    for (ll p = 2; p <= 1000000; p++)
    {
        pisano_periods[p] = calculate_pisano_period_large(p);
    }
}

int main()
{
    precompute_pisano_periods();

    ll p;
    cin >> p;

    if (p <= 5)
    {
        if (p == 2)
            cout << "3\n";
        else if (p == 5)
            cout << "20\n";
        else
            cout << "0\n";
    }
    else
    {
        ll result = pisano_periods[p];
        cout << result << "\n";
    }

    return 0;
}
