#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int tm, sm, ty, sy;
        cin >> tm >> sm >> ty >> sy;

        double t1, t2;

        if (100.0 / (tm + sm) <= 10.0 / sm)
        {
            t1 = 100.0 / (tm + sm);
        }
        else
        {
            t1 = 90.0 / tm;
        }
        if (100.0 / (ty + sy) <= 10.0 / sy)
        {
            t2 = 100.0 / (ty + sy);
        }
        else
        {
            t2 = 90.0 / ty;
        }

        if (t1 == t2)
        {
            cout << "Draw" << endl;
        }
        else if (t1 > t2)
        {
            cout << "YunYun" << endl;
        }
        else
        {
            cout << "Megumin" << endl;
        }
    }
    return 0;
}
