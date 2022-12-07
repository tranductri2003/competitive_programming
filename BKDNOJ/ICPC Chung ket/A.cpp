#include <bits/stdc++.h>
using namespace std;

int main()
{

    int h1, m1, s1, h2, m2, s2;
    for (int i = 0; i < 3; i++)
    {
        cin >> h1 >> m1 >> s1 >> h2 >> m2 >> s2;
        int t1 = h1 * 3600 + m1 * 60 + s1;
        int t2 = h2 * 3600 + m2 * 60 + s2;
        int t3 = t2 - t1;
        int ha = t3 / 3600;
        int rmt = t3 % 3600;
        int ma = rmt / 60;
        cout << ha << ' ' << ma << ' ' << rmt % 60 << endl;
    }

    return 0;
}