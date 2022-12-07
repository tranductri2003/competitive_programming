#include <iostream>
using namespace std;
const int MOD = 1e9 + 7;
const int mxN = 1e6;
int n;
void solve()
{
    string a, b, c;
    cin >> a >> b >> c;
    int f = 0, g = -1;
    for (int i = 0; i < n; ++i)
    {
        int x = a[i] - 48;
        int y = b[i] - 48;
        int z = c[i] - 48;
        if ((x + y) % 10 == z)
        {
            int div = (x + y) / 10;
            if (div == 1)
                f = max(f, g + 1);
            else
                f = f + 1;
        }
        else if ((x + y + 1) % 10 == z)
        {
            int div = (x + y) / 10;
            if (div == 1)
                g = g + 1;
            else
                g = max(g, f + 1);
        }
    }
    cout << n - f << '\n';
}

int main()
{
    int testcases;
    // cin >> testcases;
    while (true)
    {
        cin >> n;
        if (n == 0)
            break;
        solve();
    }
    return 0;
}